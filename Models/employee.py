class Employee:
    """
    Model that contains information about employees.
    """

    def __init__(
        self,
        ssn: str,
        full_name: str,
        address: str,
        phone: str,
        gsm: str,
        email: str,
        location: str,
        is_supervisor: bool
    ) -> None:
        """
        :param str ssn: The unique SSN for this employee.
        :param str full_name: The full name of the employee.
        :param str address: The address of where the employee lives.
        :param str phone: The home phone number for the employee.
        :param str gsm: The GSM for this employee.
        :param str email: The email of this employee.
        :param str location: The location where this employee works.
        :param bool is_supervisor: Whether this employee is a supervisor or not (True or False).
        """
        self.ssn = ssn
        self.full_name = full_name
        self.address = address
        self.phone = phone
        self.gsm = gsm
        self.email = email
        self.location = location
        self.is_supervisor = is_supervisor

    def to_dict(self) -> dict:
        return {
            "ssn": self.ssn,
            "full_name": self.full_name,
            "address": self.address,
            "phone": self.phone,
            "gsm": self.gsm,
            "email": self.email,
            "location": self.location,
            "is_supervisor": self.is_supervisor
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            ssn=data["ssn"],
            full_name=data["full_name"],
            address=data["address"],
            phone=data["phone"],
            gsm=data["gsm"],
            email=data["email"],
            location=data["location"],
            is_supervisor=data["is_supervisor"].lower() == 'true' if isinstance(data["is_supervisor"], str) else bool(data["is_supervisor"])
        )