from Data_Layer.PropertyData import PropertyData
from Models.property import Property

class PropertyLogic:
    def __init__(self, property_data: PropertyData):
        self.property_data = property_data

    def add_property(self, property_details: dict) -> str:
        new_property = Property(
            property_id=property_details["property_id"],
            address=property_details["address"],
            location=property_details["location"],
            property_condition=property_details["property_condition"],
            manager=property_details["manager"],
            requires_maintenance=property_details["requires_maintenance"]
        )
        self.property_data.add_property(new_property)
        return "Property added successfully."

    def list_properties(self) -> list[Property]:
        return self.property_data.get_all_properties()

    def update_property(self, property_id, updated_details: dict) -> str:
        self.property_data.update_property(property_id, updated_details)
        return "Property updated successfully."

    def get_property_by_id(self, property_id):
        return self.property_data.get_property_by_id(property_id)