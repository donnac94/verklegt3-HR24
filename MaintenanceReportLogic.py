from Data_Layer.DataWrapper import DataWrapper
from Models.maintenance_report import MaintenanceReport

class MaintenanceReportLogic:
    def __init__(self):
        self.data_wrapper = DataWrapper()

    def submit_maintenance_report(self, report_details: dict) -> str:
        """
        Submits a new maintenance report.
        """
        new_report = MaintenanceReport(
            report_id=report_details["report_id"],
            title=report_details["title"],
            description=report_details["description"],
            reported_by=report_details["reported_by"],
            assigned_to=report_details["assigned_to"],
            status="Open",
            priority=report_details["priority"],
            date_created=report_details["date_created"]
        )
        self.data_wrapper.add_maintenance_report(new_report)
        return "Maintenance report submitted successfully."

    def change_maintenance_report_info(self, report_id: str, field: str, new_value: str) -> str:
        """
        Changes a specific field in a maintenance report.
        """
        self.data_wrapper.update_maintenance_report(report_id, field, new_value)
        return "Maintenance report information updated successfully."

    def mark_report_finished(self, report_id: str) -> str:
        """
        Marks a maintenance report as finished.
        """
        self.data_wrapper.update_maintenance_report(report_id, "status", "Finished")
        return "Maintenance report marked as finished."

    def close_report(self, report_id: str) -> str:
        """
        Closes a maintenance report.
        """
        self.data_wrapper.update_maintenance_report(report_id, "status", "Closed")
        return "Maintenance report closed successfully."

    def reopen_maintenance_report(self, report_id: str) -> str:
        """
        Reopens a previously closed or finished maintenance report.
        """
        self.data_wrapper.update_maintenance_report(report_id, "status", "Open")
        return "Maintenance report reopened successfully."
