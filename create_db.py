import mysql.connector

mydb = mysql.connector.connect(user='root', password='1234',
                              host='localhost',
                              auth_plugin='mysql_native_password')

my_cursor = mydb.cursor()

#comment out the next line after the first run
#my_cursor.execute("CREATE DATABASE users")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)