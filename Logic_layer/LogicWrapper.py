

from Data_Layer.PropertyData import PropertyData
from Logic_layer.ContractorLogic import ContractorLogic
from Logic_layer.EmployeeLogic import EmployeeLogic
from Logic_layer.MaintenanceReportLogic import MaintenanceReportLogic
from Logic_layer.PropertyLogic import PropertyLogic
from Logic_layer.WorkOrderLogic import WorkOrderLogic
from Models.WorkOrder import WorkOrder

class LogicWrapper:
    def __init__(self):
        self.contractor_logic = ContractorLogic()
        self.employee_logic = EmployeeLogic()
        self.maintenance_report_logic = MaintenanceReportLogic()
        self.property_data = PropertyData()
        self.property_logic = PropertyLogic(self.property_data)
        self.work_order_logic = WorkOrderLogic()

    # WorkOrderLogic
    def CreateWorkOrder(self, work_order_obj: WorkOrder):
        """Takes in a WorkOrder object and forwards it to the data layer.
        :param WorkOrder work_order_obj: The WorkOrder object to save."""
        return self.work_order_logic.CreateWorkOrder(work_order_obj)

    # PropertyLogic
    def list_properties(self):
        """Retrieve all properties as Property objects."""
        return self.property_logic.list_properties()

    def add_property(self, property_data: dict):
        """Add a new property.
        :param dict property_data: A dictionary containing property details.
        :return: True if the property was added successfully, False otherwise.
        """
        return self.property_logic.add_property(property_data)

    def update_property(self, property_id: int, updated_data: dict):
        """Update a property's information.
        :param int property_id: The ID of the property to update.
        :param dict updated_data: A dictionary containing updated field values.
        :return: True if the update was successful, False otherwise.
        """
        return self.property_logic.update_property(property_id, updated_data)

    def search_property_by_id(self, property_id: int):
        """Search for a specific property by ID.
        :param int property_id: The ID of the property to search for.
        :return: A Property object if found, None otherwise.
        """
        return self.property_logic.search_property_by_id(property_id)

    def get_maintenance_history(self, property_id: int):
        """Retrieve the maintenance history of a property.
        :param int property_id: The ID of the property.
        :return: A list of maintenance records for the property, or an empty list if none are found.
        """
        return self.property_logic.get_maintenance_history(property_id)