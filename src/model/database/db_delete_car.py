import psycopg2

def db_delete():
    
    from json_db import json_db_read
    
    try:
        db_login = json_db_read()
        # Connection details
        conn = psycopg2.connect(
            host=db_login[0],
            database=db_login[0],
            user=db_login[0],
            password=db_login[0]
        )

        # Create a cursor
        cur = conn.cursor()

        # Delete data from the table
        cur.execute("DELETE FROM parkslot_now WHERE placa = %s", ('value_to_delete',))
        cur.execute("INSERT INTO parkslot_now (placa, nomecliente, datachegada, horariochegada) VALUES (%s, %s, %s, %s, %s)", ('value1', 'value2', 'value3', 'value4', 'value5'))

        # Commit the changes
        conn.commit()

        # Close the cursor and connection
        cur.close()
        conn.close()
    except:
        return False
    return True
