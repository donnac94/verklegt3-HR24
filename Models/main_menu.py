

class main_menu():
    
    def __init__(self):
     pass
    
    def menu(self):
        ret = self.outlines_menu()
        print(ret)
        while input is not None:
            match input:
                case 1:
                    print("1. Manage Employees")
                case 2:
                    print("2. Manage Properties")
                case 3:
                    print("3. Manage Maintenance Requests")
                case 4:
                    print("4. View Reports")
                case 5:
                    print("5. Exit")
                    
                    
    def outlines_menu(self):
        h = '-'
        c = '+'
        d = '|'
        # print (c + h*50 + c)
        print (c + "Air Nan".center(50, h) + c)
        print (d + "Welcome to Air NaN". center(50) + d)
        print (c + h*50 + c)
        for i in range(1,7):
            print(d + " " * 50 + d)
        print (d + h*50 + d)
        print (c + "Your input:".center(50, h) + c)
    
if __name__ == "__main__":
    main_menu()
    
    
            
            