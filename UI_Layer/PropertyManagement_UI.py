import os
import sys
import shutil
from Logic_layer.LogicWrapper import LogicWrapper


class PropertyUI:
    def __init__(self, logic_wrapper: LogicWrapper):
        self.logic_wrapper = logic_wrapper

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
            print(c + "Air NaN Property Portal".center(columns - 2, h) + c)
            print(d + "Welcome to the Property Management Menu".center(columns - 2) + d)
            print(c + h * (columns - 2) + c)
            print(d + " 1. List All Properties ".ljust(columns - 2) + d)
            print(d + " 2. Add New Property ".ljust(columns - 2) + d)
            print(d + " 3. Update Property Information ".ljust(columns - 2) + d)
            print(d + " 4. Approve Maintenance Reports ".ljust(columns - 2) + d)
            print(d + " b. Back to Supervisor Menu ".ljust(columns - 2) + d)
            print(d + " q. Quit ".ljust(columns - 2) + d)
            print(c + h * (columns - 2) + c)

            choice = input("\nChoose an option: ").strip().lower()

            if choice == "1":
                self.list_all_properties()
            elif choice == "2":
                self.add_new_property()
            elif choice == "3":
                self.update_property_info()
            elif choice == "4":
                self.approve_maintenance_reports()
            elif choice == "b":
                return
            elif choice == "q":
                print("Exiting Property Menu. Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to return to the menu.")

    def list_all_properties(self):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " List All Properties ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        properties = self.logic_wrapper.list_properties()
        if not properties:
            print("No properties found.")
        else:
            headers = ["Property ID", "Address", "Location", "Condition", "Manager", "Requires Maintenance"]
            col_widths = [max(len(str(getattr(prop, attr))) for prop in properties) for attr in ["property_id", "address", "location", "property_condition", "manager", "requires_maintenance"]]
            col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
            row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
            print(row_format.format(*headers))
            print("-" * (columns - 2))
            for prop in properties:
                print(row_format.format(prop.property_id, prop.address, prop.location, prop.property_condition, prop.manager, ", ".join(prop.requires_maintenance)))
        input("\nPress Enter to return to the menu.")

    def add_new_property(self):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " Add New Property ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        print("Enter 'b' at any prompt to cancel and go back to the previous menu.\n")
        property_id = self.automatic_property_id()
        property_details = {
            "property_id": property_id
        }

        address = input("Enter Address: ").strip()
        if address == 'b':
            return
        property_details["address"] = address

        location = input("Enter Location: ").strip()
        if location == 'b':
            return
        property_details["location"] = location

        property_condition = input("Enter Property Condition: ").strip()
        if property_condition == 'b':
            return
        property_details["property_condition"] = property_condition

        manager = input("Enter Manager: ").strip()
        if manager == 'b':
            return
        property_details["manager"] = manager

        requires_maintenance = input("Enter Requires Maintenance (comma-separated): ").strip()
        if requires_maintenance == 'b':
            return
        property_details["requires_maintenance"] = requires_maintenance

        result = self.logic_wrapper.add_property(property_details)
        print(result)
        print("\nProperty added successfully.")
        self.list_all_properties()

    def update_property_info(self):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " Update Property Information ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        print("Enter 'b' at any prompt to cancel and go back to the previous menu.\n")
        properties = self.logic_wrapper.list_properties()
        if not properties:
            print("No properties found.")
            input("\nPress Enter to return to the menu.")
            return

        headers = ["Property ID", "Address", "Location", "Condition", "Manager", "Requires Maintenance"]
        col_widths = [max(len(str(getattr(prop, attr))) for prop in properties) for attr in ["property_id", "address", "location", "property_condition", "manager", "requires_maintenance"]]
        col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
        row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
        print(row_format.format(*headers))
        print("-" * (columns - 2))
        for prop in properties:
            print(row_format.format(prop.property_id, prop.address, prop.location, prop.property_condition, prop.manager, ", ".join(prop.requires_maintenance)))

        property_id = input("\nEnter Property ID to update: ").strip()
        if property_id.lower() == 'b':
            return
        property = next((prop for prop in properties if prop.property_id == property_id), None)
        if not property:
            print(f"No property found with ID {property_id}")
            input("\nPress Enter to return to the menu.")
            return

        print("\nCurrent Information:")
        print(row_format.format(*headers))
        print("-" * (columns - 2))
        print(row_format.format(property.property_id, property.address, property.location, property.property_condition, property.manager, ", ".join(property.requires_maintenance)))

        selected_field = input("\nEnter the field to update: \n1. Address \n2. Location \n3. Property condition \n4. Manager \n5. Requires maintenance ").strip()
        while True:    
            if selected_field.lower() == 'b':
                return
            elif selected_field == '1':
                selected_field = "address"
                break
            elif selected_field == '2':
                field = "location"
                break
            elif selected_field == '3':
                field = "property_condition"
                break
            elif selected_field == '4':
                field = "manager"
                break
            elif selected_field == '5':
                field = "requires_maintenance"
                break
            else:
                selected_field = input("\nYou must choose a number between 1-5, try again.\n")

        new_value = input(f"Enter the new value for your chosen field: ").strip()
        if new_value.lower() == 'b':
            return
        updated_details = {field: new_value}
        result = self.logic_wrapper.update_property(property_id, updated_details)
        print(result)

        # Fetch the updated property information
        updated_property = self.logic_wrapper.get_property_by_id(property_id)
        print("\nUpdated Information:")
        print(row_format.format(*headers))
        print("-" * (columns - 2))
        print(row_format.format(updated_property.property_id, updated_property.address, updated_property.location, updated_property.property_condition, updated_property.manager, ", ".join(updated_property.requires_maintenance)))

        input("\nPress Enter to return to the menu.")

    def approve_maintenance_reports(self):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " Approve Maintenance Reports ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        # Implementation for approving maintenance reports
        input("\nPress Enter to return to the menu.")

    #Possibly should be in another layer?.
    def automatic_property_id(self):
        """
        Gets the latest property ID and give it plus 1.
        """
        properties = self.logic_wrapper.list_properties()
        latest_property = properties[-1]
        latest_id = int(latest_property.property_id)
        return latest_id + 1
