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

    def update_contractor(self, updated_contractor: Contractor) -> None:
        '''
        Change a contractors information.
        :param Contractor updated_contractor: the updated contractor to be saved.
        '''
        contractors = self.get_all_contractors()
        with open(self.filename, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["contractor_id", "name", "contact_name", "phone_nr", "opening_time", "location", "satisfaction_with_previous_work"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for contractor in contractors:
                if contractor.contractor_id == updated_contractor.contractor_id:
                    writer.writerow(updated_contractor.to_dict())
                else:
                    writer.writerow(contractor.to_dict())