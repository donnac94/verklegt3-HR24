import os

class PropertyUI:
    def __init__(self, logic_layer):
        self.logic_layer = logic_layer

    def clear_terminal(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_menu(self):
        """Display the Property Management menu and handle user input."""
        while True:
            self.clear_terminal()
            h = '-'
            c = '+'
            d = '|'

            print(c + " Air NaN ".center(63, h) + c)
            print(d + " Welcome to Air NaN Property Management ".center(63) + d)
            print(c + h * 63 + c)
            print(d + " Property Management Menu ".center(63) + d)
            print(c + h * 63 + c)
            print(d + " 1. Add Property ".ljust(62) + d)
            print(d + " 2. Update Property ".ljust(62) + d)
            print(d + " 3. List All Properties ".ljust(62) + d)
            print(d + " q. Quit ".ljust(62) + d)
            print(c + h * 63 + c)

            choice = input("\nChoose an option: ").strip().lower()

            if choice == "1":
                self.add_property()
            elif choice == "2":
                self.update_property()
            elif choice == "3":
                self.list_all_properties()
            elif choice == "q":
                print("Exiting Property Management Menu. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to return to the menu.")

    def add_property(self):
        """Add a new property."""
        self.clear_terminal()
        print("+--------------------- Add Property -----------------------------+\n")
        property_details = {
            "property_id": input("Enter Property ID: ").strip(),
            "address": input("Enter Address: ").strip(),
            "location": input("Enter Location: ").strip(),
            "property_condition": input("Enter Property Condition: ").strip(),
            "manager": input("Enter Manager: ").strip(),
            "requires_maintenance": input("Enter Requires Maintenance (comma-separated): ").strip()
        }
        result = self.logic_layer.add_property(property_details)
        print(result)
        input("\nPress Enter to return to the menu.")

    def update_property(self):
        """Update an existing property."""
        self.clear_terminal()
        print("+--------------------- Update Property --------------------------+\n")
        property_id = int(input("Enter Property ID to update: ").strip())
        updated_details = {}
        address = input("Enter new Address (leave blank to keep current): ").strip()
        if address:
            updated_details["address"] = address
        location = input("Enter new Location (leave blank to keep current): ").strip()
        if location:
            updated_details["location"] = location
        property_condition = input("Enter new Property Condition (leave blank to keep current): ").strip()
        if property_condition:
            updated_details["property_condition"] = property_condition
        manager = input("Enter new Manager (leave blank to keep current): ").strip()
        if manager:
            updated_details["manager"] = manager
        requires_maintenance = input("Enter new Requires Maintenance (comma-separated, leave blank to keep current): ").strip()
        if requires_maintenance:
            updated_details["requires_maintenance"] = requires_maintenance

        result = self.logic_layer.update_property(property_id, updated_details)
        print(result)
        input("\nPress Enter to return to the menu.")

    def list_all_properties(self):
        """List all properties."""
        self.clear_terminal()
        print("+--------------------- List All Properties ----------------------+\n")
        properties = self.logic_layer.list_properties()
        if not properties:
            print("No properties found.")
        else:
            for property in properties:
                print(f"Property ID: {property.property_id}, Address: {property.address}, Location: {property.location}, Condition: {property.property_condition}, Manager: {property.manager}, Requires Maintenance: {', '.join(property.requires_maintenance)}")
        input("\nPress Enter to return to the menu.")