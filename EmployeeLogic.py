from Models.employee import Employee

class EmployeeLogic:
    def __init__(self, employee_data):
        self.employee_data = employee_data

    def list_employees(self) -> list[Employee]:
        """
        Retrieve all employees.
        :return: A list of Employee objects.
        """
        return self.employee_data.GetAllEmployees()

    def register_employee(self, employee_details: dict) -> str:
        """
        Register a new employee.
        :param dict employee_details: A dictionary containing employee details.
        :return: A success message if the employee was registered successfully.
        """
        employees = self.list_employees()
        ssn = employee_details.get("ssn")
        if any(e.ssn == ssn for e in employees):
            return f"Employee with SSN {ssn} already exists."
        
        new_employee = Employee(
            name=employee_details.get("name"),
            ssn=ssn,
            address=employee_details.get("address"),
            gsm=employee_details.get("gsm"),
            homephone=employee_details.get("homephone"),
            email=employee_details.get("email"),
            work_location=employee_details.get("work_location")
        )
        employees.append(new_employee)
        self.employee_data.SaveEmployees(employees)
        return "Employee registered successfully."

    def change_employee_info(self, ssn, field, new_value) -> str:
        """
        Change the information of an employee.
        :param str ssn: The SSN of the employee to update.
        :param str field: The field to update.
        :param str new_value: The new value for the field.
        :return: A success message if the employee was updated successfully.
        """
        employees = self.list_employees()
        employee = next((e for e in employees if e.ssn == ssn), None)
        if not employee:
            return f"Employee with SSN {ssn} not found."

        if hasattr(employee, field):
            setattr(employee, field, new_value)
        else:
            return f"Field {field} does not exist in employee data."

        self.employee_data.SaveEmployees(employees)
        return "Employee information updated successfully."