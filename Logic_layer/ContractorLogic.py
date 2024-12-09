from Models.Contractor import Contractor

class ContractorLogic:
    def CreateContractor(contractors: list[Contractor], contractor_details: dict) -> str:
        '''
        Create new contractor.
        :param contractors: List of registered contractors.
        :param contractor_details: Dictionary containing the contractors details.
        :return: Success message or Error message.
        '''
        contractor_id = contractor_details.get("contractor_id")
        if any(c.contractor_id == contractor_id for c in contractors):
            return "Contractor already exists"
        
        new_contractor = Contractor(
            contractor_id=contractor_id,
            name=contractor_details.get("name"),
            contact_name=contractor_details.get("contact_name"),
            phone_nr=contractor_details.get("phone_nr"),
            opening_time=contractor_details.get("opening_time"),
            location=contractor_details.get("location"),
            satisfaction_with_previous_work=contractor_details.get("satisfaction_with_previous_work")
        )
        contractors.append(new_contractor)
        return "Contractor registered successfully"

        

    def ListContractors(contractors: list[Contractor]) -> list:
        '''
        List all contractors.
        :param contractors: List of existing contractors.
        :return: A list of contractors.
        '''
        return contractors if contractors else []


    def ChangeContractorInfo(contractors: list[Contractor], contractor_id: int, updated_contractor: dict) -> str:
        '''
        Change contractors information.
        :param contractors: List of existing contractors.
        :param contractor_id: The ID of the contractor to update.
        :param updated_contractor: Dictionary containing the updated details for the contractor. 
        :return: Success message or Error message'''
        
        pass