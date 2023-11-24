from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import week_read_api
import weekly_report

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
        th_entry.delete(0, END)
        ta_entry.delete(0, END)
        cya_entry.delete(0, END)

    def select_record(e):
        clear_entries()
        selected = weekly_tree.focus()
        values = weekly_tree.item(selected, 'values')
        id_entry.insert(0, values[0])
        d_entry.insert(0, values[1])
        t_entry.insert(0, values[2])
        th_entry.insert(0, values[3])
        ta_entry.insert(0, values[4])
        cya_entry.insert(0, values[5])

    def generateTree():
        weekly_tree.delete(*weekly_tree.get_children())
        sql = "SELECT * FROM poolclub.weekly_readings"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        for x in myresult:
            weekly_tree.insert(parent='', index='end', text='', values=(x[0], x[1], x[2], x[3], x[4], x[5]))
        mydb.commit()

    def addRecord():
        results = [id_entry.get(), d_entry.get(), t_entry.get(), th_entry.get(), ta_entry.get(), cya_entry.get()]
        week_read_api.addWeeklyReading(results)
        generateTree()
        clear_entries()

    def removeRecord():
        results = [id_entry.get(), d_entry.get(), t_entry.get(), th_entry.get(), ta_entry.get(), cya_entry.get()]
        week_read_api.removeWeeklyReading(results)
        generateTree()
        clear_entries()

    def updateRecord():
        results = [id_entry.get(), d_entry.get(), t_entry.get(), th_entry.get(), ta_entry.get(), cya_entry.get()]
        week_read_api.updateWeeklyReading(results)
        generateTree()
        clear_entries()

    def displayRecords():
        top = Toplevel()
        top.title("Display Filter")
        display_label = ttk.Label(top, text="Please check the variables you wish to filter by.").pack()
        checkID = ttk.Checkbutton(top, text="Week ID").pack()
    
    def waterQualRegReport():
        report_date = d_entry.get()
        weekly_report.generateWeeklyReport(report_date)
        messagebox.showinfo(message = "Your Water Quality Regulation Report for the weekly readings has been generated! You can view the file in Adobe Reader.")

    root = Tk()
    label = ttk.Label(root, text="Weekly Readings", background='#ff7f50')
    label.config(font=('Arial', 18, 'bold'))
    label.pack()
    mycursor = mydb.cursor()

    root.title('Pool Club Manager - Weekly Readings')
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

    weekly_tree = ttk.Treeview(treeframe, yscrollcommand=scrollbar.set, selectmode='extended')
    weekly_tree.pack()

    scrollbar.config(command = weekly_tree.yview)

    weekly_tree['columns']=("Week ID", "Date", "Time", "Total Hardness", "Total Alkalinity", "CYA (stabilizer)")
    weekly_tree.column("#0", width=0, stretch=NO)
    weekly_tree.heading("#0", text="", anchor=W)
    weekly_tree.column("Week ID", anchor=W, width=80)
    weekly_tree.heading("Week ID", text="Week ID", anchor=W)
    weekly_tree.column("Date", anchor=W, width=100)
    weekly_tree.heading("Date", text="Date", anchor=W)
    weekly_tree.column("Time", anchor=W, width=100)
    weekly_tree.heading("Time", text="Time", anchor=W)
    weekly_tree.column("Total Hardness", anchor=W, width=150)
    weekly_tree.heading("Total Hardness", text="Total Hardness", anchor=W)
    weekly_tree.column("Total Alkalinity", anchor=W, width=100)
    weekly_tree.heading("Total Alkalinity", text="Total Alkalinity", anchor=W)
    weekly_tree.column("CYA (stabilizer)", anchor=W, width=150)
    weekly_tree.heading("CYA (stabilizer)", text="CYA (stabilizer)", anchor=W)

    generateTree()

    input_frame = LabelFrame(root, text="Record", background='#e0ffff')
    input_frame.pack(fill='x', expand='yes', pady=10)

    id_label = Label(input_frame, text="Week ID", background='#e0ffff')
    id_label.grid(row=0, column=0, padx=10, pady=10)
    id_entry = Entry(input_frame)
    id_entry.grid(row=0, column=1, padx=10, pady=10)

    d_label = Label(input_frame, text="Date", background='#e0ffff')
    d_label.grid(row=0, column=3, padx=10, pady=10)
    d_entry = Entry(input_frame)
    d_entry.grid(row=0, column=4, padx=10, pady=10)

    t_label = Label(input_frame, text="Time", background='#e0ffff')
    t_label.grid(row=0, column=7, padx=10, pady=10)
    t_entry = Entry(input_frame)
    t_entry.grid(row=0, column=8, padx=10, pady=10)

    th_label = Label(input_frame, text="Total Hardness", background='#e0ffff')
    th_label.grid(row=1, column=0, padx=10, pady=10)
    th_entry = Entry(input_frame)
    th_entry.grid(row=1, column=1, padx=10, pady=10)

    ta_label = Label(input_frame, text="Total Alkalinity", background='#e0ffff')
    ta_label.grid(row=1, column=3, padx=10, pady=10)
    ta_entry = Entry(input_frame)
    ta_entry.grid(row=1, column=4, padx=10, pady=10)

    cya_label = Label(input_frame, text="CYA (stabilizer)", background='#e0ffff')
    cya_label.grid(row=1, column=7, padx=10, pady=10)
    cya_entry = Entry(input_frame)
    cya_entry.grid(row=1, column=8, padx=10, pady=10)

    weekly_tree.bind('<ButtonRelease-1>', select_record)

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