from Data_Layer.PropertyData import PropertyData
from Data_Layer.EmployeeData import EmployeeData
from Logic_layer.PropertyLogic import PropertyLogic
from Logic_layer.LogicWrapper import LogicWrapper
from UI_Layer.LoginUI import LoginUI
from UI_Layer.SupervisorUI import SupervisorUI
from UI_Layer.EmployeeUI import EmployeeUI
import sys

def main():
    while True:
        # Initialize the data layer
        property_data = PropertyData(file_name="Files/properties.csv")
        employee_data = EmployeeData(file_name="Files/employees.csv")
        
        # Initialize the logic layer
        property_logic = PropertyLogic(property_data)
        
        # Initialize the logic wrapper
        logic_wrapper = LogicWrapper(employee_data, property_data)
        logic_wrapper.property_logic = property_logic
        
        # Initialize the login UI
        login_ui = LoginUI(logic_wrapper)
        user_type = login_ui.display_menu()
        
        if user_type == "supervisor":
            # Initialize the supervisor UI
            supervisor_ui = SupervisorUI(logic_wrapper)
            # Run the supervisor UI
            supervisor_ui.display_menu()
        elif user_type == "employee":
            # Initialize the employee UI
            employee_ui = EmployeeUI(logic_wrapper)
            # Run the employee UI
            employee_ui.display_menu()
        elif user_type == "q":
            print("Exiting. Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()