from datetime import datetime
from employee import employee

class Location():
    """
    Model that contains information on a single location.
    """

    def __init__(
            self,
            country: str,
            airport: str,
            phone_nr: str,
            opening_time: datetime,
            manager: employee
    ) -> None:
        """
        :param str country: The country of the location.
        :param str airport: The airport nearest to the location
        :param str phone_nr: The phone number for the location.
        :param datetime opening_time: The opening times for this location.
        :param employee manager: The manager for this location.
        """
        self.country = country
        self.airport = airport
        self.phone_nr = phone_nr
        self.opening_time = opening_time
        self.manager = manager