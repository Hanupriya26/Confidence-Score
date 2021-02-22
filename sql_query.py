import mysql.connector.pooling

database_name = "ProjectDB"
table_name = "ProjectTable"


def create_connection_pool(pool_size):
    connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="project_pool",
                                                                  pool_size=pool_size,
                                                                  pool_reset_session=True,
                                                                  host="localhost",
                                                                  database=database_name,
                                                                  user="root",
                                                                  password="password")
    return connection_pool


def get_connection_from_pool(connection_pool):
    return connection_pool.get_connection()   # connection object, why need


def get_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database=database_name
    )
    return mydb


# Queries to be executed just once
def setup_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"
    )
    mycursor = mydb.cursor()

    try:
        mycursor.execute("CREATE DATABASE " + database_name)
    except mysql.connector.errors.DatabaseError as err:
        print(err)

    try:
        mydb.database = database_name
        mycursor.execute("CREATE TABLE " + table_name + " (Input VARCHAR(255), Confidence VARCHAR(255))")
    except mysql.connector.errors.ProgrammingError as err:
        print(err)

    mydb.close()


def insert_into_table(confidence_map, connection_pool):
    # mydb = get_connection()
    mydb = get_connection_from_pool(connection_pool)   # get a connection from the connection_pool
    mycursor = mydb.cursor()

    query = "INSERT INTO " + table_name + " (Input, Confidence) VALUES (%s, %s)"
    # confidence_map is a list of pairs containing our data
    mycursor.executemany(query, confidence_map)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    mycursor.execute("SHOW TABLES")

    for x in mycursor:
        print(x)

    mydb.close()
