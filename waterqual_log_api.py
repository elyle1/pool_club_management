import mysql.connector
from fpdf import FPDF

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Prof3SSi0nalPiupzzxk",
  database="mydatabase"
)

#print(mydb)

mycursor = mydb.cursor()

title = "Daily Readings"

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('python_logo.gif', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Line break
        self.ln(10)
    
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')
    
    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)
    
    def chapter_body(self, name):
        # Read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 5, '(end of excerpt)')
    
    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)

date = '2003-03-06'

print("Date: ", date, '\n')

sql = "SELECT date, time, ph, totalchlorine, freechlorine, combinedchlorine FROM daily_readings WHERE date = %s"
val = (date, )
mycursor.execute(sql, val)
myresult = mycursor.fetchall()



print("Under construction… \n")

print("Weekly Readings")
sql = "SELECT date, time, ph, totalhardness, totalalkalinity, cya FROM weekly_readings WHERE date = %s"
val = (date, )
mycursor.execute(sql, val)
myresult = mycursor.fetchall()

print("Tasks Complete")
print("Under construction… \n")

print("Manager's Approval")

