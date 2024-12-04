import csv
from Models.employee import Employee

class EmployeeData:
    def __init__(self):
        self.file_name = "Files/employees.csv"

    def register_employee(self, employee: Employee) -> None:
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["employee_id", "full_name", "address", "phone", "gsm", "email", "location"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:  
                writer.writeheader()

            writer.writerow({
                "employee_id": employee.employee_id,
                "full_name": employee.full_name,
                "address": employee.address,
                "phone": employee.phone,
                "gsm": employee.gsm,
                "email": employee.email,
                "location": employee.location
            })

    def get_all_employees(self) -> list[Employee]:
        ret_list = []
        try:
            with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    ret_list.append(
                        Employee(
                            row["employee_id"],
                            row["full_name"],
                            row["address"],
                            row["phone"],
                            row["gsm"],
                            row["email"],
                            row["location"]
                        )
                    )
        except FileNotFoundError:
            return []
        return ret_list

    def change_employee_info(self, employee_id: str, field: str, new_value: str) -> None:
        employees = self.get_all_employees()
        employee_found = False

        for employee in employees:
            if employee.employee_id == employee_id:
                setattr(employee, field, new_value)
                employee_found = True
                break

        if not employee_found:
            raise ValueError(f"Employee with ID {employee_id} not found.")

        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["employee_id", "full_name", "address", "phone", "gsm", "email", "location"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for employee in employees:
                writer.writerow({
                    "employee_id": employee.employee_id,
                    "full_name": employee.full_name,
                    "address": employee.address,
                    "phone": employee.phone,
                    "gsm": employee.gsm,
                    "email": employee.email,
                    "location": employee.location
                })
