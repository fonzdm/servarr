#!/usr/local/bin/python3

import requests
import os
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
# TO-DO: Those two variables should be part of the env I guess
COUNTRY_CODE = "IT"
PREFERRED_LANGUAGE = "it"

def post(url: str, headers: dict, body: dict | None): # -> str | dict
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
        ", ".join([": ".join(header) for header in headers]),
        str(body)
    ]))

    response = requests.post(
        url=url,
        data=body,
        headers=headers
    )

    logger.debug(" ".join([
        "Status Code:",
        response.status_code,
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
        url="http://{}/.svc.cluster.local:8096/Startup/Configuration".format(JELLYFIN_HOST)
    )
    
    # TO-DO: Check for response status code and decide what to do

setup_location()

# The following GET seems to be required, otherwise
# Jellyfin will be mad at us.

logger.info("Ping GET user endpoint")

logger.debug(" ".join([
    "GET",
    "http://{}/.svc.cluster.local:8096/Startup/User".format(JELLYFIN_HOST),
    ", ".join([": ".join(header) for header in headers])
]))

response = requests.get(
    url=url,
    headers=headers
)

logger.debug(" ".join([
    "Status Code:",
    response.status_code,
    "Response body:",
    response.text
]))

logger.info("Setup the new user")

body = {
    "Name": JELLYFIN_USERNAME,
    "Password": JELLYFIN_PASSWORD
}

res = post(
    url="http://{}/.svc.cluster.local:8096/Startup/User".format(JELLYFIN_HOST),
    headers=headers,
    body=body
)

# TO-DO: Check for response status code and decide what to do

logger.info("Setup the library")

body = {
    "LibraryOptions": {
        "EnableArchiveMediaFiles": "false",
        "EnablePhotos": "true",
        "EnableRealtimeMonitor": "true",
        "ExtractChapterImagesDuringLibraryScan": "true",
        "EnableChapterImageExtraction": "true",
        "EnableInternetProviders": "true",
        "SaveLocalMetadata": "true",
        "EnableAutomaticSeriesGrouping": "false",
        "PreferredMetadataLanguage": PREFERRED_LANGUAGE,
        "MetadataCountryCode": COUNTRY_CODE,
        "SeasonZeroDisplayName": "Specials",
        "AutomaticRefreshIntervalDays": 0,
        "EnableEmbeddedTitles": "false",
        "EnableEmbeddedEpisodeInfos": "false",
        "AllowEmbeddedSubtitles": "AllowAll",
        "SkipSubtitlesIfEmbeddedSubtitlesPresent": "false",
        "SkipSubtitlesIfAudioTrackMatches": "false",
        "SaveSubtitlesWithMedia": "true",
        "RequirePerfectSubtitleMatch": "true",
        "AutomaticallyAddToCollection": "false",
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
    url="http://{}/.svc.cluster.local:8096/Library/VirtualFolders?refreshLibrary=false&name=Library".format(JELLYFIN_HOST),
    headers=headers,
    body=body
)

# TO-DO: Check for response status code and decide what to do

logger.debug("For some reason we have to setup the location twice..")

setup_location()

logger.info("Setup the remote access")

body = {
    "EnableRemoteAccess": "true",
    "EnableAutomaticPortMapping": "false"
}

res = post(
    url="http://{}/.svc.cluster.local:8096/Startup/RemoteAccess".format(JELLYFIN_HOST),
    headers=headers,
    body=body
)

# TO-DO: Check for response status code and decide what to do

logger.info("Finalize the setup")

res = post(
    url="http://{}/.svc.cluster.local:8096/Startup/Complete".format(JELLYFIN_HOST),
    headers={},
    body={}
)

# TO-DO: Check for response status code and decide what to do