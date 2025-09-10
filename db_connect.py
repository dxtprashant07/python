import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    port = 3306,        # or your MySQL server IP
    user="root",             # your MySQL username
    password=".@.@pP5001707",# your MySQL password
    database="lab"           # your database name
)

# Create a cursor
cursor = conn.cursor()
cursor.execute("SELECT *  FROM SALES_ORDER WHERE MONTH(ORDERDATE)= 6;")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
