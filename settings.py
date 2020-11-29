# Configure global settings here
from utils.location import Location

API_TIMEOUT = 20
API_URL = "https://ssd-api.jpl.nasa.gov/fireball.api"
API_SUPPORTED_VERSION = 1.0  # https://ssd-api.jpl.nasa.gov/doc/fireball.html
loc_boston = Location(latitude="42.354558N", longitude="71.054254W", name="BOSTON")
loc_ncr = Location(latitude="28.574389N", longitude="77.312638E", name="NCR")
loc_sf = Location(latitude="37.793700N", longitude="122.403906W", name="San Francisco")
