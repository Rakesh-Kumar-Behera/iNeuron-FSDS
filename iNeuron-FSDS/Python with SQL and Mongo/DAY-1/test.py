import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost", #127.0.0.1
  user="abc",
  password="password"
)

print(mydb.is_connected())

mycursor = mydb.cursor() #pointer

mycursor.execute("SHOW DATABASES")

for i in mycursor:
    print(i)