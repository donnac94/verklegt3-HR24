from Logic_layer.LogicWrapper import LogicWrapper
from UI_Layer.Validation import validate_phone_number, validate_not_empty

import os
import shutil
import sys


class ContractorUI():
    def __init__(self, logic_wrapper: LogicWrapper):
        self.logic_wrapper = logic_wrapper

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def get_terminal_size(self):
        """ Get the current terminal size. """
        columns, rows = shutil.get_terminal_size(fallback=(80, 24))
        return columns, rows
    
    def display_menu(self):
        while True:
            self.clear_terminal()
            columns, _ = self.get_terminal_size()
            h = '-'
            c = '+'
            d = '|'
            print(c + "Air NaN Contractor Portal".center(columns - 2, h) + c)
            print(d + "Welcome to the Contractor Menu".center(columns - 2) + d)
            print(c + h * (columns - 2) + c)
            print(d + " 1. List All Contractors ".ljust(columns - 2) + d)
            print(d + " 2. Add New Contractor ".ljust(columns - 2) + d)
            print(d + " 3. Update Contractor Information ".ljust(columns - 2) + d)
            print(d + " b. Back to Login Menu ".ljust(columns - 2) + d)
            print(d + " q. Quit ".ljust(columns - 2) + d)
            print(c + h * (columns - 2) + c)

            choice = input("\nChoose an option: ").strip().lower()

            if choice == "1":
                self.list_contractors()
            elif choice == "2":
                self.create_contractor()
            elif choice == "3":
                self.change_contractor_info()
            elif choice == "b":
                return
            elif choice == "q":
                print("Exiting Contractor Menu. Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to return to the menu.")

    def list_contractors(self):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()

        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " List All Contractors ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        contractors = self.logic_wrapper.list_contractors()
        if not contractors:
            print("No contractors found.")
        else:
            headers = ["Contractor ID", "Company", "Contact Name", "Phone number", "Opening Time", "Location", "Satisfaction With Previous Work"]
            col_widths = [max(len(str(getattr(cont, attr))) for cont in contractors) for attr in ["contractor_id", "name", "contact_name", "phone_nr", "opening_time", "location", "satisfaction_with_previous_work"]]
            col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
            row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
            print(row_format.format(*headers))
            print("-" * (columns - 2))
            for cont in contractors:
                print(row_format.format(cont.contractor_id, cont.name, cont.contact_name, cont.phone_nr, cont.opening_time, cont.location, cont.satisfaction_with_previous_work))
        input("\nPress Enter to return to the menu.")
    
    def create_contractor(self):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " Add New Contractor ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        print("Enter 'b' at any prompt to cancel and go back to the previous menu.\n")
        
        contractor_id = self.logic_wrapper.automatic_contractor_id()
        contractor_details = {
            "contractor_id": contractor_id
        }
        
        while True:
            name = input("Enter Company: ").strip()
            if name.lower() == 'b':
                return
            if not validate_not_empty(name):
                print("Company name cannot be empty.")
                input("\nPress Enter to try again.")
                continue
            contractor_details["name"] = name
            break

        while True:
            contact_name = input("Enter Contact name: ").strip()
            if contact_name.lower() == 'b':
                return
            if not validate_not_empty(contact_name):
                print("Contact name cannot be empty.")
                input("\nPress Enter to try again.")
                continue
            contractor_details["contact_name"] = contact_name
            break

        while True:
            phone_nr = input("Enter Phone Number: ").strip()
            if phone_nr.lower() == 'b':
                return
            if not validate_phone_number(phone_nr):
                print("Invalid phone number. Please enter digits only.")
                input("\nPress Enter to try again.")
                continue
            contractor_details["phone_nr"] = phone_nr
            break

        while True:
            opening_time = input("Enter Opening Time: ").strip()
            if opening_time.lower() == 'b':
                return
            if not validate_not_empty(opening_time):
                print("Opening time cannot be empty.")
                input("\nPress Enter to try again.")
                continue
            contractor_details["opening_time"] = opening_time
            break

        while True:
            location = input("Enter Location: ").strip()
            if location.lower() == 'b':
                return
            if not validate_not_empty(location):
                print("Location cannot be empty.")
                input("\nPress Enter to try again.")
                continue
            contractor_details["location"] = location
            break

        while True:
            satisfaction_with_previous_work = input("Enter Satisfaction With Previous Work: ").strip()
            if satisfaction_with_previous_work.lower() == 'b':
                return
            if not validate_not_empty(satisfaction_with_previous_work):
                print("Satisfaction with previous work cannot be empty.")
                input("\nPress Enter to try again.")
                continue
            contractor_details["satisfaction_with_previous_work"] = satisfaction_with_previous_work
            break

        result = self.logic_wrapper.create_contractor(contractor_details)
        print(result)
        
        input("\nPress Enter to return to the menu.")

    def change_contractor_info(self):
        """ Change a contractor's information. """
        while True:
            self.clear_terminal()
            columns, _ = self.get_terminal_size()
            print("+".ljust(columns - 1, '-') + "+")
            print("|" + " Update Contractor Information ".center(columns - 2) + "|")
            print("+".ljust(columns - 1, '-') + "+")
            print("Enter 'b' at any prompt to cancel and go back to the previous menu.\n")

            contractor_id = input("Enter Contractor ID to update: ").strip()
            if contractor_id.lower() == 'b':
                return

            self.clear_terminal()
            print("+".ljust(columns - 1, '-') + "+")
            print("|" + " Update Contractor Information ".center(columns - 2) + "|")
            print("+".ljust(columns - 1, '-') + "+")
    
            try:
                contractor = self.logic_wrapper.get_contractor_by_id(contractor_id)
                if not contractor: 
                    print("Contractor not found.")
                    input("\nPress Enter to try again.")
                    continue

                headers = ["Contractor ID", "Company", "Contact Name", "Phone number", "Opening Time", "Location", "Satisfaction With Previous Work"]
                col_widths = [max(len(header), len(str(getattr(contractor, attr)))) for header, attr in zip(headers, ["contractor_id", "name", "contact_name", "phone_nr", "opening_time", "location", "satisfaction_with_previous_work"])]
                row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
                print("\nCurrent Information:")
                print(row_format.format(*headers))
                print("-" * (columns - 2))
                print(row_format.format(contractor.contractor_id, contractor.name, contractor.contact_name, contractor.phone_nr, contractor.opening_time, contractor.location, contractor.satisfaction_with_previous_work))

                selected_field = input("\nEnter the field to update: \n1. Company \n2. Contact Name \n3. Phone Number \n4. Opening Time \n5. Location \n6. Satisfaction With Previous Work ").strip()
                while True:    
                    if selected_field.lower() == 'b':
                        return
                    elif selected_field == '1':
                        selected_field = "name"
                        break
                    elif selected_field == '2':
                        selected_field = "contact_name"
                        break
                    elif selected_field == '3':
                        selected_field = "phone_nr"
                        break
                    elif selected_field == '4':
                        selected_field = "opening_time"
                        break
                    elif selected_field == '5':
                        selected_field = "location"
                        break
                    elif selected_field == '6':
                        selected_field = "satisfaction_with_previous_work"
                        break
                    else:
                        selected_field = input("\nYou must choose a number between 1-6, try again.\n")

                while True:
                    new_value = input(f"\nEnter the new value for {selected_field.replace('_', ' ')}: ").strip()
                    if new_value.lower() == 'b':
                        return
                    if selected_field == "phone_nr" and not validate_phone_number(new_value):
                        print("Invalid phone number. Please enter digits only.")
                        input("\nPress Enter to try again.")
                        continue
                    break

                updated_details = {selected_field: new_value}
                result = self.logic_wrapper.change_contractor_info(contractor_id, updated_details)
                print(result)

                self.clear_terminal()
                print("+".ljust(columns - 1, '-') + "+")
                print("|" + " Update Contractor Information ".center(columns - 2) + "|")
                print("+".ljust(columns - 1, '-') + "+")
                updated_contractor = self.logic_wrapper.get_contractor_by_id(contractor_id)
                print("\nUpdated Information:")
                print(row_format.format(*headers))
                print("-" * (columns - 2))
                print(row_format.format(updated_contractor.contractor_id, updated_contractor.name, updated_contractor.contact_name, updated_contractor.phone_nr, updated_contractor.opening_time, updated_contractor.location, updated_contractor.satisfaction_with_previous_work))

                input("\nPress Enter to return to the menu.")
                return
            except ValueError as e: 
                print(e)
                input("\nPress Enter to try again.")

