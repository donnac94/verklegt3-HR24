import csv
from Models.maintenance_report import MaintenanceReport

class MaintainanceReportData:
    def __init__(self):
        self.file_name = "Files/maintainancereport.csv"
        
    def submit_maintenance_report(self, maintenance_report: MaintenanceReport) -> None:
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["maintainance_report_id", "property", "work_done", "upkeep_status", "employee", "total_price", "report_status", "contractors_used"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:  
                writer.writeheader()

            writer.writerow({
                "maintainance_report_id": maintenance_report.maintainance_report_id,
                "property": maintenance_report.property,
                "work_done": maintenance_report.work_done,
                "upkeep_status": maintenance_report.upkeep_status,
                "employee": maintenance_report.employee,
                "total_price": maintenance_report.total_price,
                "report_status": maintenance_report.report_status,
                "contractors_used": maintenance_report.contractors_used
            })

    def get_all_maintenance_reports(self) -> list[MaintenanceReport]:
        reports = []
        try:
            with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    reports.append(
                        MaintenanceReport(
                            row["maintainance_report_id"],
                            row["property"],
                            row["work_done"],
                            row["upkeep_status"],
                            row["employee"],
                            row["total_price"],
                            row["report_status"],
                            row["contractors_used"]
                        )
                    )
        except FileNotFoundError:
            return []
        return reports

    def change_maintenance_report_info(self, maintainance_report_id: str, field: str, new_value: str) -> None:
        reports = self.get_all_maintenance_reports()
        report_found = False

        for report in reports:
            if report.maintainance_report_id == maintainance_report_id:
                if not hasattr(report, field):
                    raise AttributeError(f"Invalid field: {field}")
                setattr(report, field, new_value)
                report_found = True
                break

        if not report_found:
            raise ValueError(f"Maintenance report with ID {maintainance_report_id} not found.")

        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["maintainance_report_id", "property", "work_done", "upkeep_status", "employee", "total_price", "report_status", "contractors_used"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for report in reports:
                writer.writerow({
                    "maintainance_report_id": report.maintainance_report_id,
                    "property": report.property,
                    "work_done": report.work_done,
                    "upkeep_status": report.upkeep_status,
                    "employee": report.employee,
                    "total_price": report.total_price,
                    "report_status": report.report_status,
                    "contractors_used": report.contractors_used
                })

    def mark_report_as_finished(self, maintainance_report_id: str) -> None:
        self.change_maintenance_report_info(maintainance_report_id, "report_status", "Finished")

    def change_report_status(self, maintainance_report_id: str, new_status: str) -> None:
        self.change_maintenance_report_info(maintainance_report_id, "report_status", new_status)
