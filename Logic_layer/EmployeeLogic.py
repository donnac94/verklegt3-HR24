from Data_Layer.EmployeeData import EmployeeData
from Models.employee import Employee

class EmployeeLogic:
    def __init__(self, employee_data: EmployeeData):
        self.employee_data = employee_data

    def register_employee(self, employee_details: dict) -> str:
        new_employee = Employee(
            ssn=employee_details["ssn"],
            full_name=employee_details["full_name"],
            address=employee_details["address"],
            phone=employee_details["phone"],
            gsm=employee_details["gsm"],
            email=employee_details["email"],
            location=employee_details["location"],
            is_manager=employee_details["is_manager"]
        )
        self.employee_data.register_employee(new_employee)
        return "Employee registered successfully."

    def list_employees(self) -> list[Employee]:
        return self.employee_data.get_all_employees()

    def change_employee_info(self, ssn: str, field: str, new_value: str) -> str:
        self.employee_data.change_employee_info(ssn, field, new_value)
        return "Employee information updated successfully."

    def search_employee_by_id(self, ssn: str) -> Employee:
        employees = self.employee_data.get_all_employees()
        for employee in employees:
            if employee.ssn == ssn:
                return employee
        return None