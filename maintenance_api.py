import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Prof3SSi0nalPiupzzxk",
  database="poolclub"
)

#print(mydb)

mycursor = mydb.cursor()

def addMaintenanceTask(inputs):
  recordInput = inputs
  sql = "INSERT INTO maintenance(itemnumber, date, task, staffrep, status) VALUES(%s, %s, %s, %s, %s)"
  mycursor.execute(sql, recordInput)
  mydb.commit()


def removeMaintenanceTask(inputs):
  recordInput = inputs
  sql = "DELETE FROM maintenance WHERE itemnumber = %s"
  val = (recordInput[0], )
  mycursor.execute(sql, val)
  mydb.commit()
    
  
def updateMaintenanceTask(inputs):
  recordInput = inputs
  sql = "UPDATE maintenance SET date = %s, task = %s, staffrep = %s, status = %s WHERE itemnumber = %s"
  val = (recordInput[1], recordInput[2], recordInput[3], recordInput[4], recordInput[0])
  mycursor.execute(sql, val)
  mydb.commit()
  
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

""" action = int(-1)

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
      print("The number is out of bounds, so is invalid. Please pick a number between 0 and 4.") """

