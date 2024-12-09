from Logic_layer.LogicWrapper import LogicWrapper
import os
import shutil
import sys

class EmployeeUI:
    def __init__(self, logic_wrapper: LogicWrapper):
        self.logic_wrapper = logic_wrapper

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_terminal_size(self):
        """Get the current terminal size."""
        columns, rows = shutil.get_terminal_size(fallback=(80, 24))
        return columns, rows

    def display_menu(self):
        while True:
            self.clear_terminal()
            columns, _ = self.get_terminal_size()
            h = '-'
            c = '+'
            d = '|'
            print(c + "Air NaN Employee Portal".center(columns - 2, h) + c)
            print(d + "Welcome to the Employee Menu".center(columns - 2) + d)
            print(c + h * (columns - 2) + c)
            print(d + " 1. List All Employees ".ljust(columns - 2) + d)
            print(d + " b. Back to Login Menu ".ljust(columns - 2) + d)
            print(d + " q. Quit ".ljust(columns - 2) + d)
            print(c + h * (columns - 2) + c)

            choice = input("\nChoose an option: ").strip().lower()

            if choice == "1":
                self.list_all_employees()
            elif choice == "b":
                return
            elif choice == "q":
                print("Exiting Employee Menu. Goodbye!")
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
                print(row_format.format(emp.ssn, emp.full_name, emp.address, emp.phone, emp.gsm, emp.email, emp.location, emp.is_manager))
        input("\nPress Enter to return to the menu.")
