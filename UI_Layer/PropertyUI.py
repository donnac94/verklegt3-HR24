from PropertyLogic import change_property_info, list_properties, register_property

from Models.property import Property

def property_menu():
    properties = []  # Initialize an empty list of properties

    while True:
        print("\n=== Property Management Menu ===")
        print("1. Register Property")
        print("2. List Properties")
        print("3. Change Property Info")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            register_property_ui(properties)
        elif choice == "2":
            list_properties_ui(properties)
        elif choice == "3":
            change_property_info_ui(properties)
        elif choice == "4":
            print("Exiting Property Management.")
            break
        else:
            print("Invalid choice. Please try again.")

def register_property_ui(properties: list[Property]):
    try:
        property_details = {
            "property_id": int(input("Enter Property ID: ")),
            "address": input("Enter address: "),
            "location": input("Enter location (City, Country): "),
            "property_condition": input("Enter property condition: "),
            "manager": input("Enter manager name: "),
        }
        message = register_property(properties, property_details)
        print(message)
    except ValueError:
        print("Invalid input. Please enter valid data.")

def list_properties_ui(properties: list[Property]):
    props = list_properties(properties)
    if not props:
        print("No properties registered.")
    else:
        for prop in props:
            print(prop)
            print("-" * 40)

def change_property_info_ui(properties: list[Property]):
    try:
        property_id = int(input("Enter Property ID to edit: "))
        updated_details = {
            "address": input("Enter new address: "),
            "location": input("Enter new location: "),
            "property_condition": input("Enter new property condition: "),
            "manager": input("Enter new manager name: "),
        }
        message = change_property_info(properties, property_id, updated_details)
        print(message)
    except ValueError:
        print("Invalid input. Please enter valid data.")

if __name__ == "__main__":
    property_menu()