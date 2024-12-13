import csv
from Models.property import Property

class PropertyData:
    def __init__(self):
        self.file_name = "Files/properties.csv"

    def add_property(self, property: Property) -> None:
        """
        Reads the csv file properties.csv and writes the user input using the dictwriter 
        """
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["property_id", "address", "location", "property_condition", "supervisor", "requires_maintenance"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:  
                writer.writeheader()

            writer.writerow(property.to_dict())

    def get_all_properties(self) -> list[Property]:
        """
        Reads the the file properties returns it as a list 
        """
        properties = []
        try:
            with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    properties.append(Property.from_dict(row))
        except FileNotFoundError:
            return []
        return properties

    def update_property(self, property_id, updated_details: dict):
        """
        Updates the property
        :Gets all the the properties and opens the csv file 
        :returns the new value of the property 
        """
        properties = self.get_all_properties()
        property_found = False

        for property in properties:
            if property.property_id == property_id:
                for key, value in updated_details.items():
                    if hasattr(property, key):
                        setattr(property, key, value)
                property_found = True
                break

        if not property_found:
            raise ValueError(f"Property with ID {property_id} not found.")

        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["property_id", "address", "location", "property_condition", "supervisor", "requires_maintenance"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for property in properties:
                writer.writerow(property.to_dict())

    def load_locations(self):
        """
        reads the locations from the csv file
        
        valueerror: will stop the program if there is no airport in the csv file or supervisor
        """
        locations = {}
        with open(self.file_name, mode='r') as file:
            reader = csv.DictReader(file)
            if 'airport' not in reader.fieldnames or 'supervisor' not in reader.fieldnames:
                raise KeyError("CSV file is missing required headers: 'airport' and 'supervisor'")
            for row in reader:
                locations[row['airport']] = row['supervisor']
        return locations