import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Prof3SSi0nalPiupzzxk",
  database="poolclub"
)

#print(mydb)

mycursor = mydb.cursor()

def addStaffMember():
  print("ID num: ")
  ID_num = input()
  print("First Name: ")
  firstName = input()
  print("Last Name: ")
  lastName = input()
  print("Hire Date: ")
  hireDate = input()
  print("Separation Date: ")
  separationDate = input()
  print("Reason for Separation: ")
  reasonForSeparation = input()
  print("Password: ")
  password = input()
  print("User Type: ")
  userType = input()

  recordInput = [ID_num, firstName, lastName, hireDate, separationDate, reasonForSeparation, password, userType]
  print('\n', recordInput, '\n')
  sql = "INSERT INTO staff(id_num, firstname, lastname, hiredate, separationdate, reasonforseparation, password, usertype) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
  mycursor.execute(sql, recordInput)
  mydb.commit()


def removeStaffMember():
  print("Enter a category to filter the staff who will be removed using the corresponding number:")
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

  print('')

  match filterBy:
    case 1:
      sql = "SELECT * FROM staff WHERE id_num = %s"
      val = (ID_num, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 2:
      sql = "SELECT * FROM staff WHERE firstname = %s"
      val = (firstName, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 3:
      sql = "SELECT * FROM staff WHERE lastname = %s"
      val = (lastName, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 4:
      sql = "SELECT * FROM staff WHERE hiredate = %s"
      val = (hireDate, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 5:
      sql = "SELECT * FROM staff WHERE separationdate = %s"
      val = (separationDate, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 6:
      sql = "SELECT * FROM staff WHERE reasonforseparation = %s"
      val = (reasonForSeparation, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 7:
      sql = "SELECT * FROM staff WHERE password = %s"
      val = (password, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 8:
      sql = "SELECT * FROM staff WHERE usertype = %s"
      val = (userType, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case _:
      dummy = None
  
  if filterBy > 0 and filterBy < 9: 
    escVal = False
    if(filterBy == 1):
      deleteID = ID_num
    else:
      print("Specify the record you wish to delete by its ID number.")
      deleteID = input()
    while escVal == False:
      print('Do you wish to remove this record? Type \'Y\' or \'N\'')
      deletionQuery = input()
      if(deletionQuery == 'Y'):
        sql = "DELETE FROM staff WHERE id_num = %s"
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
    
  
def updateStaffMember():
  print("Updating staff member…\n")
  print("Enter a category to filter the staff who will be updated using the corresponding number:")
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

  print('')

  match filterBy:
    case 1:
      sql = "SELECT * FROM staff WHERE id_num = %s"
      val = (ID_num, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 2:
      sql = "SELECT * FROM staff WHERE firstname = %s"
      val = (firstName, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 3:
      sql = "SELECT * FROM staff WHERE lastname = %s"
      val = (lastName, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 4:
      sql = "SELECT * FROM staff WHERE hiredate = %s"
      val = (hireDate, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 5:
      sql = "SELECT * FROM staff WHERE separationdate = %s"
      val = (separationDate, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 6:
      sql = "SELECT * FROM staff WHERE reasonforseparation = %s"
      val = (reasonForSeparation, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 7:
      sql = "SELECT * FROM staff WHERE password = %s"
      val = (password, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case 8:
      sql = "SELECT * FROM staff WHERE usertype = %s"
      val = (userType, )
      mycursor.execute(sql, val)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case _:
      dummy = None
  
  if filterBy > 0 and filterBy < 9: 
    escVal = False
    if(filterBy == 1):
      updateID = ID_num
    else:
      print("Specify the record you wish to update by its ID number.")
      updateID = input()
    while escVal == False:
      print('')
      print('Select the field you wish to update through its corresponding number.')
      print("[0] Exit                    [1] ID num      [2] First Name")
      print("[3] Last Name               [4] Hire Date   [5] Separation Date")
      print("[6] Reason for Separation   [7] Password    [8] User Type")
      print("Action: ")
      updateFilter = int(input())
      match updateFilter:
        case 0:
          escVal = True
        case 1:
          print("What will you change the ID num to?")
          newFieldVal = input()
          print("Are you sure you wish to change ID num to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE staff SET id_num = %s WHERE id_num = %s"
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
          print("What will you change the First Name to?")
          newFieldVal = input()
          print("Are you sure you wish to change First Name to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE staff SET firstname = %s WHERE id_num = %s"
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
          print("What will you change the Last Name to?")
          newFieldVal = input()
          print("Are you sure you wish to change Last Name to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE staff SET lastname = %s WHERE id_num = %s"
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
          print("What will you change the Hire Date to?")
          newFieldVal = input()
          print("Are you sure you wish to change Hire Date to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE staff SET hiredate = %s WHERE id_num = %s"
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
          print("What will you change the Separation Date to?")
          newFieldVal = input()
          print("Are you sure you wish to change Separation Date to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE staff SET separationdate = %s WHERE id_num = %s"
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
          print("What will you change the Reason for Separation to?")
          newFieldVal = input()
          print("Are you sure you wish to change Reason for Separation to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE staff SET reasonforseparation = %s WHERE id_num = %s"
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
        case 7:
          print("What will you change the Password to?")
          newFieldVal = input()
          print("Are you sure you wish to change Password to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE staff SET password = %s WHERE id_num = %s"
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
        case 8:
          print("What will you change the User Type to?")
          newFieldVal = input()
          print("Are you sure you wish to change User Type to \'", newFieldVal, "\'? Type \'Y\' or \'N\'" )
          updateQuery = input()
          if (updateQuery == 'Y'):
            sql = "UPDATE staff SET usertype = %s WHERE id_num = %s"
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
  
def displayStaffMember():
  print("Enter a category to filter for staff to display using the corresponding number:")
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

""" action = int(-1)

while action != 0:
  print("What would you like to do?")
  print("[1] Create a Staff Member account.")
  print("[2] Remove a Staff Member account.")
  print("[3] Update a Staff Member account.")
  print("[4] Display a Staff Member account.")
  print("[0] Exit \n")

  print("Please input the corresponding number.")
  print("Action: ")
  
  action = int(input())
  print('')

  match action:
    case 1:
      addStaffMember()
    case 2:
      removeStaffMember()
    case 3:
      updateStaffMember()
    case 4:
      displayStaffMember()
    case 0:
      print("Goodbye!")
    case _:
      print("The number is out of bounds, so is invalid. Please pick a number between 0 and 4.") """

