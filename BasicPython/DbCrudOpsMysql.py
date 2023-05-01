import mysql.connector
#connect() will open a connection to mySQL connection object
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Iamhere4u@",
    database="myhelloDb"
)
mycursor= mydb.cursor()
#mycursor.execute("Create Database myhelloDb")
#mycursor.execute('Create table person (name varchar(200), adress varchar(344), gender varchar(10))')
sqlstatement="insert into person(name,adress,gender) values(%s,%s,%s)"
val=("Vijayan","Hyderabad", "male")
mycursor.execute(sqlstatement,val)
mydb.commit()

mycursor.execute("select * from person")
for rec in mycursor:
    print(rec)


#print(mydb)
