import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Prof3SSi0nalPiupzzxk",
  database="poolclub"
)

#print(mydb)

mycursor = mydb.cursor()

def addWeeklyReading():
  print("Week ID: ")
  week_ID = input()
  print("Date: ")
  date = input()
  print("Time: ")
  time = input()
  print("Total Hardness (in parts per million/ppm): ")
  totalHardness = input()
  print("Total Alkalinity (in parts per million/ppm): ")
  totalAlkalinity = input()
  print("Cyanuric Acid (CYA/stabilizer): ")
  cya = input()
  print("Password: ")

  recordInput = [week_ID, date, time, totalHardness, totalAlkalinity, cya]
  print('\n', recordInput, '\n')
  sql = "INSERT INTO weekly_readings(week_id, date, time, totalhardness, totalalkalinity, cya) VALUES(%s, %s, %s, %s, %s, %s)"
  mycursor.execute(sql, recordInput)
  mydb.commit()


def removeWeeklyReading():
  print("Enter a category to filter the weekly reading to be removed using the corresponding number:")
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

  print('')

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
  
  if filterBy > 0 and filterBy < 7: 
    escVal = False
    if(filterBy == 1):
      deleteID = week_ID
    else:
      print("Specify the record you wish to delete by its ID number.")
      deleteID = input()
    while escVal == False:
      print('Do you wish to remove this record? Type \'Y\' or \'N\'')
      deletionQuery = input()
      if(deletionQuery == 'Y'):
        sql = "DELETE FROM weekly_readings WHERE week_id = %s"
        val = (deleteID, )
        mycursor.execute(sql, val)
        mydb.commit()
        print("The record has been deleted!")
        escVal = True
      elif(deletionQuery == 'N'):
        print("The record deletion has been aborted!")
        escVal = True
      else:
        print(deletionQuery, " is not a valid answer.")
    print('')
    
  
def updateWeeklyReading():
  print("Enter a category to filter the weekly reading to be updated using the corresponding number:")
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

  print('')

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
  
  if filterBy > 0 and filterBy < 7: 
    escVal = False
    if(filterBy == 1):
      updateID = week_ID
    else:
      print("Specify the record you wish to update by its ID number.")
      updateID = input()
    while escVal == False:
      print('')
      print('Select the field you wish to update through its corresponding number.')
      print("[0] Exit   ")
      print("[1] Week ID          [2] Date               [3] Time")
      print("[4] Total Hardness   [5] Total Alkalinity   [6] Cyanuric Acid (CYA/stabilizer)")
      print("Action: ")
      updateFilter = int(input())
      match updateFilter:
        case 0:
          escVal = True
        case 1:
          print("What will you change the Week ID to?")
          newFieldVal = input()
          print("Are you sure you wish to change Week ID to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE weekly_readings SET week_id = %s WHERE week_id = %s"
            val = (newFieldVal, updateID)
            mycursor.execute(sql, val)
            mydb.commit()
            print("The record has been updated!")
            escVal = True
          elif(updateQuery == 'N'):
            print("The update has been aborted!")
            escVal = True
          else:
            print(updateQuery, " is not a valid answer.")
        case 2:
          print("What will you change the Date to?")
          newFieldVal = input()
          print("Are you sure you wish to change Date to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE weekly_readings SET date = %s WHERE week_id = %s"
            val = (newFieldVal, updateID)
            mycursor.execute(sql, val)
            mydb.commit()
            print("The record has been updated!")
            escVal = True
          elif(updateQuery == 'N'):
            print("The update has been aborted!")
            escVal = True
          else:
            print(updateQuery, " is not a valid answer.")
        case 3:
          print("What will you change the Time to?")
          newFieldVal = input()
          print("Are you sure you wish to change Time to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE weekly_readings SET lastname = %s WHERE week_id = %s"
            val = (newFieldVal, updateID)
            mycursor.execute(sql, val)
            mydb.commit()
            print("The record has been updated!")
            escVal = True
          elif(updateQuery == 'N'):
            print("The update has been aborted!")
            escVal = True
          else:
            print(updateQuery, " is not a valid answer.")
        case 4:
          print("What will you change the Total Hardness levels to?")
          newFieldVal = input()
          print("Are you sure you wish to change Total Hardness to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE weekly_readings SET totalhardness = %s WHERE week_id = %s"
            val = (newFieldVal, updateID)
            mycursor.execute(sql, val)
            mydb.commit()
            print("The record has been updated!")
            escVal = True
          elif(updateQuery == 'N'):
            print("The update has been aborted!")
            escVal = True
          else:
            print(updateQuery, " is not a valid answer.")
        case 5:
          print("What will you change the Total Alkalinity levels to?")
          newFieldVal = input()
          print("Are you sure you wish to change Total Alkalinity to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE weekly_readings SET totalalkalinity = %s WHERE week_id = %s"
            val = (newFieldVal, updateID)
            mycursor.execute(sql, val)
            mydb.commit()
            print("The record has been updated!")
            escVal = True
          elif(updateQuery == 'N'):
            print("The update has been aborted!")
            escVal = True
          else:
            print(updateQuery, " is not a valid answer.")
        case 6:
          print("What will you change the Cyanuric Acid (CYA/stabilizer) levels to?")
          newFieldVal = input()
          print("Are you sure you wish to change Cyanuric Acid (CYA/stabilizer) to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE weekly_readings SET cya = %s WHERE week_id = %s"
            val = (newFieldVal, updateID)
            mycursor.execute(sql, val)
            mydb.commit()
            print("The record has been updated!")
            escVal = True
          elif(updateQuery == 'N'):
            print("The update has been aborted!")
            escVal = True
          else:
            print(updateQuery, " is not a valid answer.")
        case _:
          print(updateFilter, " is not a valid parameter.")
    print('')
  
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

action = int(-1)

while action != 0:
  print("What would you like to do?")
  print("[1] Create a Weekly Reading account.")
  print("[2] Remove a Weekly Reading account.")
  print("[3] Update a Weekly Reading account.")
  print("[4] Display a Weekly Reading.")
  print("[0] Exit \n")

  print("Please input the corresponding number.")
  print("Action: ")
  
  action = int(input())
  print('')

  match action:
    case 1:
      addWeeklyReading()
    case 2:
      removeWeeklyReading()
    case 3:
      updateWeeklyReading()
    case 4:
      displayWeeklyReading()
    case 0:
      print("Goodbye!")
    case _:
      print("The number is out of bounds, so is invalid. Please pick a number between 0 and 4.")

