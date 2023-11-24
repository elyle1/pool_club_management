import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Prof3SSi0nalPiupzzxk",
  database="poolclub"
)

#print(mydb)

mycursor = mydb.cursor()

def addDailyReading():
  print("Day ID: ")
  day_ID = input()
  print("Date: ")
  date = input()
  print("Time: ")
  time = input()
  print("pH (in parts per million/ppm): ")
  pH = input()
  print("Total Chlorine (in parts per million/ppm): ")
  totalChlorine = float(input())
  print("Free Chlorine (in parts per million/ppm): ")
  freeChlorine = float(input())
  combinedChlorine = totalChlorine - freeChlorine

  recordInput = [day_ID, date, time, pH, totalChlorine, freeChlorine, combinedChlorine]
  print('\n', recordInput, '\n')
  sql = "INSERT INTO daily_readings(day_id, date, time, ph, totalchlorine, freechlorine, combinedchlorine) VALUES(%s, %s, %s, %s, %s, %s, %s)"
  mycursor.execute(sql, recordInput)
  mydb.commit()


def removeDailyReading():
  print("Enter a category to filter the daily readings to be removed using the corresponding number:")
  print("[0] Exit   [1] Day ID   [2] Date")
  print("[3] Time   [4] pH       [5] Total Chlorine")
  print("[6] Free Chlorine       [7] Combined Chlorine")
  print("Action: ")
  filterBy = int(input())

  match filterBy:
    case 0:
      dummy = None
    case 1:
      print("Enter the Day ID value.")
      day_ID = input()      
    case 2:
      print("Enter the Date value.")
      date = input()      
    case 3:
      print("Enter the Time value.")
      time = input()      
    case 4:
      print("Enter the pH value (in parts per million/ppm).")
      pH = input()      
    case 5:
      print("Enter the Total Chlorine value (in parts per million/ppm).")
      totalChlorine = input()      
    case 6:
      print("Enter the Free Chlorine value (in parts per million/ppm).")
      freeChlorine = input()      
    case 7:
      print("Enter the Combined Chlorine value (in parts per million/ppm)")
      combinedChlorine = input()
    case _:
      print("This is not a valid parameter.")

  print('')

  match filterBy:
    case 1:
      sql = "SELECT * FROM daily_readings WHERE day_id = %s"
      val = (day_ID, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 2:
      sql = "SELECT * FROM daily_readings WHERE date = %s"
      val = (date, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 3:
      sql = "SELECT * FROM daily_readings WHERE time = %s"
      val = (time, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 4:
      sql = "SELECT * FROM daily_readings WHERE ph = %s"
      val = (pH, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 5:
      sql = "SELECT * FROM daily_readings WHERE totalchlorine = %s"
      val = (totalChlorine, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 6:
      sql = "SELECT * FROM daily_readings WHERE freechlorine = %s"
      val = (freeChlorine, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 7:
      sql = "SELECT * FROM daily_readings WHERE combinedchlorine = %s"
      val = (combinedChlorine, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case _:
      dummy = None
  
  if filterBy > 0 and filterBy < 8: 
    escVal = False
    if(filterBy == 1):
      deleteID = day_ID
    else:
      print("Specify the record you wish to delete by its ID number.")
      deleteID = input()
    while escVal == False:
      print('Do you wish to remove this record? Type \'Y\' or \'N\'')
      deletionQuery = input()
      if(deletionQuery == 'Y'):
        sql = "DELETE FROM daily_readings WHERE day_id = %s"
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
    
  
def updateDailyReading():
  print("Enter a category to filter the daily readings to be updated using the corresponding number:")
  print("[0] Exit   [1] Day ID")
  print("[2] Date   [3] Time")
  print("[4] pH     [5] Total Chlorine   [6] Free Chlorine")
  print("Action: ")
  filterBy = int(input())

  match filterBy:
    case 0:
      dummy = None
    case 1:
      print("Enter the Day ID value.")
      day_ID = input()      
    case 2:
      print("Enter the Date value.")
      date = input()      
    case 3:
      print("Enter the Time value.")
      time = input()      
    case 4:
      print("Enter the pH value (in parts per million/ppm).")
      pH = input()      
    case 5:
      print("Enter the Total Chlorine value (in parts per million/ppm).")
      totalChlorine = input()      
    case 6:
      print("Enter the Free Chlorine value (in parts per million/ppm).")
      freeChlorine = input()      
    case 7:
      print("Enter the Combined Chlorine value (in parts per million/ppm)")
      combinedChlorine = input()      
    case _:
      print("This is not a valid parameter.")

  print('')

  match filterBy:
    case 1:
      sql = "SELECT * FROM daily_readings WHERE day_id = %s"
      val = (day_ID, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 2:
      sql = "SELECT * FROM daily_readings WHERE date = %s"
      val = (date, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 3:
      sql = "SELECT * FROM daily_readings WHERE time = %s"
      val = (time, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 4:
      sql = "SELECT * FROM daily_readings WHERE ph = %s"
      val = (pH, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 5:
      sql = "SELECT * FROM daily_readings WHERE totalchlorine = %s"
      val = (totalChlorine, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 6:
      sql = "SELECT * FROM daily_readings WHERE freechlorine = %s"
      val = (freeChlorine, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 7:
      sql = "SELECT * FROM daily_readings WHERE combinedchlorine = %s"
      val = (combinedChlorine, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case _:
      dummy = None
  
  if filterBy > 0 and filterBy < 8: 
    escVal = False
    if(filterBy == 1):
      updateID = day_ID
    else:
      print("Specify the record you wish to update by its ID number.")
      updateID = input()
    while escVal == False:
      print('')
      print('Select the field you wish to update through its corresponding number.')
      print("Enter a category to filter the daily readings to be removed using the corresponding number:")
      print("[0] Exit   [1] Day ID   [2] Date")
      print("[3] Time   [4] pH       [5] Total Chlorine")
      print("[6] Free Chlorine")
      print("Action: ")
      updateFilter = int(input())
      match updateFilter:
        case 0:
          escVal = True
        case 1:
          print("What will you change the ID num to?")
          newFieldVal = input()
          print("Are you sure you wish to change Day ID to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE daily_readings SET day_id = %s WHERE day_id = %s"
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
            sql = "UPDATE daily_readings SET date = %s WHERE day_id = %s"
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
            sql = "UPDATE daily_readings SET time = %s WHERE day_id = %s"
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
          print("What will you change the pH to?")
          newFieldVal = input()
          print("Are you sure you wish to change pH to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE daily_readings SET ph = %s WHERE day_id = %s"
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
          print("What will you change the Total Chlorine to?")
          newFieldVal = input()
          print("Are you sure you wish to change Total Chlorine to \'", newFieldVal, "\'? It will also change your Combined Chlorine value. \nType \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE daily_readings SET totalchlorine = %s WHERE day_id = %s"
            val = (newFieldVal, updateID)
            mycursor.execute(sql, val)
            mydb.commit()

            sql = "SELECT freechlorine FROM daily_readings WHERE day_id = %s"
            val = (updateID, )
            mycursor.execute(sql, val)
            myresult = mycursor.fetchall()
            for x in myresult:
                freeChlorine = x[0]
            
            combinedChlorine = newFieldVal - freeChlorine
            sql = "UPDATE daily_readings SET combinedchlorine = %s WHERE day_id = %s"
            val = (combinedChlorine, updateID)
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
          print("What will you change the Free Chlorine to?")
          newFieldVal = input()
          print("Are you sure you wish to change Free Chlorine to \'", newFieldVal, "\'? It will also change your Combined Chlorine value. \nType \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE daily_readings SET freechlorine = %s WHERE day_id = %s"
            val = (newFieldVal, updateID)
            mycursor.execute(sql, val)
            mydb.commit()

            sql = "SELECT totalchlorine FROM daily_readings WHERE day_id = %s"
            val = (updateID, )
            mycursor.execute(sql, val)
            myresult = mycursor.fetchall()
            for x in myresult:
                totalChlorine = x[0]
            
            combinedChlorine = totalChlorine - newFieldVal
            sql = "UPDATE daily_readings SET combinedchlorine = %s WHERE day_id = %s"
            val = (combinedChlorine, updateID)
            mycursor.execute(sql, val)
            mydb.commit()
            print("The record has been updated!")
            escVal = True
          elif(updateQuery == 'N'):
            print("The update has been aborted!")
            escVal = True
          else:
            print(updateQuery, " is not a valid answer.")
    print('')

def chlorineUpdate():
  print("Placeholder")

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

action = int(-1)

while action != 0:
  print("What would you like to do?")
  print("[1] Create a Daily Reading record.")
  print("[2] Remove a Daily Reading record.")
  print("[3] Update a Daily Reading record.")
  print("[4] Display a Daily Reading record.")
  print("[0] Exit \n")

  print("Please input the corresponding number.")
  print("Action: ")
  
  action = int(input())
  print('')

  match action:
    case 1:
      addDailyReading()
    case 2:
      removeDailyReading()
    case 3:
      updateDailyReading()
    case 4:
      displayDailyReading()
    case 0:
      print("Goodbye!")
    case _:
      print("The number is out of bounds, so is invalid. Please pick a number between 0 and 4.")

