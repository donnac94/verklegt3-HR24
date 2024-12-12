from Logic_layer.LogicWrapper import LogicWrapper
import os
import shutil

from UI_Layer.Validation import validate_boolean, validate_contractors_used, validate_employee, validate_property, validate_total_costs, validate_upkeep_status, validate_work_done

#TODO: Error handling, input validation

class MaintenanceReportUI:
    def __init__(self, logic_wrapper: LogicWrapper):
        self.logic_wrapper = logic_wrapper

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
            print(c + " Maintenance Report Portal ".center(columns - 2, h) + c)
            print(d + " Welcome to the Maintenance Menu ".center(columns - 2) + d)
            print(c + h * (columns - 2) + c)
            print(d + " 1. List All Maintenance Reports".ljust(columns - 2) + d)
            print(d + " 2. Submit New Maintenance Report  ".ljust(columns - 2) + d)
            print(d + " 3. Update Maintenance Report Information ".ljust(columns - 2) + d)
            print(d + " 4. Mark Report as Finished ".ljust(columns - 2) + d)
            print(d + " 5. Close Maintenance Report ".ljust(columns - 2) + d)
            print(d + " 6. Reopen Maintenance Report ".ljust(columns - 2) + d)
            print(d + " b. Back to Login Menu ".ljust(columns - 2) + d)
            print(c + h * (columns - 2) + c)

            choice = input("\nChoose an option: ").strip().lower()

            if choice == "1":
                self.list_all_reports()
            elif choice == "2":
                self.submit_maintenance_report()
            elif choice == "3":
                self.update_report_info()
            elif choice == "4":
                self.mark_report_finished()
            elif choice == "5":
                self.close_report()
            elif choice == "6":
                self.reopen_report()
            elif choice == "b":
                return
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to return to the menu.")
                
    def list_all_reports(self):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " List All Maintenance Reports ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        reports = self.logic_wrapper.get_all_maintenance_reports()
        if not reports:
            print("No maintenance reports found.")
        else:
            headers = ["Report ID", "connected_work_order_id", "Property", "Work Done", "Upkeep Status", "Employee", "Total Costs", "Marked as Finished", "Report Closed", "Contractors Used"]
            col_widths = [max(len(str(getattr(report, attr))) for report in reports) for attr in ["maintenance_report_id", "connected_work_order_id", "property", "work_done", "upkeep_status", "employee", "total_costs", "marked_as_finished", "report_closed", "contractors_used"]]
            col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
            row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
            print(row_format.format(*headers))
            print("-" * (columns - 2))
            for report in reports:
                print(row_format.format(
                    report.maintenance_report_id, report.connected_work_order_id, report.property, report.work_done, report.upkeep_status,
                    report.employee, report.total_costs, report.marked_as_finished, report.report_closed, ", ".join(report.contractors_used)
                ))
        input("\nPress Enter to return to the menu.")

    def submit_maintenance_report(self):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " Submit Maintenance Report ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        print("Enter 'b' at any prompt to cancel and go back to the previous menu.\n")
        
        report_id = self.automatic_report_id()
        report_details = {
            "maintenance_report_id": report_id
        }

        while True:
            property = input("Enter Property: ").strip()
            if property == 'b':
                return
            if validate_property(property):
                report_details["property"] = property
                break
            else:
                print("Invalid property. Please try again.")

        while True:
            connected_work_order_id = input("Enter the ID of the work order this report is about.").strip()
            if connected_work_order_id == 'b':
                return
            else:
                report_details["connected_work_order_id"] = connected_work_order_id
                break

        while True:
            work_done = input("Enter Work Done: ").strip()
            if work_done == 'b':
                return
            if validate_work_done(work_done):
                report_details["work_done"] = work_done
                break
            else:
                print("This field is required, please what work was done.")

        while True:
            upkeep_status = input("Enter Upkeep Status (Regular Maintenance / Emergency Repair): ").strip()
            if upkeep_status == 'b':
                return
            if validate_upkeep_status(upkeep_status):
                report_details["upkeep_status"] = upkeep_status
                break
            else:
                print("Invalid upkeep status. Please try again.")

        while True:
            employee = input("Enter Employee: ").strip()
            if employee == 'b':
                return
            if validate_employee(employee):
                report_details["employee"] = employee
                break
            else:
                print("Invalid employee. Please try again.")

        while True:
            total_costs = input("Enter Total Costs: ").strip()
            if total_costs == 'b':
                return
            if validate_total_costs(total_costs):
                report_details["total_costs"] = int(total_costs)
                break
            else:
                print("Invalid total costs. Please enter a valid integer.")

        # Input for 'marked_as_finished'
        while True:
            marked_as_finished_input = input("Enter Marked as Finished (True/False): ").strip().lower()
            if marked_as_finished_input == 'b':
                return
            if marked_as_finished_input in ['true', 'false']:
                report_details["marked_as_finished"] = marked_as_finished_input == 'true'
                break
            else:
                print("Invalid input. Please enter 'True' or 'False'.")
                input("\nPress Enter to try again.")

        # Input for 'report_closed'
        while True:
            report_closed_input = input("Enter Report Closed (True/False): ").strip().lower()
            if report_closed_input == 'b':
                return
            if report_closed_input in ['true', 'false']:
                report_details["report_closed"] = report_closed_input == 'true'
                break
            else:
                print("Invalid input. Please enter 'True' or 'False'.")
                input("\nPress Enter to try again.")


        while True:
            contractors_used = input("Enter Contractors Used (comma-separated): ").strip()
            if contractors_used == 'b':
                return
            if validate_contractors_used(contractors_used):
                report_details["contractors_used"] = set(contractors_used.split(','))
                break
            else:
                print("Invalid contractors used. Please enter a comma-separated list.")

        result = self.logic_wrapper.submit_maintenance_report(report_details)
        print(result)
        print("\nMaintenance report submitted successfully.")
        self.list_all_reports()

    def update_report_info(self):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " Update Maintenance Report Information ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        print("Enter 'b' at any prompt to cancel and go back to the previous menu.\n")

        # List all maintenance reports
        reports = self.logic_wrapper.get_all_maintenance_reports()
        if not reports:
            print("No maintenance reports found.")
            input("\nPress Enter to return to the menu.")
            return

        headers = ["Report ID", "connected_work_order_id", "Property", "Work Done", "Upkeep Status", "Employee", "Total Costs", "Marked as Finished", "Report Closed", "Contractors Used"]
        col_widths = [len(header) for header in headers]
        for report in reports:
            col_widths = [max(len(str(getattr(report, attr))), width) for attr, width in zip(
                ["maintenance_report_id", "connected_work_order_id", "property", "work_done", "upkeep_status", "employee", "total_costs", "marked_as_finished", "report_closed", "contractors_used"], col_widths)]
        row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
        print(row_format.format(*headers))
        print("-" * sum(col_widths))
        for report in reports:
            print(row_format.format(
                report.maintenance_report_id, report.connected_work_order_id, report.property, report.work_done, report.upkeep_status,
                report.employee, report.total_costs, report.marked_as_finished, report.report_closed, ", ".join(report.contractors_used)
            ))

        while True:
            report_id = input("\nEnter the Report ID of the maintenance report you want to update: ").strip()
            if report_id == 'b':
                return
            if report_id.isdigit() and any(report.maintenance_report_id == int(report_id) for report in reports):
                report_id = int(report_id)
                break
            else:
                print("Invalid Report ID. Please try again.")

        report_details = {}
        while True:
            field = input("Enter the field you want to update (connected_work_order_id, property, work_done, upkeep_status, employee, total_costs, marked_as_finished, report_closed, contractors_used): ").strip()
            if field == 'b':
                return
            if field in ["connected_work_order_id", "property", "work_done", "upkeep_status", "employee", "total_costs", "marked_as_finished", "report_closed", "contractors_used"]:
                value = input(f"Enter the new value for {field}: ").strip()
                if value == 'b':
                    return
                if field == "connected_work_order_id":
                    report_details[field] = value
                    break
                elif field == "property" and validate_property(value):
                    report_details[field] = value
                    break
                elif field == "work_done" and validate_work_done(value):
                    report_details[field] = value
                    break
                elif field == "upkeep_status" and validate_upkeep_status(value):
                    report_details[field] = value
                    break
                elif field == "employee" and validate_employee(value):
                    report_details[field] = value
                    break
                elif field == "total_costs" and validate_total_costs(value):
                    report_details[field] = int(value)
                    break
                elif field == "marked_as_finished" and validate_boolean(value):
                    report_details[field] = value.lower() == 'true'
                    break
                elif field == "report_closed" and validate_boolean(value):
                    report_details[field] = value.lower() == 'true'
                    break
                elif field == "contractors_used" and validate_contractors_used(value):
                    report_details[field] = set(value.split(','))
                    break
                else:
                    print(f"Invalid value for {field}. Please try again.")
            else:
                print("Invalid field. Please try again.")

        result = self.logic_wrapper.change_maintenance_report_info(report_id, field, report_details[field])
        print(result)
        print("\nMaintenance report updated successfully.")
        input("\nPress Enter to return to the menu.")

    def mark_report_finished(self):
        self.clear_terminal()
        print("Mark Maintenance Report as Finished")
        report_id = input("Enter Report ID: ").strip()
        result = self.logic_wrapper.mark_report_as_finished(report_id)
        print(result)
        input("\nPress Enter to return to the menu.")

    def close_report(self):
        self.clear_terminal()
        print("Close Maintenance Report")
        report_id = input("Enter Report ID: ").strip()
        result = self.logic_wrapper.close_maintenance_report(report_id)
        print(result)
        input("\nPress Enter to return to the menu.")

    def reopen_report(self):
        self.clear_terminal()
        print("Reopen Maintenance Report")
        report_id = input("Enter Report ID: ").strip()
        result = self.logic_wrapper.reopen_maintenance_report(report_id)
        print(result)
        input("\nPress Enter to return to the menu.")
    
    def automatic_report_id(self):
        """
        Gets the latest maintenance report ID and increments it by 1.
        """
        reports = self.logic_wrapper.get_all_maintenance_reports()
        if not reports:
            return 1
        latest_report = reports[-1]
        latest_id = int(latest_report.maintenance_report_id)
        return latest_id + 1
