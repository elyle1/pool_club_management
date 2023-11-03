import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Prof3SSi0nalPiupzzxk",
  database="mydatabase"
)

print(mydb)

mycursor = mydb.cursor()

print("Generating report…")
print('')

date = '2003-03-06'

print("Date: ", date, '\n')

print("Daily Readings")

sql = "SELECT date, time, ph, totalchlorine, freechlorine, combinedchlorine FROM daily_readings WHERE date = %s"
val = (date, )
mycursor.execute(sql, val)
myresult = mycursor.fetchall()

print("Under construction… \n")

print("Weekly Readings")
sql = "SELECT date, time, ph, totalhardness, totalalkalinity, cya FROM weekly_readings WHERE date = %s"
val = (date, )
mycursor.execute(sql, val)
myresult = mycursor.fetchall()

print("Tasks Complete")
print("Under construction… \n")

print("Manager's Approval")

