from Logic_layer.LogicWrapper import LogicWrapper
from Models.WorkOrder import WorkOrder
from datetime import datetime

logic_wrapper = LogicWrapper()

def CreateWorkOrder():
    #Þarf ekki að vera function hérna í UI, þetta er bara dæmi hvernig virkar.
    #nota input() til að fá svörin neðan.
    """
    Creates a work order.
    """
    
    work_order_obj = WorkOrder()
    work_order_obj.work_order_id = 2
    work_order_obj.work_to_be_done = "fix heater"
    work_order_obj.property = "Home"
    work_order_obj.submitting_supervisor = "Bob"
    work_order_obj.date = datetime.now()
    work_order_obj.priority = "High"
    work_order_obj.work_order_status = "Complete"

    logic_wrapper.CreateWorkOrder(work_order_obj)

def ChangeWorkOrderInfo():
    #Þarf ekki að vera function hérna í UI, þetta er bara dæmi hvernig virkar.
    #notar input() til að velja hvaða field þú vilt breyta, setti bara property. 
    new_data = input()
    logic_wrapper.ChangeWorkOrderInfo(2, 'property', new_data)