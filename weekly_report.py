import mysql.connector
from fpdf import FPDF

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Prof3SSi0nalPiupzzxk",
  database="mydatabase"
)

mycursor = mydb.cursor()

def generateWeeklyReport(date):
  sql = "SELECT time, totalhardness, totalalkalinity, cya FROM poolclub.weekly_readings WHERE date = %s"
  val = (date, )
  mycursor.execute(sql, val)
  myresult = mycursor.fetchall()

  title = "Weekly Readings"

  pdf = FPDF('P', 'mm', 'A4')
  pdf.add_page()
  pdf.set_font('Arial', 'B', 10)
  pdf.cell(0, 10, title, 0, 1, 'C')
  pdf.cell(40, 10, 'Date: ' + date, 0, 1)

  pdf.cell(35, 10, "Time", 1, 0, 'C')
  pdf.cell(35, 10, "Total Hardness", 1, 0, 'C')
  pdf.cell(35, 10, "Total Alkalinity", 1, 0, 'C')
  pdf.cell(35, 10, "CYA", 1, 1, 'C')

  for x in myresult:
      pdf.cell(35, 10, str(x[0]), 1, 0, 'C')
      pdf.cell(35, 10, str(x[1]), 1, 0, 'C')
      pdf.cell(35, 10, str(x[2]), 1, 0, 'C')
      pdf.cell(35, 10, str(x[3]), 1, 1, 'C')

  pdf.output(date + '_weeklyreport.pdf', 'F')