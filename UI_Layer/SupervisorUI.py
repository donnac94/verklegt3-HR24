import os
import shutil
import sys

class SupervisorUI:
    def __init__(self, logic_layer):
        self.logic_layer = logic_layer

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
            print(c + "Air NaN Supervisor Portal".center(columns - 2, h) + c)
            print(d + "Welcome to the Supervisor Menu".center(columns - 2) + d)
            print(c + h * (columns - 2) + c)
            print(d + " 1. List All Employees ".ljust(columns - 2) + d)
            print(d + " 2. Register New Employee ".ljust(columns - 2) + d)
            print(d + " 3. Update Employee Information ".ljust(columns - 2) + d)
            print(d + " 4. List All Properties ".ljust(columns - 2) + d)
            print(d + " 5. Add New Property ".ljust(columns - 2) + d)
            print(d + " 6. Update Property Information ".ljust(columns - 2) + d)
            print(d + " 7. Approve Maintenance Reports ".ljust(columns - 2) + d)
            print(d + " b. Back to Login Menu ".ljust(columns - 2) + d)
            print(d + " q. Quit ".ljust(columns - 2) + d)
            print(c + h * (columns - 2) + c)

            choice = input("\nChoose an option: ").strip().lower()

            if choice == "1":
                self.list_all_employees()
            elif choice == "2":
                self.register_employee()
            elif choice == "3":
                self.update_employee_info()
            elif choice == "4":
                self.list_all_properties()
            elif choice == "5":
                self.add_new_property()
            elif choice == "6":
                self.update_property_info()
            elif choice == "7":
                self.approve_maintenance_reports()
            elif choice == "b":
                return
            elif choice == "q":
                print("Exiting Supervisor Menu. Goodbye!")
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
        employees = self.logic_layer.list_employees()
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
                print(row_format.format(emp.ssn, emp.full_name, emp.address, emp.phone, emp.gsm, emp.email, emp.location, emp.is_manager))
        input("\nPress Enter to return to the menu.")

    def list_all_properties(self):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " List All Properties ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        properties = self.logic_layer.list_properties()
        if not properties:
            print("No properties found.")
        else:
            headers = ["Property ID", "Address", "Location", "Condition", "Manager", "Requires Maintenance"]
            col_widths = [max(len(str(getattr(prop, attr))) for prop in properties) for attr in ["property_id", "address", "location", "property_condition", "manager", "requires_maintenance"]]
            col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
            row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
            print(row_format.format(*headers))
            print("-" * (columns - 2))
            for prop in properties:
                print(row_format.format(prop.property_id, prop.address, prop.location, prop.property_condition, prop.manager, ", ".join(prop.requires_maintenance)))
        input("\nPress Enter to return to the menu.")

    def register_employee(self):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " Register New Employee ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        print("Enter 'b' at any prompt to cancel and go back to the previous menu.\n")
        employee_details = {
            "ssn": input("Enter SSN: ").strip()
        }
        if employee_details["ssn"].lower() == 'b':
            return
        employee_details.update({
            "full_name": input("Enter Full Name: ").strip(),
            "address": input("Enter Address: ").strip(),
            "phone": input("Enter Phone: ").strip(),
            "gsm": input("Enter GSM: ").strip(),
            "email": input("Enter Email: ").strip(),
            "location": input("Enter Location: ").strip(),
            "is_manager": input("Is Manager (True/False): ").strip().lower() == 'true'
        })
        if any(value.lower() == 'b' for key, value in employee_details.items() if key != "is_manager"):
            return
        result = self.logic_layer.register_employee(employee_details)
        print(result)
        print("\nEmployee registered successfully.")
        self.list_all_employees()

    def update_employee_info(self):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " Update Employee Information ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        print("Enter 'b' at any prompt to cancel and go back to the previous menu.\n")
        employees = self.logic_layer.list_employees()
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
            print(row_format.format(emp.ssn, emp.full_name, emp.address, emp.phone, emp.gsm, emp.email, emp.location, emp.is_manager))

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
        print(row_format.format(employee.ssn, employee.full_name, employee.address, employee.phone, employee.gsm, employee.email, employee.location, employee.is_manager))

        field = input("\nEnter the field to update (full_name, address, phone, gsm, email, location, is_manager): ").strip()
        if field.lower() == 'b':
            return
        new_value = input(f"Enter new value for {field}: ").strip()
        if new_value.lower() == 'b':
            return
        result = self.logic_layer.change_employee_info(ssn, field, new_value)
        print(result)

        # Fetch the updated employee information
        updated_employee = self.logic_layer.search_employee_by_ssn(ssn)
        print("\nUpdated Information:")
        print(row_format.format(*headers))
        print("-" * (columns - 2))
        print(row_format.format(updated_employee.ssn, updated_employee.full_name, updated_employee.address, updated_employee.phone, updated_employee.gsm, updated_employee.email, updated_employee.location, updated_employee.is_manager))

        input("\nPress Enter to return to the menu.")

    def add_new_property(self):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " Add New Property ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        print("Enter 'b' at any prompt to cancel and go back to the previous menu.\n")
        property_details = {
            "property_id": input("Enter Property ID: ").strip()
        }
        if property_details["property_id"].lower() == 'b':
            return
        property_details.update({
            "address": input("Enter Address: ").strip(),
            "location": input("Enter Location: ").strip(),
            "property_condition": input("Enter Property Condition: ").strip(),
            "manager": input("Enter Manager: ").strip(),
            "requires_maintenance": input("Enter Requires Maintenance (comma-separated): ").strip()
        })
        if any(value.lower() == 'b' for value in property_details.values()):
            return
        result = self.logic_layer.add_property(property_details)
        print(result)
        print("\nProperty added successfully.")
        self.list_all_properties()

    def update_property_info(self):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " Update Property Information ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        print("Enter 'b' at any prompt to cancel and go back to the previous menu.\n")
        properties = self.logic_layer.list_properties()
        if not properties:
            print("No properties found.")
            input("\nPress Enter to return to the menu.")
            return

        headers = ["Property ID", "Address", "Location", "Condition", "Manager", "Requires Maintenance"]
        col_widths = [max(len(str(getattr(prop, attr))) for prop in properties) for attr in ["property_id", "address", "location", "property_condition", "manager", "requires_maintenance"]]
        col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
        row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
        print(row_format.format(*headers))
        print("-" * (columns - 2))
        for prop in properties:
            print(row_format.format(prop.property_id, prop.address, prop.location, prop.property_condition, prop.manager, ", ".join(prop.requires_maintenance)))

        property_id = input("\nEnter Property ID to update: ").strip()
        if property_id.lower() == 'b':
            return
        property = next((prop for prop in properties if prop.property_id == property_id), None)
        if not property:
            print(f"No property found with ID {property_id}")
            input("\nPress Enter to return to the menu.")
            return

        print("\nCurrent Information:")
        print(row_format.format(*headers))
        print("-" * (columns - 2))
        print(row_format.format(property.property_id, property.address, property.location, property.property_condition, property.manager, ", ".join(property.requires_maintenance)))

        field = input("\nEnter the field to update (address, location, property_condition, manager, requires_maintenance): ").strip()
        if field.lower() == 'b':
            return
        new_value = input(f"Enter new value for {field}: ").strip()
        if new_value.lower() == 'b':
            return
        updated_details = {field: new_value}
        result = self.logic_layer.update_property(property_id, updated_details)
        print(result)

        # Fetch the updated property information
        updated_property = self.logic_layer.search_property_by_id(property_id)
        print("\nUpdated Information:")
        print(row_format.format(*headers))
        print("-" * (columns - 2))
        print(row_format.format(updated_property.property_id, updated_property.address, updated_property.location, updated_property.property_condition, updated_property.manager, ", ".join(updated_property.requires_maintenance)))

        input("\nPress Enter to return to the menu.")

    def approve_maintenance_reports(self):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " Approve Maintenance Reports ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        # Implementation for approving maintenance reports
        input("\nPress Enter to return to the menu.")