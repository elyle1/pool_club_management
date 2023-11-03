import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Prof3SSi0nalPiupzzxk",
  database="poolclub"
)

#print(mydb)

mycursor = mydb.cursor()

def addMaintenanceTask():
  print("ID Number (for task): ")
  itemNumber = input()
  print("Date: ")
  date = input()
  print("Task: ")
  task = input()
  print("Staff Representative: ")
  staffRep = input()
  print("Status of Task: ")
  status = input()
  
  recordInput = [itemNumber, date, task, staffRep, status]
  print('\n', recordInput, '\n')
  sql = "INSERT INTO maintenance(itemnumber, date, task, staffrep., status) VALUES(%s, %s, %s, %s, %s)"
  mycursor.execute(sql, recordInput)
  mydb.commit()


def removeMaintenanceTask():
  print("Enter a category to filter the maintenance task to be removed using the corresponding number:")
  print("[0] Exit   ")
  print("[1] Item Number             [2] Date             [3] Task")
  print("[4] Staff Representative    [5] Status of Task")

  print("Action: ")
  filterBy = int(input())

  match filterBy:
    case 0:
      dummy = None
    case 1:
      print("Enter the Item Number (ID) value.")
      itemNumber = input()      
    case 2:
      print("Enter the Date value.")
      date = input()      
    case 3:
      print("Enter the Task value.")
      task = input()      
    case 4:
      print("Enter the Staff Representative value.")
      staffRep = input()      
    case 5:
      print("Enter the Status value.")
      status = input()      
    case _:
      print("This is not a valid parameter.")

  print('')

  match filterBy:
    case 1:
      sql = "SELECT * FROM maintenance WHERE itemnumber = %s"
      val = (itemNumber, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 2:
      sql = "SELECT * FROM maintenance WHERE date = %s"
      val = (date, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 3:
      sql = "SELECT * FROM maintenance WHERE task = %s"
      val = (task, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 4:
      sql = "SELECT * FROM maintenance WHERE staffrep. = %s"
      val = (staffRep, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 5:
      sql = "SELECT * FROM maintenance WHERE status = %s"
      val = (status, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case _:
      dummy = None
  
  if filterBy > 0 and filterBy < 6: 
    escVal = False
    if(filterBy == 1):
      deleteID = itemNumber
    else:
      print("Specify the record you wish to delete by its ID number.")
      deleteID = input()
    while escVal == False:
      print('Do you wish to remove this record? Type \'Y\' or \'N\'')
      deletionQuery = input()
      if(deletionQuery == 'Y'):
        sql = "DELETE FROM maintenance WHERE itemnumber = %s"
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
    
  
def updateMaintenanceTask():
  print("Enter a category to filter the maintenance task to be updated using the corresponding number:")
  print("[0] Exit   ")
  print("[1] Item Number             [2] Date             [3] Task")
  print("[4] Staff Representative    [5] Status of Task")
  print("Action: ")
  filterBy = int(input())

  match filterBy:
    case 0:
      dummy = None
    case 1:
      print("Enter the Item Number (ID) value.")
      itemNumber = input()      
    case 2:
      print("Enter the Date value.")
      date = input()      
    case 3:
      print("Enter the Task value.")
      task = input()      
    case 4:
      print("Enter the Staff Representative value.")
      staffRep = input()      
    case 5:
      print("Enter the Status value.")
      status = input()      
    case _:
      print("This is not a valid parameter.")

  print('')

  match filterBy:
    case 1:
      sql = "SELECT * FROM maintenance WHERE itemnumber = %s"
      val = (itemNumber, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 2:
      sql = "SELECT * FROM maintenance WHERE date = %s"
      val = (date, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 3:
      sql = "SELECT * FROM maintenance WHERE task = %s"
      val = (task, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 4:
      sql = "SELECT * FROM maintenance WHERE staffrep. = %s"
      val = (staffRep, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 5:
      sql = "SELECT * FROM maintenance WHERE status = %s"
      val = (status, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case _:
      dummy = None
  
  if filterBy > 0 and filterBy < 6: 
    escVal = False
    if(filterBy == 1):
      updateID = itemNumber
    else:
      print("Specify the record you wish to update by its ID number.")
      updateID = input()
    while escVal == False:
      print('')
      print('Select the field you wish to update through its corresponding number.')
      print("[0] Exit   ")
      print("[1] Item Number             [2] Date             [3] Task")
      print("[4] Staff Representative    [5] Status of Task")
      print("Action: ")
      updateFilter = int(input())
      match updateFilter:
        case 0:
          escVal = True
        case 1:
          print("What will you change the Item Number to?")
          newFieldVal = input()
          print("Are you sure you wish to change Item Number to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE maintenance SET itemnumber = %s WHERE itemnumber = %s"
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
            sql = "UPDATE maintenance SET date = %s WHERE itemnumber = %s"
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
          print("What will you change the Task value to?")
          newFieldVal = input()
          print("Are you sure you wish to change Task to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE maintenance SET task = %s WHERE itemnumber = %s"
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
          print("Who will you change the Staff Representative to?")
          newFieldVal = input()
          print("Are you sure you wish to change Staff Representative to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE maintenance SET staffrep. = %s WHERE itemnumber = %s"
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
          print("What will you change the Status value to?")
          newFieldVal = input()
          print("Are you sure you wish to change Status to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE maintenance SET status = %s WHERE itemnumber = %s"
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
  
def displayMaintenanceTask():
  print("Enter a category to filter the maintenance tasks displayed using the corresponding number:")
  print("[0] Exit   ")
  print("[1] Schedule ID             [2] Date        [3] Shift")
  print("[4] Manager/Pool Operator   [5] Lifeguard   [6] Admin")
  print("Action: ")
  filterBy = int(input())

  print("[0] Exit   ")
  print("[1] Item Number             [2] Date             [3] Task")
  print("[4] Staff Representative    [5] Status of Task")
  print("Action: ")
  filterBy = int(input())

  match filterBy:
    case 0:
      dummy = None
    case 1:
      print("Enter the Item Number (ID) value.")
      itemNumber = input()      
    case 2:
      print("Enter the Date value.")
      date = input()      
    case 3:
      print("Enter the Task value.")
      task = input()      
    case 4:
      print("Enter the Staff Representative value.")
      staffRep = input()      
    case 5:
      print("Enter the Status value.")
      status = input()      
    case _:
      print("This is not a valid parameter.")

  print('\nBelow is a list based on your specification: \n')

  match filterBy:
    case 1:
      sql = "SELECT * FROM maintenance WHERE itemnumber = %s"
      val = (itemNumber, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 2:
      sql = "SELECT * FROM maintenance WHERE date = %s"
      val = (date, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 3:
      sql = "SELECT * FROM maintenance WHERE task = %s"
      val = (task, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 4:
      sql = "SELECT * FROM maintenance WHERE staffrep. = %s"
      val = (staffRep, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 5:
      sql = "SELECT * FROM maintenance WHERE status = %s"
      val = (status, )
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
  print("[1] Create a maintenance task.")
  print("[2] Remove a maintenance task.")
  print("[3] Update a maintenance task.")
  print("[4] Display a maintenance task.")
  print("[0] Exit \n")

  print("Please input the corresponding number.")
  print("Action: ")
  
  action = int(input())
  print('')

  match action:
    case 1:
      addMaintenanceTask()
    case 2:
      removeMaintenanceTask()
    case 3:
      updateMaintenanceTask()
    case 4:
      displayMaintenanceTask()
    case 0:
      print("Goodbye!")
    case _:
      print("The number is out of bounds, so is invalid. Please pick a number between 0 and 4.")

