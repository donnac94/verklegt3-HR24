from Data_Layer.EmployeeData import EmployeeData
from Data_Layer.PropertyData import PropertyData
from Data_Layer.WorkOrderData import WorkOrderData
from Models.WorkOrder import WorkOrder
from Models.employee import Employee
from Models.property import Property

class DataWrapper:
    def __init__(self, employee_file: str, property_file: str):
        self.employee_data = EmployeeData(file_name=employee_file)
        self.property_data = PropertyData(file_name=property_file)
        self.work_order_data = WorkOrderData()

    # WorkOrder methods
    def CreateWorkOrder(self, work_order_obj: WorkOrder):
        """
        Register a work order in the CSV file.
        :param WorkOrder work_order_obj: The WorkOrder object to save.
        """
        return self.work_order_data.CreateWorkOrder(work_order_obj)
    
    def GetAllWorkOrders(self) -> list[WorkOrder]:
        """
        Retrieve all work orders from the CSV file.
        :return: A list of work order objects or raises an exception.
        """
        return self.work_order_data.GetAllWorkOrders()
    
    def ChangeWorkOrderInfo(self, work_order_id, field, new_data):
        """
        Change the information of a work order.
        :param int work_order_id: The ID of the work order to update.
        :param str field: The field to update.
        :param str new_data: The new value for the field.
        """
        return self.work_order_data.ChangeWorkOrderInfo(work_order_id, field, new_data)

    # Property methods
    def list_properties(self) -> list[Property]:
        """
        Retrieve all properties from the CSV file.
        :return: A list of property objects or raises an exception.
        """
        return self.property_data.GetAllProperties()

    def add_property(self, property_details: dict):
        """
        Add a new property to the CSV file.
        :param dict property_details: The details of the property to add.
        """
        property_obj = Property.from_dict(property_details)
        return self.property_data.CreateProperty(property_obj)

    def update_property(self, property_id, updated_details: dict):
        """
        Update the information of a property.
        :param str property_id: The ID of the property to update.
        :param dict updated_details: The updated details of the property.
        """
        return self.property_data.UpdateProperty(property_id, updated_details)

    # Employee methods
    def list_employees(self) -> list[Employee]:
        """
        Retrieve all employees from the CSV file.
        :return: A list of employee objects or raises an exception.
        """
        return self.employee_data.GetAllEmployees()

    def add_employee(self, employee_details: dict):
        """
        Add a new employee to the CSV file.
        :param dict employee_details: The details of the employee to add.
        """
        employee_obj = Employee.from_dict(employee_details)
        return self.employee_data.CreateEmployee(employee_obj)

    def update_employee(self, ssn, updated_details: dict):
        """
        Update the information of an employee.
        :param str ssn: The SSN of the employee to update.
        :param dict updated_details: The updated details of the employee.
        """
        return self.employee_data.UpdateEmployee(ssn, updated_details)