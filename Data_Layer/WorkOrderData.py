import csv
from Models.WorkOrder import WorkOrder

class WorkOrderData():

    def __init__(self):
        self.file_name = "Files/work_orders.csv"

    def CreateWorkOrder(self, work_order_obj: WorkOrder) -> str:
        """
        Register a work order in the csv file.
        :param WorkOrder work_order_obj: The WorkOrder object to save.
        :return: Success message or raises an exception.
        """
        try:
            with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
                    fieldnames = ["work_order_id","work_to_be_done","property","submitting_supervisor","date","priority","work_order_status"]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    if csvfile.tell() == 0:
                        writer.writeheader()

                    writer.writerow({
                        'work_order_id': work_order_obj.work_order_id,
                        'work_to_be_done': work_order_obj.work_to_be_done,
                        'property': work_order_obj.property,
                        'submitting_supervisor': work_order_obj.submitting_supervisor,
                        'date': work_order_obj.date,
                        'priority': work_order_obj.priority,
                        'work_order_status': work_order_obj.work_order_status
                        })
            return "Work order registered successfully."
        except Exception as e:
            raise Exception(f"Error saving work order: {e}")

    def GetAllWorkOrders(self) -> list[WorkOrder]:
        """
        Retrieve all work orders from the CSV file.
        :return: A list of work order objects or raises an exception.
        """
        ret_list=[]
        try:
            with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    ret_list.append(WorkOrder(row["work_order_id"], row["work_to_be_done"], row["property"], 
                                            row["submitting_supervisor"], row["date"], row["priority"], row["work_order_status"]))
            return ret_list
        except FileNotFoundError:
            return []  # Return an empty list if the file doesn't exist
        except Exception as e:
            raise Exception(f"Error reading work orders: {e}")
        
    def ChangeWorkOrderInfo(self, work_order_id, field, new_data):
        """
        Change the information of a work order.
        """
        
        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            header = reader.fieldnames
            rows = []
            for row in reader:
                if row['work_order_id'].strip() == str(work_order_id):
                    row[field] = new_data
                rows.append(row)

        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            writer.writerows(rows)


# Bara hægt að nota ChangeWorkOrderInfo í UI til að breyta status.
# Þarf raun ekki sín eigin function held ég
    # def CloseWorkOrder():
    #     pass

    # def ReopenWorkOrder():
    #     pass