import csv
from Models.WorkOrder import WorkOrder

class WorkOrderData():

    def __init__(self):
        self.file_name = "Files/work_orders.csv"

    def CreateWorkOrder(self, WorkOrder):
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
                fieldnames = ["work_order_id","work_to_be_done","property","submitting_manager","date","priority","work_order_status"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writerow({
                    'work_order_id': WorkOrder.work_order_id,
                    'work_to_be_done': WorkOrder.work_to_be_done,
                    'property': WorkOrder.property,
                    'submitting_manager': WorkOrder.submitting_manager,
                    'date': WorkOrder.date,
                    'priority': WorkOrder.priority,
                    'work_order_status': WorkOrder.work_order_status
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