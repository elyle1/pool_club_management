from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import weekly_report

def display():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Prof3SSi0nalPiupzzxk",
    database="poolclub"
  )

  def reportDateButton():
      reportDate_str = reportDate_entry.get()
      print(reportDate_str)

  root = Tk()
  label = ttk.Label(root, text = "Hello, tkinter!")
  label.pack()
  mycursor = mydb.cursor()

  root.title('Explore California Feedback')
  root.resizable(True, True)
  root.configure(background = '#e1d8b9')

  style = ttk.Style()
  style.configure('TFrame', background = '#e1d8b9')
  style.configure('TButton', background = '#e1d8b9')
  style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
  style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))

  frame_header = ttk.Frame(root)
  frame_header.pack()

  pandedwindow = ttk.PanedWindow(root, orient = HORIZONTAL)
  pandedwindow.pack(fill = BOTH, expand = True)
  frame1 = ttk.Frame(pandedwindow, width = 450, height = 600, relief = SUNKEN)

  dateframe = Frame()
  dateframe.pack(fill="x", expand="yes", pady=10)

  genReport_button = ttk.Button(dateframe, text="Generate Report", command=reportDateButton)
  genReport_button.grid(row=0, column=0, padx=10, pady=10)

  reportDate_entry = Entry(dateframe)
  reportDate_entry.grid(row=0, column=1, padx=10, pady=10)

  treeframe = LabelFrame(root, text="Weekly Report Preview")
  treeframe.pack(pady = 10)

  scrollbar = ttk.Scrollbar(treeframe)
  scrollbar.pack(side=RIGHT, fill=Y)

  wReport_tree = ttk.Treeview(treeframe, yscrollcommand=scrollbar.set, selectmode='extended')
  wReport_tree.pack()

  wReport_tree['columns'] = ("Preview")
  wReport_tree.column("#0", width=0, stretch=NO)
  wReport_tree.column("Preview", anchor=W, width=690)

  scrollbar.config(command=wReport_tree.yview)

  button_frame = LabelFrame(root, text="Actions")
  button_frame.pack(fill="x", expand="yes", pady=10)

  download_button = ttk.Button(button_frame, text="Download")
  download_button.grid(row=0, column=0, padx=10, pady=10)

  print_button = ttk.Button(button_frame, text="Print")
  print_button.grid(row=0, column=1, padx=10, pady=10)

  root.mainloop()