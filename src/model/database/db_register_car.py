import psycopg2

def database_create(car_data):
   
    from .json_db import json_db_read
    from ..time import time_now


    try:
        db_login = json_db_read()
    
        conn = psycopg2.connect(
            host=db_login[0],
            database=db_login[0],
            user=db_login[0],
            password=db_login[0]
        )

        placa = car_data[0]
        nomecliente = car_data[1]
        datachegada = time_now()[0] 
        horariochegada = time_now()[1]
    

        cur = conn.cursor()

        # Insert some data into an existing table
        cur.execute("INSERT INTO parkslot_now (placa, nomecliente, datachegada, horariochegada) VALUES (%s, %s, %s, %s)", ( placa, nomecliente, datachegada, horariochegada ))

        # Commit the changes
        conn.commit()

        # Close the cursor and connection
        cur.close()
        conn.close()
    except:
        return False
    return True
