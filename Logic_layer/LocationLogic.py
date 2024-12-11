from Models.location import Location
from Data_Layer.DataWrapper import DataWrapper

class LocationLogic:
    
    def __init__(self):
        self.data_wrapper = DataWrapper()
        
    
    def list_locations(self) -> list[Location]:
        return self.data_wrapper.list_location()
        
    