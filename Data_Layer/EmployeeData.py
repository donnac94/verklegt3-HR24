import csv
from Models.employee import Employee

class EmployeeData:
    def __init__(self):
        self.file_name = "Files/employees.csv"

    def get_all_employees(self) -> list[Employee]:
        """
        Retrieve all employees from the CSV file.
        :return: A list of employees.
        """
        with open(self.file_name, 'r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            return [Employee.from_dict(row) for row in reader]

    def register_employee(self, employee: Employee):
        """
        Register an employee in the CSV file.
        :param Employee employee_obj: The Employee object to save.
        """
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["ssn","full_name","address","phone","gsm","email","location","is_supervisor"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:  
                writer.writeheader()

            writer.writerow(employee.to_dict())

    def change_employee_info(self, ssn: int, field: str, new_value:str):
        """
        Change an employees information. 
        :param int ssn: The SSN (ID) of the employees info you want to change.
        :param str field: The field you want to change.
        :param str new_value: The new value to replace the chosen field.
        """
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