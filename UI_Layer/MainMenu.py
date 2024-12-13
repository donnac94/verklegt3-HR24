from Logic_layer.LogicWrapper import LogicWrapper
import os
import shutil

from UI_Layer.ContractorManagment_UI import ContractorUI
from UI_Layer.EmployeeManagement_UI import EmployeeManagementUI
from UI_Layer.MaintenanceReportManagement_UI import MaintenanceReportUI
from UI_Layer.PropertyManagement_UI import PropertyUI
from UI_Layer.WorkOrderManagement_UI import WorkOrderUI
from UI_Layer.SearchUI import SearchUI

class MainMenu:
    def __init__(self, logic_wrapper: LogicWrapper):
        self.logic_wrapper = logic_wrapper
        self.employee_management_ui = EmployeeManagementUI(logic_wrapper)
        self.property_management_ui = PropertyUI(logic_wrapper)
        self.maintenance_report_ui = MaintenanceReportUI(logic_wrapper)  
        self.work_order_ui = WorkOrderUI(logic_wrapper)
        self.contractor_ui = ContractorUI(logic_wrapper)
        self.search_ui = SearchUI(logic_wrapper)
    def clear_terminal(self):
        """Clears the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_terminal_size(self):
        """Get the current terminal size."""
        columns, rows = shutil.get_terminal_size(fallback=(80, 24))
        return columns, rows

    def display_menu(self, employee_status: str):
        """
        Shows display for the main menu and handle user input.
        :param str employee_status: Either "employee" or "supervisor" which the display uses to know what options should show.
        """
        while True:
            self.clear_terminal()
            columns, _ = self.get_terminal_size()
            h = '-'
            c = '+'
            d = '|'
            print(c + "Air NaN Portal".center(columns - 2, h) + c)
            print(d + "Welcome to the Main Menu".center(columns - 2) + d)
            print(c + h * (columns - 2) + c)
            print(d + " 1. Employee Management ".ljust(columns - 2) + d)
            print(d + " 2. Property Management ".ljust(columns - 2) + d)
            print(d + " 3. Maintenance Report Management ".ljust(columns - 2) + d)
            print(d + " 4. Work Order Management ".ljust(columns - 2) + d)
            print(d + " 5. Contractor Management ".ljust(columns - 2) + d)
            print(d + " 6. Search ".ljust(columns - 2) + d)
            print(d + " b. Back to Login Menu ".ljust(columns - 2) + d)
            print(c + h * (columns - 2) + c)

            choice = input("\nChoose an option: ").strip().lower()

            if choice == "1":
                self.employee_management_ui.display_menu(employee_status)
            elif choice == "2":
                self.property_management_ui.display_menu(employee_status)
            elif choice == "3":
                self.maintenance_report_ui.display_menu(employee_status)
            elif choice == "4":
                self.work_order_ui.display_menu(employee_status) 
            elif choice == "5":
                self.contractor_ui.display_menu(employee_status)
            elif choice == "6":
                self.search_ui.display_menu()
            elif choice == "b":
                return
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to return to the menu.")