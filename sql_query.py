import mysql.connector

database_name = "ProjectDB"
table_name = "ProjectTable"


def get_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database=database_name
    )
    return mydb


# Queries to be executed just once
def setup_table():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE " + database_name)
    mydb.database = database_name
    mycursor.execute("CREATE TABLE " + table_name + " (Input VARCHAR(255), Confidence VARCHAR(255))")
    mydb.close()


def insert_into_table(confidence_map):
    mydb = get_connection()
    mycursor = mydb.cursor()

    query = "INSERT INTO " + table_name + " (Input, Confidence) VALUES (%s, %s)"
    # val is a list containing our data
    mycursor.executemany(query, confidence_map)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    mycursor.execute("SHOW TABLES")

    for x in mycursor:
        print(x)

    mydb.close()
