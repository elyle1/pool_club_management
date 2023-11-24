import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Prof3SSi0nalPiupzzxk",
  database="poolclub"
)

#print(mydb)

mycursor = mydb.cursor()

def addScheduledTask():
  print("Schedule ID (for task):")
  sched_ID = input()
  print("Date: ")
  date = input()
  print("Shift: ")
  shift = input()
  print("Manager/Pool Operator: ")
  manager_poolOperator = input()
  print("Lifeguard: ")
  lifeguard = input()
  print("Admin: ")
  admin = input()

  recordInput = [sched_ID, date, shift, manager_poolOperator, lifeguard, admin]
  print('\n', recordInput, '\n')
  sql = "INSERT INTO schedule(sched_id, date, shift, manager_pooloperator, lifeguard, admin) VALUES(%s, %s, %s, %s, %s, %s)"
  mycursor.execute(sql, recordInput)
  mydb.commit()


def removeScheduledTask():
  print("Enter a category to filter the scheduled task to be removed using the corresponding number:")
  print("[0] Exit   ")
  print("[1] Schedule ID             [2] Date        [3] Shift")
  print("[4] Manager/Pool Operator   [5] Lifeguard   [6] Admin")
  print("Action: ")
  filterBy = int(input())

  match filterBy:
    case 0:
      dummy = None
    case 1:
      print("Enter the Schedule ID value.")
      sched_ID = input()      
    case 2:
      print("Enter the Date value.")
      date = input()      
    case 3:
      print("Enter the Shift value.")
      shift = input()      
    case 4:
      print("Enter the Manager/PoolOperator value.")
      manager_poolOperator = input()      
    case 5:
      print("Enter the Lifeguard value.")
      lifeguard = input()      
    case 6:
      print("Enter the Admin value.")
      admin = input()      
    case _:
      print("This is not a valid parameter.")

  print('')

  match filterBy:
    case 1:
      sql = "SELECT * FROM schedule WHERE sched_id = %s"
      val = (sched_ID, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 2:
      sql = "SELECT * FROM schedule WHERE date = %s"
      val = (date, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 3:
      sql = "SELECT * FROM schedule WHERE shift = %s"
      val = (shift, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 4:
      sql = "SELECT * FROM schedule WHERE manager_pooloperator = %s"
      val = (manager_poolOperator, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 5:
      sql = "SELECT * FROM schedule WHERE lifeguard = %s"
      val = (lifeguard, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 6:
      sql = "SELECT * FROM schedule WHERE admin = %s"
      val = (admin, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case _:
      dummy = None
  
  if filterBy > 0 and filterBy < 7: 
    escVal = False
    if(filterBy == 1):
      deleteID = sched_ID
    else:
      print("Specify the record you wish to delete by its ID number.")
      deleteID = input()
    while escVal == False:
      print('Do you wish to remove this record? Type \'Y\' or \'N\'')
      deletionQuery = input()
      if(deletionQuery == 'Y'):
        sql = "DELETE FROM schedule WHERE sched_id = %s"
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
    
  
def updateScheduledTask():
  print("Enter a category to filter the scheduled task to be updated using the corresponding number:")
  print("[0] Exit   ")
  print("[1] Schedule ID             [2] Date        [3] Shift")
  print("[4] Manager/Pool Operator   [5] Lifeguard   [6] Admin")
  print("Action: ")
  filterBy = int(input())

  match filterBy:
    case 0:
      dummy = None
    case 1:
      print("Enter the Schedule ID value.")
      sched_ID = input()      
    case 2:
      print("Enter the Date value.")
      date = input()      
    case 3:
      print("Enter the Shift value.")
      shift = input()      
    case 4:
      print("Enter the Manager/PoolOperator value.")
      manager_poolOperator = input()      
    case 5:
      print("Enter the Lifeguard value.")
      lifeguard = input()      
    case 6:
      print("Enter the Admin value.")
      admin = input()      
    case _:
      print("This is not a valid parameter.")

  print('')

  match filterBy:
    case 1:
      sql = "SELECT * FROM schedule WHERE sched_id = %s"
      val = (sched_ID, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 2:
      sql = "SELECT * FROM schedule WHERE date = %s"
      val = (date, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 3:
      sql = "SELECT * FROM schedule WHERE shift = %s"
      val = (shift, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 4:
      sql = "SELECT * FROM schedule WHERE manager_pooloperator = %s"
      val = (manager_poolOperator, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 5:
      sql = "SELECT * FROM schedule WHERE lifeguard = %s"
      val = (lifeguard, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 6:
      sql = "SELECT * FROM schedule WHERE admin = %s"
      val = (admin, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case _:
      dummy = None
  
  if filterBy > 0 and filterBy < 7: 
    escVal = False
    if(filterBy == 1):
      updateID = sched_ID
    else:
      print("Specify the record you wish to update by its ID number.")
      updateID = input()
    while escVal == False:
      print('')
      print('Select the field you wish to update through its corresponding number.')
      print("[0] Exit   ")
      print("[1] Schedule ID             [2] Date        [3] Shift")
      print("[4] Manager/Pool Operator   [5] Lifeguard   [6] Admin")
      print("Action: ")
      updateFilter = int(input())
      match updateFilter:
        case 0:
          escVal = True
        case 1:
          print("What will you change the Schedule ID to?")
          newFieldVal = input()
          print("Are you sure you wish to change Schedule ID to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE schedule SET sched_id = %s WHERE sched_id = %s"
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
            sql = "UPDATE schedule SET date = %s WHERE sched_id = %s"
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
          print("What will you change the Shift value to?")
          newFieldVal = input()
          print("Are you sure you wish to change Shift to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE schedule SET shift = %s WHERE sched_id = %s"
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
          print("Who will you change the Manager/Pool Operator to?")
          newFieldVal = input()
          print("Are you sure you wish to change Manager/Pool Operator to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE schedule SET manager_pooloperator = %s WHERE sched_id = %s"
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
          print("Who will you change the Lifeguard to?")
          newFieldVal = input()
          print("Are you sure you wish to change Lifeguard to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE schedule SET lifeguard = %s WHERE sched_id = %s"
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
          print("Who will you change the Admin to?")
          newFieldVal = input()
          print("Are you sure you wish to change Admin to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE schedule SET admin = %s WHERE sched_id = %s"
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
  
def displayScheduledTask():
  print("Enter a category to filter the scheduled tasks displayed using the corresponding number:")
  print("[0] Exit   ")
  print("[1] Schedule ID             [2] Date        [3] Shift")
  print("[4] Manager/Pool Operator   [5] Lifeguard   [6] Admin")
  print("Action: ")
  filterBy = int(input())

  match filterBy:
    case 0:
      dummy = None
    case 1:
      print("Enter the Schedule ID value.")
      sched_ID = input()      
    case 2:
      print("Enter the Date value.")
      date = input()      
    case 3:
      print("Enter the Shift value.")
      shift = input()      
    case 4:
      print("Enter the Manager/PoolOperator value.")
      manager_poolOperator = input()      
    case 5:
      print("Enter the Lifeguard value.")
      lifeguard = input()      
    case 6:
      print("Enter the Admin value.")
      admin = input()      
    case _:
      print("This is not a valid parameter.")

  print('\nBelow is a list based on your specification: \n')

  match filterBy:
    case 1:
      sql = "SELECT * FROM schedule WHERE sched_id = %s"
      val = (sched_ID, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 2:
      sql = "SELECT * FROM schedule WHERE date = %s"
      val = (date, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 3:
      sql = "SELECT * FROM schedule WHERE shift = %s"
      val = (shift, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 4:
      sql = "SELECT * FROM schedule WHERE manager_pooloperator = %s"
      val = (manager_poolOperator, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 5:
      sql = "SELECT * FROM schedule WHERE lifeguard = %s"
      val = (lifeguard, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 6:
      sql = "SELECT * FROM schedule WHERE admin = %s"
      val = (admin, )
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
  print("[1] Create a scheduled task.")
  print("[2] Remove a scheduled task.")
  print("[3] Update a scheduled task.")
  print("[4] Display a scheduled task.")
  print("[0] Exit \n")

  print("Please input the corresponding number.")
  print("Action: ")
  
  action = int(input())
  print('')

  match action:
    case 1:
      addScheduledTask()
    case 2:
      removeScheduledTask()
    case 3:
      updateScheduledTask()
    case 4:
      displayScheduledTask()
    case 0:
      print("Goodbye!")
    case _:
      print("The number is out of bounds, so is invalid. Please pick a number between 0 and 4.")

