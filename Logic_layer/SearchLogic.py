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
    
    
    def search_by_location(self, location_id):
        pass
    
    def search_employee_by_ssn(self, ssn):
        pass
    
    def search_property_id(self, property_id):
        pass
    
    def search_workorder_id(self, workorder_id):
        pass