#see if there are any database login info in login.json
#if there is, ok, menu. Else, connect
import os
import sys

main_directory = 'C:/Users/fsxre/OneDrive/GitHub/ParkSlot/src'

for root, dirs, files in os.walk(main_directory):
    sys.path.append(root)

#--------------------------------------------------------

from model.database.json_read import login_check 
from view.connect.db_login import login_register
from model.database.json_write import login_save

#--------------------------------------------------------

from model.verification.menu_return import menu_return
from model.verification.plate_return import plate_return

from view.menu.historic import #historic
from view.menu.delete import #delete
from view.menu.Search import #search
from view.menu.List import #list_
from view.menu.menu import menu
from view.menu.add import add

from view.errors.menu_error import menu_error
#--------------------------------------------------------

def login_control():

    if login_check() == False:
        db_login = login_register()
        login_save(db_login)

login_control()

def main():

    while(True):

        job = menu()
        
        if menu_return(job) == False: 
            menu_error() ; continue        

        match job:
            case "0": #Add
                plate_return(add())
            case "1":#Search
                None
            case "2":#List
                None
            case "3":#Delete
                None
            case "4":#Historic
                None
        

        

main()