from Models.property import Property

class PropertyLogic:
    def register_property(properties: list[Property], property_details: dict) -> str:
        """
        Register a new property.
        :param properties: List of existing properties.
        :param property_details: Dictionary containing property details.
        :return: Success or error message.
        """
        property_id = property_details.get("property_id")
        if any(p.property_id == property_id for p in properties):
            return "Property ID already exists."

        new_property = Property(
            property_id=property_id,
            address=property_details.get("address"),
            location=property_details.get("location"),
            property_condition=property_details.get("property_condition"),
            manager=property_details.get("manager"),
        )
        properties.append(new_property)
        return "Property registered successfully."

    def list_properties(properties: list[Property]) -> list:
        """
        List all properties.
        :param properties: List of existing properties.
        :return: A list of properties.
        """
        return properties if properties else []

    def change_property_info(properties: list[Property], property_id: int, updated_details: dict) -> str:
        """
        Change information of an existing property.
        :param properties: List of existing properties.
        :param property_id: ID of the property to update.
        :param updated_details: Dictionary containing updated property details.
        :return: Success or error message.
        """
        property_to_edit = next((p for p in properties if p.property_id == property_id), None)

        if not property_to_edit:
            return "Property not found."

        property_to_edit.address = updated_details.get("address", property_to_edit.address)
        property_to_edit.location = updated_details.get("location", property_to_edit.location)
        property_to_edit.property_condition = updated_details.get("property_condition", property_to_edit.property_condition)
        property_to_edit.manager = updated_details.get("manager", property_to_edit.manager)

        return "Property updated successfully."