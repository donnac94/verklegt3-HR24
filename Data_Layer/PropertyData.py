import csv
from Models.property import Property

class PropertyData:
    """
    This class is responsible for handling the data of the properties.
    """

    def __init__(self, file_name="Files/properties.csv"):
        self.file_name = file_name

    def add_property(self, property_obj: Property) -> bool:
        """
        Add a new property to the CSV file.
        :param property_obj: Property object containing property details.
        :return: True if the property was successfully added, False otherwise.
        """
        try:
            with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=[
                    "property_id", "address", "location", "property_condition", "manager", "requires_maintenance"
                ])
                # Write header only if the file is empty
                if csvfile.tell() == 0:
                    writer.writeheader()

                writer.writerow(property_obj.to_dict())
            return True
        except Exception as e:
            raise Exception(f"Error saving property: {e}")

    def get_all_properties(self) -> list[Property]:
        """
        Retrieve all properties from the CSV file.
        :return: A list of Property objects.
        """
        properties = []
        try:
            with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    property_obj = Property.from_dict(row)
                    properties.append(property_obj)
            return properties
        except FileNotFoundError:
            return []  # Return an empty list if the file doesn't exist
        except Exception as e:
            raise Exception(f"Error retrieving properties: {e}")

    def get_property_by_id(self, property_id: int) -> dict:
        """
        Retrieve a property by its ID.
        :param property_id: The ID of the property to retrieve.
        :return: A dictionary representation of the property, or None if not found.
        """
        properties = self.get_all_properties()
        for property_obj in properties:
            if property_obj.property_id == property_id:
                return property_obj.to_dict()
        return None

    def update_property(self, property_id: int, updated_property: Property) -> bool:
        """
        Update a property in the CSV file.
        :param property_id: The ID of the property to update.
        :param updated_property: The updated Property object.
        :return: True if the update was successful, False otherwise.
        """
        success = False
        try:
            properties = self.get_all_properties()
            with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=[
                    "property_id", "address", "location", "property_condition", "manager", "requires_maintenance"
                ])
                writer.writeheader()

                for property_obj in properties:
                    if property_obj.property_id == property_id:
                        # Replace with updated property
                        property_obj = updated_property
                        success = True
                    writer.writerow(property_obj.to_dict())
            return success
        except Exception as e:
            raise Exception(f"Error updating property: {e}")