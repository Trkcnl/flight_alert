from datetime import datetime

from location import Location


class Info:
    """
    Base class to hold information

    :param departure_time: Departure time
    :param arrival_time: Arrival time
    :param departure_loc: Departure location
    :param arrival_loc: Arrival location
    """

    # TODO: Specify time attributes as datetime objects, locations attributes as location objects
    def __init__(self, departure_loc, arrival_loc, departure_time, arrival_time):
        self._departure_loc = departure_loc
        self._arrival_loc = arrival_loc
        self._departure_time = departure_time
        self._arrival_time = arrival_time

    # TODO: Add methods to convert datetime object to appropriate representation of strings
    @property
    def departure_time(self):
        return self._departure_time

    @property
    def arrival_time(self):
        return self._arrival_time

    @property
    def departure_loc(self):
        return self._departure_loc

    @property
    def arrival_loc(self):
        return self._arrival_loc
