from Data_Layer.PropertyData import PropertyData
from Logic_layer.ContractorLogic import ContractorLogic
from Logic_layer.EmployeeLogic import EmployeeLogic
from Logic_layer.MaintenanceReportLogic import MaintenanceReportLogic
from Logic_layer.PropertyLogic import PropertyLogic
from Logic_layer.WorkOrderLogic import WorkOrderLogic
from Models.WorkOrder import WorkOrder

class LogicWrapper:
    def __init__(self, contractor_logic: ContractorLogic, employee_logic: EmployeeLogic, 
                 maintenance_report_logic: MaintenanceReportLogic, property_logic: PropertyLogic, 
                 work_order_logic: WorkOrderLogic):
        self.contractor_logic = contractor_logic
        self.employee_logic = employee_logic
        self.maintenance_report_logic = maintenance_report_logic
        self.property_logic = property_logic
        self.work_order_logic = work_order_logic

    # WorkOrderLogic
    def CreateWorkOrder(self, work_order_obj: WorkOrder) -> bool:
        """Takes in a WorkOrder object and forwards it to the data layer.
        
        :param WorkOrder work_order_obj: The WorkOrder object to save.
        :return: True if the work order was created successfully, False otherwise.
        """
        return self.work_order_logic.CreateWorkOrder(work_order_obj)

    # PropertyLogic
    def list_properties(self) -> list:
        """Retrieve all properties as Property objects.
        
        :return: A list of Property objects.
        """
        return self.property_logic.list_properties()

    def add_property(self, property_data: dict) -> bool:
        """Add a new property.
        
        :param dict property_data: A dictionary containing property details.
        :return: True if the property was added successfully, False otherwise.
        """
        return self.property_logic.add_property(property_data)

    def update_property(self, property_id: int, updated_data: dict) -> bool:
        """Update a property's information.
        
        :param int property_id: The ID of the property to update.
        :param dict updated_data: A dictionary containing updated field values.
        :return: True if the update was successful, False otherwise.
        """
        return self.property_logic.update_property(property_id, updated_data)

    def get_property_by_id(self, property_id: int):
        """Search for a specific property by ID.
        
        :param int property_id: The ID of the property to search for.
        :return: A Property object if found, None otherwise.
        """
        return self.property_logic.get_property_by_id(property_id)

    def get_maintenance_history(self, property_id: int) -> list:
        """Retrieve the maintenance history of a property.
        
        :param int property_id: The ID of the property.
        :return: A list of maintenance records for the property, or an empty list if none are found.
        """
        return self.property_logic.get_maintenance_history(property_id)

    # EmployeeLogic
    def list_employees(self) -> list:
        """Retrieve all employees as Employee objects.
        
        :return: A list of Employee objects.
        """
        return self.employee_logic.list_employees()

    def register_employee(self, employee_details: dict) -> str:
        """Register a new employee.
        
        :param dict employee_details: A dictionary containing employee details.
        :return: A success message if the employee was registered successfully.
        """
        return self.employee_logic.register_employee(employee_details)
        return self.work_order_logic.GetAllWorkOrders()
    
    def ChangeWorkOrderInfo(self, work_order_id, field, new_data):
        """
        Change the information of a work order.
        """
        return self.work_order_logic.ChangeWorkOrderInfo(work_order_id, field, new_data)
