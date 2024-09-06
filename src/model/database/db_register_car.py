import psycopg2
from psycopg2 import OperationalError, InterfaceError, DatabaseError

def database_create(plate,custumer_name):
   
    from src.model.database.json_db import json_db_read
    from ..time import time_now

    try:
        
        db_login = json_db_read()
    
        conn = psycopg2.connect(
            host=db_login[0],
            database=db_login[1],
            user=db_login[2],
            password=db_login[3]
        )
        times = time_now()

        time_arrive = times[1]
        date_arrive = times[0]
        
        cur = conn.cursor()

        # Insert some data into an existing table
        cur.execute("INSERT INTO parkslot_now (plate, custumer_name, time_arrive, date_arrive) VALUES (%s, %s, %s, %s)", ( plate, custumer_name, time_arrive, date_arrive ))

        # Commit the changes
        conn.commit()

        # Close the cursor and connection
        cur.close()
        conn.close()

    except OperationalError as e:
        print(f"Erro de operação: {e}")
    except InterfaceError as e:
        print(f"Erro de interface: {e}")
    except DatabaseError as e:
        print(f"Erro de banco de dados: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    return True
