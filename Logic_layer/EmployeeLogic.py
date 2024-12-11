from Data_Layer.DataWrapper import DataWrapper
from Models.employee import Employee

class EmployeeLogic:
    def __init__(self):
        self.data_wrapper = DataWrapper()

    def register_employee(self, employee_details: dict) -> str:
        new_employee = Employee(
            ssn=employee_details["ssn"],
            full_name=employee_details["full_name"],
            address=employee_details["address"],
            phone=employee_details["phone"],
            gsm=employee_details["gsm"],
            email=employee_details["email"],
            location=employee_details["location"],
            is_supervisor=employee_details["is_supervisor"]
        )
        self.data_wrapper.add_employee(new_employee)
        return "Employee registered successfully."

    def list_employees(self) -> list[Employee]:
        return self.data_wrapper.list_employees()

    def change_employee_info(self, ssn: str, field: str, new_value: str) -> str:
        self.data_wrapper.update_employee(ssn, field, new_value)
        return "Employee information updated successfully."
    
    def search_employee_by_ssn(self, ssn):
        employees = self.data_wrapper.list_employees()
        for employee in employees:
            if employee.ssn == ssn:
                return employee
        raise ValueError(f"Employee with SSN {ssn} not found.")