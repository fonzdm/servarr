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

PROWLARR_HOST = os.getenv("PROWLARR_HOST")
API_KEY = os.getenv("API_KEY")
TORRENT_USERNAME = os.getenv("TORRENT_USERNAME")
TORRENT_PASSWORD = os.getenv("TORRENT_PASSWORD")
TORRENT_HOST = os.getenv("TORRENT_HOST", "servarr-qbittorrent")
PROWLARR_SERVICE = os.getenv("PROWLARR_SERVICE", "servarr-prowlarr")
RADARR_SERVICE = os.getenv("RADARR_SERVICE", "servarr-radarr")
FLARESOLVERR_SERVICE = os.getenv("FLARESOLVERR_SERVICE", "servarr-flaresolverr")

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
    
logger.info("Setup Flaresolverr tags in Prowlarr")

headers = {
    "content-type": "application/json",
    "x-api-key": API_KEY,
    "x-requested-with": "XMLHttpRequest"
}

body = {
    "label":"flare"
}

res = post(
    url="http://{}/api/v1/tag".format(PROWLARR_HOST),
    headers=headers,
    body=body
)

# TO-DO: Check for response status code and decide what to do

logger.info("Setup Radarr in Prowlarr")

headers = {
    "content-type": "application/json",
    "x-api-key": API_KEY,
    "x-requested-with": "XMLHttpRequest",
    "X-Prowlarr-Client": "true"
}

body = {
    "syncLevel": "fullSync",
    "fields": [
        {
            "name": "prowlarrUrl",
            "value": "http://{}:9696".format(PROWLARR_SERVICE)
        },
        {
            "name": "baseUrl",
            "value": "http://{}:7878".format(RADARR_SERVICE)
        },
        {
            "name": "apiKey",
            "value": API_KEY
        },
        {
            "name": "syncCategories",
            "value": [
                2000,
                2010,
                2020,
                2030,
                2040,
                2045,
                2050,
                2060,
                2070,
                2080,
                2090
            ]
        }
    ],
    "implementationName": "Radarr",
    "implementation": "Radarr",
    "configContract": "RadarrSettings",
    "infoLink": "https://wiki.servarr.com/prowlarr/supported#radarr",
    "tags": [],
    "name": "Radarr"
}

res = post(
    url="http://{}/api/v1/applications".format(PROWLARR_HOST),
    headers=headers,
    body=body
)

# TO-DO: Check for response status code and decide what to do

logger.info("Setup Sonarr in Prowlarr")

body = {
    "syncLevel": "fullSync",
    "fields": [
        {
            "name": "prowlarrUrl",
            "value": "http://servarr-prowlarr:9696"
        },
        {
            "name": "baseUrl",
            "value": "http://servarr-sonarr:8989"
        },
        {
            "name": "apiKey",
            "value": API_KEY
        },
        {
            "name": "syncCategories",
            "value": [
                5000,
                5010,
                5020,
                5030,
                5040,
                5045,
                5050,
                5090
            ]
        },
        {
            "name": "animeSyncCategories",
            "value": [
                5070
            ]
        },
        {
            "name": "syncAnimeStandardFormatSearch",
            "value": false
        }
    ],
    "implementationName": "Sonarr",
    "implementation": "Sonarr",
    "configContract": "SonarrSettings",
    "infoLink": "https://wiki.servarr.com/prowlarr/supported#sonarr",
    "tags": [],
    "name": "Sonarr"
}

res = post(
    url="http://{}/api/v1/applications".format(PROWLARR_HOST),
    headers=headers,
    body=body
)

# TO-DO: Check for response status code and decide what to do

logger.info("Setup qBitTorrent in Prowlarr")

headers = {
    "content-type": "application/json",
    "x-api-key": API_KEY,
    "x-requested-with": "XMLHttpRequest"
}

body = {
    "enable": true,
    "protocol": "torrent",
    "priority": 1,
    "removeCompletedDownloads": true,
    "removeFailedDownloads": true,
    "name": "qBittorrent",
    "fields": [
        {
            "name": "host",
            "value": TORRENT_HOST
        },
        {
            "name": "port",
            "value": "10095"
        },
        {
            "name": "useSsl",
            "value": false
        },
        {
            "name": "urlBase"
        },
        {
            "name": "username",
            "value": TORRENT_USERNAME
        },
        {
            "name": "password",
            "value": TORRENT_PASSWORD
        },
        {
            "name": "movieCategory",
            "value": "radarr"
        },
        {
            "name": "movieImportedCategory"
        },
        {
            "name": "recentMoviePriority",
            "value": 0
        },
        {
            "name": "olderMoviePriority",
            "value": 0
        },
        {
            "name": "initialState",
            "value": 0
        },
        {
            "name": "sequentialOrder",
            "value": false
        },
        {
            "name": "firstAndLast",
            "value": false
        },
        {
            "name": "contentLayout",
            "value": 0
        }
    ],
    "implementationName": "qBittorrent",
    "implementation": "QBittorrent",
    "configContract": "QBittorrentSettings",
    "infoLink": "https://wiki.servarr.com/radarr/supported#qbittorrent",
    "tags": []
}

res = post(
    url="http://{}/api/v1/downloadclient".format(PROWLARR_HOST),
    headers=headers,
    body=body
)

# TO-DO: Check for response status code and decide what to do

logger.info("Setup Remote Path Mapping")

body = {
    "host": "servarr-qbittorrent",
    "remotePath": "/downloads",
    "localPath":"/mnt/downloads/"
}

res = post(
    url="http://{}/api/v3/remotepathmapping".format(PROWLARR_HOST),
    headers=headers,
    body=body
)

# TO-DO: Check for response status code and decide what to do

logger.info("Setup Flaresolverr in Prowlarr")

body = {
    "onHealthIssue": false,
    "supportsOnHealthIssue": false,
    "includeHealthWarnings": false,
    "name": "FlareSolverr",
    "fields": [
        {
            "name": "host",
            "value": "http://{}:8191/".format(FLARESOLVERR_SERVICE)
        },
        {
            "name": "requestTimeout",
            "value": 60
        }
    ],
    "implementationName": "FlareSolverr",
    "implementation": "FlareSolverr",
    "configContract": "FlareSolverrSettings",
    "infoLink": "https://wiki.servarr.com/prowlarr/supported#flaresolverr",
    "tags": [
        1
    ]
}

res = post(
    url="http://{}/api/v1/indexerProxy".format(PROWLARR_HOST),
    headers=headers,
    body=body
)

# TO-DO: Check for response status code and decide what to do