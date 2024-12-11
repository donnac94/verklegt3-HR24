import csv
from Models.Contractor import Contractor


class ContractorData():
    ''' This class is responsible for handling the data of contractors'''
    def __init__(self):
        self.filename = "Files/contractors.csv"

    def register_contractor(self, contractor_obj: Contractor) -> str:
        ''' Register new contractor in the CSV file.
          :param Contractor_obj: the contractor to save. 
        '''

        contractors = self.get_all_contractors()
        contractors.append(contractor_obj)
        with open(self.filename, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["contractor_id", "name", "contact_name", "phone_nr", "opening_time", "location", "satisfaction_with_previous_work"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for contractor in contractors:
                writer.writerow(contractor.to_dict())

    def get_all_contractors(self) -> list[Contractor]:
        '''
        Retrieve all contractors from the CSV file.
        :return: A list of all contractors.
        '''

        with open(self.filename, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            return [Contractor.from_dict(row) for row in reader]

    def change_contractor_info(self, contractor_id, field, new_value):
        '''
        Change a contractors information. 
        '''

        contractors = self.get_all_contractors()
        success = False
        for contractor in contractors:
            if contractor.contractor_id == contractor_id:
                setattr(contractor, field, new_value)
                success = True
        
        if not success: 
            raise ValueError(f"Contractor with ID {contractor_id} not found.")
        
        with open(self.filename, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["contractor_id", "name", "contact_name", "phone_nr", "opening_time", "location", "satisfaction_with_previous_work"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for contractor in contractors:
                writer.writerow(contractor.to_dict())