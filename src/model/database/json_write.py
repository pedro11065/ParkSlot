import json

file_path = "c:/Users/fsxre/OneDrive/GitHub/ParkSlot/src/model/database/login.json"

def login_save(db_login):

   data = {"last_login":
   {
       "logged": 0,
       "host":f'"{db_login[0]}"',
       "database":f'"{db_login[1]}"',
       "user":f'"{db_login[2]}"',
       "password":f'"{db_login[3]}"'
   }
   }
   with open(file_path, 'w') as file:
       json.dump(data, file)