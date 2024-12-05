from Logic_layer.ContractorLogic import ContractorLogic
from Logic_layer.EmployeeLogic import EmployeeLogic
from Logic_layer.MaintenanceReportLogic import MaintenanceReportLogic
from Logic_layer.PropertyLogic import PropertyLogic
from Logic_layer.WorkOrderLogic import WorkOrderLogic

class LogicWrapper:
    def __init__(self):
        self.contractor_logic = ContractorLogic()
        self.employee_logic = EmployeeLogic()
        self.maintenance_report_logic = MaintenanceReportLogic()
        self.property_logic = PropertyLogic()
        self.work_order_logic = WorkOrderLogic()

    def CreateWorkOrder(self, WorkOrder):
        return self.work_order_logic.CreateWorkOrder(WorkOrder)