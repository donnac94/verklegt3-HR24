from Logic_layer.ContractorLogic import ContractorLogic
from Logic_layer.EmployeeLogic import EmployeeLogic
from Logic_layer.MaintenanceReportLogic import MaintenanceReportLogic
from Logic_layer.PropertyLogic import PropertyLogic
from Logic_layer.WorkOrderLogic import WorkOrderLogic
from Logic_layer.SearchLogic import SearchLogic
from Models.WorkOrder import WorkOrder
from Models.employee import Employee
from Models.maintenance_report import MaintenanceReport


class LogicWrapper:
    def __init__(self):
        self.contractor_logic = ContractorLogic()
        self.employee_logic = EmployeeLogic()
        self.maintenance_report_logic = MaintenanceReportLogic()
        self.property_logic = PropertyLogic()
        self.work_order_logic = WorkOrderLogic()
        self.search_logic = SearchLogic()

    # PropertyLogic
    def list_properties(self) -> list:
        """Returns all the properties as a list"""
        return self.property_logic.list_properties()

    def add_property(self, property_details: dict) -> str:
        """"""
        return self.property_logic.add_property(property_details)

    def update_property(self, property_id, updated_details: dict) -> str:
        """test"""
        return self.property_logic.update_property(property_id, updated_details)

    def get_property_by_id(self, property_id):
        """test"""
        return self.property_logic.get_property_by_id(property_id)
    
    def automatic_property_id(self):
        """test"""
        return self.property_logic.automatic_property_id()

    def property_exists(self, address: str) -> bool:
        """test"""
        return self.property_logic.property_exists(address)

    # EmployeeLogic
    def list_employees(self) -> list:
        """test"""
        return self.employee_logic.list_employees()

    def register_employee(self, employee_details: dict) -> str:
        """test"""
        return self.employee_logic.register_employee(employee_details)

    def change_employee_info(self, ssn, field, new_value):
        """test"""
        return self.employee_logic.change_employee_info(ssn, field, new_value)

    def search_employee_by_ssn(self, ssn: str) -> Employee:
        """test"""
        try:
            return self.employee_logic.search_employee_by_ssn(ssn)
        except ValueError:
            return None

    # WorkOrderLogic
    def create_work_order(self, work_order_details: dict):
        """test"""
        return self.work_order_logic.create_work_order(work_order_details)
    
    def get_all_work_orders(self) -> list:
        """test"""
        return self.work_order_logic.get_all_work_orders()
    
    def get_work_order_by_id(self, work_order_id: str) -> WorkOrder:
        """test"""
        return self.work_order_logic.get_work_order_by_id(work_order_id)
    
    def change_work_order_info(self, work_order_id, field, new_data):
        """test"""
        return self.work_order_logic.change_work_order_info(work_order_id, field, new_data)
    
    def close_work_order(self, work_order_id: str) -> str:
        """test"""
        return self.work_order_logic.close_work_order(work_order_id)
    
    def reopen_work_order(self, work_order_id: str) -> str:
        """test"""
        return self.work_order_logic.reopen_work_order(work_order_id)
    
    def automatic_work_order_id(self):
        """test"""
        return self.work_order_logic.automatic_work_order_id()
    
    def mark_work_order_finished(self, work_order_id: int):
        """test"""
        return self.work_order_logic.mark_work_order_finished(work_order_id)
    
    # ContractorLogic
    def create_contractor(self, contractor_details: dict):
        """test"""
        return self.contractor_logic.create_contractor(contractor_details)
    
    def list_contractors(self) -> list:
        """test"""
        return self.contractor_logic.list_contractors()
    
    def change_contractor_info(self, contractor_id, updated_details: dict) -> str:
        """test"""
        return self.contractor_logic.change_contractor_info(contractor_id, updated_details)
    
    def get_contractor_by_id(self, contractor_id):
        """test"""
        return self.contractor_logic.get_contractor_by_id(contractor_id)
    
    def automatic_contractor_id(self):
        """test"""
        return self.contractor_logic.automatic_contractor_id()
    
    # MaintenanceReportLogic
    def submit_maintenance_report(self, report_details: dict):
        """test"""
        return self.maintenance_report_logic.submit_maintenance_report(report_details)
    
    def get_all_maintenance_reports(self) -> list[MaintenanceReport]:
        """test"""
        return self.maintenance_report_logic.get_all_maintenance_reports()
    
    def change_maintenance_report_info(self, maintenance_report_id, field, new_value):
        """test"""
        return self.maintenance_report_logic.change_maintenance_report_info(maintenance_report_id, field, new_value)
    
    def mark_report_as_finished(self, maintenance_report_id: int) -> str:
        """test"""
        return self.maintenance_report_logic.mark_report_as_finished(maintenance_report_id)
    
    def close_maintenance_report(self, maintenance_report_id: int) -> str:
        """test"""
        return self.maintenance_report_logic.close_maintenance_report(maintenance_report_id)

    def reopen_maintenance_report(self, maintenance_report_id: int) -> str:
        """test"""
        return self.maintenance_report_logic.reopen_maintenance_report(maintenance_report_id)
    
    def get_report_by_id(self, maintenance_report_id: int) -> MaintenanceReport:
        """test"""
        return self.maintenance_report_logic.get_report_by_id(maintenance_report_id)
    #SearchLogic

    def search_employee_by_ssn(self, ssn):
        """Search employees by SSN"""
        return self.search_logic.search_employees_by_ssn(ssn)
    
    def search_employees_by_location(self, location):
        """Search Employees by Location"""
        return self.search_logic.search_employee_by_location(location)
    
    def search_properties_by_location(self, location):
        """Search Properties by their Location"""
        return self.search_logic.search_properties_by_location(location)
    
    def search_property_by_id(self, property_id):
        """Search property by id"""
        return self.search_logic.search_property_by_id(property_id)
    
    def search_work_order_by_id(self, work_order_id):
        """test"""
        return self.search_logic.search_work_order_by_id(work_order_id)
    
    def search_work_orders_by_property(self, property_name):
        """test"""
        return self.search_logic.search_work_orders_by_property(property_name)
    
    def search_maintenance_reports_by_property(self, property_name):
        """test"""
        return self.search_logic.search_maintenance_reports_by_property(property_name)
    
    def search_work_orders_by_employee(self, employee_ssn):
        """test"""
        return self.search_logic.search_work_orders_by_employee(employee_ssn)
    
    def search_maintenance_reports_by_employee(self, employee_ssn):
        """test"""
        return self.search_logic.search_maintenance_reports_by_employee(employee_ssn)
    
    def get_work_plan(self):
        """test"""
        return self.employee_logic.get_work_plan()
    
    def check_if_employee_exists(self, ssn: int):
        return self.employee_logic.check_if_employee_exists(ssn)
