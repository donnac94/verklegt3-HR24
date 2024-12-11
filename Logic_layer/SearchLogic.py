import csv
from Logic_layer.EmployeeLogic import EmployeeLogic
from Logic_layer.PropertyLogic import PropertyLogic
from Logic_layer.ContractorLogic import ContractorLogic
from Logic_layer.MaintenanceReportLogic import MaintenanceReportLogic
from Logic_layer.LocationLogic import LocationLogic


class SearchLogic:
    
    def __init__(self):
        self.employee_logic = EmployeeLogic
        self.property_logic = PropertyLogic
        self.contractor_logic = ContractorLogic
        self.maintenance_report_logic = MaintenanceReportLogic
        self.location_logic = LocationLogic
    
    def search_by_location(self, location_id) -> list:
        while location_id != None and location_id < 0 and location_id > 100:
            return []
        
        employees_at_location = []
        
        if location_id in self.location_logic:
            employees_at_location = self.location_logic[location_id]
            
            return employees_at_location
            # if self.employee_logic and location_id != False:
            #     value = location_id
            #     for value in self.location_logic:
            #         for self.employee_logic in value:
            #             return value
                     
    def search_employee_by_ssn(self, ssn):
        while ssn != None and ssn < 0 and ssn > 10:
            print("Employee does not exist in the system try again")
            return []
        employee_ssn = []
        if ssn in self.employee_logic:
            employee_ssn = self.employee_logic[ssn]
            return employee_ssn
        
    def search_property_id(self, property_id):
        while property_id != None and property_id < 0 and property_id > 100:
            return []
        property_search_id = []
        if property_id in self.property_logic:
            property_search_id = self.property_logic[property_id]
            return property_search_id
        
    def search_workorder_id(self, workorder_id):
        while workorder_id != None and workorder_id < 0 and workorder_id > 100:
            return []
    
        workorder_search_id = []
        if workorder_search_id in self.maintenance_report_logic:
            workorder_search_id = self.maintenance_report_logic[workorder_id]
            
            return workorder_search_id