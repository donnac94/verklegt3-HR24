from Models.property import Property

class LogicWrapper:
    def __init__(self, employee_data, property_data):
        self.employee_data = employee_data
        self.property_data = property_data

    def list_employees(self):
        return self.employee_data.get_all_employees()

    def register_employee(self, employee_details):
        return self.employee_data.add_employee(employee_details)

    def change_employee_info(self, ssn, field, new_value):
        return self.employee_data.change_employee_info(ssn, field, new_value)

    def search_employee_by_ssn(self, ssn):
        return self.employee_data.get_employee_by_ssn(ssn)

    def list_properties(self):
        return self.property_data.get_all_properties()

    def add_property(self, property_details):
        new_property = Property(**property_details)
        return self.property_data.add_property(new_property)

    def update_property(self, property_id, updated_details):
        for field, new_value in updated_details.items():
            self.property_data.update_property(property_id, field, new_value)
        return "Property updated successfully."

    def search_property_by_id(self, property_id):
        return self.property_data.get_property_by_id(property_id)