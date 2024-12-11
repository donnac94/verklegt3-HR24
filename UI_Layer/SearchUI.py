import sys
from Logic_layer.ContractorLogic import ContractorLogic
from Logic_layer.EmployeeLogic import EmployeeLogic
from Logic_layer.LocationLogic import LocationLogic
from Logic_layer.MaintenanceReportLogic import MaintenanceReportLogic
from Logic_layer.PropertyLogic import PropertyLogic
from Logic_layer.WorkOrderLogic import WorkOrderLogic

class SearchUI:
    
    def __init__(self):
        self.contractor_logic = ContractorLogic
        self.employee_logic = EmployeeLogic
        self.location_logic = LocationLogic
        self.maintenance_report_logic = MaintenanceReportLogic
        self.property_logic = PropertyLogic
        self.workorder_logic = WorkOrderLogic 
    
    def display_search_main_menu(self):
        while True:
            self.clear_terminal()
            columns, _ = self.get_terminal_size()
            h = '-'
            c = '+'
            d = '|'
            print(c + "Air NaN Employee Portal".center(columns - 2, h) + c)
            print(d + "Welcome to the Search Menu".center(columns - 2) + d)
            print(c + h * (columns - 2) + c)
            print(d + " 1. List All Employees and Properties by Location ".ljust(columns - 2) + d)
            print(d + " 2. Search Employee by SSN ".ljust(columns - 2) + d)
            print(d + " 3. Search Property by ID ".ljust(columns - 2) + d)
            print(d + " 4. Search Workorder by ID".ljust(columns - 2) + d)
            print(d + " q. Quit ".ljust(columns - 2) + d)
            print(c + h * (columns - 2) + c)

            choice = input("\nChoose an option: ").strip().lower()

            if choice == '1':
                location = input("Enter a Location: ")
                 
            elif choice == '2':
                pass
            elif choice == '3':
                pass
            elif choice == '4':
                pass
            elif choice == "q":
                print("Exiting Employee Menu. Goodbye!")
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to return to the menu.")
        