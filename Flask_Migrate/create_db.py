import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Current-Root-Password"
)

my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE test1")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)


