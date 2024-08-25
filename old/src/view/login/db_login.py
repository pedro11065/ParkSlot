import sys 

def login_register():

    sys.path.append('C:/Users/fsxre/OneDrive/GitHub/ParkSlot/src/view')
    from v_global_functions.clear_terminal import clean_terminal
    
    while(True):

        print("--- Registrar servidor ---\n")

        host = input("host:")
        database = input("Database:")
        user = input("Usuário:")
        password = input("senha:")

        login_check = input("\n Todas informações estão corretas?(S/N)")

        if login_check in ["S","s"]:
            return host,database,user,password
    
        clean_terminal()
        
        



    

    
    


