from Logic_layer.LogicWrapper import LogicWrapper
import os
import shutil
from UI_Layer.Validation import InputValidation

class EmployeeManagementUI:
    def __init__(self, logic_wrapper: LogicWrapper):
        self.logic_wrapper = logic_wrapper

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_terminal_size(self):
        columns, rows = shutil.get_terminal_size(fallback=(80, 24))
        return columns, rows

    def display_menu(self, employee_status: str):
        while True:
            self.clear_terminal()
            columns, _ = self.get_terminal_size()
            h = '-'
            c = '+'
            d = '|'
            print(c + "Air NaN Employee Management".center(columns - 2, h) + c)
            print(d + " 1. List All Employees ".ljust(columns - 2) + d)
            print(d + " 2. Show work plan ".ljust(columns - 2) + d)
            if employee_status == "supervisor":
                print(d + " 3. Update Employee Information ".ljust(columns - 2) + d)
                print(d + " 4. Register New Employee ".ljust(columns - 2) + d)
            print(d + " b. Back to Supervisor Menu ".ljust(columns - 2) + d)
            print(c + h * (columns - 2) + c)

            choice = input("\nChoose an option: ").strip().lower()

            if choice == "1":
                self.list_all_employees()
            elif choice == "2":    
                self.get_work_plan()
            if employee_status == "supervisor":
                if choice == "3":
                    self.update_employee_info()
                elif choice == "4":
                    self.register_employee()
            if choice == "b":
                return
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
            headers = ["SSN", "Full Name", "Address", "Phone", "GSM", "Email", "Location", "Is Supervisor"]
            col_widths = [max(len(str(getattr(emp, attr))) for emp in employees) for attr in
                          ["ssn", "full_name", "address", "phone", "gsm", "email", "location", "is_supervisor"]]
            col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
            row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
            print(row_format.format(*headers))
            print("-" * (columns - 2))
            for emp in employees:
                print(row_format.format(emp.ssn, emp.full_name, emp.address, emp.phone, emp.gsm, emp.email,
                                        emp.location, "True" if emp.is_supervisor else "False"))
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
            if not InputValidation.validate_ssn(employee_details["ssn"]):
                print("Invalid SSN. Must only contain digits and should be exactly 10 digits.")
                input("\nPress Enter to try again.")
            else:
                if self.logic_wrapper.search_employee_by_ssn(employee_details["ssn"]):
                    print("Error: Employee with this SSN already exists.")
                    input("\nPress Enter to try again.")
                else:
                    break

        while True:
            employee_details["full_name"] = input("Enter Full Name: ").strip()
            if employee_details["full_name"].lower() == 'b':
                return
            if not InputValidation.validate_full_name(employee_details["full_name"]):
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
            is_supervisor_input = input("Is Supervisor (y/n): ").strip().lower()

            if is_supervisor_input == 'b':
                return

            if is_supervisor_input == 'y':
                employee_details["is_supervisor"] = True
                break
            elif is_supervisor_input == 'n':
                employee_details["is_supervisor"] = False
                break
            else:
                print("Invalid input. Please enter 'y' for Yes or 'n' for No.")
                input("\nPress Enter to try again.")

        while True:
            employee_details["email"] = input("Enter Email: ").strip()
            if employee_details["email"].lower() == 'b':
                return
            if not InputValidation.validate_email(employee_details["email"]):
                print("Invalid Email. It should contain '@' and '.' and not exceed 100 characters.")
                input("\nPress Enter to try again.")
            else:
                break

        result = self.logic_wrapper.register_employee(employee_details)
        if result == "Error: Employee with this SSN already exists.":
            print("\n" + result)
            input("\nPress Enter to try again.")
            return self.register_employee()
        elif result:
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

        headers = ["SSN", "Full Name", "Address", "Phone", "GSM", "Email", "Location", "Is Supervisor"]
        col_widths = [max(len(str(getattr(emp, attr))) for emp in employees) for attr in
                      ["ssn", "full_name", "address", "phone", "gsm", "email", "location", "is_supervisor"]]
        col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
        row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
        print(row_format.format(*headers))
        print("-" * (columns - 2))
        for emp in employees:
            print(row_format.format(emp.ssn, emp.full_name, emp.address, emp.phone, emp.gsm, emp.email,
                                    emp.location, "True" if emp.is_supervisor else "False"))

        ssn = input("\nEnter SSN of the employee to update: ").strip()
        if ssn.lower() == 'b':
            return
        employee = next((emp for emp in employees if emp.ssn == ssn), None)
        if not employee:
            print(f"No employee found with SSN {ssn}")
            input("\nPress Enter to return to the menu.")
            return

        print("\nSelect the field to update:")
        fields = {
            "1": "full_name",
            "2": "address",
            "3": "phone",
            "4": "gsm",
            "5": "email",
            "6": "location",
            "7": "is_supervisor"
        }
        for key, value in fields.items():
            print(f" {key}. {value.replace('_', ' ').capitalize()}")

        field_choice = input("\nEnter the number corresponding to the field: ").strip()
        if field_choice not in fields:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to continue.")
            return
        field = fields[field_choice]

        while True:
            new_value = input(f"Enter new value for {field.replace('_', ' ').capitalize()}: ").strip()
            if new_value.lower() == 'b':
                return
            if field == "email" and not InputValidation.validate_email(new_value):
                print("Invalid Email. It should contain '@' and '.' and not exceed 100 characters.")
                input("\nPress Enter to try again.")
            elif field == "ssn" and not InputValidation.validate_ssn(new_value):
                print("Invalid SSN. It should be exactly 10 digits.")
                input("\nPress Enter to try again.")
            elif field == "full_name" and not InputValidation.validate_full_name(new_value):
                print("Invalid Full Name. It should not exceed 100 characters.")
                input("\nPress Enter to try again.")
            else:
                break

        result = self.logic_wrapper.change_employee_info(ssn, field, new_value)
        print(result)

        updated_employee = self.logic_wrapper.search_employee_by_ssn(ssn)
        print("\nUpdated Information:")
        print(row_format.format(*headers))
        print("-" * (columns - 2))
        print(row_format.format(updated_employee.ssn, updated_employee.full_name, updated_employee.address,
                                updated_employee.phone, updated_employee.gsm, updated_employee.email,
                                updated_employee.location, "True" if updated_employee.is_supervisor else "False"))

        input("\nPress Enter to return to the menu.")

    def get_work_plan(self):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " Show Work Plan ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        filtered_work_orders = self.logic_wrapper.get_work_plan()
        if not filtered_work_orders:
            print("No work orders are available")
        else:
             headers = ["work_order_id", "work_to_be_done", "property", "submitting_supervisor", "date", "priority", "work_order_status"]
             col_widths = [max(len(str(getattr(work_order, attr))) for work_order in filtered_work_orders) for attr in
                          ["work_order_id", "work_to_be_done", "property", "submitting_supervisor", "date", "priority", "work_order_status"]]
             col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
             row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
             print(row_format.format(*headers))
             print("-" * (columns - 2))
             for work_order in filtered_work_orders:
                print(row_format.format(work_order.work_order_id, work_order.work_to_be_done, work_order.property, work_order.submitting_supervisor, work_order.date, 
                                        work_order.priority, work_order.work_order_status))
        input("\nPress Enter to return to the menu.")