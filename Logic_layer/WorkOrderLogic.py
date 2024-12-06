from Data_Layer.DataWrapper import DataWrapper
from Models.WorkOrder import WorkOrder


class WorkOrderLogic:
    def __init__(self, data_wrapper: DataWrapper):
        self.data_wrapper = data_wrapper

    def CreateWorkOrder(self, work_order_obj: WorkOrder):
        """Takes in a WorkOrder object and forwards it to the data layer.
        :param WorkOrder work_order_obj: The WorkOrder object to save."""
        return self.data_wrapper.CreateWorkOrder(work_order_obj)


    def ListWorkOrders(self):
        pass


    def ChangeWorkOrderInfo(self):
        pass


    def CloseWorkOrder(self):
        pass


    def ReopenWorkOrder(self):
        pass  