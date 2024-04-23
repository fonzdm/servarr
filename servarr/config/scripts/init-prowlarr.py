#!/usr/local/bin/python3

import requests
import os, sys
import logging
from json import JSONDecodeError
import json

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(log_format)
logger.addHandler(console_handler)

PROWLARR_HOST = os.getenv("PROWLARR_HOST")
API_KEY = os.getenv("API_KEY")
TORRENT_USERNAME = os.getenv("TORRENT_ADMIN")
TORRENT_PASSWORD = os.getenv("TORRENT_PASSWORD")
TORRENT_SERVICE = os.getenv("TORRENT_SERVICE")
PROWLARR_SERVICE = os.getenv("PROWLARR_SERVICE")
RADARR_SERVICE = os.getenv("RADARR_SERVICE")
FLARESOLVERR_SERVICE = os.getenv("FLARESOLVERR_SERVICE")
SONARR_SERVICE = os.getenv("SONARR_SERVICE")

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

if res["code"] != 201:
    logger.error("There was an error while setting the Flaresolverr tags!")
    sys.exit(1)

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
            "value": "http://{}".format(PROWLARR_SERVICE)
        },
        {
            "name": "baseUrl",
            "value": "http://{}".format(RADARR_SERVICE)
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

if res["code"] != 201:
    logger.error("There was an error while setting Radarr in Prowlarr!")
    sys.exit(1)

logger.info("Setup Sonarr in Prowlarr")

body = {
    "syncLevel": "fullSync",
    "fields": [
        {
            "name": "prowlarrUrl",
            "value": "http://{}".format(PROWLARR_SERVICE)
        },
        {
            "name": "baseUrl",
            "value": "http://{}".format(SONARR_SERVICE)
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
            "value": False
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

if res["code"] != 201:
    logger.error("There was an error while setting Sonarr in Prowlarr!")
    sys.exit(1)

logger.info("Setup qBitTorrent in Prowlarr")

headers = {
    "content-type": "application/json",
    "x-api-key": API_KEY,
    "x-requested-with": "XMLHttpRequest"
}

body = {
    "enable": True,
    "protocol": "torrent",
    "priority": 1,
    "categories": [],
    "supportsCategories": True,
    "name": "qBittorrent",
    "fields": [
        {
            "name": "host",
            "value": TORRENT_SERVICE
        },
        {
            "name": "port",
            "value": "10095"
        },
        {
            "name": "useSsl",
            "value": False
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
            "name": "category",
            "value": "prowlarr"
        },
        {
            "name": "priority",
            "value": 0
        },
        {
            "name": "initialState",
            "value": 0
        },
        {
            "name": "sequentialOrder",
            "value": False
        },
        {
            "name": "firstAndLast",
            "value": False
        },
        {
            "name": "contentLayout",
            "value": 0
        }
    ],
    "implementationName": "qBittorrent",
    "implementation": "QBittorrent",
    "configContract": "QBittorrentSettings",
    "infoLink": "https://wiki.servarr.com/prowlarr/supported#qbittorrent",
    "tags": []
}

res = post(
    url="http://{}/api/v1/downloadclient".format(PROWLARR_HOST),
    headers=headers,
    body=body
)

if res["code"] != 201:
    logger.error("There was an error while setting qBitTorrent in Prowlarr!")
    sys.exit(1)

logger.info("Setup Flaresolverr in Prowlarr")

body = {
    "onHealthIssue": False,
    "supportsOnHealthIssue": False,
    "includeHealthWarnings": False,
    "name": "FlareSolverr",
    "fields": [
        {
            "name": "host",
            "value": "http://{}/".format(FLARESOLVERR_SERVICE)
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

if res["code"] != 201:
    logger.error("There was an error while setting Flaresolverr in Prowlarr!")
    sys.exit(1)

indexersFile = "/mnt/indexers.json"
if os.path.isfile(indexersFile):
    logger.info("Setup Prowlarr indexers")

    with open(indexersFile) as file:
        indexers = json.load(file)
    
    headers = {
        "Content-Type": "application/json",
        "X-Api-Key": API_KEY,
        "X-Prowlarr-Client": "true",
        "X-Requested-With": "XMLHttpRequest"
    }

    for index in indexers:
        logger.debug("Setup {} index".format(index["name"]))
        res = post(
            url="http://{}/api/v1/indexer".format(PROWLARR_HOST),
            body=index["body"],
            headers=headers
        )

        if res["code"] != 201:
            logger.error("There was an error while setting the indexer {}!".format(index["name"]))