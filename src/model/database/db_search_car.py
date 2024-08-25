import psycopg2


def db_search(search_data):

    from .json_db import json_db_read

    try:
        db_login = json_db_read()
        # Connection details
        conn = psycopg2.connect(
            host=db_login[0],
            database=db_login[0],
            user=db_login[0],
            password=db_login[0]
        )
        cur = conn.cursor()

        placa = search_data

        cur.execute(f"SELECT * WHERE 'placa' = {placa}")

        db_data = cur.fetchall()

        cur.close()
        conn.close()
    except:
        return False
    return True