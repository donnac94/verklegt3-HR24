import csv
from Models.WorkOrder import WorkOrder

class WorkOrderData():

    def __init__(self):
        self.file_name = "Files/work_orders.csv"

    def CreateWorkOrder(self, Work_order_obj: WorkOrder):
        """
        Register a work order in the csv file.
        :param WorkOrder work_order_obj: The WorkOrder object to save.
        """
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
                fieldnames = ["work_order_id","work_to_be_done","property","submitting_manager","date","priority","work_order_status"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writerow({
                    'work_order_id': Work_order_obj.work_order_id,
                    'work_to_be_done': Work_order_obj.work_to_be_done,
                    'property': Work_order_obj.property,
                    'submitting_manager': Work_order_obj.submitting_manager,
                    'date': Work_order_obj.date,
                    'priority': Work_order_obj.priority,
                    'work_order_status': Work_order_obj.work_order_status
                    })

    def GetAllWorkOrders(self):
        ret_list=[]
        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(WorkOrder(row["work_order_id"], row["work_to_be_done"], row["property"], 
                                          row["submitting_manager"], row["date"], row["priority"], row["work_order_status"]))
        return ret_list

    def ChangeWorkOrderInfo():
        pass

    def CloseWorkOrder():
        pass

    def ReopenWorkOrder():
        pass