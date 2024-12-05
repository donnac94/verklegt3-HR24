import os


class SupervisorUI:
    def __init__(self, logic_layer):
        """
        Initialize the Supervisor UI with a reference to the logic layer.
        :param logic_layer: An object containing the logic for supervisor-related operations.
        """
        self.logic_layer = logic_layer

    def clear_terminal(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_menu(self):
        """Display the supervisor menu and handle user input."""
        while True:
            self.clear_terminal()
            h = '-'
            c = '+'
            d = '|'
            print(c + "Air NaN Supervisor Portal".center(63, h) + c)
            print(d + "Welcome to the Supervisor Menu".center(63) + d)
            print(c + h * 63 + c)
            print(d + " 1. List All Employees ".ljust(62) + d)
            print(d + " 2. Add New Employee ".ljust(62) + d)
            print(d + " 3. Update Employee Information ".ljust(62) + d)
            print(d + " 4. List All Properties ".ljust(62) + d)
            print(d + " 5. Add New Property ".ljust(62) + d)
            print(d + " 6. Update Property Information ".ljust(62) + d)
            print(d + " 7. Approve Maintenance Reports ".ljust(62) + d)
            print(d + " q. Quit ".ljust(62) + d)
            print(c + h * 63 + c)

            choice = input("\nChoose an option: ").strip().lower()

            if choice == "1":
                self.list_all_employees()
            elif choice == "2":
                self.add_new_employee()
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
            elif choice == "q":
                print("Exiting Supervisor Menu. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to return to the menu.")