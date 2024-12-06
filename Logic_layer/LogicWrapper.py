from Logic_layer.ContractorLogic import ContractorLogic
from Logic_layer.EmployeeLogic import EmployeeLogic
from Logic_layer.MaintenanceReportLogic import MaintenanceReportLogic
from Logic_layer.PropertyLogic import PropertyLogic
from Logic_layer.WorkOrderLogic import WorkOrderLogic
from Models.employee import Employee

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

    # EmployeeLogic
    def list_employees(self) -> list:
        return self.employee_logic.list_employees()

    def register_employee(self, employee_details: dict) -> str:
        return self.employee_logic.register_employee(employee_details)

    def change_employee_info(self, ssn, field, new_value):
        employees = self.list_employees()
        employee = next((emp for emp in employees if emp.ssn == ssn), None)
        if not employee:
            return f"Employee with SSN {ssn} not found."

        if hasattr(employee, field):
            setattr(employee, field, new_value)
            return self.employee_logic.change_employee_info(ssn, field, new_value)
        else:
            return f"Field {field} does not exist in employee data."

    def search_employee_by_ssn(self, ssn: str) -> Employee:
        employees = self.list_employees()
        return next((emp for emp in employees if emp.ssn == ssn), None)

    # WorkOrderLogic
    def create_work_order(self, work_order_obj):
        return self.work_order_logic.CreateWorkOrder(work_order_obj)
    
    def get_all_work_orders(self) -> list:
        return self.work_order_logic.GetAllWorkOrders()
    
    def change_work_order_info(self, work_order_id, field, new_data):
        return self.work_order_logic.ChangeWorkOrderInfo(work_order_id, field, new_data)