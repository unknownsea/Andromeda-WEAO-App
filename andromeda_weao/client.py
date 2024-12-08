# andromeda_weao/client.py
from .enums import API
from .network import Network; network = Network()

class Client:
    def __init__(self):
        pass

    def _get_current_version(self, api: API = API.Main):
        return network._get("versions/current").json()
    
    def _get_future_version(self, api: API = API.Main):
        return network._get("versions/future").json()
    
    def _get_current_android_version(self, api: API = API.Main):
        return network._get("versions/android").json()
    
    def _get_exploit_statuses(self, api: API = API.Main):
        return network._get("status/exploits").json()
    
    def _get_exploit_status(self, exploit: str = "synapse z", api: API = API.Main):
        exploit = exploit.replace(" ", "%20")
        return network._get(f"status/exploits/{exploit}").json()