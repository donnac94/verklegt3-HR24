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
            workLocation: str, 
            isManager: bool
    ) -> None:
        """
        :param str name: name of employee
        :param int ssn: social security number for employee
        :param str address: address of living for employee
        :param str gsm: employee's private phone number
        :param str homephone: the employee's homephone number
        :param str email: email address for employee
        :param str workLocation: where employee works
        :param bool isManager: to check if employee is a manager
        """
        self.name = name
        self.ssn = ssn
        self.address = address
        self.gsm = gsm
        self.homephone = homephone
        self.email = email
        self.workLocation = workLocation
        self.isManager = isManager