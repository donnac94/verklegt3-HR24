import os
import shutil
import sys

class PropertyUI:
    def __init__(self, logic_layer):
        self.logic_layer = logic_layer

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_terminal_size(self):
        """Get the current terminal size."""
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
            print(d + "Welcome to the Property Menu".center(columns - 2) + d)
            print(c + h * (columns - 2) + c)
            print(d + " 1. List All Properties ".ljust(columns - 2) + d)
            print(d + " 2. Add New Property ".ljust(columns - 2) + d)
            print(d + " 3. Update Property Information ".ljust(columns - 2) + d)
            print(d + " b. Back to Login Menu ".ljust(columns - 2) + d)
            print(d + " q. Quit ".ljust(columns - 2) + d)
            print(c + h * (columns - 2) + c)

            choice = input("\nChoose an option: ").strip().lower()

            if choice == "1":
                self.list_all_properties()
            elif choice == "2":
                self.add_new_property()
            elif choice == "3":
                self.update_property()
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
        properties = self.logic_layer.list_properties()
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
        property_details = {
            "property_id": input("Enter Property ID: ").strip()
        }
        if property_details["property_id"].lower() == 'b':
            return
        property_details.update({
            "address": input("Enter Address: ").strip(),
            "location": input("Enter Location: ").strip(),
            "property_condition": input("Enter Property Condition: ").strip(),
            "manager": input("Enter Manager: ").strip(),
            "requires_maintenance": input("Enter Requires Maintenance (comma-separated): ").strip()
        })
        if any(value.lower() == 'b' for value in property_details.values()):
            return
        result = self.logic_layer.add_property(property_details)
        print(result)
        input("\nPress Enter to return to the menu.")

    def update_property(self):
        """Update an existing property."""
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " Update Property ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        print("Enter 'b' at any prompt to cancel and go back to the previous menu.\n")
        property_id = input("Enter Property ID to update: ").strip()
        if property_id.lower() == 'b':
            return
        updated_details = {}
        address = input("Enter new Address (leave blank to keep current): ").strip()
        if address.lower() == 'b':
            return
        if address:
            updated_details["address"] = address
        location = input("Enter new Location (leave blank to keep current): ").strip()
        if location.lower() == 'b':
            return
        if location:
            updated_details["location"] = location
        property_condition = input("Enter new Property Condition (leave blank to keep current): ").strip()
        if property_condition.lower() == 'b':
            return
        if property_condition:
            updated_details["property_condition"] = property_condition
        manager = input("Enter new Manager (leave blank to keep current): ").strip()
        if manager.lower() == 'b':
            return
        if manager:
            updated_details["manager"] = manager
        requires_maintenance = input("Enter new Requires Maintenance (comma-separated, leave blank to keep current): ").strip()
        if requires_maintenance.lower() == 'b':
            return
        if requires_maintenance:
            updated_details["requires_maintenance"] = requires_maintenance

        result = self.logic_layer.update_property(property_id, updated_details)
        print(result)
        input("\nPress Enter to return to the menu.")