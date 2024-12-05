from Models.employee import Employee


def register_employee(employees: list[Employee], employee_details: dict) -> str:
    """
    Register a new employee.
    :param employees: List of existing employees.
    :param employee_details: Dictionary containing employee details.
    :return: Success or error message.
    """
    ssn = employee_details.get("ssn")
    if any(e.ssn == ssn for e in employees):
        return "Employee SSN already exists."
    
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
    return "Employee registered successfully."


def list_employees(employees: list[Employee]) -> list[dict]:
    """
    List all employees.
    :param employees: List of existing employees.
    :return: A list of dictionaries representing employees or an empty list if no employees exist.
    """
    return [
        {
            "name": e.name,
            "ssn": e.ssn,
            "address": e.address,
            "gsm": e.gsm,
            "homephone": e.homephone,
            "email": e.email,
            "work_location": {
                "name": e.work_location.name,
                "address": e.work_location.address,
                "city": e.work_location.city,
                "country": e.work_location.country,
            } if e.work_location else None
        }
        for e in employees
    ]


def change_employee_info(employees: list[Employee], ssn: int, updated_details: dict) -> str:
    """
    Change information of an existing employee.
    :param employees: List of existing employees.
    :param ssn: ID of the employee to update.
    :param updated_details: Dictionary containing updated employee details.
    :return: Success or error message.
    """
    employee_to_edit = next((e for e in employees if e.ssn == ssn), None)

    if not employee_to_edit:
        return "Employee not found."
    
    employee_to_edit.name = updated_details.get("name", employee_to_edit.name)
    employee_to_edit.address = updated_details.get("address", employee_to_edit.address)
    employee_to_edit.gsm = updated_details.get("gsm", employee_to_edit.gsm)
    employee_to_edit.homephone = updated_details.get("homephone", employee_to_edit.homephone)
    employee_to_edit.email = updated_details.get("email", employee_to_edit.email)

    if "work_location" in updated_details:
        work_location_details = updated_details["work_location"]
        if isinstance(work_location_details, dict):
            employee_to_edit.work_location.name = work_location_details.get(
                "name", employee_to_edit.work_location.name
            )
            employee_to_edit.work_location.address = work_location_details.get(
                "address", employee_to_edit.work_location.address
            )
            employee_to_edit.work_location.city = work_location_details.get(
                "city", employee_to_edit.work_location.city
            )
            employee_to_edit.work_location.country = work_location_details.get(
                "country", employee_to_edit.work_location.country
            )

    return "Employee information updated successfully."
