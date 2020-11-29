#!/usr/bin/env python3
import urllib3
import pytest
from api.nasa_api import Nasa
from settings import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # disable ssl warning
nasa = Nasa()


class FireballException(Exception):
    pass


def fireball(locations):
    """
    :param locations: List of locations object
    :return: Prints location which saw the max star energy since 01/01/2017
    """
    fireball_response = nasa.get_fireball_response_for_location_with_max_star_energy(locations=locations)
    location = fireball_response[-1]
    energy = fireball_response[1]
    date = fireball_response[0]
    for loc in locations:
        if loc.name == location:
            print("Delphix - {} has seen the brightest star on {}. Its energy was {} Joules.".format(loc, date,
                                                                                                     energy))
            return
    raise FireballException("Something went wrong")


if __name__ == '__main__':
    print("============================= App starts ==============================")
    fireball(locations=[loc_boston, loc_ncr, loc_sf])
    print("============================= App Ends ==============================\n\n")
    exit_code = pytest.main()
