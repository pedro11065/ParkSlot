import psycopg2

def db_delete(exit):
    
    from json_db import json_db_read
    from ..time import time_now
    
    try:
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

        plate = exit[3]
        custumer_name = exit[4]
        time_arrive = exit[5]
        date_arrive = exit[6]

        date_exit = exit[1]
        time_exit = exit[0]
        

        # Delete data from the table
        cur.execute("DELETE FROM parkslot_now WHERE plate = %s", (plate))
        cur.execute("INSERT INTO parkslot_historic (plate, custumer_name, time_arrive, date_arrive, time_exit, date_exit) VALUES (%s, %s, %s, %s)", (f'{plate}', f'{custumer_name}', f'{time_arrive}', f'{date_arrive}', f'{time_exit}', f'{date_exit}'))

        # Commit the changes
        conn.commit()

        # Close the cursor and connection
        cur.close()
        conn.close()
    except:
        return False
    return True
