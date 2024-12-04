import os
from Models.property import Property
import Data_Layer.PropertyData as PropertyData

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def property_menu():
    """
    Displays the property management menu and handles user choices.
    """
    property_data = PropertyData()
    
    while True:
        clear_screen()
        print("=== Property Management System ===")
        print("1. Register Property")
        print("2. List All Properties")
        print("3. Update Property Info")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            register_property_tui(property_data)
        elif choice == "2":
            list_properties_tui(property_data)
        elif choice == "3":
            update_property_info_tui(property_data)
        elif choice == "4":
            print("Exiting Property Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

def register_property_tui(property_data: PropertyData):
    """
    Handles registering a new property via TUI.
    """
    clear_screen()
    print("=== Register New Property ===")
    try:
        property_id = int(input("Enter Property ID: "))
        address = input("Enter Address: ")
        location = input("Enter Location (City, Country): ")
        property_condition = input("Enter Property Condition: ")
        manager = input("Enter Manager Name: ")
        features = input("Enter Features (comma-separated): ").split(",")
        requires_maintenance = input("Enter Maintenance Needs (comma-separated): ").split(",")

        new_property = Property(
            property_id=property_id,
            address=address,
            location=location,
            property_condition=property_condition,
            manager=manager,
            features=[f.strip() for f in features if f.strip()],
            requires_maintenance=[rm.strip() for rm in requires_maintenance if rm.strip()],
        )
        property_data.RegisterProperty(new_property)
        print("Property registered successfully!")
    except ValueError:
        print("Invalid input. Please enter the correct data types.")
    except Exception as e:
        print(f"An error occurred: {e}")
    input("Press Enter to continue...")

def list_properties_tui(property_data: PropertyData):
    """
    Handles listing all properties via TUI.
    """
    clear_screen()
    print("=== List of All Properties ===")
    properties = property_data.GetAllProperties()

    if not properties:
        print("No properties found.")
    else:
        for prop in properties:
            print(prop)
            print("-" * 40)
    input("Press Enter to continue...")

def update_property_info_tui(property_data: PropertyData):
    """
    Handles updating property information via TUI.
    """
    clear_screen()
    print("=== Update Property Information ===")
    try:
        property_id = int(input("Enter the Property ID to update: "))
        properties = property_data.GetAllProperties()
        property_to_edit = next((p for p in properties if p.property_id == property_id), None)

        if not property_to_edit:
            print("Property not found!")
        else:
            print(f"Editing Property ID: {property_id}")
            address = input(f"Enter new Address (current: {property_to_edit.address}): ") or property_to_edit.address
            location = input(f"Enter new Location (current: {property_to_edit.location}): ") or property_to_edit.location
            property_condition = input(f"Enter new Condition (current: {property_to_edit.property_condition}): ") or property_to_edit.property_condition
            manager = input(f"Enter new Manager (current: {property_to_edit.manager}): ") or property_to_edit.manager
            features = input(f"Enter new Features (current: {', '.join(property_to_edit.features)}): ")
            requires_maintenance = input(f"Enter new Maintenance Needs (current: {', '.join(property_to_edit.requires_maintenance)}): ")

            updated_property = Property(
                property_id=property_id,
                address=address,
                location=location,
                property_condition=property_condition,
                manager=manager,
                features=[f.strip() for f in features.split(",")] if features else property_to_edit.features,
                requires_maintenance=[rm.strip() for rm in requires_maintenance.split(",")] if requires_maintenance else property_to_edit.requires_maintenance,
            )

            success = property_data.ChangePropertyInfo(property_id, updated_property)
            if success:
                print("Property updated successfully!")
            else:
                print("Failed to update property.")
    except ValueError:
        print("Invalid input. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
    input("Press Enter to continue...")

if __name__ == "__main__":
    property_menu()