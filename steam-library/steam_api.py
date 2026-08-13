import os
import requests
from dotenv import load_dotenv

load_dotenv()

STEAM_API_KEY = os.getenv("STEAM_API_KEY")
STEAM_ID = os.getenv("STEAM_ID")

def get_owned_games():
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"

    params = {
        "key": STEAM_API_KEY,
        "steamid": STEAM_ID,
        "format": "json",
        "include_appinfo": True,
        "include_played_free_games": True
    }

    response = requests.get(url, params=params)

    response.raise_for_status()

    return response.json()