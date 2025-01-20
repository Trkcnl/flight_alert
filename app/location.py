class Location:
    """
    Class to represent a location

    :param country: country name
    :param city: city name

    """
    def __init__(self, country, city):
        self._country = country
        self._city = city

    @property
    def country(self):
        return self._country

    @property
    def city(self):
        return self._city

