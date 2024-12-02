class WorkOrder:
    """
    Model that contains information about the Work Order.
    """

    def __init__(
        self,
        work_order_id: str,
        work_to_be_done: str,
        property: str
        submitting_manager : str,
        date : datetime
        priority : str
        work_order_status : str
    ) -> None:
        """
        :param str work_order_id: The unique id of the work order.
        :param str work_to_be_done: Work that needs to be done
        :param str property: The property of the work order.
        :param str submitting_manager: The manager submitting the work order
        :param str date: The datetime of the work order
        :para, str priority: The priority order of the work to be done
        :param work_order_status: The status on the work order
        """
        self.work_order_id = work_order_id
        self.work_to_be_done = work_to_be_done
        self.property = property
        self.submitting_manager = submitting_manager
        self.date = date
        self.priority = priority
        self.work_order_status = work_order_status
