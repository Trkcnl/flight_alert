from user import User


class PriceAlert:
    """
    Class for handling price alerts

    :param: flight: Flight object that holds flight information
    :param: threshold: Threshold for price alert
    :param: is_on: Boolean value indicating if price alert is on or off
    """
    def __init__(self, flight, threshold):
        self.flight = flight
        self.threshold = threshold
        self._is_on = True

    def check_price(self, user, curr_price):
        if not isinstance(user, User):
            raise TypeError('User must be of type User')
        if (curr_price < self.threshold) & self._is_on:
            self._is_on = False
            self._alert_user(user)
            print(f"Price alert has been triggered and {user.name} is alerted")

    # TODO: Implement a functionality that sends an email to the given user notifying them about the flightprice
    def _alert_user(self, user):
        print(f"Price alert has been triggered and {user.name} is alerted")
        pass
    # A notification class can be created to manage notification types
