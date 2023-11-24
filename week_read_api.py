import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Prof3SSi0nalPiupzzxk",
  database="poolclub"
)

#print(mydb)

mycursor = mydb.cursor()

def addWeeklyReading(inputs):
  recordInput = inputs
  sql = "INSERT INTO weekly_readings(week_id, date, time, totalhardness, totalalkalinity, cya) VALUES(%s, %s, %s, %s, %s, %s)"
  mycursor.execute(sql, recordInput)
  mydb.commit()


def removeWeeklyReading(inputs):
  recordInput = inputs
  sql = "DELETE FROM weekly_readings WHERE week_id = %s"
  val = (recordInput[0], )
  mycursor.execute(sql, val)
  mydb.commit()
    
  
def updateWeeklyReading(inputs):
  recordInput = inputs
  sql = "UPDATE weekly_readings SET date = %s, time = %s, totalhardness = %s, totalalkalinity = %s, cya = %s WHERE week_id = %s"
  val = (recordInput[1], recordInput[2], recordInput[3], recordInput[4], recordInput[5], recordInput[0])
  mycursor.execute(sql, val)
  mydb.commit()
  
def displayWeeklyReading():
  print("Enter a category to filter the weekly readings displayed using the corresponding number:")
  print("[0] Exit   ")
  print("[1] Week ID          [2] Date               [3] Time")
  print("[4] Total Hardness   [5] Total Alkalinity   [6] Cyanuric Acid (CYA/stabilizer)")
  print("Action: ")
  filterBy = int(input())

  match filterBy:
    case 0:
      dummy = None
    case 1:
      print("Enter the Week ID value.")
      week_ID = input()      
    case 2:
      print("Enter the Date value.")
      date = input()      
    case 3:
      print("Enter the Time value.")
      time = input()      
    case 4:
      print("Enter the Total Hardness value (in parts per million/ppm).")
      totalHardness = input()      
    case 5:
      print("Enter the Total Alkalinity value (in parts per million/ppm).")
      totalAlkalinity = input()      
    case 6:
      print("Enter the Cyanuric Acid (CYA/stabilizer) value.")
      cya = input()      
    case _:
      print("This is not a valid parameter.")

  print('\nBelow is a list based on your specification: \n')

  match filterBy:
    case 1:
      sql = "SELECT * FROM weekly_readings WHERE week_id = %s"
      val = (week_ID, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 2:
      sql = "SELECT * FROM weekly_readings WHERE date = %s"
      val = (date, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 3:
      sql = "SELECT * FROM weekly_readings WHERE time = %s"
      val = (time, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 4:
      sql = "SELECT * FROM weekly_readings WHERE totalhardness = %s"
      val = (totalHardness, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 5:
      sql = "SELECT * FROM weekly_readings WHERE totalalkalinity = %s"
      val = (totalAlkalinity, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 6:
      sql = "SELECT * FROM weekly_readings WHERE cya = %s"
      val = (cya, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case _:
      dummy = None
  
  print('')

