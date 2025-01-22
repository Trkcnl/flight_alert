from flight import Flight


class User:
    """
    Class that generates new instances of users

    :param: user_id: Unique identifier of the user
    :param: name: Name of user
    :param: email: Email address of user
    :param: alerts: List of alert objects
    """
    def __init__(self, user_id, email, name):
        self._user_id = user_id
        self.email = email
        self.name = name
        self._alerts = []

    @property
    def user_id(self):
        return self._user_id

    @property
    def alerts(self):
        return self._alerts


    def set_alert(self, flight, threshold):
        if not isinstance(flight, Flight):
            raise TypeError('flight must be of type Flight')
        if threshold < 1:
            raise ValueError('threshold must be greater than or equal to 1')
        else:
            new_alert = None
            self._alerts.append(new_alert)

            print(f'Alert {flight.pnr_no} has been set to {threshold}')
