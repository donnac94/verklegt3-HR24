from Data_Layer.DataWrapper import DataWrapper
from Models.WorkOrder import WorkOrder


class WorkOrderLogic:
    def __init__(self):
        self.data_wrapper = DataWrapper()

    def create_work_order(self, work_order_details: dict) -> str:
        """
        Creates a work order object with specified details and forwards it to the data layer.
        :param dict work_order_details: The details of the work order.
        """
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
    
    def get_work_order_by_id(self, work_order_id: str) -> WorkOrder:
        """
        Retrieve a work order by its ID.
        :param work_order_id: The ID of the work order to retrieve.
        :return: The WorkOrder object if found, otherwise None.
        """
        work_orders = self.get_all_work_orders()
        for work_order in work_orders:
            if work_order.work_order_id == work_order_id:
                return work_order
        return None


    def change_work_order_info(self, work_order_id, field, new_value):
        """
        Change the information of a work order.
        """
        return self.data_wrapper.change_work_order_info(work_order_id, field, new_value)


    def close_work_order(self, work_order_id: str) -> str:
        """
        Close a work order by setting its status to 'Closed'.
        :param work_order_id: The ID of the work order to close.
        :return: A success message if the work order is closed, otherwise an error message.
        """
        work_order = self.get_work_order_by_id(work_order_id)
        if not work_order:
            return "Work order not found."

        self.change_work_order_info(work_order_id, "work_order_status", "Closed")
        return "Work order closed successfully."


    def reopen_work_order(self, work_order_id: str) -> str:
        """
        Reopen a work order by setting its status to 'Open'.
        :param work_order_id: The ID of the work order to reopen.
        :return: A success message if the work order is reopened, otherwise an error message.
        """
        work_order = self.get_work_order_by_id(work_order_id)
        if not work_order:
            return "Work order not found."

        self.change_work_order_info(work_order_id, "work_order_status", "Open")
        maintenance_reports = self.data_wrapper.get_all_maintenance_reports()
        for maintenance_report in maintenance_reports:
            if maintenance_report.connected_work_order_id == work_order_id:
                self.data_wrapper.change_maintenance_report_info(maintenance_report.maintenance_report_id, 'report_closed', False)
        return "Work order and connected maintenance report reopened successfully."
    
    def automatic_work_order_id(self):
        work_orders = self.get_all_work_orders()
        if not work_orders:
            return 1
        latest_work_order = work_orders[-1]
        return int(latest_work_order.work_order_id) + 1