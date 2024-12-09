from Data_Layer.DataWrapper import DataWrapper
from Models.WorkOrder import WorkOrder


class WorkOrderLogic:
    def __init__(self):
        self.data_wrapper = DataWrapper()

    def create_work_order(self, work_order_details: dict) -> str:
        """Takes in a WorkOrder object and forwards it to the data layer.
        :param WorkOrder work_order_obj: The WorkOrder object to save."""
        new_work_order = WorkOrder(
            work_order_id=work_order_details["work_order_id"],
            work_to_be_done=work_order_details["work_to_be_done"],
            property=work_order_details["property"],
            submitting_supervisor=work_order_details["submitting_supervisor"],
            date=work_order_details["date"],
            priority=work_order_details["priority"],
            work_order_status=work_order_details["work_order_status"]
        )
        self.data_wrapper.create_work_order(new_work_order)
        return "Work order registered successfully."


    def get_all_work_orders(self) -> list[WorkOrder]:
        """
        Retrieve all work orders from the CSV file.
        :return: A list of work order objects or raises an exception.
        """
        return self.data_wrapper.get_all_work_orders()


    def change_work_order_info(self, work_order_id, field, new_value):
        """
        Change the information of a work order.
        """
        return self.data_wrapper.change_work_order_info(work_order_id, field, new_value)


    def CloseWorkOrder(self):
        pass


    def ReopenWorkOrder(self):
        pass  