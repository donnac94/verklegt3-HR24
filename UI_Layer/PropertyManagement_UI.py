import os
import shutil
from Logic_layer.LogicWrapper import LogicWrapper
from UI_Layer.Validation import validate_not_empty


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
            print(d + " b. Back to Supervisor Menu ".ljust(columns - 2) + d)
            print(c + h * (columns - 2) + c)

            choice = input("\nChoose an option: ").strip().lower()

            if choice == "1":
                self.list_all_properties()
            elif choice == "2":
                self.add_new_property()
            elif choice == "3":
                self.update_property_info()
            elif choice == "b":
                return
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
            headers = ["Property ID", "Address", "Location", "Condition", "Supervisor", "Requires Regular Maintenance"]
            col_widths = [max(len(str(getattr(prop, attr))) for prop in properties) for attr in
                          ["property_id", "address", "location", "property_condition", "supervisor", "requires_maintenance"]]
            col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
            row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
            print(row_format.format(*headers))
            print("-" * (columns - 2))
            for prop in properties:
                print(row_format.format(prop.property_id, prop.address, prop.location, prop.property_condition,
                                        prop.supervisor, ", ".join(prop.requires_maintenance)))
        input("\nPress Enter to return to the menu.")

    def add_new_property(self):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " Add New Property ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        print("Enter 'b' at any prompt to cancel and go back to the previous menu.\n")

        # Automatically generate a property ID
        try:
            property_id = self.logic_wrapper.automatic_property_id()
        except Exception as e:
            print(f"Error generating property ID: {e}")
            input("\nPress Enter to return to the menu.")
            return

        property_details = {"property_id": property_id}

        # Input for property address
        while True:
            address = input("Enter Address: ").strip()
            if address.lower() == 'b':
                return
            if not validate_not_empty(address):
                print("Address cannot be empty.")
                input("\nPress Enter to try again.")
                continue
            if self.logic_wrapper.property_exists(address):
                print("Error: Property with this address already exists in the system. Please try again.")
            else:
                property_details["address"] = address
                break

        # Input for property location
        while True:
            location = input("Enter Location: ").strip()
            if location.lower() == 'b':
                return
            if not validate_not_empty(location):
                print("Location cannot be empty.")
                input("\nPress Enter to try again.")
                continue
            property_details["location"] = location
            break

        # Input for property condition
        while True:
            property_condition = input("Enter Property Condition: ").strip()
            if property_condition.lower() == 'b':
                return
            if not validate_not_empty(property_condition):
                print("Property Condition cannot be empty.")
                input("\nPress Enter to try again.")
                continue
            property_details["property_condition"] = property_condition
            break

        supervisor = input("Enter Supervisor for property location").strip()
        if supervisor.lower() == 'b':
            return
        property_details["supervisor"] = supervisor

        # Input for maintenance requirements
        while True:
            requires_maintenance = input("Enter Requires Maintenance (comma-separated, can be empty): ").strip()
            if requires_maintenance.lower() == 'b':
                return
            property_details["requires_maintenance"] = [item.strip() for item in requires_maintenance.split(",") if item.strip()]
            break

        # Save the new property using LogicWrapper
        result = self.logic_wrapper.add_property(property_details)
        if result == "Property added successfully.":
            print("\nProperty added successfully!")
        else:
            print("\n" + result)
            input("\nPress Enter to return to the menu.")
            return

        # Confirm the new property has been added
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

        headers = ["Property ID", "Address", "Location", "Condition", "Supervisor", "Requires Maintenance"]
        col_widths = [max(len(str(getattr(prop, attr))) for prop in properties) for attr in ["property_id", "address", "location", "property_condition", "supervisor", "requires_maintenance"]]
        col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
        row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
        print(row_format.format(*headers))
        print("-" * (columns - 2))
        for prop in properties:
            print(row_format.format(prop.property_id, prop.address, prop.location, prop.property_condition, prop.supervisor, ", ".join(prop.requires_maintenance)))

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
        print(row_format.format(property.property_id, property.address, property.location, property.property_condition, property.supervisor, ", ".join(property.requires_maintenance)))

        selected_field = input("\nEnter the field to update: \n1. Address \n2. Location \n3. Property condition \n4. Supervisor \n5. Requires maintenance ").strip()
        while True:    
            if selected_field.lower() == 'b':
                return
            elif selected_field == '1':
                selected_field = "address"
                break
            elif selected_field == '2':
                selected_field = "location"
                break
            elif selected_field == '3':
                selected_field = "property_condition"
                break
            elif selected_field == '4':
                selected_field = "supervisor"
                break
            elif selected_field == '5':
                selected_field = "requires_maintenance"
                break
            else:
                selected_field = input("\nYou must choose a number between 1-5, try again.\n")

        new_value = input(f"Enter the new value for your chosen field: ").strip()
        if new_value.lower() == 'b':
            return
        if selected_field == "requires_maintenance":
            updated_details = {selected_field: [item.strip() for item in new_value.split(",") if item.strip()]}
        else:
            updated_details = {selected_field: new_value}
        result = self.logic_wrapper.update_property(property_id, updated_details)
        print(result)

        updated_property = self.logic_wrapper.get_property_by_id(property_id)
        print("\nUpdated Information:")
        print(row_format.format(*headers))
        print("-" * (columns - 2))
        print(row_format.format(updated_property.property_id, updated_property.address, updated_property.location, updated_property.property_condition, updated_property.supervisor, ", ".join(updated_property.requires_maintenance)))

        input("\nPress Enter to return to the menu.")