import csv
from Data_Layer.EmployeeData import EmployeeData
from Data_Layer.HouseData import HouseData
from Data_Layer.WorkData import WorkData

class Search: 
    
    def __init__(self,name_id, employee_ssn, location, workorder, house_id):
        self.name_id = name_id
        self.employee_ssn = employee_ssn
        self.location = location
        self.workorder = workorder
        self.house_id = house_id
        
    
      
        
    def search_filter(self):
         while True:
                h = '-'
                c = '+'
                d = '|'
                print (c + "Air Nan".center(81, h) + c)
                print (d + "Welcome to Air NaN". center(81) + d)
                print (c + h*81 + c)
                print(d + " " + "Home(home)" + " " + d + " " + d + "Search(search)" + " " + d +" "+ "Destinations(des)" + " " + d +" " + "Housing(Hou)" + " " + d + " " + "Employees(Em)" + " " + d)
                print(d + h*81 + d)
                print(d + "Search Menu".center(81) + d)
                print(d + "1. Location" + "- List of Employees and properties by location".center(70) + d)
                print(d + "2. Employee" + "- Search Employee by Social Security Number".center(70) + d)
                print(d + "3. Property" + "- Search Properties by the property id".center(70) + d)
                print(d + "4. WorkId" + "- Search Work by the WorkID".center(72) + d)
                print(d + "Quit(q)" + "- Exit The program".center(74) + d)
                print (d + h*81 + d)
                print (c + ":Your input:".center(81, h) + c)
                choice = input("Select filter: ")
                if choice == 'home':
                    return self.main_menu()
                elif choice == '1':
                    return self.search_empAndhou()
                elif choice == '2':
                    return self.search_empSSN()
                elif choice == '3':
                    return self.search_HouseID()
                elif choice == '4':
                    return self.search_WorkID()
                elif choice == '5':
                    return self.search_all_WorkId()
                elif choice == '6':
                    return self.search_WorkID_Emp()
                else:
                    raise ValueError("Input value not valid")
                
                
    def search_empAndhou(self):
        search_part = input("Enter search: ")
        file = csv.reader(open('./Files/empAndhou.csv', 'r'))
        with open(file):
            if search_part != None:
                