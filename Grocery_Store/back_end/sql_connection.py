import datetime
import mysql.connector

connect = None

def get_sql_connection():
    print("Opening my sql connection")
    global connect
    if connect is None:
        connect = mysql.connector.connect(user = 'root', password = 'abc13579',
        database = 'grocery_store')
    return connect
