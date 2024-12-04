class login:
    
    def __init__(self, username, password):
        self.password = password
        self.username = username
    
    def input_login(self):
        while input() is not None:
            
            use = input("\nEnter Username: ")
            pas = input("\nEnter Password: ")
            with open(r'users.txt', 'r') as fp:
                lines = fp.readlines()
                for row in lines:
                    word = use
                    if row.find(word)!= None:
                        return self.supervisor_menu()
                if use == 1 and pas == 1:
                    return self.supervisor_menu
                else:
                    return self.employee_menu
if __name__ == "__main__":
    login_menu = login(username=(), password=())
    login_menu.input_login() 
                
            