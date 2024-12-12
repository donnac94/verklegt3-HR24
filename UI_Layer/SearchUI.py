from Logic_layer.LogicWrapper import LogicWrapper
import os
import shutil

class SearchUI:
    
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
            print(c + "Air NaN Employee Portal".center(columns - 2, h) + c)
            print(d + "Welcome to the Search Menu".center(columns - 2) + d)
            print(c + h * (columns - 2) + c)
            print(d + " 1. List All Employees and Properties by Location ".ljust(columns - 2) + d)
            print(d + " 2. Search Employee by SSN ".ljust(columns - 2) + d)
            print(d + " 3. Search Property by ID ".ljust(columns - 2) + d)
            print(d + " 4. Search Workorder by ID".ljust(columns - 2) + d)
            print(d + " 5. Search Workorder by Property".ljust(columns - 2) + d)
            print(d + " 6. Search maintenance reports by property".ljust(columns - 2) + d)
            print(d + " 7. Search Workorders by employee".ljust(columns - 2) + d)
            print(d + " 8. Search maintenance reports by employee".ljust(columns - 2) + d)
            print(d + " 9. Get work plan".ljust(columns - 2) + d)
            print(c + h * (columns - 2) + c)

            choice = input("\nChoose an option: ").strip().lower()

            if choice == '1':
                self.clear_terminal()
                columns, _ = self.get_terminal_size()
                h = '-'
                c = '+'
                d = '|'
                print(c + "Air NaN Employee Portal".center(columns - 2, h) + c)
                print(d + "Welcome to the Search Menu".center(columns - 2) + d)
                print(c + h * (columns - 2) + c)
                print(d + " 1. List All Employees by Location ".ljust(columns - 2) + d)
                print(d + " 2. List All Properties by location ".ljust(columns - 2) + d)
                print(c + h * (columns - 2) + c)
                choice = input("\nEnter what list you want to see: ")
                if choice == '1':
                    location = input("\n Enter Location: ")
                    self.list_all_employee_by_loc(location)
                elif choice == '2':
                    location_prop = input("\nEnter location: ")
                    self.list_all_prop_by_loc(location_prop)
                else:
                    print("invalid input")
            elif choice == '2':
                ssn = input("\n Enter Social Security number: ")
                
                self.search_employee_by_ssn(ssn)
            elif choice == '3':
                # return self.property_filter
                location = input("\nEnter a property id: ")
                self.list_all_prop_by_loc(location)
            elif choice == '4':
                work_order_id = input("\nEnter Workorder Id: ")
                self.search_work_order_by_id( work_order_id)
            elif choice == '5':
                property_name = input("\nEnter Property Name: ")
                self.search_work_orders_by_property(property_name)
            elif choice == '6':
                property_name = input("\nEnter Property: ")
                self.search_maintenance_reports_by_property(property_name)
            elif choice == '7':
                employee_ssn = input("\nEnter Employee Social Security Number: ")
                self.search_work_orders_by_employee(employee_ssn)
            elif choice == '8':
                employee_ssn = input("\nEnter Employee Social Security Number to search work order: ")
                self.search_work_orders_by_employee(employee_ssn)
            elif choice == "b":
                return
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to return to the menu.")
                
    
    def search_employee_by_ssn(self, ssn):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " List All Employees ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        employee = self.logic_wrapper.search_employee_by_ssn(ssn)
        if not employee:
            print("No employee found.")
        else:
            headers = ["ssn", "full_name", "address", "phone", "gsm", "email", "location", "is_supervisor"]
            col_widths = [(max(len(header), len(str( getattr(employee, attr))))) 
            for header, attr in zip(
                headers, ["ssn", "full_name", "address", "phone", "gsm", "email", "location", "is_supervisor"]
            )]
            row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
            print(row_format.format(*headers))
            print("-" * (columns - 2))

            is_supervisor = employee.is_supervisor
            if is_supervisor == 1:
                is_supervisor = "True"
            else:
                is_supervisor = "False"
            print(row_format.format(employee.ssn, employee.full_name, employee.address, employee.phone, employee.gsm, employee.email, employee.location, is_supervisor))
        input("\nPress Enter to return to the menu.")
        
        
    def list_all_employee_by_loc(self, location):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " List All Employees by Location ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        location = self.logic_wrapper.search_employees_by_location(location)
        if not location:
            print("No employees at location")
        else:
             headers = ["ssn", "full_name", "address", "phone", "gsm", "email", "location", "is_supervisor"]
             col_widths = [max(len(str(getattr(loc, attr))) for loc in location) for attr in
                          ["ssn", "full_name", "address", "phone", "gsm", "email", "location", "is_supervisor"]]
             col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
             row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
             print(row_format.format(*headers))
             print("-" * (columns - 2))
             for loc in location:
                print(row_format.format(loc.ssn, loc.full_name, loc.address, loc.phone, loc.gsm, loc.email,
                                        loc.location, "True" if loc.is_supervisor else "False"))
        input("\nPress Enter to return to the menu.")
        
        
    def list_all_prop_by_loc(self, location):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " List All Properties by Location ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        filtered_properties = self.logic_wrapper.search_properties_by_location(location)
        if not filtered_properties:
            print("No Properties at location")
        else:
             headers = ["property_id", "address", "location", "property_condition", "supervisor", "requires_maintenance"]
             col_widths = [max(len(str(getattr(property, attr))) for property in filtered_properties) for attr in
                          ["property_id", "address", "location", "property_condition", "supervisor", "requires_maintenance"]]
             col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
             row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
             print(row_format.format(*headers))
             print("-" * (columns - 2))
             for property in filtered_properties:
                print(row_format.format(property.property_id, property.address, property.location, property.property_condition, property.supervisor, property.requires_maintenance,  
                                         ))
        input("\nPress Enter to return to the menu.")
        

    def list_property_by_id(self, property_id):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " List Property by ID ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        property = self.logic_wrapper.search_property_by_id(property_id)
        if not property:
            print("No property found.")
        else:
            headers = ["property_id", "address", "location", "property_condition", "supervisor", "requires_maintenance"]
            col_widths = [(max(len(header), len(str( getattr(property, attr))))) 
            for header, attr in zip(
                headers, ["property_id", "address", "location", "property_condition", "supervisor", "requires_maintenance"]
            )]
            row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
            print(row_format.format(*headers))
            print("-" * (columns - 2))

            print(row_format.format(property.property_id, property.address, property.location, property.property_condition, property.supervisor, 
                                    property.requires_maintenance))
        input("\nPress Enter to return to the menu.")

    def search_work_order_by_id(self, work_order_id):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " List Work Order By ID ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        work_order = self.logic_wrapper.search_work_order_by_id(work_order_id)
        if not work_order:
            print("No work order found.")
        else:
            headers = ["work_order_id", "work_to_be_done", "property", "submitting_supervisor", "date", "priority", "work_order_status"]
            col_widths = [(max(len(header), len(str( getattr(work_order, attr))))) 
            for header, attr in zip(
                headers, ["work_order_id", "work_to_be_done", "property", "submitting_supervisor", "date", "priority", "work_order_status"]
            )]
            row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
            print(row_format.format(*headers))
            print("-" * (columns - 2))

            print(row_format.format(work_order.work_order_id, work_order.work_to_be_done, work_order.property, work_order.submitting_supervisor, work_order.date, 
                                    work_order.priority, work_order.work_order_status))
        input("\nPress Enter to return to the menu.")

    def search_work_orders_by_property(self, property_name):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " List All Work Orders By Property ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        filtered_work_orders = self.logic_wrapper.search_work_orders_by_property(property_name)
        if not filtered_work_orders:
            print("No work orders for this property")
        else:
             headers = ["work_order_id", "work_to_be_done", "property", "submitting_supervisor", "date", "priority", "work_order_status"]
             col_widths = [max(len(str(getattr(work_order, attr))) for work_order in filtered_work_orders) for attr in
                          ["work_order_id", "work_to_be_done", "property", "submitting_supervisor", "date", "priority", "work_order_status"]]
             col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
             row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
             print(row_format.format(*headers))
             print("-" * (columns - 2))
             for work_order in filtered_work_orders:
                print(row_format.format(work_order.work_order_id, work_order.work_to_be_done, work_order.property, work_order.submitting_supervisor, work_order.date, 
                                        work_order.priority, work_order.work_order_status))
        input("\nPress Enter to return to the menu.")

    def search_maintenance_reports_by_property(self, property_name):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " List All Maintenance Reports By Property ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        filtered_maintenance_reports = self.logic_wrapper.search_maintenance_reports_by_property(property_name)
        if not filtered_maintenance_reports:
            print("No maintenance reports for this property")
        else:
             headers = ["maintenance_report_id", "connected_work_order_id", "property", "work_done", "upkeep_status", "employee", "total_costs", "marked_as_finished", "report_closed", "contractors_used"]
             col_widths = [max(len(str(getattr(work_order_id, attr))) for work_order_id in filtered_maintenance_reports) for attr in
                          ["maintenance_report_id", "connected_work_order_id", "property", "work_done", "upkeep_status", "employee", "total_costs", "marked_as_finished", "report_closed", "contractors_used"]]
             col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
             row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
             print(row_format.format(*headers))
             print("-" * (columns - 2))
             for maintenance_report in filtered_maintenance_reports:
                print(row_format.format(maintenance_report.maintenance_report_id, maintenance_report.connected_work_order_id, maintenance_report.property, 
                                        maintenance_report.work_done, maintenance_report.upkeep_status, maintenance_report.employee, maintenance_report.total_costs, 
                                        maintenance_report.marked_as_finished, maintenance_report.report_closed, maintenance_report.contractors_used))
        input("\nPress Enter to return to the menu.")
    
    def search_work_orders_by_employee(self, employee_ssn):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " List All Work Orders By Employee SSN ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        filtered_work_orders = self.logic_wrapper.search_work_orders_by_employee(employee_ssn)
        if not filtered_work_orders:
            print("No work orders for this employee")
        else:
             headers = ["work_order_id", "work_to_be_done", "property", "submitting_supervisor", "date", "priority", "work_order_status"]
             col_widths = [max(len(str(getattr(work_order, attr))) for work_order in filtered_work_orders) for attr in
                          ["work_order_id", "work_to_be_done", "property", "submitting_supervisor", "date", "priority", "work_order_status"]]
             col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
             row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
             print(row_format.format(*headers))
             print("-" * (columns - 2))
             for work_order in filtered_work_orders:
                print(row_format.format(work_order.work_order_id, work_order.work_to_be_done, work_order.property, work_order.submitting_supervisor, work_order.date, 
                                        work_order.priority, work_order.work_order_status))
        input("\nPress Enter to return to the menu.")

    def search_maintenance_reports_by_employee(self, employee_ssn):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " List All Maintenance Reports By Employee SSN".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        filtered_maintenance_reports = self.logic_wrapper.search_maintenance_reports_by_employee(employee_ssn)
        if not filtered_maintenance_reports:
            print("No maintenance reports for this employee")
        else:
             headers = ["maintenance_report_id", "connected_work_order_id", "property", "work_done", "upkeep_status", "employee", "total_costs", "marked_as_finished", "report_closed", "contractors_used"]
             col_widths = [max(len(str(getattr(work_order, attr))) for work_order in filtered_maintenance_reports) for attr in
                          ["maintenance_report_id", "connected_work_order_id", "property", "work_done", "upkeep_status", "employee", "total_costs", "marked_as_finished", "report_closed", "contractors_used"]]
             col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
             row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
             print(row_format.format(*headers))
             print("-" * (columns - 2))
             for maintenance_report in filtered_maintenance_reports:
                print(row_format.format(maintenance_report.maintenance_report_id, maintenance_report.connected_work_order_id, maintenance_report.property, 
                                        maintenance_report.work_done, maintenance_report.upkeep_status, maintenance_report.employee, maintenance_report.total_costs, 
                                        maintenance_report.marked_as_finished, maintenance_report.report_closed, maintenance_report.contractors_used))
        input("\nPress Enter to return to the menu.")