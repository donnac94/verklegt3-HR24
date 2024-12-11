from Data_Layer.DataWrapper import DataWrapper
from Models.property import Property

class PropertyLogic:
    def __init__(self):
        self.data_wrapper = DataWrapper()

    def add_property(self, property_details: dict) -> str:

        # Check if property already in system
        existing_properties = self.data_wrapper.list_properties()
        for property in existing_properties:
            if property.address == property_details["address"]:
                return "Error: Property with this address already exists in the system."

        new_property = Property(
            property_id=property_details["property_id"],
            address=property_details["address"],
            location=property_details["location"],
            property_condition=property_details["property_condition"],
            supervisor=property_details["supervisor"],
            requires_maintenance=[item.strip() for item in property_details["requires_maintenance"] if item.strip()]
        )
        self.data_wrapper.add_property(new_property)
        return "Property added successfully."

    def list_properties(self) -> list[Property]:
        properties = self.data_wrapper.list_properties()
        if not properties:
            return []
        return properties

    def update_property(self, property_id, updated_details: dict) -> str:
        if "requires_maintenance" in updated_details:
            updated_details["requires_maintenance"] = [item.strip() for item in updated_details["requires_maintenance"] if item.strip()]
        self.data_wrapper.update_property(property_id, updated_details)
        return "Property updated successfully."

    def get_property_by_id(self, property_id):
        properties = self.data_wrapper.list_properties()
        for property in properties:
            if property.property_id == property_id:
                return property
        raise ValueError(f"Property with ID {property_id} not found.")

    def property_exists(self, address: str) -> bool:
        existing_properties = self.data_wrapper.list_properties()
        for property in existing_properties:
            if property.address == address:
                return True
        return False
    
    def automatic_property_id(self):
        """
        Gets the latest property ID and give it plus 1.
        """
        properties = self.list_properties()
        latest_property = properties[-1]
        latest_id = int(latest_property.property_id)
        return latest_id + 1
