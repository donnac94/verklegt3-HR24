from datetime import datetime

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
            manager: str
    ) -> None:
        """
        :param str country: The country of the location.
        :param str airport: The airport nearest to the location
        :param str phone_nr: The phone number for the location.
        :param datetime opening_time: The opening times for this location.
        :param str manager: The manager for this location.
        """
        self.country = country
        self.airport = airport
        self.phone_nr = phone_nr
        self.opening_time = opening_time
        self.manager = manager
        
    def to_dict_loc(self):
        return {
            "country": self.country,
            "airport": self.airport,
            "phone_nr": self.phone_nr,
            "opening_time": self.phone_nr,
            "manager": self.manager
        }
    
    @classmethod
    def from_dict_loc(cls, data):
        return cls(
            country=data["country"],
            airport=data["airport"],
            phone_nr=data["phone_nr"],
            opening_time=data["opening_time"],
            manager=data["manager"]
        )