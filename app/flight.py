from datetime import datetime


class Flight:
    """
    Flight class to represent a commercial flight
    
    :param: pnr_no: PNR number of the flight
    :param: flight_date: Flight date of the flight
    :param: price: Price of the flight
    """
    def __init__(self, pnr_no, price, flight_date):
        self._pnr_no = pnr_no
        self._flight_date: datetime = flight_date
        self.price = price

    @property
    def pnr_no(self):
        return self._pnr_no

    @property
    def flight_date(self):
        return self._flight_date
