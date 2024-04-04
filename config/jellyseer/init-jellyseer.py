import requests
import os

APIKEY = os.getenv("APIKEY")
JELLYFIN_USERNAME = os.getenv("JELLYFIN_USERNAME")
JELLYFIN_PASSWORD = os.getenv("JELLYFIN_PASSWORD")
JELLYFIN_EMAIL = os.getenv("JELLYFIN_EMAIL")
JELLYSEERR_HOST = os.getenv("JELLYSEERR_HOST")
JELLYSEERR_PORT = os.getenv("JELLYSEERR_PORT")

jellyfin_url = "http://servarr-jellyfin:8096/"

jellyseer_url = "http://{0}:{1}".format(JELLYSEERR_HOST, JELLYSEERR_PORT)


def make_post(endpoint="", cookies=None, body=None):

    print("Using endpoint =  {0}".format(str(endpoint)))
    print("Using body =  {0}".format(str(body)))
    print("Using cookies =  {0}".format(str(cookies)))

    response = requests.post(
        url="{0}{1}".format(jellyseer_url, endpoint),
        cookies=cookies,
        json=body,
        verify=False,
    )

    print(
        "Response code: {0}. Response body: {1}".format(
            str(response.status_code), str(response.json)
        )
    )

    return response.json


print("Initizalizing JellySeer")
print("")


########## AUTH

print("Obtaining Jellyfin token")

token_endpoint = "/api/v1/auth/jellyfin"

auth_body = {
    "username": JELLYFIN_USERNAME,
    "password": JELLYFIN_PASSWORD,
    "hostname": jellyfin_url,
    "email": JELLYFIN_EMAIL,
}


auth_response = make_post(token_endpoint, cookies=None, body=auth_body)

print("Fetching info from response...")
token = auth_response["jellyfinAuthToken"]
device_id = auth_response["jellyfinDeviceId"]

cookies = {"connect.sid": token}

############ SONARR

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

sonarr_response = make_post(sonarr_endpoint, cookies=cookies, body=sonarr_body)

############ RADARR

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

radarr_response = make_post(radarr_endpoint, cookies=cookies, body=radarr_body)


############ FINALIZE

finalize_endpoint = "/api/v1/settings/radarr"
finalize_body = None

finalize_response = make_post(finalize_endpoint, cookies=cookies, body=finalize_body)
