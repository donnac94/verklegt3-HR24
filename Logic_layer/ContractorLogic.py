from Data_Layer.DataWrapper import DataWrapper
from Models.Contractor import Contractor


class ContractorLogic:
    def __init__(self):
        self.data_wrapper = DataWrapper()


    def create_contractor(self, contractor_details: dict) -> str:
        '''
        Takes in a contractor object and forwards it to the data layer.
        :param contractor_details: The details for the contractor to create
        '''
        new_contractor = Contractor(
            contractor_id=contractor_details["contractor_id"],
            name=contractor_details["name"],
            contact_name=contractor_details["contact_name"],
            phone_nr=contractor_details["phone_nr"],
            opening_time=contractor_details["opening_time"],
            location=contractor_details["location"],
            satisfaction_with_previous_work=contractor_details["satisfaction_with_previous_work"]
        )
        self.data_wrapper.register_contractor(new_contractor)
        return "Contractor registered successfully."
    

    def list_contractors(self) -> list[Contractor]:
        '''
        List all contractors.
        '''
        return self.data_wrapper.get_all_contractors()


    def change_contractor_info(self, contractor_id, field, updated_contractor) -> str:
        '''
        Change contractors information.
        '''
        return self.data_wrapper.change_contractor_info(contractor_id, field, updated_contractor)