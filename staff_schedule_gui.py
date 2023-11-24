from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import staff_schedule_api

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
        s_entry.delete(0, END)
        ma_po_entry.delete(0, END)
        l_entry.delete(0, END)
        a_entry.delete(0, END)

    def select_record(e):
        clear_entries()
        selected = sched_tree.focus()
        values = sched_tree.item(selected, 'values')
        id_entry.insert(0, values[0])
        d_entry.insert(0, values[1])
        s_entry.insert(0, values[2])
        ma_po_entry.insert(0, values[3])
        l_entry.insert(0, values[4])
        a_entry.insert(0, values[5])

    def generateTree():
        sched_tree.delete(*sched_tree.get_children())
        sql = "SELECT * FROM poolclub.schedule"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        for x in myresult:
            sched_tree.insert(parent='', index='end', text='', values=(x[0], x[1], x[2], x[3], x[4], x[5]))
        mydb.commit()

    def addRecord():
        results = [id_entry.get(), d_entry.get(), s_entry.get(), ma_po_entry.get(), l_entry.get(), a_entry.get()]
        staff_schedule_api.addScheduledTask(results)
        generateTree()
        clear_entries()

    def removeRecord():
        results = [id_entry.get(), d_entry.get(), s_entry.get(), ma_po_entry.get(), l_entry.get(), a_entry.get()]
        staff_schedule_api.removeScheduledTask(results)
        generateTree()
        clear_entries()

    def updateRecord():
        results = [id_entry.get(), d_entry.get(), s_entry.get(), ma_po_entry.get(), l_entry.get(), a_entry.get()]
        staff_schedule_api.updateScheduledTask(results)
        generateTree()
        clear_entries()

    def displayRecords():
        top = Toplevel()
        top.title("Display Filter")
        display_label = ttk.Label(top, text="Please check the variables you wish to filter by.").pack()
        checkID = ttk.Checkbutton(top, text="Schedule ID").pack()

    root = Tk()
    label = ttk.Label(root, text="Staff Scheduling", background='#ff7f50')
    label.config(font=('Arial', 18, 'bold'))
    label.pack()
    mycursor = mydb.cursor()

    root.title('Pool Club Manager - Staff Scheduling')
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

    sched_tree = ttk.Treeview(treeframe, yscrollcommand=scrollbar.set, selectmode='extended')
    sched_tree.pack()

    scrollbar.config(command = sched_tree.yview)

    sched_tree['columns']=("Schedule ID", "Date", "Shift", "Manager/Pool Operator", "Lifeguards", "Admin")
    sched_tree.column("#0", width=0, stretch=NO)
    sched_tree.heading("#0", text="", anchor=W)
    sched_tree.column("Schedule ID", anchor=W, width=80)
    sched_tree.heading("Schedule ID", text="Schedule ID", anchor=W)
    sched_tree.column("Date", anchor=W, width=80)
    sched_tree.heading("Date", text="Date", anchor=W)
    sched_tree.column("Shift", anchor=W, width=80)
    sched_tree.heading("Shift", text="Shift", anchor=W)
    sched_tree.column("Manager/Pool Operator", anchor=W, width=150)
    sched_tree.heading("Manager/Pool Operator", text="Manager/Pool Operator", anchor=W)
    sched_tree.column("Lifeguards", anchor=W, width=150)
    sched_tree.heading("Lifeguards", text="Lifeguards", anchor=W)
    sched_tree.column("Admin", anchor=W, width=150)
    sched_tree.heading("Admin", text="Admin", anchor=W)

    generateTree()

    input_frame = LabelFrame(root, text="Record", background='#e0ffff')
    input_frame.pack(fill='x', expand='yes', pady=10)

    id_label = Label(input_frame, text="Schedule ID", background='#e0ffff')
    id_label.grid(row=0, column=0, padx=10, pady=10)
    id_entry = Entry(input_frame)
    id_entry.grid(row=0, column=1, padx=10, pady=10)

    d_label = Label(input_frame, text="Date", background='#e0ffff')
    d_label.grid(row=0, column=3, padx=10, pady=10)
    d_entry = Entry(input_frame)
    d_entry.grid(row=0, column=4, padx=10, pady=10)

    s_label = Label(input_frame, text="Shift", background='#e0ffff')
    s_label.grid(row=0, column=7, padx=10, pady=10)
    s_entry = Entry(input_frame)
    s_entry.grid(row=0, column=8, padx=10, pady=10)

    ma_po_label = Label(input_frame, text="Manager/Pool Operator", background='#e0ffff')
    ma_po_label.grid(row=1, column=0, padx=10, pady=10)
    ma_po_entry = Entry(input_frame)
    ma_po_entry.grid(row=1, column=1, padx=10, pady=10)

    l_label = Label(input_frame, text="Lifeguards", background='#e0ffff')
    l_label.grid(row=1, column=3, padx=10, pady=10)
    l_entry = Entry(input_frame)
    l_entry.grid(row=1, column=4, padx=10, pady=10)

    a_label = Label(input_frame, text="Admin", background='#e0ffff')
    a_label.grid(row=1, column=7, padx=10, pady=10)
    a_entry = Entry(input_frame)
    a_entry.grid(row=1, column=8, padx=10, pady=10)

    sched_tree.bind('<ButtonRelease-1>', select_record)

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

    root.mainloop()