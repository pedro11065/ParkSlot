import sys
import json

#sys.path.insert(1, 'parkslot/src/view')
#from view.db_login import login_register

file_path = "c:/Users/fsxre/OneDrive/GitHub/ParkSlot/src/model/database/login.json"

sys.path.insert(1, 'parkslot/src/model/database')

with open(file_path,"r") as file: #abrindo .json
    data = json.load(file)

print(data['last_login']['logged']) #descobrindo valor de logged