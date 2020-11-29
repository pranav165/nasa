from .api_base import ApiBase
from settings import API_URL, API_SUPPORTED_VERSION
from enum import Enum
from utils.range import check_in_range


class NasaApiResponseError(Exception):
    pass


class NasaApiNoMatchingDataFoundError(Exception):
    pass


class NasaApiVersionNotSupportedError(Exception):
    pass


class NasaApiResponseMapper(Enum):
    """
    Map response fields with the index number.
    """
    DATE = 0
    ENERGY = 1
    IMPACT_LE = 2
    LATITUDE = 3
    LAT_DIR = 4
    LONGITUDE = 5
    LONG_DIR = 6
    alt = 7
    vel = 8


class Nasa(ApiBase):

    def __init__(self):
        super().__init__()
        self.date = NasaApiResponseMapper.DATE.value
        self.lat = NasaApiResponseMapper.LATITUDE.value
        self.long = NasaApiResponseMapper.LONGITUDE.value
        self.lat_dir = NasaApiResponseMapper.LAT_DIR.value
        self.long_dir = NasaApiResponseMapper.LONG_DIR.value
        self.star_energy = NasaApiResponseMapper.ENERGY.value

    def get_fireball_response(self, params):
        """
        Get response of fireball api based on query param. Sort desc by energy value
        :param date_min : response with date more than min date
        :param sort_by : sort on the field ( default is ascending , - for descending)
        :param req_loc : Only filter out response which has location data
        """
        response = self.get(url=API_URL,
                            params=params)
        if response.status_code != self.response_ok:
            raise NasaApiResponseError("Could not fetch Fireball API Response. Err ->{}".format(response.text))
        response = response.json()

        if response["signature"]["version"] != str(API_SUPPORTED_VERSION):
            raise NasaApiVersionNotSupportedError(
                "NASA Fireball api version {} is not yet supported by the application. Current supported version is {}".format(
                    response["signature"]["version"], API_SUPPORTED_VERSION))
        if response["count"] == '0':
            raise NasaApiNoMatchingDataFoundError("ZERO records found for the filter criteria {}".format(params))
        return response

    def filter_fireball_api_response(self, location=None, date_min='2017-01-01', buffer=15):
        """
        Filter out response by lat /long. Buffer of +-15 is taken
        """
        lat = round(float(location.lat), 1)
        long = round(float(location.long), 1)
        lat_min = round(float(lat - buffer), 1)
        lat_max = round(float(lat + buffer), 1)
        long_min = round(float(long - buffer), 1)
        long_max = round(float(long + buffer), 1)
        lat_dir = location.lat_direction.value
        long_dir = location.long_direction.value

        result = []

        resp = self.get_fireball_response(params={"date-min": date_min, "req-loc": True, "sort": "-energy"})
        for res in resp["data"]:
            if (lat_dir == res[self.lat_dir] and long_dir == res[self.long_dir]
                    and check_in_range(res[self.lat], lat_min, lat_max) and check_in_range(res[self.long], long_min,
                                                                                           long_max)):
                res.append(location.name)
                result.append(res)
        if len(result) == 0:
            raise NasaApiNoMatchingDataFoundError("Could not find any records for the location {}".format(location))
        return result[0]

    def get_fireball_response_for_location_with_max_star_energy(self, locations=None):
        """
        Return the location with max star energy
        :param locations: List of location objects
        :return: fireball response with max star energy of all the locations
        """
        max_for_each_location = []
        for location in locations:
            response = self.filter_fireball_api_response(location=location)
            max_for_each_location.append(response)
        max_star_energy_of_all = [round(float(res[self.star_energy]), 1) for res in max_for_each_location]
        max_idx = max_star_energy_of_all.index(max(max_star_energy_of_all))
        return max_for_each_location[max_idx]
