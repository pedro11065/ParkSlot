import psycopg2

def db_delete(plate,custumer_name,entry_time,entry_data):
    
    from src.model.database.json_db import json_db_read
    from ..time import time_now
    
    db_login = json_db_read()
    # Connection details
    conn = psycopg2.connect(
        host=db_login[0],
        database=db_login[1],
        user=db_login[2],
        password=db_login[3]
    )

    # Create a cursor
    cur = conn.cursor()

    #id, plate, custumer_name, time_arrive, date_arrive

    date_exit = time_now()[0]
    time_exit = time_now()[1]
    

    # Delete data from the table
    cur.execute(f"DELETE FROM parkslot_now WHERE plate = '{plate}'")
    
    """ adicionar valor pago, remover placa unica """ cur.execute(f"INSERT INTO parkslot_historic (plate, custumer_name, time_arrive, date_arrive, time_exit, date_exit) VALUES ('{plate}', '{custumer_name}', '{entry_time}', '{entry_data}', '{time_exit}', '{date_exit}')")

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()
