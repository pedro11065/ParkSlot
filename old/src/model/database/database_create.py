import psycopg2
from json_read_cnn import json_read_cnn_db
from db_global_functions.data import data_time

db_login = json_read_cnn_db()
# Connection details
conn = psycopg2.connect(
    host=db_login[0],
    database=db_login[0],
    user=db_login[0],
    password=db_login[0]
)
# Create a cursor
cur = conn.cursor()

# Insert some data into an existing table
cur.execute("INSERT INTO parkslot_now (id, placa, nomecliente, datachegada, horariochegada) VALUES (%s, %s, %s, %s, %s)", ('value1', 'value2', 'value3', 'value4', 'value5'))

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
