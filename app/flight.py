from datetime import datetime


class Flight:
    """
    Flight class to represent a commercial flight
    
    :param: flight_no: Flight number of the flight
    :param: flight_date: Flight date of the flight
    """
    def __init__(self, flight_no, flight_date: datetime):
        self._flight_no = flight_no
        self._flight_date: datetime = flight_date

    def __eq__(self, other):
        return (self._flight_no == other.flight_no) & (self._flight_date == other.flight_date)

    @property
    def pnr_no(self):
        return self._flight_no

    @property
    def flight_date(self):
        return self._flight_date
