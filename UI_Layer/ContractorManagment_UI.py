from Logic_layer.LogicWrapper import LogicWrapper
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
            headers = ["Contractor ID", "Name", "Contact Name", "Phone number", "Opening Time", "Location", "Satisfaction With Previous Work"]
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
        
        contractor_id = self.automatic_contractor_id()
        contractor_details = {
            "contractor_id": contractor_id
        }
        
        if contractor_details["contractor_id"].lower() == 'b':
            return
        
        contractor_details.update({
            "name": input("Enter name: ").strip(),
            "contact_name": input("Enter Contact name: ").strip(),
            "phone_nr": input("Enter Phone Number: ").strip(),
            "opening_time": input("Enter Opening Time: ").strip(),
            "location": input("Enter Location: ").strip(),
            "satisfaction_with_previous_work": input("Enter Satisfaction With Previous Work: ").strip()
        })
        if any(value.lower() == 'b' for value in contractor_details.values()):
            return
        result = self.logic_wrapper.create_contractor(contractor_details)
        print(result)
        input("\nPress Enter to return to the menu.")

    def change_contractor_info(self):
        """ Change a contractors information. """
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " Update Contractor Information ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        print("Enter 'b' at any prompt to cancel and go back to the previous menu.\n")

        contractor_id = input("Enter Contractor ID to update: ").strip()
        if contractor_id.lower() == 'b':
            return
    
        contractor = self.logic_wrapper.get_contractor_by_id(contractor_id)
        if not contractor: 
            print("Contractor not found.")
            input("\nPress Enter to return to the menu.")
            return

        updated_details = {}
        name = input("Enter new Name (leave blank to keep current): ").strip()
        if name.lower() == 'b':
            return
        if name:
            updated_details["name"] = name

        contact_name = input("Enter Contact Name (leave blank to keep current): ").strip()
        if contact_name.lower() == 'b':
            return
        if contact_name:
            updated_details["contact_name"] = contact_name

        phone_nr = input("Enter Phone Number (leave blank to keep current): ").strip()
        if phone_nr.lower() == 'b':
            return
        if phone_nr:
            updated_details["phone_nr"] = phone_nr

        opening_time = input("Enter the opening time (leave blank to keep current): ").strip()
        if opening_time.lower() == 'b':
            return
        if opening_time:
            updated_details["opening_time"] = opening_time

        location = input("Enter the Location (leave blank to keep current): ").strip()
        if location.lower() == 'b':
            return
        if location:
            updated_details["location"] = location

        satisfaction_with_previous_work = input("Enter Satisfaction With Previous Work (leave blank to keep current): ").strip()
        if satisfaction_with_previous_work.lower() == 'b':
            return
        if satisfaction_with_previous_work:
            updated_details["satisfaction_with_previous_work"] = satisfaction_with_previous_work
        
        result = self.logic_wrapper.change_contractor_info(contractor_id, updated_details)
        print(result)
        input("\nPress Enter to return to the menu.")

    def automatic_contractor_id(self):
        """
        Gets the latest contractor ID and give it plus 1.
        """
        contractors = self.logic_wrapper.list_contractors()
        latest_contractor = contractors[-1]
        latest_id = int(latest_contractor.contractor_id)
        return latest_id + 1
        
