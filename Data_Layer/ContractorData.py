import csv
from Models.Contractor import Contractor


class ContractorData():
    ''' This class is responsible for handling the data of contractors'''
    def __init__(self):
        self.filename = "Files/contractors.csv"


    def RegisterContractor(self, contractor_obj: Contractor) -> str:
        ''' Register new contractor in the CSV file.
          :param Contractor_obj: the contractor to save. 
          :return: Success message or raise exemption 
        '''
        try:
            with open(self.filename, "a", newline="", encoding="utf-8") as csvfile:
                fieldnames = [
                    "contractor_id",
                    "name",
                    "contact_name",
                    "phone_nr",
                    "opening_time",
                    "location",
                    "satisfaction_with_previous_work"
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                if csvfile.tell() == 0:
                    writer.writeheader()
                
                writer.writerow({
                    "contractor_id": contractor_obj.contractor_id,
                    "name": contractor_obj.name,
                    "contact_name": contractor_obj.contact_name,
                    "phone_nr": contractor_obj.phone_nr,
                    "opening_time": contractor_obj.opnening_time,
                    "location": contractor_obj.location,
                    "satisfaction_with_previous_work": contractor_obj.satisfaction_with_previous_work
                })
                return "Contractor registered successfully"

        except Exception as e:
             raise Exception(f"Error saving contractor: {e}")
    


    def GetAllContractors(self) -> list[Contractor]:
        '''
        Retrieve all contractors from the CSV file.
        :return: A list of all contractors objects or raises an exception.
        '''
        ret_list = []
        try: 
            with open(self.filename, "r", newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    ret_list.append(Contractor(
                        contractor_id=int(row["contractor_id"]), 
                        name=row["name"], 
                        contact_name=row["contact_name"], 
                        phone_nr=row["phone_nr"], 
                        opening_time=row["opening_time"], 
                        location=row["location"],
                        satisfaction_with_previous_work=row["satisfaction_with_previous_work"]
                    ))
                return ret_list
        except FileNotFoundError:
            return []  # Return an empty list if the file doesn't exist
        except Exception as e:
            raise Exception(f"Error reading contractors: {e}")

    

    def ChangeContractorInfo(self, contractor_id: int, updated_contractor: Contractor) -> str:
        '''
        Change a contractors information. 
        :param contractor_id: the ID of the cotractor to update.
        :param updated_contractor: The updated contractor information.
        :return: Success message or raises an exception.
        '''

        success = False
        try: 
            contractors = self.GetAllContractors()
            with open(self.filename, "w", newline="", encoding="utf-8") as csvfile:
                fieldnames = [
                    "contractor_id",
                    "name",
                    "contact_name",
                    "phone_nr",
                    "opening_time",
                    "location",
                    "satisfaction_with_previous_work"
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for contractor_obj in contractors:
                    if contractor_obj.contractor_id == contractor_id:
                        # Replace with updated contractor
                        contractor_obj = updated_contractor
                        success = True
                    writer.writerow({
                        "contractor_id": contractor_obj.contractor_id,
                        "name": contractor_obj.name,
                        "contact_name": contractor_obj.contact_name,
                        "phone_nr": contractor_obj.phone_nr,
                        "opening_time": contractor_obj.opnening_time,
                        "location": contractor_obj.location,
                        "satisfaction_with_previous_work": contractor_obj.satisfaction_with_previous_work
                    })
            if success: 
                return "Contractor updated successfully"
            else:
                return "Contractor not found"
        except Exception as e:
            raise Exception(f"Error updating contractor: {e}")