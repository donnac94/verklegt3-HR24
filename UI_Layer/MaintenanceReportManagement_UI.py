from Logic_layer.LogicWrapper import LogicWrapper
import os
import shutil
import sys

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
            print(d + " 1. Submit New Maintenance Report ".ljust(columns - 2) + d)
            print(d + " 2. List All Maintenance Reports ".ljust(columns - 2) + d)
            print(d + " 3. Update Maintenance Report Information ".ljust(columns - 2) + d)
            print(d + " 4. Mark Report as Finished ".ljust(columns - 2) + d)
            print(d + " 5. Close Maintenance Report ".ljust(columns - 2) + d)
            print(d + " 6. Reopen Maintenance Report ".ljust(columns - 2) + d)
            print(d + " b. Back to Login Menu ".ljust(columns - 2) + d)
            print(d + " q. Quit ".ljust(columns - 2) + d)
            print(c + h * (columns - 2) + c)

            choice = input("\nChoose an option: ").strip().lower()

            if choice == "1":
                self.submit_maintenance_report()
            elif choice == "2":
                self.list_all_reports()
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
            elif choice == "q":
                print("Exiting Maintenance Report Menu. Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to return to the menu.")

    def submit_maintenance_report(self):
        self.clear_terminal()
        print("Submit New Maintenance Report")
        report_details = {
            "report_id": input("Enter Report ID: ").strip(),
            "title": input("Enter Title: ").strip(),
            "description": input("Enter Description: ").strip(),
            "reported_by": input("Reported By: ").strip(),
            "assigned_to": input("Assigned To: ").strip(),
            "priority": input("Priority (High/Medium/Low): ").strip(),
            "date_created": input("Date Created (YYYY-MM-DD): ").strip()
        }
        result = self.logic_wrapper.submit_maintenance_report(report_details)
        print(result)
        input("\nPress Enter to return to the menu.")

    def list_all_reports(self):
        self.clear_terminal()
        print("List All Maintenance Reports")
        reports = self.logic_wrapper.list_all_reports()
        if not reports:
            print("No maintenance reports found.")
        else:
            headers = ["Report ID", "Title", "Description", "Reported By", "Assigned To", "Status", "Priority", "Date Created"]
            col_widths = [len(header) for header in headers]
            for report in reports:
                col_widths = [max(len(str(getattr(report, attr))), width) for attr, width in zip(
                    ["report_id", "title", "description", "reported_by", "assigned_to", "status", "priority", "date_created"], col_widths)]
            row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
            print(row_format.format(*headers))
            print("-" * sum(col_widths))
            for report in reports:
                print(row_format.format(
                    report.report_id, report.title, report.description, report.reported_by,
                    report.assigned_to, report.status, report.priority, report.date_created
                ))
        input("\nPress Enter to return to the menu.")

    def update_report_info(self):
        self.clear_terminal()
        print("Update Maintenance Report Information")
        report_id = input("Enter Report ID: ").strip()
        field = input("Enter the field to update (e.g., title, description, status): ").strip()
        new_value = input("Enter the new value: ").strip()
        result = self.logic_wrapper.change_maintenance_report_info(report_id, field, new_value)
        print(result)
        input("\nPress Enter to return to the menu.")

    def mark_report_finished(self):
        self.clear_terminal()
        print("Mark Maintenance Report as Finished")
        report_id = input("Enter Report ID: ").strip()
        result = self.logic_wrapper.mark_report_finished(report_id)
        print(result)
        input("\nPress Enter to return to the menu.")

    def close_report(self):
        self.clear_terminal()
        print("Close Maintenance Report")
        report_id = input("Enter Report ID: ").strip()
        result = self.logic_wrapper.close_report(report_id)
        print(result)
        input("\nPress Enter to return to the menu.")

    def reopen_report(self):
        self.clear_terminal()
        print("Reopen Maintenance Report")
        report_id = input("Enter Report ID: ").strip()
        result = self.logic_wrapper.reopen_maintenance_report(report_id)
        print(result)
        input("\nPress Enter to return to the menu.")
