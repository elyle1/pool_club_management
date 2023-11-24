import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Prof3SSi0nalPiupzzxk",
  database="poolclub"
)

mycursor = mydb.cursor()

def addPoolChemical(inputs):
  recordInput = inputs
  sql = "INSERT INTO pool_chemical_supply(chem_id, chemicalname, amountpurchased, datepurchased, amountused, dateused, amountonhand) VALUES(%s, %s, %s, %s, %s, %s, %s)"
  mycursor.execute(sql, recordInput)
  mydb.commit()


def removePoolChemical(inputs):
  recordInput = inputs
  sql = "DELETE FROM pool_chemical_supply WHERE chem_id = %s"
  val = (recordInput[0], )
  mycursor.execute(sql, val)
  mydb.commit()
    
  
def updatePoolChemical(inputs):
  recordInput = inputs
  sql = "UPDATE pool_chemical_supply SET chemicalname = %s, amountpurchased = %s, datepurchased = %s, amountused = %s, dateused = %s, amountonhand = %s WHERE chem_id = %s"
  val = (recordInput[1], recordInput[2], recordInput[3], recordInput[4], recordInput[5], recordInput[6], recordInput[0])
  mycursor.execute(sql, val)
  mydb.commit()