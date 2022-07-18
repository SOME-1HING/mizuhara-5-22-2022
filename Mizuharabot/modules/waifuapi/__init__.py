import requests
import json

RANDOM_WAIFU_API_URL = 'https://api.jikan.moe/v4/random/characters'

class WaifuClient:
    def __init__():
        pass

    def getRandomWaifu():
        r = requests.get(RANDOM_WAIFU_API_URL)
        if r.status_code != 200:
            raise Exception(r.content)
        return r.json()['data']

__version__ = '0.0.1'
