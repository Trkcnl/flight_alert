from info import Info


class FlightInfo(Info):
    """
    Flight info class extends Info class: to represent a single flight

    :param departure_loc: departure location
    :param arrival_loc: arrival location
    :param departure_time: departure time
    :param arrival_time: arrival time
    :param flight_number: flight number
    :param company: company name
    :param aircraft: aircraft type
    """
    def __init__(self, departure_loc, departure_time, arrival_loc, arrival_time, flight_number, company, aircraft):
        Info.__init__(self, departure_loc, departure_time, arrival_loc, arrival_time)
        self._flight_number = flight_number
        self._company = company
        self._aircraft = aircraft

    @property
    def flight_number(self):
        return self._flight_number

    @property
    def company(self):
        return self._company

    @property
    def aircraft(self):
        return self._aircraft

    def __str__(self):
        return \
            f'Flight Number: %d\n{10 * "-"}\nDeparture:\n%s\t%s\nArrival:\n%s\t%s ' % (self._flight_number,
                                                                                       self._departure_time,
                                                                                       self._departure_loc,
                                                                                       self._arrival_time,
                                                                                       self._arrival_loc)
