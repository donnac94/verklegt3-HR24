
from Data_Layer.DataWrapper import DataWrapper
from Data_Layer.EmployeeData import EmployeeData

class SearchLogic:
    
    def __init__(self):
        self.data_wrapper = DataWrapper
        self.employee_data = EmployeeData
        
        
    def search_by_location(self, location):
        """Search employees by location"""
        try:
            results = []
            location_filter = self.data_wrapper.list_employees(self) #þarf að gera lista sem listar upp starfsmenn eftir location 
            for row in location_filter:
                    if location.row == row.get("location", ""):
                        return row.append(results)
            return results
        except FileNotFoundError:
            return "Employee file not found"
        except UnicodeDecodeError:
            return "Error decoding the file. Please check the file encoding."

    def search_employee_by_ssn(self, ssn):
        """Search employees by SSN"""
        try:
            ssn_filter = self.employee_data.get_all_employees(self)
            for row in ssn_filter:
                    if ssn.row == row.get("ssn", ""):
                        return row
            return "No Employee found with that ssn"
        except FileNotFoundError:
            return "Employee file not found"
        except UnicodeDecodeError:
            return "Error decoding the file. Please check the file encoding."

    def search_property_id(self, property_id):
        """Search for a property by id"""
        try:
            results = []
            property_id_filter = self.data_wrapper.list_properties(self)
            for row in property_id_filter:
                    if property_id.row == row.get("property_id", ""):
                        return row.append(results)
            return "No property found"
        except FileNotFoundError:
            return "Property not found in file"
        except UnicodeDecodeError:
            return "Error decoding the file. Please check the file encoding."

    def search_workorder_id(self, workorder_id):
        """Search for Workorder id"""
        try:
            results = []
            workorder_id_filter = self.data_wrapper.get_property_by_id(self)
            for row in workorder_id_filter:
                    if workorder_id == row.get("workorder_id", ""):
                        return row.append(results)
            return "No workorder found"
        except FileNotFoundError:
            return "File does not exist"
        except UnicodeDecodeError:
            return "Error decoding the file. Please check the file encoding."    
        
    
        
  