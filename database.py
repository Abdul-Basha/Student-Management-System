import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Abdul@123",
        database="student_sql"
    )
    return conn