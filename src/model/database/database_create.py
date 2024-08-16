import psycopg2

# Connection details
conn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_user",
    password="your_password"
)

# Create a cursor
cur = conn.cursor()

# Insert some data into an existing table
cur.execute("INSERT INTO your_table_name (column1, column2) VALUES (%s, %s)", ('value1', 'value2'))
cur.execute("INSERT INTO your_table_name (column1, column2) VALUES (%s, %s)", ('value3', 'value4'))

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
