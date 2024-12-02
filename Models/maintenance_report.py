class MaintenanceReport():
    """
    Model that contains information from a single maintenance report.
    """

    def __init__(
            self,
            maintenance_report_id: int,
            property: str,
            work_done: str,
            upkeep_status: str,
            employee: str,
            total_costs: int,
            marked_as_finished: bool,
            report_closed: bool,
            contractors_used: set[str] = []
    ) -> None:
        """
        :param int maintenance_report_id: The unique id for the maintenance report.
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
        self.property = property
        self.work_done  = work_done
        self.upkeep_status  = upkeep_status
        self.employee = employee
        self.total_costs = total_costs
        self.marked_as_finished = marked_as_finished
        self.report_closed = report_closed
        self.contractors_used = contractors_used