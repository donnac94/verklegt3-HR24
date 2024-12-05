from Models.employee import Employee


def register_employee(employees: list[Employee], employee_details: dict) -> str:
    """
    Register a new employee.
    :param employees: List of existing employees.
    :param employee_details: Dictionary containing employee details.
    :return: Success or error message.
    """
    employee_id = employee_details.get("employee_id")
    if any(e.employee_id == employee_id for e in employees):
        return "Employee ID already exists."
    
    new_employee = Employee(
        employee_id=employee_id,
        full_name=employee_details.get("full_name"),
        address=employee_details.get("address"),
        phone=employee_details.get("phone"),
        gsm=employee_details.get("gsm"),
        email=employee_details.get("email"),
        location=employee_details.get("location")
    )
    employees.append(new_employee)
    return "Employee registered successfully."


def list_employees(employees: list[Employee]) -> list:
    """
    List all employees.
    :param employees: List of existing employees.
    :return: A list of employees or an empty list if no employees exist.
    """
    return employees if employees else []


def change_employee_info(employees: list[Employee], employee_id: int, updated_details: dict) -> str:
    """
    Change information of an existing employee.
    :param employees: List of existing employees.
    :param employee_id: ID of the employee to update.
    :param updated_details: Dictionary containing updated employee details.
    :return: Success or error message.
    """
    employee_to_edit = next((e for e in employees if e.employee_id == employee_id), None)

    if not employee_to_edit:
        return "Employee not found."
    
    employee_to_edit.full_name = updated_details.get("full_name", employee_to_edit.full_name)
    employee_to_edit.address = updated_details.get("address", employee_to_edit.address)
    employee_to_edit.phone = updated_details.get("phone", employee_to_edit.phone)
    employee_to_edit.gsm = updated_details.get("gsm", employee_to_edit.gsm)
    employee_to_edit.email = updated_details.get("email", employee_to_edit.email)
    employee_to_edit.location = updated_details.get("location", employee_to_edit.location)

    return "Employee information updated successfully."
