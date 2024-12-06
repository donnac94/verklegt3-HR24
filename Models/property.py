class Property:
    def __init__(self, property_id, address, location, property_condition, manager, requires_maintenance):
        self.property_id = property_id
        self.address = address
        self.location = location
        self.property_condition = property_condition
        self.manager = manager
        self.requires_maintenance = requires_maintenance.split(", ") if isinstance(requires_maintenance, str) else requires_maintenance

    def to_dict(self):
        return {
            "property_id": self.property_id,
            "address": self.address,
            "location": self.location,
            "property_condition": self.property_condition,
            "manager": self.manager,
            "requires_maintenance": ", ".join(self.requires_maintenance)
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            property_id=data["property_id"],
            address=data["address"],
            location=data["location"],
            property_condition=data["property_condition"],
            manager=data["manager"],
            requires_maintenance=data["requires_maintenance"]
        )