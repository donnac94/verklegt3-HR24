from Data_Layer.EmployeeData import EmployeeData
from Data_Layer.PropertyData import PropertyData
from Data_Layer.WorkOrderData import WorkOrderData
from Data_Layer.MaintenanceReportData import MaintenanceReportData
from Data_Layer.ContractorData import ContractorData
from Data_Layer.LocationData import LocationData
from Models.WorkOrder import WorkOrder
from Models.employee import Employee
from Models.property import Property
from Models.Contractor import Contractor

class DataWrapper:
    def __init__(self):
        self.employee_data = EmployeeData()
        self.property_data = PropertyData()
        self.work_order_data = WorkOrderData()
        self.maintenance_report_data = MaintenanceReportData()
        self.contractor_data = ContractorData()
        self.location_data = LocationData

    # WorkOrder methods
    def create_work_order(self, work_order_obj: WorkOrder):
        """
        Register a work order in the CSV file.
        :param WorkOrder work_order_obj: The WorkOrder object to save.
        """
        return self.work_order_data.create_work_order(work_order_obj)
    
    def get_all_work_orders(self) -> list[WorkOrder]:
        """
        Retrieve all work orders from the CSV file.
        :return: A list of work order objects or raises an exception.
        """
        return self.work_order_data.get_all_work_orders()
    
    def change_work_order_info(self, work_order_id, field, new_value):
        """
        Change the information of a work order.
        :param int work_order_id: The ID of the work order to update.
        :param str field: The field to update.
        :param str new_value: The new value for the field.
        """
        return self.work_order_data.change_work_order_info(work_order_id, field, new_value)

    # Property methods
    def list_properties(self) -> list[Property]:
        """
        Retrieve all properties from the CSV file.
        :return: A list of property objects or raises an exception.
        """
        return self.property_data.get_all_properties()

    def add_property(self, new_property: Property):
        """
        Add a new property to the CSV file.
        :param Property new_property: The new property to be added.
        """
        return self.property_data.add_property(new_property)

    def update_property(self, property_id, updated_details: dict):
        """
        Update the information of a property.
        :param str property_id: The ID of the property to update.
        :param dict updated_details: The updated details of the property.
        """
        return self.property_data.update_property(property_id, updated_details)

    # Employee methods
    def list_employees(self) -> list[Employee]:
        """
        Retrieve all employees from the CSV file.
        :return: A list of employee objects or raises an exception.
        """
        return self.employee_data.get_all_employees()

    def add_employee(self, new_employee: Employee):
        """
        Add a new employee to the CSV file.
        :param Employee new_employee: The new employee to add.
        """
        return self.employee_data.register_employee(new_employee)

    def update_employee(self, ssn: str, field: str, new_value: str):
        """
        Update the information of an employee.
        :param str ssn: The SSN of the employee to update.
        """
        return self.employee_data.change_employee_info(ssn, field, new_value)
    
    def get_property_by_id(self, property_id):
        return self.property_data.get_property_by_id(property_id)
    

    # Contractor methods
    def register_contractor(self, contractor_obj: Contractor):
        """
        Register a contractor in the CSV file.
        :param Contractor contractor_obj: The contractor to save.
        """
        return self.contractor_data.register_contractor(contractor_obj)
    
    def get_all_contractors(self) -> list[Contractor]:
        """
        Retrieve all contractors from the CSV file.
        :return: A list of all contractors 
        """
        return self.contractor_data.get_all_contractors()
    
    def change_contractor_info(self, contractor_id, field, new_value):
        """
        Change contractors info.
        :param contractor_id: The ID of the contractor to update.
        :param field: The field to update.
        :param new_value: The new value for the field. 
        """
        return self.contractor_data.change_contractor_info(contractor_id, field, new_value)