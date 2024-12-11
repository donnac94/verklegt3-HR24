import csv
from Models.maintenance_report import MaintenanceReport

class MaintenanceReportData:
    def __init__(self):
        self.file_name = "Files/maintenance_reports.csv"
        
    def submit_maintenance_report(self, maintenance_report_obj: MaintenanceReport) -> None:
        """
        Save a maintenance report in the CSV file.
        :param MaintenanceReport maintenance_report: The maintenance report to be saved.
        """
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["maintenance_report_id", "property", "work_done", "upkeep_status", "employee", "total_costs", "marked_as_finished", "report_closed", "contractors_used"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:  
                writer.writeheader()

            writer.writerow(maintenance_report_obj.to_dict())

    def get_all_maintenance_reports(self) -> list[MaintenanceReport]:
        """
        Retrieve all maintenance reports from the CSV file.
        :return: A list of maintenance reports.
        """
        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            return [MaintenanceReport.from_dict(row) for row in reader]

    def change_maintenance_report_info(self, maintenance_report_id: int, field: str, new_value: str) -> None:
        """
        Change the information of a maintenance report
        :param int maintenance_report_id: The ID of the maintenance report to be changed.
        :param str field: The field to be changed.
        :param str new_value: The new value that will replace the old value in specified field.
        """
        maintenance_reports = self.get_all_maintenance_reports()
        maintenance_report_found = False

        for maintenance_report in maintenance_reports:
            if maintenance_report.maintenance_report_id == maintenance_report_id:
                setattr(maintenance_report, field, new_value)
                maintenance_report_found = True

        if not maintenance_report_found:
            raise ValueError(f"Maintenance report with ID {maintenance_report_id} not found.")

        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["maintenance_report_id", "property", "work_done", "upkeep_status", "employee", "total_costs", "marked_as_finished", "report_closed", "contractors_used"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for maintenance_report in maintenance_reports:
                writer.writerow(maintenance_report.to_dict())

    def mark_report_as_finished(self, maintenance_report_id: str) -> None:
        self.change_maintenance_report_info(maintenance_report_id, "report_status", "Finished")

    def change_report_status(self, maintenance_report_id: str, new_status: str) -> None:
        self.change_maintenance_report_info(maintenance_report_id, "report_status", new_status)
