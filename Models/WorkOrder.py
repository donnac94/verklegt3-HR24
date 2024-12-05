from datetime import datetime

class WorkOrder:
    """
    Model that contains information about the Work Order.
    """
    def __init__(
            self,
            work_order_id: int="",
            work_to_be_done: str="",
            property: str="",
            submitting_supervisor: str="",
            date: datetime="",
            priority: str="",
            work_order_status: str=""
    ) -> None:
        """
        :param int work_order_id: The unique id of the work order.
        :param str work_to_be_done: Work that needs to be done
        :param str property: The property of the work order.
        :param str submitting_supervisor: The supervisor submitting the work order
        :param str date: The datetime of the work order
        :param str priority: The priority order of the work to be done
        :param work_order_status: The status on the work order
        """
        self.work_order_id = work_order_id
        self.work_to_be_done = work_to_be_done
        self.property = property
        self.submitting_supervisor = submitting_supervisor
        self.date = date
        self.priority = priority
        self.work_order_status = work_order_status

    def __str__(self):
        return (
            f"Work order ID: {self.work_order_id}\n"
            f"Work to be done: {self.work_to_be_done}\n"
            f"Property: {self.property}\n"
            f"Submitting supervisor: {self.submitting_supervisor}\n"
            f"Date: {self.date}\n"
            f"Priority: {self.priority}\n"
            f"Work order Status: {self.work_order_status}\n"
        )