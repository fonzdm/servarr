#!/usr/local/bin/python3

import requests
import os, sys
import logging
from json import JSONDecodeError

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(log_format)
logger.addHandler(console_handler)

JELLYFIN_HOST = os.getenv("JELLYFIN_HOST")
JELLYFIN_USERNAME = os.getenv("JELLYFIN_USERNAME")
JELLYFIN_PASSWORD = os.getenv("JELLYFIN_PASSWORD")
COUNTRY_CODE = os.getenv("COUNTRY_CODE")
PREFERRED_LANGUAGE = os.getenv("PREFERRED_LANGUAGE")

def post(url: str, headers: dict, body: dict):
    """
    Handle POST requests towards an url, logging both
    the details before sending it and the response.

    Parameters
    ----------
    url : str
        HTTP request URL as string
    headers : dict
        HTTP headers to be used in the request
    body : dict
        Request body needed for the POST
    """

    logger.debug(" ".join([
        "POST",
        url,
        ", ".join(f'{key}: {value}' for key,value in headers.items()),
        str(body)
    ]))

    response = requests.post(
        url=url,
        json=body,
        headers=headers
    )

    logger.debug(" ".join([
        "Status Code:",
        str(response.status_code),
        "Response body:",
        response.text
    ]))

    try:
        return {"code": response.status_code, "response": response.json()}
    except JSONDecodeError:
        return {"code": response.status_code, "response": response.text}

def setup_location():   
    logger.info("Setup Location")

    headers = {
        "Content-Type": "application/json"
    }

    body = {
        "UICulture": "en-US",
        "MetadataCountryCode": COUNTRY_CODE,
        "PreferredMetadataLanguage": PREFERRED_LANGUAGE
    }

    res = post(
        url="http://{}/Startup/Configuration".format(JELLYFIN_HOST),
        headers=headers,
        body=body
    )
    
    if res["code"] != 204:
        logger.error("There was an error while setting the location!")
        sys.exit(1)

setup_location()

headers = {
    "Content-Type": "application/json"
}

# The following GET seems to be required, otherwise
# Jellyfin will be mad at us.

logger.info("Ping GET user endpoint")

logger.debug(" ".join([
    "GET",
    "http://{}/Startup/User".format(JELLYFIN_HOST),
    ", ".join(f'{key}: {value}' for key,value in headers.items()),
]))

response = requests.get(
    url="http://{}/Startup/User".format(JELLYFIN_HOST),
    headers=headers
)

logger.debug(" ".join([
    "Status Code:",
    str(response.status_code),
    "Response body:",
    response.text
]))

logger.info("Setup the new user")

body = {
    "Name": JELLYFIN_USERNAME,
    "Password": JELLYFIN_PASSWORD
}

res = post(
    url="http://{}/Startup/User".format(JELLYFIN_HOST),
    headers=headers,
    body=body
)

if res["code"] != 204:
    logger.error("There was an error while setting the user {}!".format(JELLYFIN_USERNAME))
    sys.exit(1)

logger.info("Setup the library")

body = {
    "LibraryOptions": {
        "EnableArchiveMediaFiles": False,
        "EnablePhotos": True,
        "EnableRealtimeMonitor": True,
        "ExtractChapterImagesDuringLibraryScan": True,
        "EnableChapterImageExtraction": True,
        "EnableInternetProviders": True,
        "SaveLocalMetadata": True,
        "EnableAutomaticSeriesGrouping": False,
        "PreferredMetadataLanguage": PREFERRED_LANGUAGE,
        "MetadataCountryCode": COUNTRY_CODE,
        "SeasonZeroDisplayName": "Specials",
        "AutomaticRefreshIntervalDays": 0,
        "EnableEmbeddedTitles": False,
        "EnableEmbeddedEpisodeInfos": False,
        "AllowEmbeddedSubtitles": "AllowAll",
        "SkipSubtitlesIfEmbeddedSubtitlesPresent": False,
        "SkipSubtitlesIfAudioTrackMatches": False,
        "SaveSubtitlesWithMedia": True,
        "RequirePerfectSubtitleMatch": True,
        "AutomaticallyAddToCollection": False,
        "MetadataSavers": [],
        "TypeOptions": [
            {
                "Type": "Series",
                "MetadataFetchers": [
                    "TheMovieDb",
                    "The Open Movie Database"
                ],
                "MetadataFetcherOrder": [
                    "TheMovieDb",
                    "The Open Movie Database"
                ],
                "ImageFetchers": [
                    "TheMovieDb"
                ],
                "ImageFetcherOrder": [
                    "TheMovieDb"
                ]
            },
            {
                "Type": "Season",
                "MetadataFetchers": [
                    "TheMovieDb"
                ],
                "MetadataFetcherOrder": [
                    "TheMovieDb"
                ],
                "ImageFetchers": [
                    "TheMovieDb"
                ],
                "ImageFetcherOrder": [
                    "TheMovieDb"
                ]
            },
            {
                "Type": "Episode",
                "MetadataFetchers": [
                    "TheMovieDb",
                    "The Open Movie Database"
                ],
                "MetadataFetcherOrder": [
                    "TheMovieDb",
                    "The Open Movie Database"
                ],
                "ImageFetchers": [
                    "TheMovieDb",
                    "The Open Movie Database",
                    "Embedded Image Extractor",
                    "Screen Grabber"
                ],
                "ImageFetcherOrder": [
                    "TheMovieDb",
                    "The Open Movie Database",
                    "Embedded Image Extractor",
                    "Screen Grabber"
                ]
            },
            {
                "Type": "Movie",
                "MetadataFetchers": [
                    "TheMovieDb",
                    "The Open Movie Database"
                ],
                "MetadataFetcherOrder": [
                    "TheMovieDb",
                    "The Open Movie Database"
                ],
                "ImageFetchers": [
                    "TheMovieDb",
                    "The Open Movie Database",
                    "Embedded Image Extractor",
                    "Screen Grabber"
                ],
                "ImageFetcherOrder": [
                    "TheMovieDb",
                    "The Open Movie Database",
                    "Embedded Image Extractor",
                    "Screen Grabber"
                ]
            }
        ],
        "LocalMetadataReaderOrder": [
            "Nfo"
        ],
        "SubtitleDownloadLanguages": [],
        "DisabledSubtitleFetchers": [],
        "SubtitleFetcherOrder": [],
        "PathInfos": [
            {
                "Path": "/mnt/media"
            }
        ]
    }
}

res = post(
    url="http://{}/Library/VirtualFolders?refreshLibrary=false&name=Library".format(JELLYFIN_HOST),
    headers=headers,
    body=body
)

if res["code"] != 204:
    logger.error("There was an error while setting the library!")
    sys.exit(1)

logger.debug("For some reason we have to setup the location twice..")

setup_location()

logger.info("Setup the remote access")

body = {
    "EnableRemoteAccess": True,
    "EnableAutomaticPortMapping": False
}

res = post(
    url="http://{}/Startup/RemoteAccess".format(JELLYFIN_HOST),
    headers=headers,
    body=body
)

if res["code"] != 204:
    logger.error("There was an error while setting the remote access!")
    sys.exit(1)

logger.info("Finalize the setup")

res = post(
    url="http://{}/Startup/Complete".format(JELLYFIN_HOST),
    headers={},
    body={}
)

if res["code"] != 204:
    logger.error("There was an error while finalizing the Jellyfin setup!")
    sys.exit(1)
