import csv
from Models.employee import Employee

class EmployeeData:
    def __init__(self):
        self.file_name = "Files/employees.csv"

    def get_all_employees(self) -> list[Employee]:
        with open('/Files/employees.csv', 'r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            return [Employee.from_dict(row) for row in reader]

    def register_employee(self, employee: Employee):
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["ssn","full_name","address","phone","gsm","email","location","is_supervisor"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:  
                writer.writeheader()

            writer.writerow(employee.to_dict())

    def change_employee_info(self, ssn, field, new_value):
        employees = self.get_all_employees()
        employee_found = False

        for employee in employees:
            if employee.ssn == ssn:
                setattr(employee, field, new_value)
                employee_found = True
                break

        if not employee_found:
            raise ValueError(f"Employee with SSN {ssn} not found.")

        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["ssn", "full_name", "address", "phone", "gsm", "email", "location", "is_supervisor"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for employee in employees:
                writer.writerow(employee.to_dict())