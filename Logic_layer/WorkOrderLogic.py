from Data_Layer.DataWrapper import DataWrapper
from Models.WorkOrder import WorkOrder


class WorkOrderLogic:
    def __init__(self, data_wrapper: DataWrapper):
        self.data_wrapper = data_wrapper

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


    def ChangeWorkOrderInfo(self, work_order_id, field, new_data):
        """
        Change the information of a work order.
        """
        return self.data_wrapper.ChangeWorkOrderInfo(work_order_id, field, new_data)


    def CloseWorkOrder(self):
        pass


    def ReopenWorkOrder(self):
        pass  