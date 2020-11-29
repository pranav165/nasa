from enum import Enum


class Direction(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'


class Location:
    """
    Locations class to define location type object
    """

    def __init__(self, latitude=None, longitude=None, name=None):
        self.lat = latitude[:-1]
        self.lat_direction = Direction(latitude[-1])
        self.long_direction = Direction(longitude[-1])
        self.long = longitude[:-1]
        self.name = name

    def __str__(self):
        return "{0} with Latitude {1}-{2} and Longitude {3}-{4}".format(self.name, self.lat,
                                                                        self.lat_direction.name,
                                                                        self.long, self.long_direction.name)
