from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import maintenance_api

def display():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Prof3SSi0nalPiupzzxk",
    database="poolclub"
    )

    def clear_entries():
        in_entry.delete(0, END)
        d_entry.delete(0, END)
        task_entry.delete(0, END)
        sr_entry.delete(0, END)
        s_entry.delete(0, END)
        
    def select_record(e):
        clear_entries()
        selected = main_tree.focus()
        values = main_tree.item(selected, 'values')
        in_entry.insert(0, values[0])
        d_entry.insert(0, values[1])
        task_entry.insert(0, values[2])
        sr_entry.insert(0, values[3])
        s_entry.insert(0, values[4])

    def generateTree():
        main_tree.delete(*main_tree.get_children())
        sql = "SELECT * FROM poolclub.maintenance"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        for x in myresult:
            main_tree.insert(parent='', index='end', text='', values=(x[0], x[1], x[2], x[3], x[4]))
        mydb.commit()


    def addRecord():
        results = [in_entry.get(), d_entry.get(), task_entry.get(), sr_entry.get(), s_entry.get()]
        maintenance_api.addMaintenanceTask(results)
        generateTree()
        clear_entries()

    def removeRecord():
        results = [in_entry.get(), d_entry.get(), task_entry.get(), sr_entry.get(), s_entry.get()]
        maintenance_api.removeMaintenanceTask(results)
        generateTree()
        clear_entries()


    def updateRecord():
        results = [in_entry.get(), d_entry.get(), task_entry.get(), sr_entry.get(), s_entry.get()]
        maintenance_api.updateMaintenanceTask(results)
        generateTree()
        clear_entries()

    def displayRecords():
        top = Toplevel()
        top.title("Display Filter")
        display_label = ttk.Label(top, text="Please check the variables you wish to filter by.").pack()
        checkID = ttk.Checkbutton(top, text="Item Number").pack()


    root = Tk()
    label = ttk.Label(root, text="Schedule Maintenance", background='#ff7f50')
    label.config(font=('Arial', 18, 'bold'))
    label.pack()
    mycursor = mydb.cursor()

    root.title('Pool Club Manager - Schedule Maintenance')
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

    main_tree = ttk.Treeview(treeframe, yscrollcommand=scrollbar.set, selectmode='extended')
    main_tree.pack()

    scrollbar.config(command = main_tree.yview)

    main_tree['columns']=("Item Number", "Date", "Task", "Staff Representative", "Status")
    main_tree.column("#0", width=0, stretch=NO)
    main_tree.heading("#0", text="", anchor=W)
    main_tree.column("Item Number", anchor=W, width=80)
    main_tree.heading("Item Number", text="Item Number", anchor=W)
    main_tree.column("Date", anchor=W, width=100)
    main_tree.heading("Date", text="Date", anchor=W)
    main_tree.column("Task", anchor=W, width=150)
    main_tree.heading("Task", text="Task", anchor=W)
    main_tree.column("Staff Representative", anchor=W, width=150)
    main_tree.heading("Staff Representative", text="Staff Representative", anchor=W)
    main_tree.column("Status", anchor=W, width=80)
    main_tree.heading("Status", text="Status", anchor=W)

    generateTree()

    input_frame = LabelFrame(root, text="Record", background='#e0ffff')
    input_frame.pack(fill='x', expand='yes', pady=10)

    in_label = Label(input_frame, text="Item Number", background='#e0ffff')
    in_label.grid(row=0, column=0, padx=10, pady=10)
    in_entry = Entry(input_frame)
    in_entry.grid(row=0, column=1, padx=10, pady=10)

    d_label = Label(input_frame, text="Date", background='#e0ffff')
    d_label.grid(row=0, column=3, padx=10, pady=10)
    d_entry = Entry(input_frame)
    d_entry.grid(row=0, column=4, padx=10, pady=10)

    task_label = Label(input_frame, text="Task", background='#e0ffff')
    task_label.grid(row=0, column=7, padx=10, pady=10)
    task_entry = Entry(input_frame)
    task_entry.grid(row=0, column=8, padx=10, pady=10)

    sr_label = Label(input_frame, text="Staff Rep.", background='#e0ffff')
    sr_label.grid(row=1, column=0, padx=10, pady=10)
    sr_entry = Entry(input_frame)
    sr_entry.grid(row=1, column=1, padx=10, pady=10)

    s_label = Label(input_frame, text="Status", background='#e0ffff')
    s_label.grid(row=1, column=3, padx=10, pady=10)
    s_entry = Entry(input_frame)
    s_entry.grid(row=1, column=4, padx=10, pady=10)

    main_tree.bind('<ButtonRelease-1>', select_record)

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