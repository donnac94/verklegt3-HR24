from Data_Layer.PropertyData import PropertyData
from Data_Layer.EmployeeData import EmployeeData
from Data_Layer.DataWrapper import DataWrapper
from Logic_layer.PropertyLogic import PropertyLogic
from Logic_layer.WorkOrderLogic import WorkOrderLogic
from Logic_layer.EmployeeLogic import EmployeeLogic
from Logic_layer.ContractorLogic import ContractorLogic
from Logic_layer.MaintenanceReportLogic import MaintenanceReportLogic
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
        
        # Initialize the data wrapper
        data_wrapper = DataWrapper(employee_file="Files/employees.csv", property_file="Files/properties.csv")
        
        # Initialize the logic layer
        property_logic = PropertyLogic(property_data)
        employee_logic = EmployeeLogic(employee_data)
        work_order_logic = WorkOrderLogic(data_wrapper)
        contractor_logic = ContractorLogic()
        maintenance_report_logic = MaintenanceReportLogic()
        
        # Initialize the logic wrapper
        logic_wrapper = LogicWrapper(contractor_logic, employee_logic, maintenance_report_logic, property_logic, work_order_logic)
        
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