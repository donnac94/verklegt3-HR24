import csv
from Models.property import Property


class PropertyData:
    # This class is responsible for handling the data of the properties.
    def __init__(self):
        self.file_name = "Files/properties.csv"

    def RegisterProperty(self, property_obj: Property) -> None:
        """
        Register a new property in the CSV file.
        :param property_obj: The Property object to save.
        """
        try:
            with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
                fieldnames = [
                    "property_id", "address", "location", "property_condition", 
                    "manager", "requires_maintenance"
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                # Write header only if the file is empty
                if csvfile.tell() == 0:
                    writer.writeheader()
                
                writer.writerow({
                    "property_id": property_obj.property_id,
                    "address": property_obj.address,
                    "location": property_obj.location,
                    "property_condition": property_obj.property_condition,
                    "manager": property_obj.manager,
                    "requires_maintenance": ",".join(property_obj.requires_maintenance),
                })
        except Exception as e:
            print(f"Error saving property: {e}")

    def GetAllProperties(self) -> list[Property]:
        """
        Retrieve all properties from the CSV file.
        :return: A list of Property objects.
        """
        ret_list = []
        try:
            with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    ret_list.append(Property(
                        property_id=int(row["property_id"]),
                        address=row["address"],
                        location=row["location"],
                        property_condition=row["property_condition"],
                        manager=row["manager"],
                        requires_maintenance=row["requires_maintenance"].split(","),
                    ))
        except FileNotFoundError:
            print("File not found. Returning an empty list.")
        except Exception as e:
            print(f"Error reading properties: {e}")
        return ret_list

    def ChangePropertyInfo(self, property_id: int, updated_property: Property) -> bool:
        """
        Change the information of a property.
        :param property_id: The ID of the property to update.
        :param updated_property: The updated Property object.
        :return: True if successful, False otherwise.
        """
        success = False
        try:
            properties = self.GetAllProperties()
            with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
                fieldnames = [
                    "property_id", "address", "location", "property_condition", 
                    "manager", "requires_maintenance"
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for property_obj in properties:
                    if property_obj.property_id == property_id:
                        # Replace with updated property
                        property_obj = updated_property
                        success = True
                    writer.writerow({
                        "property_id": property_obj.property_id,
                        "address": property_obj.address,
                        "location": property_obj.location,
                        "property_condition": property_obj.property_condition,
                        "manager": property_obj.manager,
                        "requires_maintenance": ",".join(property_obj.requires_maintenance),
                    })
        except Exception as e:
            print(f"Error updating property: {e}")
        return success