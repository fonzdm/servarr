#!/usr/local/bin/python3

import requests
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(log_format)
logger.addHandler(console_handler)

APIKEY = os.getenv("APIKEY")
PROWLARR_HOST = os.getenv("PROWLARR_HOST")
SONARR_HOST = os.getenv("SONARR_HOST")
RADARR_HOST = os.getenv("RADARR_HOST")
NAMESPACE = os.getenv("NAMESPACE")

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