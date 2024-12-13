from Data_Layer.DataWrapper import DataWrapper
from Data_Layer.PropertyData import PropertyData
from Models.property import Property

class PropertyLogic:
    def __init__(self):
        self.data_wrapper = DataWrapper()
        self.property_data = PropertyData()

    def add_property(self, property_details: dict) -> str:
        """
        Adds a new property 
        :takes all the existing properties and compares them to check if the new property exist
        :if the property exist there will be a error message else the new property will be added
        """
        # Check if property already in system
        existing_properties = self.data_wrapper.list_properties()
        for property in existing_properties:
            if property.address == property_details["address"]:
                raise ValueError ("Error: Property with this address already exists in the system.")

        # Validate location
        # locations = self.property_data.load_locations()
        # if property_details["location"] not in locations:
        #     return "Error: Invalid location. Please enter a valid location from the locations list."

        # # Automatically assign supervisor based on location
        # property_details["supervisor"] = locations[property_details["location"]]

        new_property = Property(
            property_id=property_details["property_id"],
            address=property_details["address"],
            location=property_details["location"],
            property_condition=property_details["property_condition"],
            supervisor=property_details["supervisor"],
            requires_maintenance=property_details["requires_maintenance"] #[item.strip() for item in property_details["requires_maintenance"] if item.strip()]
        )
        self.data_wrapper.add_property(new_property)
        return "Property added successfully."

    def list_properties(self) -> list[Property]:
        """Takes all the properties and returns them in a list  """
        properties = self.data_wrapper.list_properties()
        if not properties:
            return []
        return properties

    def update_property(self, property_id, updated_details: dict) -> str:
        """
        Updates the property info and returns the new value 
        """
        if "requires_maintenance" in updated_details:
            updated_details["requires_maintenance"] = [item.strip() for item in updated_details["requires_maintenance"] if item.strip()]
        self.data_wrapper.update_property(property_id, updated_details)
        return "Property updated successfully."

    def get_property_by_id(self, property_id):
        """
        Gets all the properties
        :will check if the all the properties and return the property by the id 
        :if the id does not exist then there will be a error message that says that the input was invalid
        """
        properties = self.data_wrapper.list_properties()
        for property in properties:
            if property.property_id == property_id:
                return property
        raise ValueError(f"Property with ID {property_id} not found.")

    def property_exists(self, address: str) -> bool:
        """
        Checks if the property exists or not
        :if the address exists it will return True
        :else if the address does not exist it will return False
        """
        existing_properties = self.data_wrapper.list_properties()
        for property in existing_properties:
            if property.address == address:
                return True
        return False
    
    def automatic_property_id(self):
        """
    Generate the next property ID by incrementing the highest existing ID.
    If no properties exist, start with ID 1.
    """
        properties = self.list_properties()  # Fetch all properties
        if not properties:  # Check if the list is empty
            return 1  # Start IDs from 1 if the list is empty
        latest_property = properties[-1]  # Get the last property
        latest_id = int(latest_property.property_id)  # Extract its ID
        return latest_id + 1  # Increment and return the new ID

