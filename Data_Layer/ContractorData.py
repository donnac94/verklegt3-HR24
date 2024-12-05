import csv

#file = open("contractor_list.txt", "a+")



def RegisterContractor(name, company, connection, phone, opening, location):
    info = [name, company, connection, phone, opening, location]
    with open('contractor_csvfile.txt', 'a+') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(info)

    

    


def GetAllContractors():
    dict_of_contractors = {}
    with open('contractor_csvfile.txt', 'r') as csvfile:
        count = 0
        info_dict = {}
        for line in csvfile:
            
            line.split(",")
            dict_contr = 'company'; line[1], 'connection'; line[2], 'phone'; line[3], 'opening'; line[4], 'location'; line[5]
                
                
            info_dict[line[0]] = {dict_contr}    
    return info_dict

    #pass

def ChangeContractorInfo():
    pass


name = "emil"
company= "einn"
connection = "tómas"
phone = "5558888"
opening = "6-9"
location = "ísland"
RegisterContractor(name, company, connection, phone, opening, location)
#print(new_str)
#print(csvfile)
list_of_contractors = GetAllContractors()
print(GetAllContractors())