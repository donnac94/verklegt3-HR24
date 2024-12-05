
from Data_Layer.PropertyData import PropertyData
from Logic_layer.PropertyLogic import PropertyLogic
from Logic_layer.LogicWrapper import LogicWrapper
from UI_Layer.PropertyUI import PropertyUI

def main():
    # Initialize the data layer
    property_data = PropertyData(file_name="Files/properties.csv")
    
    # Initialize the logic layer
    property_logic = PropertyLogic(property_data)
    
    # Initialize the logic wrapper
    logic_wrapper = LogicWrapper()
    logic_wrapper.property_logic = property_logic
    
    # Initialize the UI layer
    property_ui = PropertyUI(logic_wrapper)
    
    # Run the UI
    property_ui.display_menu()

if __name__ == "__main__":
    main()