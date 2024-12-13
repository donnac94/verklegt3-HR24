from UI_Layer.MainMenu import SupervisorUI
from Logic_layer.LogicWrapper import LogicWrapper
import os
import shutil

class LoginUI:
    def __init__(self):
        self.logic_wrapper = LogicWrapper()

    def clear_terminal(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_terminal_size(self):
        """Get the current terminal size."""
        columns, rows = shutil.get_terminal_size(fallback=(80, 24))
        return columns, rows

    def display_menu(self):
        """Display the login menu and handle user input."""
        supervisor_ui = SupervisorUI(self.logic_wrapper)
        # employee_ui = EmployeeUI(self.logic_wrapper)
        while True:
            self.clear_terminal()
            columns, _ = self.get_terminal_size()
            h = '-'
            c = '+'
            d = '|'

            print(c + " Air NaN Login ".center(columns - 2, h) + c)
            print(d + " Welcome to Air NaN ".center(columns - 2) + d)
            print(c + h * (columns - 2) + c)
            print(d + " 1. Supervisor ".ljust(columns - 2) + d)
            print(d + " 2. Employee ".ljust(columns - 2) + d)
            print(d + " q. Quit ".ljust(columns - 2) + d)
            print(c + h * (columns - 2) + c)

            choice = input("\nChoose an option: ").strip().lower()

            if choice == "1":
                supervisor_ui.display_menu("supervisor")
            elif choice == "2":
                supervisor_ui.display_menu("employee")
            elif choice == "q":
                print("\n Exiting. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to return to the menu.")