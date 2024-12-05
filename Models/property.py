class Property:
    """
    Model that contains information about a Property.
    """

    def __init__(
        self,
        property_id: int = 0,
        address: str = "",
        location: str = "",
        property_condition: str = "",
        manager: str = "",
        requires_maintenance: list = None,
    ) -> None:
        self.property_id = property_id
        self.address = address
        self.location = location
        self.property_condition = property_condition
        self.manager = manager
        self.requires_maintenance = requires_maintenance or []

    def to_dict(self) -> dict:
        return {
            "property_id": self.property_id,
            "address": self.address,
            "location": self.location,
            "property_condition": self.property_condition,
            "manager": self.manager,
            "requires_maintenance": ",".join(self.requires_maintenance),
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            property_id=int(data.get("property_id", 0)),
            address=data.get("address", ""),
            location=data.get("location", ""),
            property_condition=data.get("property_condition", ""),
            manager=data.get("manager", ""),
            requires_maintenance=data.get("requires_maintenance", "").split(",") if data.get("requires_maintenance") else []
        )