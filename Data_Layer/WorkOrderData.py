import csv
from Models.WorkOrder import WorkOrder

class WorkOrderData():

    def __init__(self):
        self.file_name = "Files/work_orders.csv"

    def create_work_order(self, work_order_obj: WorkOrder) -> None:
        """
        Register a work order in the CSV file.
        :param WorkOrder work_order_obj: The WorkOrder object to save.
        """
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["work_order_id", "work_to_be_done", "property", "submitting_supervisor", "date", "priority", "work_order_status"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(work_order_obj.to_dict())

    def get_all_work_orders(self) -> list[WorkOrder]:
        """
        Retrieve all work orders from the CSV file.
        :return: A list of work orders.
        """
        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            return [WorkOrder.from_dict(row) for row in reader]

    def change_work_order_info(self, work_order_id: int, field: str, new_value: str):
        """
        Change the information of a work order.
        """
        work_orders = self.get_all_work_orders()
        work_order_found = False

        for work_order in work_orders:
            if work_order.work_order_id == work_order_id:
                setattr(work_order, field, new_value)
                work_order_found = True

        if not work_order_found:
            raise ValueError(f"Work order with ID {work_order_id} not found.")

        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["work_order_id", "work_to_be_done", "property", "submitting_supervisor", "date", "priority", "work_order_status"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for work_order in work_orders:
                writer.writerow(work_order.to_dict())