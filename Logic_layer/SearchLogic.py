import csv
from Data_Layer.LocationData import LocationData
from Data_Layer.EmployeeData import EmployeeData
from Data_Layer.PropertyData import PropertyData
from Data_Layer.WorkOrderData import WorkOrderData
from Data_Layer.ContractorData import ContractorData
from Data_Layer.MaintenanceReportData import MaintenanceReportData
from Data_Layer.DataWrapper import DataWrapper

class SearchLogic:
    
    def __init__(self):
        self.file_name_location = ('Files/locations.csv')
        self.file_name_employees = ('Files/employees.csv')
        self.file_name_properties = ('Files/properties.csv')
        self.file_name_workorder = ('Files/work_orders.csv')
        
    def search_by_location(self, location):
        """Search employees by location"""
        results = []
        try:
            with open(self.file_name_employees, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if location.lower() in row.get("location", "").lower():
                        results.append(row)
            return results
        except FileNotFoundError:
            return "Employee file not found"
                     
    def search_employee_by_ssn(self, ssn):
        """Search employees by SSN"""
        try:
            with open(self.file_name_employees, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if ssn == row.get("ssn", ""):
                        return row
            return "No Employee found with that ssn"
        except FileNotFoundError:
            return "Employee file not found"
        
    def search_property_id(self, property_id):
        """Search for a property by id"""
        try:
            with open(self.file_name_properties, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if property_id == row.get("property_id", ""):
                        return row
            return "No property found"
        except FileNotFoundError:
            return "Property no found on file"
        
    def search_workorder_id(self, workorder_id):
        """Search for Workorder id"""
        try:
            with open(self.file_name_workorder, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if workorder_id == row.get("workorder_id", ""):
                        return row
            return "No workorder found"
        except FileNotFoundError:
            return "File does not exist"