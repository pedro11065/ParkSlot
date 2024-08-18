#resposible to see if there are or not login informations in login.json.
#if it is, will use it to connect to database, if its not, will return False
import json

def json_read_cnn_db():

    file_path = "c:/Users/fsxre/OneDrive/GitHub/ParkSlot/src/model/database/login.json"

    with open(file_path,"r") as file: #abrindo .json
        data = json.load(file)

    host = (data['last_login']['host']) #descobrindo valor de logged
    database = (data['last_login']['database'])
    user = (data['last_login']['user'])
    password = (data['last_login']['password'])

    return host,database,user,password