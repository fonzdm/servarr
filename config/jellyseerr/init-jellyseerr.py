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
JELLYFIN_USERNAME = os.getenv("JELLYFIN_USERNAME")
JELLYFIN_PASSWORD = os.getenv("JELLYFIN_PASSWORD")
JELLYFIN_EMAIL = os.getenv("JELLYFIN_EMAIL")
JELLYSEERR_HOST = os.getenv("JELLYSEERR_HOST")
JELLYSEERR_PORT = os.getenv("JELLYSEERR_PORT")
JELLYFIN_HOST = os.getenv("JELLYFIN_HOST")
JELLYFIN_PORT = os.getenv("JELLYFIN_PORT")

jellyfin_url = "http://{0}:{1}/".format(JELLYFIN_HOST, JELLYFIN_PORT)
jellyseer_url = "http://{0}:{1}".format(JELLYSEERR_HOST, JELLYSEERR_PORT)

session = requests.Session()

def make_get(endpoint=""):

    url = "{0}{1}".format(jellyseer_url, endpoint)
    print("Using url =  {0}".format(str(url)))

    response = session.get(
        url=url,
        verify=False,
    )

    print(
        "Response code: {0}. Response body: {1}".format(
            str(response.status_code), str(response.text)
        )
    )
    response.raise_for_status()
    try:
        return response.json()
    except JSONDecodeError:
        return response.text

def make_post(endpoint="", body=None):

    url = "{0}{1}".format(jellyseer_url, endpoint)
    print("Using url =  {0}".format(str(url)))
    print("Using body =  {0}".format(str(body)))

    response = session.post(
        url=url,
        json=body,
        verify=False,
    )

    print(
        "Response code: {0}. Response body: {1}".format(str(response.status_code), str(response.text))
        )
    response.raise_for_status()
    try:
        return response.json()
    except JSONDecodeError:
        return response.text

print("")
print("#######################")
print("Initizalizing JellySeer")
print("#######################")
print("")

########## JELLYFIN INTEGRATION

print("")
print("Integrating Jellyfin")
print("")

jellyfin_endpoint = "/api/v1/auth/jellyfin"

jellyfin_body = {
    "username": JELLYFIN_USERNAME,
    "password": JELLYFIN_PASSWORD,
    "hostname": jellyfin_url,
    "email": JELLYFIN_EMAIL,
}


jellyfin_response = make_post(jellyfin_endpoint, body=jellyfin_body)

print("Fetching info from response...")
token = jellyfin_response["jellyfinAuthToken"]
device_id = jellyfin_response["jellyfinDeviceId"]

print("")
print("Device ID: {0}. Jellyfin Token: {1}".format(device_id, token))
print("")

######### AUTH

#print("")
#print("Getting API Key")
#print("")

#settings_endpoint="/settings/main"

#settings_response = make_get(settings_endpoint)

#apikey=settings_response['apiKey']

#headers={ 'X-Api-Key': apikey }
#print("API KEY OBTAINED: {0}.".format(apikey))

############ SONARR

print("")
print("Integrating Sonarr")
print("")

sonarr_endpoint = "/api/v1/settings/sonarr"
sonarr_body = {
    "name": "Sonarr",
    "hostname": "servarr-sonarr",
    "port": 8989,
    "apiKey": APIKEY,
    "useSsl": False,
    "activeProfileId": 4,
    "activeLanguageProfileId": 1,
    "activeProfileName": "HD-1080p",
    "activeDirectory": "/mnt/media",
    "activeAnimeProfileId": 4,
    "activeAnimeLanguageProfileId": 1,
    "activeAnimeProfileName": "HD-1080p",
    "activeAnimeDirectory": "/mnt/media",
    "tags": [],
    "animeTags": [],
    "is4k": False,
    "isDefault": True,
    "enableSeasonFolders": True,
    "syncEnabled": False,
    "preventSearch": False,
    "tagRequests": True,
}

sonarr_response = make_post(sonarr_endpoint, body=sonarr_body)

############ RADARR

print("")
print("Integrating Radarr")
print("")

print("")

radarr_endpoint = "/api/v1/settings/radarr"
radarr_body = {
    "name": "Radarr",
    "hostname": "servarr-radarr",
    "port": 7878,
    "apiKey": APIKEY,
    "useSsl": False,
    "activeProfileId": 4,
    "activeProfileName": "HD-1080p",
    "activeDirectory": "/mnt/media",
    "is4k": False,
    "minimumAvailability": "released",
    "tags": [],
    "isDefault": True,
    "syncEnabled": False,
    "preventSearch": False,
    "tagRequests": True,
}

radarr_response = make_post(radarr_endpoint, body=radarr_body)


############ FINALIZE

print("")
print("Finalize")
print("")

finalize_endpoint = "/api/v1/settings/initialize"
finalize_body = {}

finalize_response = make_post(finalize_endpoint, body=finalize_body)

enable_telegram = os.getenv("TELEGRAM_NOTIFICATION_ENABLED", 'False').lower() in ('true', '1', 't')
telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
telegram_apitoken = os.getenv("TELEGRAM_BOT_APITOKEN")

if enable_telegram:
    telegram_endpoint = "/api/v1/settings/notifications/telegram"
    telegram_body = {"enabled":True,"types":4062,"options":{}}
    telegram_body['options']= {"botAPI":telegram_apitoken,"chatId":telegram_chat_id,"sendSilently":False}

    telegram_response = make_post(telegram_endpoint, body=telegram_body)


