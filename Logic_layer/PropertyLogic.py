from Data_Layer.DataWrapper import DataWrapper
from Models.property import Property

class PropertyLogic:
    def __init__(self):
        self.data_wrapper = DataWrapper()

    def add_property(self, property_details: dict) -> str:
        new_property = Property(
            property_id=property_details["property_id"],
            address=property_details["address"],
            location=property_details["location"],
            property_condition=property_details["property_condition"],
            supervisor=property_details["supervisor"],
            requires_maintenance=property_details["requires_maintenance"]
        )
        self.data_wrapper.add_property(new_property)
        return "Property added successfully."

    def list_properties(self) -> list[Property]:
        properties = self.data_wrapper.list_properties()
        if not properties:
            return []
        return properties

    def update_property(self, property_id, updated_details: dict) -> str:
        self.data_wrapper.update_property(property_id, updated_details)
        return "Property updated successfully."

    def get_property_by_id(self, property_id):
        properties = self.data_wrapper.list_properties()
        for property in properties:
            if property.property_id == property_id:
                return property
        raise ValueError(f"Property with ID {property_id} not found.")