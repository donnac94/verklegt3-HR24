from datetime import datetime
class WorkOrder:
    def __init__(
            self, 
            work_order_id: int, 
            work_to_be_done: str, 
            property: str, 
            submitting_supervisor: str, 
            date: datetime, 
            priority: str, 
            work_order_status: str,
            marked_as_finished: bool
            ) -> None:
        """
        :param int work_order_id: The unique id for the work order.
        :param str work_to_be_done: Description of what work should be done.
        :param str property: What property is to be worked on.
        :param str submitting_supervisor: The supervisor that made the work order.
        :param dateime date: The time when the work order was made.
        :param str priority: The priority of the work order (High, medium, low).
        :param str work_order_status: The status of the work order (Closed or open).
        :param bool marked_as_finished: States whether the work order is marked as finished or not (True or False).
        """
        self.work_order_id = work_order_id
        self.work_to_be_done = work_to_be_done
        self.property = property
        self.submitting_supervisor = submitting_supervisor
        self.date = date
        self.priority = priority
        self.work_order_status = work_order_status
        self.marked_as_finished = marked_as_finished

    def to_dict(self):
        return {
            "work_order_id": self.work_order_id,
            "work_to_be_done": self.work_to_be_done,
            "property": self.property,
            "submitting_supervisor": self.submitting_supervisor,
            "date": self.date,
            "priority": self.priority,
            "work_order_status": self.work_order_status,
            "marked_as_finished": self.marked_as_finished
        }

    @classmethod
    def from_dict(cls, dict_obj):
        return cls(
            dict_obj["work_order_id"],
            dict_obj["work_to_be_done"],
            dict_obj["property"],
            dict_obj["submitting_supervisor"],
            dict_obj["date"],
            dict_obj["priority"],
            dict_obj["work_order_status"],
            dict_obj["marked_as_finished"]
        )