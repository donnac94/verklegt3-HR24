class Main:
    
    def __init__(self, fullName, username):
        self.fullName = fullName
        self.username = username
    
    
    def main_menu_input(self):
        while True:
            h = '-'
            c = '+'
            d = '|'
            print (c + "Air Nan".center(63, h) + c)
            print (d + "Welcome to Air NaN". center(63) + d)
            print (c + h*63 + c)
            print(d + " " + "Home(home)" + " " + d + " " + "Destinations(des)" + " " + d +" " + "Housing(Hou)" + " " + d + " " + "Employees(Em)" + " " + d)
            print(d + h*63 + d)
            print(d + "Main Menu".center(63) + d)
            print(d + "Work" + "- Goes to the home worksheet".center(59) + d)
            print(d + "Work" + "- Goes to the home worksheet".center(59) + d)
            print(d + "Work" + "- Goes to the home worksheet".center(59) + d)
            print(d + "Work" + "- Goes to the home worksheet".center(59) + d)
            print(d + "Work" + "- Goes to the home worksheet".center(59) + d)
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
                return self.quit()
    
    # def read_file(self) -> login:
    #     while True:
    #         with open('users.txt', 'r'):
    #             if username in 'user.txt':
    #                 return self.supervisor_menu()
    #             else:
    #                 return self.employee_menu()

if __name__ == "__main__":
    testtest_menu = Main(fullName=(), username=())
    testtest_menu.main_menu_input()
