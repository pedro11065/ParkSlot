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

# Delete data from the table
cur.execute("DELETE FROM your_table_name WHERE column_name = %s", ('value_to_delete',))

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
