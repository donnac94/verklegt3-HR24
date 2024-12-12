
from Data_Layer.DataWrapper import DataWrapper


class SearchLogic:
    
    def __init__(self):
        self.data_wrapper = DataWrapper()
        
        
        
    def search_employee_by_location(self, location):
        """Search employees by location"""
        filtered_list= []
        employees = self.data_wrapper.list_employees()
        for employee in employees:
                if employee.location.lower() == location.lower():
                    filtered_list.append(employee)
        return filtered_list
    
    def search_properties_by_location(self, location):
        """Search properties by location"""
        filtered_list= []
        properties = self.data_wrapper.list_properties()
        for property in properties:
                if property.location.lower() == location.lower():
                    filtered_list.append(property)
        return filtered_list
        
    def search_employees_by_ssn(self, ssn):
        """Search employees by SSN"""

        employees = self.data_wrapper.list_employees()
        for employee in employees:
                if employee.ssn == ssn:
                    return employee
        return "No Employee found with that ssn"
   

    def search_property_by_id(self, property_id):
        """Search for a property by id"""
        properties = self.data_wrapper.list_properties()
        for property in properties:
                if property.property_id == property_id:
                    return property
        return "No property found"
        
        
    def search_work_order_by_id(self, work_order_id):
        """Search for a work order by id"""
        work_orders = self.data_wrapper.get_all_work_orders()
        for work_order in work_orders:
                if work_order.work_order_id == work_order_id:
                    return work_order
        return "No work order found"
    
    def search_work_orders_by_property(self, property_name):
        """Search for work orders by property name"""
        filtered_list = []
        work_orders = self.data_wrapper.get_all_work_orders()
        for work_order in work_orders:
                if work_order.property.lower() == property_name.lower():
                    filtered_list.append(work_order)
        return filtered_list
    
    def search_maintenance_reports_by_property(self, property_name):
        """Search for maintenance reports by property name"""
        filtered_list = []
        maintenance_reports = self.data_wrapper.get_all_maintenance_reports()
        for maintenance_report in maintenance_reports:
                if maintenance_report.property.lower() == property_name.lower():
                    filtered_list.append(maintenance_report)
        return filtered_list
    
    def search_work_orders_by_employee(self, employee_ssn):
        """Search for work orders by employee ssn"""
        filtered_list = []
        work_orders = self.data_wrapper.get_all_work_orders()
        for work_order in work_orders:
                if work_order.submitting_supervisor == employee_ssn:
                    filtered_list.append(work_order)
        return filtered_list
    
    def search_maintenance_reports_by_employee(self, employee_ssn):
        """Search for maintenance reports by employee ssn"""
        filtered_list = []
        maintenance_reports = self.data_wrapper.get_all_maintenance_reports()
        for maintenance_report in maintenance_reports:
                if maintenance_report.employee == employee_ssn:
                    filtered_list.append(maintenance_report)
        return filtered_list