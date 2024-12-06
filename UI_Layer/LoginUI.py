import os
import shutil

class LoginUI:
    def __init__(self, logic_layer):
        self.logic_layer = logic_layer

    def clear_terminal(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_terminal_size(self):
        """Get the current terminal size."""
        columns, rows = shutil.get_terminal_size(fallback=(80, 24))
        return columns, rows

    def display_menu(self):
        """Display the login menu and handle user input."""
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
                return "supervisor"
            elif choice == "2":
                return "employee"
            elif choice == "q":
                return "q"
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to return to the menu.")