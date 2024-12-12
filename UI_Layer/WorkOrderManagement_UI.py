from Logic_layer.LogicWrapper import LogicWrapper
import os
import shutil
import sys

class WorkOrderUI:
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
            print(c + " Air NaN Work Order Portal ".center(columns - 2, h) + c)
            print(d + " Welcome to the Work Order Management Menu ".center(columns - 2) + d)
            print(c + h * (columns - 2) + c)
            print(d + " 1. List All Work Orders ".ljust(columns - 2) + d)
            print(d + " 2. Submit New Work Order ".ljust(columns - 2) + d)
            print(d + " 3. Update Work Order Information ".ljust(columns - 2) + d)
            print(d + " 4. Close Work Order ".ljust(columns - 2) + d)
            print(d + " 5. Reopen Work Order ".ljust(columns - 2) + d)
            print(d + " b. Go Back ".ljust(columns - 2) + d)
            print(c + h * (columns - 2) + c)

            choice = input("Enter your choice: ").strip().lower()
            if choice == "1":
                self.list_all_work_orders()
            elif choice == "2":
                self.submit_work_order()
            elif choice == "3":
                self.update_work_order_info()
            elif choice == "4":
                self.close_work_order()
            elif choice == "5":
                self.reopen_work_order()
            elif choice == "b":
                return
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to return to the menu.")

    def list_all_work_orders(self):
        self.clear_terminal()
        print("List All Work Orders")
        print("Press 'b' to go back to the Work Order Management Menu.")
        work_orders = self.logic_wrapper.get_all_work_orders()
        if not work_orders:
            print("No work orders found.")
        else:
            self.display_work_orders(work_orders)
        
        while True:
            choice = input("\nEnter 'b' to go back: ").strip().lower()
            if choice == 'b':
                return
            else:
                print("Invalid choice. Please try again.")

    def submit_work_order(self):
        self.clear_terminal()
        print("Submit New Work Order")
        print("Press 'b' to go back to the Work Order Management Menu.")

        work_order_id = self.logic_wrapper.automatic_work_order_id()
        work_order_details = {
            "work_order_id": work_order_id
        }

        work_to_be_done = input("Enter Work to be Done: ").strip()
        if work_to_be_done.lower() == 'b':
            return
        work_order_details["work_to_be_done"] = work_to_be_done

        property = input("Enter Property: ").strip()
        if property.lower() == 'b':
            return
        work_order_details["property"] = property

        submitting_supervisor = input("Enter SSN of submitting supervisor: ").strip()
        if submitting_supervisor.lower() == 'b':
            return
        work_order_details["submitting_supervisor"] = submitting_supervisor

        date = input("Enter Date (YYYY-MM-DD HH:MM:SS): ").strip()
        if date.lower() == 'b':
            return
        work_order_details["date"] = date

        priority = input("Priority (High/Medium/Low): ").strip()
        if priority.lower() == 'b':
            return
        work_order_details["priority"] = priority

        work_order_details["work_order_status"] = "Open"

        result = self.logic_wrapper.create_work_order(work_order_details)
        print(result)
        input("\nPress Enter to return to the menu.")

    def update_work_order_info(self):
        self.clear_terminal()
        columns, _ = self.get_terminal_size()
        print("+".ljust(columns - 1, '-') + "+")
        print("|" + " Update Work Order Information ".center(columns - 2) + "|")
        print("+".ljust(columns - 1, '-') + "+")
        print("Enter 'b' at any prompt to cancel and go back to the previous menu.\n")
        work_orders = self.logic_wrapper.get_all_work_orders()
        if not work_orders:
            print("No work orders found.")
            input("\nPress Enter to return to the menu.")
            return

        headers = ["Work Order ID", "Work to be Done", "Property", "Supervisor", "Date", "Priority", "Status"]
        col_widths = [max(len(str(getattr(order, attr))) for order in work_orders) for attr in ["work_order_id", "work_to_be_done", "property", "submitting_supervisor", "date", "priority", "work_order_status"]]
        col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
        row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
        print(row_format.format(*headers))
        print("-" * (columns - 2))
        for order in work_orders:
            print(row_format.format(order.work_order_id, order.work_to_be_done, order.property, order.submitting_supervisor, order.date, order.priority, order.work_order_status))

        work_order_id = input("\nEnter the Work Order ID to update: ").strip()
        if work_order_id.lower() == 'b':
            return

        work_order = self.logic_wrapper.get_work_order_by_id(work_order_id)
        if not work_order:
            print("Work Order not found.")
            input("\nPress Enter to return to the menu.")
            return

        work_to_be_done = input(f"Enter Work to be Done [{work_order.work_to_be_done}]: ").strip()
        if work_to_be_done.lower() == 'b':
            return
        if work_to_be_done:
            self.logic_wrapper.change_work_order_info(work_order_id, "work_to_be_done", work_to_be_done)

        property = input(f"Enter Property [{work_order.property}]: ").strip()
        if property.lower() == 'b':
            return
        if property:
            self.logic_wrapper.change_work_order_info(work_order_id, "property", property)

        submitting_supervisor = input(f"Enter SSN of Submitting Supervisor [{work_order.submitting_supervisor}]: ").strip()
        if submitting_supervisor.lower() == 'b':
            return
        if submitting_supervisor:
            self.logic_wrapper.change_work_order_info(work_order_id, "submitting_supervisor", submitting_supervisor)

        date = input(f"Enter Date (YYYY-MM-DD HH:MM:SS) [{work_order.date}]: ").strip()
        if date.lower() == 'b':
            return
        if date:
            self.logic_wrapper.change_work_order_info(work_order_id, "date", date)

        priority = input(f"Enter Priority [{work_order.priority}]: ").strip()
        if priority.lower() == 'b':
            return
        if priority:
            self.logic_wrapper.change_work_order_info(work_order_id, "priority", priority)

        status = input(f"Enter Status [{work_order.work_order_status}]: ").strip()
        if status.lower() == 'b':
            return
        if status:
            self.logic_wrapper.change_work_order_info(work_order_id, "work_order_status", status)

        print("Work order updated successfully.")
        input("\nPress Enter to return to the menu.")

    def close_work_order(self):
        self.clear_terminal()
        print("Close Work Order")
        print("Press 'b' to go back to the Work Order Management Menu.")
        work_orders = self.logic_wrapper.get_all_work_orders()
        if not work_orders:
            print("No work orders found.")
            input("\nPress Enter to return to the menu.")
            return
        else:
            self.display_work_orders(work_orders)
            work_order_id = input("Enter the Work Order ID to close: ").strip()
            if work_order_id.lower() == 'b':
                return
            result = self.logic_wrapper.close_work_order(work_order_id)
            print(result)
        
        while True:
            choice = input("\nEnter 'b' to go back: ").strip().lower()
            if choice == 'b':
                return
            else:
                print("Invalid choice. Please try again.")

    def reopen_work_order(self):
        self.clear_terminal()
        print("Reopen Work Order")
        print("Press 'b' to go back to the Work Order Management Menu.")
        work_orders = self.logic_wrapper.get_all_work_orders()
        if not work_orders:
            print("No work orders found.")
            input("\nPress Enter to return to the menu.")
            return
        else:
            self.display_work_orders(work_orders)
            work_order_id = input("Enter the Work Order ID to reopen: ").strip()
            if work_order_id.lower() == 'b':
                return
            result = self.logic_wrapper.reopen_work_order(work_order_id)
            print(result)
        while True:
            choice = input("\nEnter 'b' to go back: ").strip().lower()
            if choice == 'b':
                return
            else:
                print("Invalid choice. Please try again.")

    def display_work_orders(self, work_orders):
        headers = ["Work Order ID", "Work to be Done", "Property", "Submitting Supervisor", "Date", "Priority", "Status"]
        col_widths = [len(header) for header in headers]
        for work_order in work_orders:
            col_widths = [max(len(str(getattr(work_order, attr))), width) for attr, width in zip(
                ["work_order_id", "work_to_be_done", "property", "submitting_supervisor", "date", "priority", "work_order_status"], col_widths)]
        row_format = "  |  ".join([f"{{:<{width}}}" for width in col_widths])
        print(row_format.format(*headers))
        print("-" * sum(col_widths))
        for work_order in work_orders:
            print(row_format.format(
                work_order.work_order_id,
                work_order.work_to_be_done,
                work_order.property,
                work_order.submitting_supervisor,
                work_order.date,
                work_order.priority,
                work_order.work_order_status
            ))