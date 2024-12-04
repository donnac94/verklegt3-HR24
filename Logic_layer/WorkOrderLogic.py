from Data_Layer.DataWrapper import DataWrapper

class WorkOrderLogic:
    def __init__(self):
        self.data_wrapper = DataWrapper()
        self.file_name = "Files/work_orders.csv"

    def CreateWorkOrder(self, WorkOrder):
        return self.data_wrapper.CreateWorkOrder(WorkOrder)


    def ListWorkOrders(self):
        pass


    def ChangeWorkOrderInfo(self):
        pass


    def CloseWorkOrder(self):
        pass


    def ReopenWorkOrder(self):
        pass  