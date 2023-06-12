import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()

#mycursor.execute("select studentid,first_name,last_name from ineuron.fsds")

#mycursor.execute("select * from ineuron.fsds where studentid = 130")

#mycursor.execute("select * from ineuron.fsds where studentid > 130")

#mycursor.execute("select * from ineuron.fsds where first_name = 'Aditya' and class = 'sql'")

#mycursor.execute("update ineuron.fsds set first_name = 'Yashobanta' where studentid = 124")
#mydb.commit()
#mycursor.execute("select studentid,first_name,last_name from ineuron.fsds")

#mycursor.execute("update ineuron.fsds set class = 'mysql'")
#mydb.commit()
#mycursor.execute("select studentid,first_name,last_name,class from ineuron.fsds")

# mycursor.execute("delete from ineuron.fsds where last_name = 'Mishra'")
# mydb.commit()
# mycursor.execute("select studentid,first_name,last_name from ineuron.fsds")

#mycursor.execute("select min(studentid) from ineuron.fsds")
#mycursor.execute("select max(studentid) from ineuron.fsds")

#mycursor.execute("select count(*) from ineuron.fsds")

# mycursor.execute("update ineuron.fsds set class = 'sql' where studentid between 126 and 128 ")

# mycursor.execute("update ineuron.fsds set class = 'mongodb' where studentid between 129 and 130 ")
# mydb.commit()
# mycursor.execute("select studentid,first_name,last_name,class from ineuron.fsds")

# mycursor.execute("select class,count(*) from ineuron.fsds group by class")

# mycursor.execute("drop table ineuron.fsds")
# mydb.commit()

mycursor.execute("drop database ineuron")

for i in mycursor:
    print(i)