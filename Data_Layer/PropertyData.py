import csv
from Models.property import Property

class PropertyData():

    def __init__(self):
        self.file_name = "Files/properties.csv"

    def RegisterProperty(self, Property) -> None:
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["property_id","property_condition","requires_maintenance"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({
                'property_id': Property.property_id, 
                'property_condition': Property.property_condition, 
                'requires_maintenance': Property.requires_maintenance
                })

    def GetAllProperties(self) -> list[Property]:
        ret_list=[]
        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Property(row["property_id"], row["property_condition"], row["requires_maintenance"]))
        return ret_list

    def ChangePropertyInfo():
        pass