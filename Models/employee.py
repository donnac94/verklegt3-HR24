class employee():
    """ Model that contains information about employees """
    def __init__(
            self, 
            name: str, 
            ssn: int, 
            address: str, 
            gsm: str, 
            homephone: str, 
            email: str, 
            work_location: str, 
            is_manager: bool
    ) -> None:
        """
        :param str name: name of employee.
        :param int ssn: social security number for employee.
        :param str address: address of living for employee.
        :param str gsm: employee's private phone number.
        :param str homephone: the employee's homephone number.
        :param str email: email address for employee.
        :param str work_location: where employee works.
        :param bool is_manager: to check if employee is a manager.
        """
        self.name = name
        self.ssn = ssn
        self.address = address
        self.gsm = gsm
        self.homephone = homephone
        self.email = email
        self.work_location = work_location
        self.is_manager = is_manager