class WorkOrder:
    """
    Model that contains information about the Work Order.
    """

    def __init__(
        self,
        work_order_id: str,
        property: str,
        work_done: str,
        upkeep_status: str,
        employee: str,
        total_price: int,
        marked_as_finished: bool,
        report_status: int,
        contractors_used: str,
    ) -> None:
        """
        :param str work_order_id: The unique id of the work order.
        :param str property: The property of the work order.
        :param str work_done: The work done in the work order.
        :param str upkeep_status: The status of the work order.
        :param str employee: The full name of the employee of the work order.
        :param int total_price: The total price of the work order.
        :param bool marked_as_finished: Whether the work order is finished.
        :param int report_status: The report status of the work order.
        :param str contractors_used: Contractors used in the work order.
        """
        self.work_order_id = work_order_id
        self.property = property
        self.work_done = work_done
        self.upkeep_status = upkeep_status
        self.employee = employee
        self.total_price = total_price
        self.marked_as_finished = marked_as_finished
        self.report_status = report_status
        self.contractors_used = contractors_used
