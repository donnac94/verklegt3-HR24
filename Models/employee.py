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
        is_manager: bool
    ) -> None:
        self.ssn = ssn
        self.full_name = full_name
        self.address = address
        self.phone = phone
        self.gsm = gsm
        self.email = email
        self.location = location
        self.is_manager = is_manager

    def to_dict(self) -> dict:
        return {
            "ssn": self.ssn,
            "full_name": self.full_name,
            "address": self.address,
            "phone": self.phone,
            "gsm": self.gsm,
            "email": self.email,
            "location": self.location,
            "is_manager": self.is_manager
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
            is_manager=data["is_manager"].lower() == 'true' if isinstance(data["is_manager"], str) else bool(data["is_manager"])
        )