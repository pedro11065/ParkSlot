#see if there are any database login info in login.json
#if there is, ok, menu. Else, connect
import os
import sys

main_directory = 'C:/Users/fsxre/OneDrive/GitHub/ParkSlot/src'

for root, dirs, files in os.walk(main_directory):
    sys.path.append(root)

def login_control():

    from src.model.database.json_read import login_check 
    from src.model.database.json_write import login_save
    from view.db_login import login_register

    if login_check() == False:
        db_login = login_register()
        login_save(db_login)

