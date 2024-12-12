class MaintenanceReport():
    """
    Model that contains information from a single maintenance report.
    """

    def __init__(
            self,
            maintenance_report_id: int,
            connected_work_order_id: int,
            property: str,
            work_done: str,
            upkeep_status: str,
            employee: str,
            total_costs: int,
            marked_as_finished: bool,
            report_closed: bool,
            contractors_used: list
    ) -> None:
        """
        :param int maintenance_report_id: The unique id for the maintenance report.
        :param int connected_work_order_id: The id for the work order that the maintenance report is about.
        :param str property: The property which the maintenance report is about.
        :param str work_done: Description of what work was done.
        :param str upkeep_status: States whether upkeep was regular maintenance or emergency repair.
        :param str employee: The employee who wrote the report.
        :param int total_costs: The total costs for the maintenance.
        :param bool marked_as_finished: States whether the report marked as finished or not.
        :param bool report_closed: States whether the report is closed or open (True if closed, False if open).
        :param set[str] contractors_used: A set of contractors used, if any.
        """

        self.maintenance_report_id = maintenance_report_id
        self.connected_work_order_id = connected_work_order_id
        self.property = property
        self.work_done  = work_done
        self.upkeep_status  = upkeep_status
        self.employee = employee
        self.total_costs = total_costs
        self.marked_as_finished = marked_as_finished
        self.report_closed = report_closed
        self.contractors_used = contractors_used

    def to_dict(self):
        return {
            "maintenance_report_id": self.maintenance_report_id,
            "connected_work_order_id": self.connected_work_order_id,
            "property": self.property,
            "work_done": self.work_done,
            "upkeep_status": self.upkeep_status,
            "employee": self.employee,
            "total_costs": self.total_costs,
            "marked_as_finished": self.marked_as_finished,
            "report_closed": self.report_closed,
            "contractors_used": self.contractors_used
        }

    @classmethod
    def from_dict(cls, dict_obj):
        return cls(
            dict_obj["maintenance_report_id"],
            dict_obj["connected_work_order_id"],
            dict_obj["property"],
            dict_obj["work_done"],
            dict_obj["upkeep_status"],
            dict_obj["employee"],
            dict_obj["total_costs"],
            dict_obj["marked_as_finished"],
            dict_obj["report_closed"],
            dict_obj["contractors_used"]
        )