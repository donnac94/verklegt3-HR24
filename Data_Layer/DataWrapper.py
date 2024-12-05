from Data_Layer.EmployeeData import EmployeeData
# from Data_Layer.MaintenanceReportData import MaintenanceReportData
from Data_Layer.PropertyData import PropertyData
from Data_Layer.WorkOrderData import WorkOrderData
# from Data_Layer.ContractorData import ContractorData
from Models.WorkOrder import WorkOrder


class DataWrapper():
    def __init__(self):
        self.employee_data = EmployeeData()
        # self.maintenance_report_data = MaintenanceReportData()
        self.property_data = PropertyData()
        self.work_order_data = WorkOrderData()
        # self.contractor_data = ContractorData()

    def CreateWorkOrder(self, work_order_obj: WorkOrder):
        """
        Register a work order in the csv file.
        :param WorkOrder work_order_obj: The WorkOrder object to save.
        """
        return self.work_order_data.CreateWorkOrder(work_order_obj)
    
    def GetAllWorkOrders(self) -> list[WorkOrder]:
        """
        Retrieve all work orders from the CSV file.
        :return: A list of work order objects or raises an exception.
        """
        return self.work_order_data.GetAllWorkOrders()
    
    def ChangeWorkOrderInfo(self, work_order_id, field, new_data):
        """
        Change the information of a work order.
        """
        return self.work_order_data.ChangeWorkOrderInfo(work_order_id, field, new_data)