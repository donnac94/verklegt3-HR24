import csv 
from Models.location import Location

class LocationData:
    
    def __init__(self):
        self.file_name = "Files/locations.csv"
    
    
    def get_all_locations(self) -> list[Location]:
        """
        Retrieve all locations from the CSV file.
        :return: A list of location objects.
        """
        locations = []
        try:
            with open(self.file_name, 'r', ) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    locations.append(Location.from_dict_loc(row))
        except FileNotFoundError:
            return None
        return locations