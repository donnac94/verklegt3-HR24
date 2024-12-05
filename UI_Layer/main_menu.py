import sys
class Main:
    
    def __init__(self, fullName, username):
        self.fullName = fullName
        self.username = username
    
    
    def main_menu_input(self):
        curr = input("\n Enter 1 if you are Supervisor and 2 if you are Employee: ")
        if curr == '1':
            while True:
                h = '-'
                c = '+'
                d = '|'
                print (c + "Air Nan".center(63, h) + c)
                print (d + "Welcome to Air NaN". center(63) + d)
                print (c + h*63 + c)
                print(d + " " + "Home(home)" + " " + d + " " + "Destinations(des)" + " " + d +" " + "Housing(Hou)" + " " + d + " " + "Employees(Em)" + " " + d)
                print(d + h*63 + d)
                print(d + "SuperVisor Main Menu".center(63) + d)
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
    
    # def read_file(self) -> login:
    #     while True:
    #         with open('users.txt', 'r'):
    #             if username in 'user.txt':
    #                 return self.supervisor_menu()
    #             else:
    #                 return self.employee_menu()
    
    def exit_line():
        sys.exit(0)

if __name__ == "__main__":
    testtest_menu = Main(fullName=(), username=())
    testtest_menu.main_menu_input()
