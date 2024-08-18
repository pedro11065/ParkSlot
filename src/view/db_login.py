

def login_register():

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
        
        



    

    
    


