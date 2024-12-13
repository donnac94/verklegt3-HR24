class Property:
    def __init__(self, property_id:int, address:str, location:str, property_condition:str, supervisor:str, requires_maintenance:str):
        self.property_id = property_id
        self.address = address
        self.location = location
        self.property_condition = property_condition
        self.supervisor = supervisor
        self.requires_maintenance = requires_maintenance

    def to_dict(self):
        return {
            "property_id": self.property_id,
            "address": self.address,
            "location": self.location,
            "property_condition": self.property_condition,
            "supervisor": self.supervisor,
            "requires_maintenance": self.requires_maintenance
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            property_id=data["property_id"],
            address=data["address"],
            location=data["location"],
            property_condition=data["property_condition"],
            supervisor=data["supervisor"],
            requires_maintenance=data["requires_maintenance"]
        )