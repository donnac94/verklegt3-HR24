from Data_Layer.DataWrapper import DataWrapper
from Models.maintenance_report import MaintenanceReport

class MaintenanceReportLogic:
    def __init__(self):
        self.data_wrapper = DataWrapper()

    def submit_maintenance_report(self, report_details: dict) -> str:
        """
        Creates a maintenance report object with specified details and forwards it to the data layer.
        :param dict report_details: The details of the maintenance report.
        """

        new_report = MaintenanceReport(
            maintenance_report_id=report_details["maintenance_report_id"],
            connected_work_order_id=report_details["connected_work_order_id"],
            property=report_details["property"],
            work_done=report_details["work_done"],
            upkeep_status=report_details["upkeep_status"],
            employee=report_details["employee"],
            total_costs=report_details["total_costs"],
            marked_as_finished=report_details["marked_as_finished"],
            report_closed=report_details["report_closed"],
            contractors_used=report_details["contractors_used"]
        )
        self.data_wrapper.submit_maintenance_report(new_report)
        return "Maintenance report submitted successfully."
    
    def get_all_maintenance_reports(self) -> list[MaintenanceReport]:
        """
        Retrieve all maintenance reports from the CSV file.
        :return: A list of maintenance reports.
        """
        return self.data_wrapper.get_all_maintenance_reports()

    def change_maintenance_report_info(self, maintenance_report_id: int, field: str, new_value: str) -> str:
        """
        Changes a specific field in a maintenance report.
        :param int maintenance_report_id: The ID of the maintenance report to be changed.
        :param str field: The field to be changed.
        :param str new_value: The new value that will replace the old value in specified field.
        """
        self.data_wrapper.change_maintenance_report_info(maintenance_report_id, field, new_value)
        return "Maintenance report information updated successfully."

    def mark_report_as_finished(self, maintenance_report_id: int) -> str:
        """
        Marks a maintenance report as finished.
        :param int maintenance_report_id: The ID of the maintenance report to be marked as finished.
        """
        try: 
            self.change_maintenance_report_info(maintenance_report_id, "marked_as_finished", "True")
            return "Maintenance report marked as finished."
        except ValueError:
            return False

    def close_maintenance_report(self, maintenance_report_id: int) -> str:
        """
        Closes a maintenance report.
        :param int maintenance_report_id: The ID of the maintenance report to be closed.
        """
        try:
            self.change_maintenance_report_info(maintenance_report_id, "report_closed", "True")
            maintenance_reports = self.data_wrapper.get_all_maintenance_reports()
            for maintenance_report in maintenance_reports:
                if maintenance_report.maintenance_report_id == maintenance_report_id:
                    connected_work_order_id = maintenance_report.connected_work_order_id
                    self.data_wrapper.change_work_order_info(connected_work_order_id,'work_order_status',"Closed")
            return "Maintenance report and connected work order closed successfully."
        except ValueError:
            return False

    def reopen_maintenance_report(self, maintenance_report_id: int) -> str:
        """
        Reopens a previously closed maintenance report.
        :param int maintenance_report_id: The ID of the maintenance report to be reopened.
        """
        try:
            self.change_maintenance_report_info(maintenance_report_id, "report_closed", "False")
            return "Maintenance report reopened successfully."
        except ValueError:
            return False

    def get_report_by_id(self, maintenance_report_id):
        """
        Gets specific report by their ID.
        :param maintenance_report_id: The report ID to look for.
        :return: A maintenance report and the information or raise an error if not found.
        """
        reports = self.data_wrapper.get_all_maintenance_reports()
        for report in reports:
            if report.maintenance_report_id == maintenance_report_id:
                return report
            
        return False
    
    def automatic_report_id(self):
        """
        Gets the latest maintenance report ID and increments it by 1.
        """
        reports = self.get_all_maintenance_reports()
        if not reports:
            return 1
        latest_report = reports[-1]
        latest_id = int(latest_report.maintenance_report_id)
        return latest_id + 1