from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import day_read_api
import daily_report

def display():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Prof3SSi0nalPiupzzxk",
    database="poolclub"
    )

    def clear_entries():
        id_entry.delete(0, END)
        d_entry.delete(0, END)
        t_entry.delete(0, END)
        ph_entry.delete(0, END)
        tChl_entry.delete(0, END)
        fChl_entry.delete(0, END)
        cChl_entry.delete(0, END)

    def select_record(e):
        clear_entries()
        selected = daily_tree.focus()
        values = daily_tree.item(selected, 'values')
        id_entry.insert(0, values[0])
        d_entry.insert(0, values[1])
        t_entry.insert(0, values[2])
        ph_entry.insert(0, values[3])
        tChl_entry.insert(0, values[4])
        fChl_entry.insert(0, values[5])
        cChl_entry.insert(0, values[6])

    def generateTree():
        daily_tree.delete(*daily_tree.get_children())
        sql = "SELECT * FROM poolclub.daily_readings"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        for x in myresult:
            daily_tree.insert(parent='', index='end', text='', values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6]))
        mydb.commit()

    def addRecord():
        results = [id_entry.get(), d_entry.get(), t_entry.get(), ph_entry.get(), tChl_entry.get(), fChl_entry.get(), cChl_entry.get()]
        if(results[6] == ''):
            results[6] = 0
        day_read_api.addDailyReading(results)
        generateTree()
        clear_entries()

    def removeRecord():
        results = [id_entry.get(), d_entry.get(), t_entry.get(), ph_entry.get(), tChl_entry.get(), fChl_entry.get(), cChl_entry.get()]
        day_read_api.removeDailyReading(results)
        generateTree()
        clear_entries()

    def updateRecord():
        results = [id_entry.get(), d_entry.get(), t_entry.get(), ph_entry.get(), tChl_entry.get(), fChl_entry.get(), cChl_entry.get()]
        day_read_api.updateDailyReading(results)
        generateTree()
        clear_entries()

    def displayRecords():
        top = Toplevel()
        top.title("Display Filter")
        display_label = ttk.Label(top, text="Please check the variables you wish to filter by.").pack()
        checkID = ttk.Checkbutton(top, text="Day ID").pack()
    
    def waterQualRegReport():
        report_date = d_entry.get()
        daily_report.generateDailyReport(report_date)
        messagebox.showinfo(message = "Your Water Quality Regulation Report for the daily readings has been generated! You can view the file in Adobe Reader.")

    root = Tk()
    label = ttk.Label(root, text="Daily Readings", background = '#ff7f50')
    label.config(font=('Arial', 18, 'bold'))
    label.pack()
    mycursor = mydb.cursor()

    root.title('Pool Club Manager - Daily Readings')
    root.resizable(True, True)
    root.configure(background = '#ff7f50')

    style = ttk.Style()
    style.configure('TFrame', background='#ff7f50')
    style.configure('TButton', background='#ff7f50')
    style.configure('TLabel', background='#ff7f50', font=('Arial', 11))

    pandedwindow = ttk.PanedWindow(root, orient=HORIZONTAL)
    pandedwindow.pack(fill=BOTH, expand=True)
    
    treeframe = Frame(root)
    treeframe.pack(pady = 10)

    scrollbar = ttk.Scrollbar(treeframe)
    scrollbar.pack(side=RIGHT, fill=Y)

    daily_tree = ttk.Treeview(treeframe, yscrollcommand=scrollbar.set, selectmode='extended')
    daily_tree.pack()

    scrollbar.config(command = daily_tree.yview)

    daily_tree['columns']=("Day ID", "Date", "Time", "pH", "Total Chlorine", "Free Chlorine", "Combined Chlorine")
    daily_tree.column("#0", width=0, stretch=NO)
    daily_tree.heading("#0", text="", anchor=W)
    daily_tree.column("Day ID", anchor=W, width=80)
    daily_tree.heading("Day ID", text="Day ID", anchor=W)
    daily_tree.column("Date", anchor=W, width=100)
    daily_tree.heading("Date", text="Date", anchor=W)
    daily_tree.column("Time", anchor=W, width=100)
    daily_tree.heading("Time", text="Time", anchor=W)
    daily_tree.column("pH", anchor=W, width=100)
    daily_tree.heading("pH", text="pH", anchor=W)
    daily_tree.column("Total Chlorine", anchor=W, width=200)
    daily_tree.heading("Total Chlorine", text="Total Chlorine", anchor=W)
    daily_tree.column("Free Chlorine", anchor=W, width=150)
    daily_tree.heading("Free Chlorine", text="Free Chlorine", anchor=W)
    daily_tree.column("Combined Chlorine", anchor=W, width=200)
    daily_tree.heading("Combined Chlorine", text="Combined Chlorine", anchor=W)

    generateTree()

    input_frame = LabelFrame(root, text="Record", background='#e0ffff')
    input_frame.pack(fill='x', expand='yes', pady=10)

    id_label = Label(input_frame, text="Day ID", background='#e0ffff')
    id_label.grid(row=0, column=0, padx=10, pady=10)
    id_entry = Entry(input_frame)
    id_entry.grid(row=0, column=1, padx=10, pady=10)

    d_label = Label(input_frame, text="Date", background='#e0ffff')
    d_label.grid(row=0, column=2, padx=10, pady=10)
    d_entry = Entry(input_frame)
    d_entry.grid(row=0, column=3, padx=10, pady=10)

    t_label = Label(input_frame, text="Time", background='#e0ffff')
    t_label.grid(row=0, column=4, padx=10, pady=10)
    t_entry = Entry(input_frame)
    t_entry.grid(row=0, column=5, padx=10, pady=10)

    ph_label = Label(input_frame, text="pH", background='#e0ffff')
    ph_label.grid(row=1, column=0, padx=10, pady=10)
    ph_entry = Entry(input_frame)
    ph_entry.grid(row=1, column=1, padx=10, pady=10)

    tChl_label = Label(input_frame, text="Total Chlorine", background='#e0ffff')
    tChl_label.grid(row=1, column=2, padx=10, pady=10)
    tChl_entry = Entry(input_frame)
    tChl_entry.grid(row=1, column=3, padx=10, pady=10)

    fChl_label = Label(input_frame, text="Free Chlorine", background='#e0ffff')
    fChl_label.grid(row=1, column=4, padx=10, pady=10)
    fChl_entry = Entry(input_frame)
    fChl_entry.grid(row=1, column=5, padx=10, pady=10)

    cChl_label = Label(input_frame, text="Combined Chlorine", background='#e0ffff')
    cChl_label.grid(row=1, column=6, padx=10, pady=10)
    cChl_entry = Entry(input_frame)
    cChl_entry.grid(row=1, column=7, padx=10, pady=10)

    daily_tree.bind('<ButtonRelease-1>', select_record)

    button_frame = LabelFrame(root, text="Actions", background='#e0ffff')
    button_frame.pack(fill='x', expand='yes', pady=10)

    add_button = ttk.Button(button_frame, text="Add Record", command=addRecord)
    add_button.grid(row=0, column=0, padx=10, pady=10)

    remove_button = ttk.Button(button_frame, text="Remove Record", command=removeRecord)
    remove_button.grid(row=0, column=1, padx=10, pady=10)

    update_button = ttk.Button(button_frame, text="Update Record", command=updateRecord)
    update_button.grid(row=0, column=2, padx=10, pady=10)

    display_button = ttk.Button(button_frame, text="Display Record", command=displayRecords)
    display_button.grid(row=0, column=3, padx=10, pady=10)

    clear_button = ttk.Button(button_frame, text="Clear Fields", command=clear_entries)
    clear_button.grid(row=0, column=4, padx=10, pady=10)

    wqrr_button = ttk.Button(button_frame, text="Generate Water Quality Regulation Report", command=waterQualRegReport)
    wqrr_button.grid(row=0, column=5, padx=10, pady=10)

    root.mainloop()