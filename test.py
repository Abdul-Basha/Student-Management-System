from database import connect_db

conn = connect_db()

if conn.is_connected():
    print("Database Connected Successfully")

conn.close()