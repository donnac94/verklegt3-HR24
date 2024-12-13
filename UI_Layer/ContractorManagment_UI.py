from Logic_layer.LogicWrapper import LogicWrapper
from UI_Layer.Validation import InputValidation


import os
import shutil

class ContractorUI():
    def __init__(self, logic_wrapper: LogicWrapper):
        self.logic_wrapper = logic_wrapper

    def clear_terminal(self):
        """Clears the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def get_terminal_size(self):
        """ Get the current terminal size. """
        columns, rows = shutil.get_terminal_size(fallback=(80, 24))
        return columns, rows
    
    def display_menu(self, employee_status: str):
        """
        Shows display menu for contractor management and handle user input.
        :param str employee_status: Either "employee" or "supervisor" which the display uses to know what options should show.
        """
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
            if employee_status == "supervisor":
                print(d + " 2. Add New Contractor ".ljust(columns - 2) + d)
                print(d + " 3. Update Contractor Information ".ljust(columns - 2) + d)
            print(d + " b. Back to Login Menu ".ljust(columns - 2) + d)
            print(c + h * (columns - 2) + c)

            choice = input("\nChoose an option: ").strip().lower()

            if choice == "b":
                return
            if choice == "1":
                self.list_contractors()
            if employee_status == "supervisor":
                if choice == "2":
                    self.create_contractor()
                elif choice == "3":
                    self.change_contractor_info()
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to return to the menu.")

    def list_contractors(self):
        """
        Lists all contractors in CSV file.
        """
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
        """
        Adds a new contractor to the contractors CSV file.
        """
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
            if not InputValidation.validate_not_empty(name):
                print("Company name cannot be empty.")
                input("\nPress Enter to try again.")
                continue
            contractor_details["name"] = name
            break

        while True:
            contact_name = input("Enter Contact name: ").strip()
            if contact_name.lower() == 'b':
                return
            if not InputValidation.validate_not_empty(contact_name):
                print("Contact name cannot be empty.")
                input("\nPress Enter to try again.")
                continue
            contractor_details["contact_name"] = contact_name
            break

        while True:
            phone_nr = input("Enter Phone Number: ").strip()
            if phone_nr.lower() == 'b':
                return
            if not InputValidation.validate_phone_number(phone_nr):
                print("Invalid phone number. Please enter digits only.")
                input("\nPress Enter to try again.")
                continue
            contractor_details["phone_nr"] = phone_nr
            break

        while True:
            opening_time = input("Enter Opening Time: ").strip()
            if opening_time.lower() == 'b':
                return
            if not InputValidation.validate_not_empty(opening_time):
                print("Opening time cannot be empty.")
                input("\nPress Enter to try again.")
                continue
            contractor_details["opening_time"] = opening_time
            break

        while True:
            location = input("Enter Location: ").strip()
            if location.lower() == 'b':
                return
            if not InputValidation.validate_not_empty(location):
                print("Location cannot be empty.")
                input("\nPress Enter to try again.")
                continue
            contractor_details["location"] = location
            break

        while True:
            satisfaction_with_previous_work = input("Enter Satisfaction With Previous Work: ").strip()
            if satisfaction_with_previous_work.lower() == 'b':
                return
            if not InputValidation.validate_not_empty(satisfaction_with_previous_work):
                print("Satisfaction with previous work cannot be empty.")
                input("\nPress Enter to try again.")
                continue
            contractor_details["satisfaction_with_previous_work"] = satisfaction_with_previous_work
            break

        result = self.logic_wrapper.create_contractor(contractor_details)
        print(result)
        
        input("\nPress Enter to return to the menu.")

    def change_contractor_info(self):
        """
        Updates selected contractor with a new value in the chosen field.
        """
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " Update Contractor Information ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        print("Enter 'b' at any prompt to cancel and go back to the previous menu.\n")

        contractors = self.logic_wrapper.list_contractors()
        if not contractors:
            print("No contractors found.")
            input("\nPress Enter to return to the menu.")
            return

        headers = ["Contractor ID", "Company", "Contact Name", "Phone number", "Opening Time", "Location", "Satisfaction With Previous Work"]
        col_widths = [max(len(str(getattr(cont, attr))) for cont in contractors) for attr in ["contractor_id", "name", "contact_name", "phone_nr", "opening_time", "location", "satisfaction_with_previous_work"]]
        col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
        row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
        print(row_format.format(*headers))
        print("-" * (columns - 2))
        for cont in contractors:
            print(row_format.format(cont.contractor_id, cont.name, cont.contact_name, cont.phone_nr, cont.opening_time, cont.location, cont.satisfaction_with_previous_work))

        # Prompt for contractor ID
        while True:
            contractor_id = input("\nEnter Contractor ID to update (or 'b' to go back): ").strip()
            if contractor_id.lower() == 'b':
                return
            try:
                contractor = self.logic_wrapper.get_contractor_by_id(contractor_id)
                if not contractor:
                    print("Contractor not found. Please try again.")
                else:
                    break
            except Exception as e:
                print(f"Error: {e}. Please try again.")

        # Display current information
        print("\nCurrent Information:")
        print(row_format.format(*headers))
        print("-" * (columns - 2))
        print(row_format.format(contractor.contractor_id, contractor.name, contractor.contact_name, contractor.phone_nr, contractor.opening_time, contractor.location, contractor.satisfaction_with_previous_work))

        # Select field to update
        while True:
            print("\nFields to update:")
            print("1. Company")
            print("2. Contact Name")
            print("3. Phone Number")
            print("4. Opening Time")
            print("5. Location")
            print("6. Satisfaction With Previous Work")
            selected_field = input("\nEnter the field number to update (or 'b' to go back): ").strip()
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
                print("Invalid choice. Please select a valid field number.")

        # Prompt for new value
        while True:
            new_value = input(f"Enter the new value for {selected_field.replace('_', ' ').capitalize()} (or 'b' to go back): ").strip()
            if new_value.lower() == 'b':
                return
            if new_value:
                break
            else:
                print("Value cannot be empty. Please enter a valid value.")

        # Update contractor information
        try:
            updated_details = {selected_field: new_value}
            result = self.logic_wrapper.change_contractor_info(contractor_id, updated_details)
            print(result)
        except Exception as e:
            print(f"Error while updating contractor: {e}")
            input("\nPress Enter to return to the menu.")
            return

        # Fetch and display updated contractor information
        try:
            updated_contractor = self.logic_wrapper.get_contractor_by_id(contractor_id)
            print("\nUpdated Information:")
            print(row_format.format(*headers))
            print("-" * (columns - 2))
            print(row_format.format(updated_contractor.contractor_id, updated_contractor.name, updated_contractor.contact_name, 
                                updated_contractor.phone_nr, updated_contractor.opening_time, updated_contractor.location, 
                                updated_contractor.satisfaction_with_previous_work))
        except Exception as e:
            print(f"Error fetching updated contractor: {e}")

        input("\nPress Enter to return to the menu.")
