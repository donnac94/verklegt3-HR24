import csv
from Models.employee import Employee


class EmployeeData:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_all_employees(self):
        with open(self.file_name, 'r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            return [Employee(**row) for row in reader]

    def add_employee(self, employee_details):
        employees = self.get_all_employees()
        employees.append(Employee(**employee_details))
        self._save_employees(employees)

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

        self._save_employees(employees)

    def get_employee_by_ssn(self, ssn):
        employees = self.get_all_employees()
        for employee in employees:
            if employee.ssn == ssn:
                return employee
        raise ValueError(f"Employee with SSN {ssn} not found.")

    def _save_employees(self, employees):
        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["ssn", "full_name", "address", "phone", "gsm", "email", "location", "is_manager"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for employee in employees:
                writer.writerow(employee.to_dict())