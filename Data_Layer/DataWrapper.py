from Data_Layer.EmployeeData import EmployeeData
from Data_Layer.PropertyData import PropertyData
from Data_Layer.WorkOrderData import WorkOrderData
from Models.WorkOrder import WorkOrder

class DataWrapper:
    def __init__(self, employee_file: str, property_file: str):
        self.employee_data = EmployeeData(file_name=employee_file)
        self.property_data = PropertyData(file_name=property_file)
        self.work_order_data = WorkOrderData()

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