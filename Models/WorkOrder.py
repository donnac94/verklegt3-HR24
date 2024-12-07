from datetime import datetime

class WorkOrder:
    """
    Model that contains information about the Work Order.
    """
    def __init__(
            self,
            work_order_id: int,
            work_to_be_done: str,
            property: str,
            submitting_supervisor: str,
            date: datetime,
            priority: str,
            work_order_status: str
    ) -> None:
        """
        :param int work_order_id: The unique id of the work order.
        :param str work_to_be_done: Work that needs to be done.
        :param str property: The property of the work order.
        :param str submitting_supervisor: The supervisor submitting the work order.
        :param str date: The time when work order was made.
        :param str priority: The priority order of the work to be done.
        :param work_order_status: The status on the work order.
        """
        self.work_order_id = work_order_id
        self.work_to_be_done = work_to_be_done
        self.property = property
        self.submitting_supervisor = submitting_supervisor
        self.date = date
        self.priority = priority
        self.work_order_status = work_order_status

    def to_dict(self) -> dict:
        return {
            "work_order_id": self.work_order_id,
            "work_to_be_done": self.work_to_be_done,
            "property": self.property,
            "submitting_supervisor": self.submitting_supervisor,
            "date": self.date,
            "priority": self.priority,
            "work_order_status": self.work_order_status
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            work_order_id=data["work_order_id"],
            work_to_be_done=data["work_to_be_done"],
            property=data["property"],
            submitting_supervisor=data["submitting_supervisor"],
            date=data["date"],
            priority=data["priority"],
            work_order_status=data["work_order_status"]
        )