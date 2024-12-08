# andromeda_weao/network.py
import requests
from .enums import API

class Network:
    def __init__(self):
        pass

    def _get(self, directory: str = None, api: API = API.Main):
        return requests.get(api + (directory or ""), headers={"User-Agent": "WEAO-3PService"})