import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Prof3SSi0nalPiupzzxk",
  database="poolclub"
)

#print(mydb)

mycursor = mydb.cursor()

def addDailyReading(inputs):
  recordInput = inputs
  recordInput[6] = float(recordInput[4]) - float(recordInput[5])
  sql = "INSERT INTO daily_readings(day_id, date, time, ph, totalchlorine, freechlorine, combinedchlorine) VALUES(%s, %s, %s, %s, %s, %s, %s)"
  mycursor.execute(sql, recordInput)
  mydb.commit()


def removeDailyReading(inputs):
  recordInput = inputs
  sql = "DELETE FROM daily_readings WHERE day_id = %s"
  val = (recordInput[0], )
  mycursor.execute(sql, val)
  mydb.commit()
    
  
def updateDailyReading(inputs):
  recordInput = inputs
  recordInput[6] = float(recordInput[4]) - float(recordInput[5])
  sql = "UPDATE daily_readings SET date = %s, time = %s, ph = %s, totalchlorine = %s, freechlorine = %s, combinedchlorine = %s WHERE day_id = %s"
  val = (recordInput[1], recordInput[2], recordInput[3], recordInput[4], recordInput[5], recordInput[6], recordInput[0])
  mycursor.execute(sql, val)
  mydb.commit()

def displayDailyReading():
  print("Enter a category to filter the daily readings displayed using the corresponding number:")
  print("[0] Cancel                  [1] ID num      [2] First Name")
  print("[3] Last Name               [4] Hire Date   [5] Separation Date")
  print("[6] Reason for Separation   [7] Password    [8] User Type")
  print("Action: ")
  filterBy = int(input())

  match filterBy:
    case 0:
      dummy = None
    case 1:
      print("Enter the ID num value.")
      ID_num = input()      
    case 2:
      print("Enter the First Name value.")
      firstName = input()      
    case 3:
      print("Enter the Last Name value.")
      lastName = input()      
    case 4:
      print("Enter the Hire Date value (YYYY-MM-DD).")
      hireDate = input()      
    case 5:
      print("Enter the Separation Date value (YYYY-MM-DD).")
      separationDate = input()      
    case 6:
      print("Enter the Reason for Separation.")
      reasonForSeparation = input()      
    case 7:
      print("Enter the Password.")
      password = input()      
    case 8:
      print("Enter the User Type.")
      userType = input()      
    case _:
      print("This is not a valid parameter.")

  print('\nBelow is a list based on your specification: \n')

  match filterBy:
    case 1:
      print('\nBelow is a list based on your specification: \n')
      sql = "SELECT * FROM staff WHERE id_num = %s"
      val = (ID_num, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 2:
      print('\nBelow is a list based on your specification: \n')
      sql = "SELECT * FROM staff WHERE firstname = %s"
      val = (firstName, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 3:
      print('\nBelow is a list based on your specification: \n')
      sql = "SELECT * FROM staff WHERE lastname = %s"
      val = (lastName, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 4:
      print('\nBelow is a list based on your specification: \n')
      sql = "SELECT * FROM staff WHERE hiredate = %s"
      val = (hireDate, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 5:
      print('\nBelow is a list based on your specification: \n')
      sql = "SELECT * FROM staff WHERE separationdate = %s"
      val = (separationDate, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 6:
      print('\nBelow is a list based on your specification: \n')
      sql = "SELECT * FROM staff WHERE reasonforseparation = %s"
      val = (reasonForSeparation, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 7:
      print('\nBelow is a list based on your specification: \n')
      sql = "SELECT * FROM staff WHERE password = %s"
      val = (password, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 8:
      print('\nBelow is a list based on your specification: \n')
      sql = "SELECT * FROM staff WHERE usertype = %s"
      val = (userType, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case _:
      dummy = None
  
  print('')