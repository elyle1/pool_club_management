import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Prof3SSi0nalPiupzzxk",
  database="poolclub"
)

#print(mydb)

mycursor = mydb.cursor()

def addScheduledTask(inputs):
  recordInput = inputs
  sql = "INSERT INTO schedule(sched_id, date, shift, manager_pooloperator, lifeguard, admin) VALUES(%s, %s, %s, %s, %s, %s)"
  mycursor.execute(sql, recordInput)
  mydb.commit()


def removeScheduledTask(inputs):
  recordInput = inputs
  sql = "DELETE FROM schedule WHERE sched_id = %s"
  val = (recordInput[0], )
  mycursor.execute(sql, val)
  mydb.commit()
    
  
def updateScheduledTask(inputs):
  recordInput = inputs
  sql = "UPDATE schedule SET date = %s, shift = %s, manager_pooloperator = %s, lifeguard = %s, admin = %s WHERE sched_id = %s"
  val = (recordInput[1], recordInput[2], recordInput[3], recordInput[4], recordInput[5], recordInput[0])
  mycursor.execute(sql, val)
  mydb.commit()
  
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


