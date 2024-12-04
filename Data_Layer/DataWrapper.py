from Data_Layer.EmployeeData import EmployeeData
# from Data_Layer.MaintenanceReportData import MaintenanceReportData
from Data_Layer.PropertyData import PropertyData
from Data_Layer.WorkOrderData import WorkOrderData
# from Data_Layer.ContractorData import ContractorData

class DataWrapper():
    def __init__(self):
        self.employee_data = EmployeeData()
        # self.maintenance_report_data = MaintenanceReportData()
        self.property_data = PropertyData()
        self.work_order_data = WorkOrderData()
        # self.contractor_data = ContractorData()

    def CreateWorkOrder(self, WorkOrder):
        return self.work_order_data.CreateWorkOrder(WorkOrder)