from Logic_layer.ContractorLogic import ContractorLogic
from Logic_layer.EmployeeLogic import EmployeeLogic
from Logic_layer.MaintenanceReportLogic import MaintenanceReportLogic
from Logic_layer.PropertyLogic import PropertyLogic
from Logic_layer.WorkOrderLogic import WorkOrderLogic
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

    # PropertyLogic
    def get_maintenance_history(self, property_id: int) -> list:
        return self.property_logic.get_maintenance_history(property_id)

    def list_properties(self) -> list:
        return self.property_logic.list_properties()

    def add_property(self, property_details: dict) -> str:
        return self.property_logic.add_property(property_details)

    def update_property(self, property_id, updated_details: dict) -> str:
        return self.property_logic.update_property(property_id, updated_details)

    def get_property_by_id(self, property_id):
        return self.property_logic.get_property_by_id(property_id)
    
    def automatic_property_id(self):
        return self.property_logic.automatic_property_id()

    # EmployeeLogic
    def list_employees(self) -> list:
        return self.employee_logic.list_employees()

    def register_employee(self, employee_details: dict) -> str:
        return self.employee_logic.register_employee(employee_details)

    def change_employee_info(self, ssn, field, new_value):
        return self.employee_logic.change_employee_info(ssn, field, new_value)

    def search_employee_by_ssn(self, ssn: str) -> Employee:
        return self.employee_logic.search_employee_by_ssn(ssn)

    # WorkOrderLogic
    def create_work_order(self, work_order_details: dict):
        return self.work_order_logic.create_work_order(work_order_details)
    
    def get_all_work_orders(self) -> list:
        return self.work_order_logic.get_all_work_orders()
    
    def get_work_order_by_id(self, work_order_id: str) -> WorkOrder:
        return self.work_order_logic.get_work_order_by_id(work_order_id)
    
    def change_work_order_info(self, work_order_id, field, new_data):
        return self.work_order_logic.change_work_order_info(work_order_id, field, new_data)
    
    def close_work_order(self, work_order_id: str) -> str:
        return self.work_order_logic.close_work_order(work_order_id)
    
    def reopen_work_order(self, work_order_id: str) -> str:
        return self.work_order_logic.reopen_work_order(work_order_id)
    
    def automatic_work_order_id(self):
        return self.work_order_logic.automatic_work_order_id()
    
    # ContractorLogic
    def create_contractor(self, contractor_details: dict):
        return self.contractor_logic.create_contractor(contractor_details)
    
    def list_contractors(self) -> list:
        return self.contractor_logic.list_contractors()
    
    def change_contractor_info(self, contractor_id, field, updated_contractor):
        return self.contractor_logic.change_contractor_info(contractor_id, field, updated_contractor)
    
    def get_contractor_by_id(self, contractor_id):
        return self.contractor_logic.get_contractor_by_id(contractor_id)
    
    def automatic_contractor_id(self):
        return self.contractor_logic.automatic_contractor_id()
    
    # MaintenanceReportLogic
    def submit_maintenance_report(self, report_details: dict):
        return self.maintenance_report_logic.submit_maintenance_report(report_details)
    
    def get_all_maintenance_reports(self) -> list[MaintenanceReport]:
        return self.maintenance_report_logic.get_all_maintenance_reports()
    
    def change_maintenance_report_info(self, maintenance_report_id, field, new_value):
        return self.maintenance_report_logic.change_maintenance_report_info(maintenance_report_id, field, new_value)
    
    def mark_report_as_finished(self, maintenance_report_id: int) -> str:
        return self.maintenance_report_logic.mark_report_as_finished(maintenance_report_id)
    
    def close_maintenance_report(self, maintenance_report_id: int) -> str:
        return self.maintenance_report_logic.close_maintenance_report(maintenance_report_id)

    def reopen_maintenance_report(self, maintenance_report_id: int) -> str:
        return self.maintenance_report_logic.reopen_maintenance_report(maintenance_report_id)