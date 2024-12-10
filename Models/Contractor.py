from datetime import datetime

class Contractor():
    """
    Model that contains information about a contractor
    """

    def __init__(
            self,
            contractor_id: int,
            name: str,
            contact_name: str,
            phone_nr: str,
            opening_time: datetime,
            location: str,
            satisfaction_with_previous_work: str 
            ) -> None:
                """
                :param str contractor_id : the unique id for contractor
                :param str name: the full name of the contractor
                :param contact_name : contact name of contractor
                :param phone_nr: phone number of contractor 
                :param opening_time : opening time for contractors
                :param location : location of contractor
                :param satisfaction_with_previous_work : shows the satisfaction of previous work from contractor.
                """
                self.contractor_id = contractor_id
                self.name = name
                self.contact_name = contact_name
                self.phone_nr = phone_nr
                self.opening_time = opening_time
                self.location = location
                self.satisfaction_with_previous_work = satisfaction_with_previous_work

    def to_dict(self) -> dict:
        return {
               "contractor_id": self.contractor_id,
               "name": self.name,
               "contact_name": self.contact_name,
               "phone_nr": self.phone_nr,
               "opening_time": self.opening_time,
               "location": self.location,
               "satisfaction_with_previous_work": self.satisfaction_with_previous_work
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
                contractor_id=data["contractor_id"],
                name=data["name"],
                contact_name=data["contact_name"],
                phone_nr=data["phone_nr"],
                opening_time=data["opening_time"],
                location=data["location"],
                satisfaction_with_previous_work=data["satisfaction_with_previous_work"]

           )