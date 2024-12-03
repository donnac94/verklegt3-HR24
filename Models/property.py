class Property:
    """
    Model that contains information about a single property.
    """

    def __init__(
        self,
        property_id: int,
        address: str,
        location: str,
        property_condition: str,
        manager: str,
        features: list[str] = [],
        requires_maintenance: list[str] = [],
    ) -> None:
        """
        :param int property_id: The unique ID for this property.
        :param str address: The address of the property.
        :param str location: The geographical location of the property (City, Country).
        :param str property_condition: A description of the condition of the property.
        :param str manager: The manager assigned to oversee the property.
        :param list[str] features: A list of features available in the property (e.g., pool, sauna).
        :param list[str] requires_maintenance: A list of everything that requires maintenance on the property.
        """
        self.property_id = property_id
        self.address = address
        self.location = location
        self.property_condition = property_condition
        self.manager = manager
        self.features = features
        self.requires_maintenance = requires_maintenance

    def __str__(self):
        return (
            f"Property ID: {self.property_id}\n"
            f"Address: {self.address}\n"
            f"Location: {self.location}\n"
            f"Condition: {self.property_condition}\n"
            f"Manager: {self.manager}\n"
            f"Features: {', '.join(self.features)}\n"
            f"Requires Maintenance: {', '.join(self.requires_maintenance)}"
        )
    