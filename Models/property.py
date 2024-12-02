class Property():
    """
    Model that containts information about a single property
    """

    def __init__(
            self,
            location_id: int,
            property_condition: str,
            requires_maintenance: list[str] = []
    ) -> None:
        """
        :param int location_id: the unique id for this location.
        :param str property_condition: A description of the condition of the property.
        :param list[str] requires_maintenance: A list of everthing that requires maintenance on the property.
        """
        self.location_id = location_id
        self.property_condition = property_condition
        self.requires_maintenance = requires_maintenance 