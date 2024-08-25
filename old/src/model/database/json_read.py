#resposible to see if there are or not login informations in login.json.
#if it is, will use it to connect to database, if its not, will return False
import json

def login_check():

    file_path = "c:/Users/fsxre/OneDrive/GitHub/ParkSlot/src/model/database/login.json"

    with open(file_path,"r") as file: #abrindo .json
        data = json.load(file)

    logged = (data['last_login']['logged']) #descobrindo valor de logged
    
    if logged == 0: #Se já tiver algum registro no .json, vai devolver 1, do contrário, 0.
        return False
    return True 
    