from Models.property import Property


def RegisterProperty(properties: list[Property]):
    """
    Register a new property.
    :param properties: List of existing properties.
    """
    try:
        property_id = int(input("Enter Property ID: "))
        if any(p.property_id == property_id for p in properties):
            print("Property ID already exists!")
            return

        address = input("Enter address: ")
        location = input("Enter location (City, Country): ")
        property_condition = input("Enter property condition: ")
        manager = input("Enter manager name: ")
        features = input("Enter features (comma-separated): ").split(",")
        
        new_property = Property(
            property_id=property_id,
            address=address,
            location=location,
            property_condition=property_condition,
            manager=manager,
            features=features,
        )
        properties.append(new_property)
        print("Property registered successfully!")
    except ValueError:
        print("Invalid input. Please try again.")


def ListProperties(properties: list[Property]):
    """
    List all properties.
    :param properties: List of existing properties.
    """
    if not properties:
        print("No properties registered.")
        return

    print("Properties List:")
    for prop in properties:
        print(prop)
        print("-" * 40)


def ChangePropertiesInfo(properties: list[Property]):
    """
    Change information of an existing property.
    :param properties: List of existing properties.
    """
    property_id = int(input("Enter Property ID to edit: "))
    property_to_edit = next((p for p in properties if p.property_id == property_id), None)

    if not property_to_edit:
        print("Property not found!")
        return

    print(f"Editing Property ID: {property_id}")
    property_to_edit.address = input(f"Enter new address (current: {property_to_edit.address}): ") or property_to_edit.address
    property_to_edit.location = input(f"Enter new location (current: {property_to_edit.location}): ") or property_to_edit.location
    property_to_edit.property_condition = input(f"Enter new condition (current: {property_to_edit.property_condition}): ") or property_to_edit.property_condition
    property_to_edit.manager = input(f"Enter new manager (current: {property_to_edit.manager}): ") or property_to_edit.manager
    features = input(f"Enter new features (current: {', '.join(property_to_edit.features)}): ")
    if features:
        property_to_edit.features = features.split(",")

    print("Property updated successfully!")