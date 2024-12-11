class WorkOrder:
    def __init__(self, work_order_id, work_to_be_done, property, submitting_supervisor, date, priority, work_order_status):
        self.work_order_id = work_order_id
        self.work_to_be_done = work_to_be_done
        self.property = property
        self.submitting_supervisor = submitting_supervisor
        self.date = date
        self.priority = priority
        self.work_order_status = work_order_status

    def to_dict(self):
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
    def from_dict(cls, dict_obj):
        return cls(
            dict_obj["work_order_id"],
            dict_obj["work_to_be_done"],
            dict_obj["property"],
            dict_obj["submitting_supervisor"],
            dict_obj["date"],
            dict_obj["priority"],
            dict_obj["work_order_status"]
        )