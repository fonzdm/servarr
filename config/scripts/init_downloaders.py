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