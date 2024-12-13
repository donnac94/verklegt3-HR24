from Data_Layer.DataWrapper import DataWrapper
from Models.employee import Employee

class EmployeeLogic:
    def __init__(self):
        self.data_wrapper = DataWrapper()

    def register_employee(self, employee_details: dict) -> str:
        """
        Register a new employee, takes the input and assigns by id 
        Args:
            employee_details (dict): checks if the employee details already exist and return a error message

        Returns:
            str: Returns the new value and a message that the employee was registered successfully 
        """
        existing_employees = self.data_wrapper.list_employees()
        if any(emp.ssn == employee_details["ssn"] for emp in existing_employees):
            return "Error: Employee with this SSN already exists." #Mögulega betra að hafa raise ValueError("Error: Employee with this SSN already exists.")
        
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
        """
        Takes all the employees and lists them up in a list 
        Returns:
            list[Employee]: Takes the employee model and shows it in a list 
        """
        return self.data_wrapper.list_employees()

    def change_employee_info(self, ssn: str, field: str, new_value: str) -> str:
        """
        Shows all the employees in a list, then the employee is selected by their id  
        Args:
            ssn (str): the ssn that you want to change
            field (str): the field that you want to change
            new_value (str): the new value that is replacing the old one

        Returns:
            str: returns the message that the information change about the employee was successful 
        """
        self.data_wrapper.update_employee(ssn, field, new_value)
        return "Employee information updated successfully."
    
    def search_employee_by_ssn(self, ssn):
        """Search the employee by their Socail Security Number(SSN)"""
        employees = self.data_wrapper.list_employees()
        for employee in employees:
            if employee.ssn == ssn:
                return employee
        return None
    
    def get_work_plan(self):
        """Creates a work plan. List of all open work orders, ordered by priority"""
        work_plan = []
        open_work_orders = []
        work_orders = self.data_wrapper.get_all_work_orders()
        for work_order in work_orders:
            if work_order.work_order_status.lower() == "open":
                open_work_orders.append(work_order)

        for work_order in open_work_orders:
            if work_order.priority.lower() == "high":
                work_plan.append(work_order)
        for work_order in open_work_orders:
            if work_order.priority.lower() == "medium":
                work_plan.append(work_order)
        for work_order in open_work_orders:
            if work_order.priority.lower() == "low":
                work_plan.append(work_order)
        return work_plan