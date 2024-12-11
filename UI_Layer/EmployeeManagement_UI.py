from Logic_layer.LogicWrapper import LogicWrapper
import os
import shutil
import sys
from UI_Layer.Validation import validate_email, validate_full_name, validate_ssn

class EmployeeManagementUI:
    def __init__(self, logic_wrapper: LogicWrapper):
        self.logic_wrapper = logic_wrapper

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_terminal_size(self):
        columns, rows = shutil.get_terminal_size(fallback=(80, 24))
        return columns, rows

    def display_menu(self):
        while True:
            self.clear_terminal()
            columns, _ = self.get_terminal_size()
            h = '-'
            c = '+'
            d = '|'
            print(c + "Air NaN Employee Management".center(columns - 2, h) + c)
            print(d + " 1. List All Employees ".ljust(columns - 2) + d)
            print(d + " 2. Register New Employee ".ljust(columns - 2) + d)
            print(d + " 3. Update Employee Information ".ljust(columns - 2) + d)
            print(d + " b. Back to Supervisor Menu ".ljust(columns - 2) + d)
            print(d + " q. Quit ".ljust(columns - 2) + d)
            print(c + h * (columns - 2) + c)

            choice = input("\nChoose an option: ").strip().lower()

            if choice == "1":
                self.list_all_employees()
            elif choice == "2":
                self.register_employee()
            elif choice == "3":
                self.update_employee_info()
            elif choice == "b":
                return
            elif choice == "q":
                print("Exiting Employee Management Menu. Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to return to the menu.")

    def list_all_employees(self):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " List All Employees ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        employees = self.logic_wrapper.list_employees()
        if not employees:
            print("No employees found.")
        else:
            headers = ["SSN", "Full Name", "Address", "Phone", "GSM", "Email", "Location", "Is Manager"]
            col_widths = [max(len(str(getattr(emp, attr))) for emp in employees) for attr in ["ssn", "full_name", "address", "phone", "gsm", "email", "location", "is_manager"]]
            col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
            row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
            print(row_format.format(*headers))
            print("-" * (columns - 2))
            for emp in employees:
                print(row_format.format(emp.ssn, emp.full_name, emp.address, emp.phone, emp.gsm, emp.email, emp.location, "True" if emp.is_manager else "False"))
        input("\nPress Enter to return to the menu.")

    def register_employee(self):
    self.clear_terminal()
    columns, _ = self.get_terminal_size()
    print("+".ljust(columns - 1, '-') + "+")
    print("|" + " Register New Employee ".center(columns - 2) + "|")
    print("+".ljust(columns - 1, '-') + "+")
    print("Enter 'b' at any prompt to cancel and go back to the previous menu.\n")
    
    employee_details = {}

    while True:
        employee_details["ssn"] = input("Enter SSN (10 digits): ").strip()
        if employee_details["ssn"].lower() == 'b':
            return
        if not validate_ssn(employee_details["ssn"]):
            print("Invalid SSN. It should be exactly 10 digits.")
            input("\nPress Enter to try again.")
        else:
            break
            
    while True:
        employee_details["full_name"] = input("Enter Full Name: ").strip()
        if employee_details["full_name"].lower() == 'b':
            return
        if not validate_full_name(employee_details["full_name"]):
            print("Invalid Full Name. It should not exceed 100 characters.")
            input("\nPress Enter to try again.")
        else:
            break

    for field in ["address", "phone", "gsm", "location"]:
        value = input(f"Enter {field.capitalize()}: ").strip()
        if value.lower() == 'b':
            return
        employee_details[field] = value

    while True:
        is_manager_input = input("Is Manager (True/False): ").strip().lower()
        if is_manager_input == 'b':
            return
        if is_manager_input in ['true', 'false']:
            employee_details["is_manager"] = is_manager_input == 'true'
            break
        else:
            print("Invalid input. Please enter 'True' or 'False'.")
            input("\nPress Enter to try again.")

    while True:
        employee_details["email"] = input("Enter Email: ").strip()
        if employee_details["email"].lower() == 'b':
            return
        if not validate_email(employee_details["email"]):
            print("Invalid Email. It should contain '@' and '.' and not exceed 100 characters.")
            input("\nPress Enter to try again.")
        else:
            break
            
    result = self.logic_wrapper.register_employee(employee_details)
    if result:
        print("\nEmployee registered successfully.")
    else:
        print("\nAn error occurred while registering the employee.")

    input("\nPress Enter to return to the menu.")


    def update_employee_info(self):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " Update Employee Information ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        print("Enter 'b' at any prompt to cancel and go back to the previous menu.\n")
        employees = self.logic_wrapper.list_employees()
        if not employees:
            print("No employees found.")
            input("\nPress Enter to return to the menu.")
            return

        headers = ["SSN", "Full Name", "Address", "Phone", "GSM", "Email", "Location", "Is Manager"]
        col_widths = [max(len(str(getattr(emp, attr))) for emp in employees) for attr in ["ssn", "full_name", "address", "phone", "gsm", "email", "location", "is_manager"]]
        col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
        row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
        print(row_format.format(*headers))
        print("-" * (columns - 2))
        for emp in employees:
            print(row_format.format(emp.ssn, emp.full_name, emp.address, emp.phone, emp.gsm, emp.email, emp.location, "True" if emp.is_manager else "False"))

        ssn = input("\nEnter SSN of the employee to update: ").strip()
        if ssn.lower() == 'b':
            return
        employee = next((emp for emp in employees if emp.ssn == ssn), None)
        if not employee:
            print(f"No employee found with SSN {ssn}")
            input("\nPress Enter to return to the menu.")
            return

        print("\nCurrent Information:")
        print(row_format.format(*headers))
        print("-" * (columns - 2))
        print(row_format.format(employee.ssn, employee.full_name, employee.address, employee.phone, employee.gsm, employee.email, employee.location, "True" if employee.is_manager else "False"))

        field = input("\nEnter the field to update (full_name, address, phone, gsm, email, location, is_manager): ").strip()
        if field.lower() == 'b':
            return
        if field == "email":
            while True:
                new_value = input(f"Enter new value for {field}: ").strip()
                if new_value.lower() == 'b':
                    return
                if not validate_email(new_value):
                    print("Invalid Email. It should contain '@' and '.' and not be longer than 100 characters.")
                    input("\nPress Enter to try again.")
                else:
                    break
        else:
            new_value = input(f"Enter new value for {field}: ").strip()
            if new_value.lower() == 'b':
                return
            if field == "ssn" and not validate_ssn(new_value):
                print("Invalid SSN. It should be 10 digits.")
                return
            if field == "full_name" and not validate_full_name(new_value):
                print("Invalid Full Name. It should not be longer than 100 characters.")
                return
        result = self.logic_wrapper.change_employee_info(ssn, field, new_value)
        print(result)

        # Fetch the updated employee information
        updated_employee = self.logic_wrapper.search_employee_by_ssn(ssn)
        print("\nUpdated Information:")
        print(row_format.format(*headers))
        print("-" * (columns - 2))
        print(row_format.format(updated_employee.ssn, updated_employee.full_name, updated_employee.address, updated_employee.phone, updated_employee.gsm, updated_employee.email, updated_employee.location, "True" if updated_employee.is_manager else "False"))

        input("\nPress Enter to return to the menu.")