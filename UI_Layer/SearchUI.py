from Logic_layer.LogicWrapper import LogicWrapper
import os
import shutil
import sys

from Logic_layer.SearchLogic import SearchLogic
from Logic_layer.LogicWrapper import LogicWrapper
class SearchUI:
    
    def __init__(self):
        self.search_logic = SearchLogic()
        self.logic_wrapper = LogicWrapper
    
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
            print(c + "Air NaN Employee Portal".center(columns - 2, h) + c)
            print(d + "Welcome to the Search Menu".center(columns - 2) + d)
            print(c + h * (columns - 2) + c)
            print(d + " 1. List All Employees and Properties by Location ".ljust(columns - 2) + d)
            print(d + " 2. Search Employee by SSN ".ljust(columns - 2) + d)
            print(d + " 3. Search Property by ID ".ljust(columns - 2) + d)
            print(d + " 4. Search Workorder by ID".ljust(columns - 2) + d)
            print(c + h * (columns - 2) + c)

            choice = input("\nChoose an option: ").strip().lower()

            if choice == '1':
                # return self.location_filter
                location_input = input("\nEnter location: ")
                results = self.search_logic.search_by_location(location_input)
                print("\nResults: ",results)
            elif choice == '2':
                # return self.ssn_filter
                employee_input = input("\n Enter Social Security number: ")
                results = self.search_logic.search_employee_by_ssn(employee_input)
                print("\nResults: ", results)
            elif choice == '3':
                # return self.property_filter
                property_input = input("\nEnter a property id: ")
                results = self.search_logic.search_property_id(property_input)
                print("\nResults: ", results)
            elif choice == '4':
                workorder = input("\nEnter a workorder id: ")
                result = self.search_logic.search_workorder_id(workorder)
                return result
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to return to the menu.")
    
    # def location_filter(self):
    #     location = input("\nEnter a location: ")
    #     if location != None: 
    #         result = self.search_logic.search_by_location(location)
    #     return result
        
    
    # def ssn_filter(self):
    #     ssn = input("\nEnter a SSN: ")
    #     if ssn != None:
    #         result = self.search_logic.search_employee_by_ssn(ssn)
    #     return result 
        
    
    # def property_filter(self):
    #     property_id = input("\nEnter a Property id: ")
    #     if property_id != None:
    #         result = self.search_logic.search_property_id(property_id)
    #     return result
    
    # def workid_filter(self):
    #     work_id = input("\nEnter a work id: ")
    #     if work_id != None:
    #         result = self.search_logic.search_workorder_id(work_id)
    #     return result
    
        
    
        