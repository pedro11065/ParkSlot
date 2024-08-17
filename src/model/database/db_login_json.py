import sys
import json

#sys.path.insert(1, 'parkslot/src/view')
#from view.db_login import login_register

sys.path.insert(1, 'parkslot/src/model/database')

with open("login.json","r") as file: #abrindo .json
    data = json.load(file)

print(data)