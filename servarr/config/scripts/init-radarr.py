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

RADARR_HOST = os.getenv("RADARR_HOST")
API_KEY = os.getenv("API_KEY")
TORRENT_SERVICE = os.getenv("TORRENT_SERVICE")
TORRENT_USERNAME = os.getenv("TORRENT_ADMIN")
TORRENT_PASSWORD = os.getenv("TORRENT_PASSWORD")

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
    
logger.info("Setup qBitTorrent in Radarr")

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
            "value": TORRENT_SERVICE
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

post(
    url="http://{}/api/v3/downloadclient".format(RADARR_HOST),
    headers=headers,
    body=body
)