import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Prof3SSi0nalPiupzzxk",
  database="mydatabase"
)

#print(mydb)

mycursor = mydb.cursor()

print("Username: ")
username = input()

print("Password: ")
password = input()

print(username + " " + password)