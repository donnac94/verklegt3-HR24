import os


class EmployeeUI:
    def __init__(self, logic_layer):
        """
        Initialize the Employee UI with a reference to the logic layer.
        :param logic_layer: An object containing the logic for employee-related operations.
        """
        self.logic_layer = logic_layer

    def clear_terminal(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_menu(self):
        """Display the employee menu and handle user input."""
        while True:
            self.clear_terminal()
            h = '-'
            c = '+'
            d = '|'
            print(c + "Air NaN Employee Portal".center(63, h) + c)
            print(d + "Welcome to the Employee Menu".center(63) + d)
            print(c + h * 63 + c)
            print(d + " 1. List Assigned Work Orders ".ljust(62) + d)
            print(d + " 2. Submit Maintenance Report ".ljust(62) + d)
            print(d + " 3. View Past Work Orders ".ljust(62) + d)
            print(d + " 4. Mark Work Order as Ready for Approval ".ljust(62) + d)
            print(d + " 5. Search Work Orders by ID ".ljust(62) + d)
            print(d + " q. Quit ".ljust(62) + d)
            print(c + h * 63 + c)

            choice = input("\nChoose an option: ").strip().lower()

            if choice == "1":
                self.list_assigned_work_orders()
            elif choice == "2":
                self.submit_maintenance_report()
            elif choice == "3":
                self.view_past_work_orders()
            elif choice == "4":
                self.mark_work_order_ready()
            elif choice == "5":
                self.search_work_orders()
            elif choice == "q":
                print("Exiting Employee Menu. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to return to the menu.")