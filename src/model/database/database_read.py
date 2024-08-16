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

# Execute a query to fetch data
cur.execute("SELECT column1, column2 FROM your_table_name")

# Fetch all results
rows = cur.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()
