from Data_Layer.DataWrapper import DataWrapper
from Models.Contractor import Contractor
import csv


class ContractorLogic:
    def __init__(self):
        self.data_wrapper = DataWrapper()

    def create_contractor(self, contractor_details: dict) -> str:
        '''
        Takes in a contractor object and forwards it to the data layer.
        :param contractor_details: The details for the contractor to create
        '''

        # Check if contractor already in system
        existing_contractors = self.data_wrapper.get_all_contractors()
        for contractor in existing_contractors:
            if contractor.phone_nr == contractor_details["phone_nr"]:
                return "Contractor is already registered in system"

        contractor_id = self.automatic_contractor_id()
        contractor_details["contractor_id"] = contractor_id  # Ensure contractor_id is set
        new_contractor = Contractor(
            contractor_id=contractor_id,
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
        contractors = self.data_wrapper.get_all_contractors()
        if not contractors:
            return []
        return contractors


    def change_contractor_info(self, contractor_id, updated_details: dict) -> str:
        """_summary_

        Args:
            contractor_id (_type_): _description_
            updated_details (dict): _description_

        Raises:
            ValueError: _description_

        Returns:
            str: _description_
        """
        contractors = self.data_wrapper.get_all_contractors()
        contractor_found = False
        for contractor in contractors:
            if contractor.contractor_id == contractor_id:
                contractor_found = True
                for field, new_value in updated_details.items():
                    setattr(contractor, field, new_value)
                self.data_wrapper.update_contractor(contractor)
                return "Contractor information updated successfully."
        if not contractor_found:
            raise ValueError(f"Contractor with ID {contractor_id} not found.")
    

    def get_contractor_by_id(self, contractor_id):
        """ 
        Gets a specific contractor by their ID
        :param contractor_id: The contractor ID to look for.
        :return: A contractor and their information or raises an error if not found.
        """
        contractors = self.data_wrapper.get_all_contractors()
        for contractor in contractors:
            if contractor.contractor_id == contractor_id:
                return contractor
        raise ValueError(f"Contractor with ID {contractor_id} not found.")

    def automatic_contractor_id(self) -> int:
        """
        Gets the latest contractor ID and give it plus 1.
        """
        contractors = self.list_contractors()
        if not contractors:
            return 1
        latest_contractor = contractors[-1]
        latest_id = int(latest_contractor.contractor_id)
        return latest_id + 1