from Logic_layer.LogicWrapper import LogicWrapper
from Models.WorkOrder import WorkOrder
from datetime import datetime

def CreateWorkOrder():
    """
    Creates a work order.
    Needs to be finished, using inputs instead of fixed answers. Also needs a UI.
    """
    logic_wrapper = LogicWrapper()
    work_order = WorkOrder()
    work_order.work_order_id = 2
    work_order.work_to_be_done = "fix heater"
    work_order.property = "Home"
    work_order.submitting_manager = "Bob"
    work_order.date = datetime.now()
    work_order.priority = "High"
    work_order.work_order_status = "Complete"

    logic_wrapper.CreateWorkOrder(work_order)