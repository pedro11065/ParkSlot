import psycopg2
from json_read_cnn import json_read_cnn_db

def db_read():
    try:
        db_login = json_read_cnn_db()
        # Connection details
        conn = psycopg2.connect(
            host=db_login[0],
            database=db_login[0],
            user=db_login[0],
            password=db_login[0]
        )
        cur = conn.cursor()

        cur.execute("SELECT id, placa, nomecliente, datachegada, horariochegada FROM parkslot_now")

        db_data = cur.fetchall()

        cur.close()
        conn.close()
    except:
        return False
    return True