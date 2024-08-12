import geopy
from geopy.geocoders import Nominatim
import requests

class InsecureNominatim(Nominatim):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.requester = requests.Session()
        self.requester.verify = False  # Bypass SSL verification

    def _call_geocoder(self, url, timeout=DEFAULT_TIMEOUT, raw=False, **kwargs):
        return super()._call_geocoder(url, timeout=timeout, raw=raw, requester=self.requester, **kwargs)

geolocator = InsecureNominatim(user_agent="your_user_agent")
location = geolocator.geocode("1600 Amphitheatre Parkway, Mountain View, CA")
print(location)
