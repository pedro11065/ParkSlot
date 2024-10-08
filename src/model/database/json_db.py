# Analisa se há informações de login para o banco de dados no json_db.json.
# Se houver, o banco de dados será conectado, se não, irá retornar False.
import json

def json_db_read():
    
    # Facilmente substituível por um arquivo .env (o qual contem informações sensíveis do PROJETO, como TOKENS.)
    file_path = "src/model/database/json_db.json"

    with open(file_path,"r") as file: #openning .json
        data = json.load(file)

    host = (data['db']['host']) 
    database = (data['db']['database'])
    user = (data['db']['user'])
    password = (data['db']['password'])

    return host,database,user,password
