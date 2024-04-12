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

APIKEY = os.getenv("APIKEY")
JELLYFIN_HOST = os.getenv("JELLYFIN_HOST")
NAMESPACE = os.getenv("NAMESPACE")
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