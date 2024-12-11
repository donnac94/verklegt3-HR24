class Property:
    def __init__(self, property_id, address, location, property_condition, supervisor, requires_maintenance):
        self.property_id = property_id
        self.address = address
        self.location = location
        self.property_condition = property_condition
        self.supervisor = supervisor
        if isinstance(requires_maintenance, str):
            self.requires_maintenance = [item.strip() for item in requires_maintenance.split(",") if item.strip()]
        elif isinstance(requires_maintenance, list):
            self.requires_maintenance = [str(item).strip() for item in requires_maintenance if item]
        else:
            self.requires_maintenance = []

    def to_dict(self):
        return {
            "property_id": self.property_id,
            "address": self.address,
            "location": self.location,
            "property_condition": self.property_condition,
            "supervisor": self.supervisor,
            "requires_maintenance": ", ".join(self.requires_maintenance)
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