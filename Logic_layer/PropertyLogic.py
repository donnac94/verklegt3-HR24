from Models.property import Property

class PropertyLogic:
    """
    Logic layer for managing property operations.
    """

    def __init__(self, data_layer):
        self.data_layer = data_layer

    def list_properties(self) -> list[Property]:
        return self.data_layer.get_all_properties()

    def add_property(self, property_details: dict) -> str:
        property_obj = Property.from_dict(property_details)
        existing_property = self.data_layer.get_property_by_id(property_obj.property_id)
        if existing_property:
            return "Property ID already exists."
        if self.data_layer.add_property(property_obj):
            return "Property added successfully."
        return "Failed to add property."

    def update_property(self, property_id: int, updated_data: dict) -> str:
        existing_property = self.data_layer.get_property_by_id(property_id)
        if not existing_property:
            return "Property not found."
        updated_property = Property.from_dict({**existing_property, **updated_data})
        if self.data_layer.update_property(property_id, updated_property):
            return "Property updated successfully."
        return "Failed to update property."

    def get_all_properties(self) -> list[Property]:
        return self.data_layer.get_all_properties()