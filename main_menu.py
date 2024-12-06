import sys
from search import Search

class Main:
    
    def __init__(self, fullName, username):
        self.fullName = fullName
        self.username = username
        self.Search = Search(name_id=(), employee_ssn=(), location=(),workorder=(),house_id=())
    
    def main_menu_input(self):
        curr = input("\n Enter 1 if you are Supervisor and 2 if you are Employee: ")
        if curr == '1':
            while True:
                h = '-'
                c = '+'
                d = '|'
                print (c + "Air Nan".center(81, h) + c)
                print (d + "Welcome to Air NaN". center(81) + d)
                print (c + h*81 + c)
                print(d + " " + "Home(home)" + " " + d + " " + d + "Search(search)" + " " + d +" "+ "Destinations(des)" + " " + d +" " + "Housing(hou)" + " " + d + " " + "Employees(em)" + " " + d)
                print(d + h*81 + d)
                print(d + "Supervisor Menu".center(81) + d)
                print(d + h*81 + d)
                print(d + "1. Location" + "- List of Employees and properties by location".center(70) + d)
                print(d + "2. Employee" + "- Search Employee by Social Security Number".center(70) + d)
                print(d + "3. Property" + "- Search Properties by the property id".center(70) + d)
                print(d + "4. WorkId" + "- Search Work by the WorkID".center(72) + d)
                print(d + "Quit(q)" + "- Exit The program".center(74) + d)
                print (d + h*81 + d)
                print (c + ":Your input:".center(81, h) + c)

                choice = input("\n choose a option: ")
                if choice == '1':
                    return self.work()
                elif choice == '2':
                    return self.work()
                elif choice == '3':
                    return self.work()
                elif choice == '4':
                    return self.work()
                elif choice == '5':
                    return self.work()
                elif choice == 'home':
                    return self.main_menu_input()
                elif choice == 'search':
                    return self.Search
                elif choice == 'des':
                    return self.destination()
                elif choice == 'hou':
                    return self.Housing()
                elif choice == 'em':
                    return self.employee()
                elif choice == 'q':
                    return self.exit_line()
        elif curr == '2':
            while True:
                h = '-'
                c = '+'
                d = '|'
                print (c + "Air Nan".center(63, h) + c)
                print (d + "Welcome to Air NaN". center(63) + d)
                print (c + h*63 + c)
                print(d + " " + "Home(home)" + " " + d + " " + "Destinations(des)" + " " + d +" " + "Housing(Hou)" + " " + d + " " + "Employees(Em)" + " " + d)
                print(d + h*63 + d)
                print(d + "Employee Main Menu".center(63) + d)
                print(d + "Work" + "- Goes to the home worksheet".center(59) + d)
                print(d + "Work" + "- Goes to the home worksheet".center(59) + d)
                print(d + "Work" + "- Goes to the home worksheet".center(59) + d)
                print(d + "Work" + "- Goes to the home worksheet".center(59) + d)
                print(d + "Quit(q)" + "- Exit The program".center(59) + d)
                print (d + h*63 + d)
                print (c + "Your input:".center(63, h) + c)

                choice = input("\n choose a option: ")
                if choice == '1':
                    return self.work()
                elif choice == '2':
                    return self.work()
                elif choice == '3':
                    return self.work()
                elif choice == '4':
                    return self.work()
                elif choice == '5':
                    return self.work()
                elif choice == 'q'.lower():
                    return self.exit_line()
        else:
            raise ValueError("invalid value input")
    
    def exit_line():
        sys.exit(0)

if __name__ == "__main__":
    testtest_menu = Main(fullName=(), username=())
    testtest_menu.main_menu_input()
    testtest_menu.Search
