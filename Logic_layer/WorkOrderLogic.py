from Data_Layer.DataWrapper import DataWrapper
from Models.WorkOrder import WorkOrder


class WorkOrderLogic:
    def __init__(self):
        self.data_wrapper = DataWrapper()
        self.file_name = "Files/work_orders.csv"

    def CreateWorkOrder(self, work_order_obj: WorkOrder):
        """Takes in a WorkOrder object and forwards it to the data layer.
        :param WorkOrder work_order_obj: The WorkOrder object to save."""
        return self.data_wrapper.CreateWorkOrder(work_order_obj)


    def GetAllWorkOrders(self) -> list[WorkOrder]:
        """
        Retrieve all work orders from the CSV file.
        :return: A list of work order objects or raises an exception.
        """
        return self.data_wrapper.GetAllWorkOrders()


    def ChangeWorkOrderInfo(self):
        pass


    def CloseWorkOrder(self):
        pass


    def ReopenWorkOrder(self):
        pass  