from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import staff_api

def display():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Prof3SSi0nalPiupzzxk",
    database="poolclub"
    )

    def clear_entries():
        id_entry.delete(0, END)
        fn_entry.delete(0, END)
        ln_entry.delete(0, END)
        hd_entry.delete(0, END)
        sd_entry.delete(0, END)
        rfs_entry.delete(0, END)
        pswd_entry.delete(0, END)
        ut_entry.delete(0, END)

    def select_record(e):
        clear_entries()
        selected = staff_tree.focus()
        values = staff_tree.item(selected, 'values')
        id_entry.insert(0, values[0])
        fn_entry.insert(0, values[1])
        ln_entry.insert(0, values[2])
        hd_entry.insert(0, values[3])
        sd_entry.insert(0, values[4])
        rfs_entry.insert(0, values[5])
        pswd_entry.insert(0, values[6])
        ut_entry.insert(0, values[7])

    def generateTree():
        staff_tree.delete(*staff_tree.get_children())
        sql = "SELECT * FROM poolclub.staff"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        for x in myresult:
            staff_tree.insert(parent='', index='end', text='', values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]))
        mydb.commit()

    def addRecord():
        results = [id_entry.get(), fn_entry.get(), ln_entry.get(), hd_entry.get(), sd_entry.get(), rfs_entry.get(), pswd_entry.get(), ut_entry.get()]
        staff_api.addStaffMember(results)
        generateTree()
        clear_entries()

    def removeRecord():
        results = [id_entry.get(), fn_entry.get(), ln_entry.get(), hd_entry.get(), sd_entry.get(), rfs_entry.get(), pswd_entry.get(), ut_entry.get()]
        staff_api.removeStaffMember(results)
        generateTree()
        clear_entries()

    def updateRecord():
        results = [id_entry.get(), fn_entry.get(), ln_entry.get(), hd_entry.get(), sd_entry.get(), rfs_entry.get(), pswd_entry.get(), ut_entry.get()]
        staff_api.updateStaffMember(results)
        generateTree()
        clear_entries()

    def displayRecords():
        top = Toplevel()
        top.title("Display Filter")
        display_label = ttk.Label(top, text="Please check the variables you wish to filter by.").pack()
        checkID = ttk.Checkbutton(top, text="ID Num").pack()
        

    root = Tk()
    label = ttk.Label(root, text="Staff Organization", background = '#ff7f50')
    label.config(font=('arial', 18, 'bold'))
    label.pack()
    mycursor = mydb.cursor()

    root.title('Pool Club Manager - Staff Organization')
    root.resizable(True, True)
    root.configure(background='#ff7f50')

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

    staff_tree = ttk.Treeview(treeframe, yscrollcommand=scrollbar.set, selectmode='extended')
    staff_tree.pack()

    scrollbar.config(command=staff_tree.yview)

    staff_tree['columns']=("ID Num", "First Name", "Last Name", "Hire Date", "Separation Date", "Reason for Separation", "Password", "User Type")
    staff_tree.column("#0", width=0, stretch=NO)
    staff_tree.heading("#0", text="", anchor=W)
    staff_tree.column("ID Num", anchor=W, width=100)
    staff_tree.heading("ID Num", text="ID Num", anchor=W)
    staff_tree.column("First Name", anchor=W, width=200)
    staff_tree.heading("First Name", text="First Name", anchor=W)
    staff_tree.column("Last Name", anchor=W, width=200)
    staff_tree.heading("Last Name", text="Last Name", anchor=W)
    staff_tree.column("Hire Date", anchor=W, width=100)
    staff_tree.heading("Hire Date", text="Hire Date", anchor=W)
    staff_tree.column("Separation Date", anchor=W, width=100)
    staff_tree.heading("Separation Date", text="Separation Date", anchor=W)
    staff_tree.column("Reason for Separation", anchor=W, width=200)
    staff_tree.heading("Reason for Separation", text="Reason for Separation", anchor=W)
    staff_tree.column("Password", anchor=W, width=100)
    staff_tree.heading("Password", text="Password", anchor=W)
    staff_tree.column("User Type", anchor=W, width=200)
    staff_tree.heading("User Type", text="User Type", anchor=W)

    generateTree()

    input_frame = LabelFrame(root, text="Record", background='#e0ffff')
    input_frame.pack(fill='x', expand='yes', pady=10)

    id_label = Label(input_frame, text="ID Num", background='#e0ffff')
    id_label.grid(row=0, column=0, padx=10, pady=10)
    id_entry = Entry(input_frame)
    id_entry.grid(row=0, column=1, padx=10, pady=10)

    fn_label = Label(input_frame, text="First Name", background='#e0ffff')
    fn_label.grid(row=0, column=3, padx=10, pady=10)
    fn_entry = Entry(input_frame)
    fn_entry.grid(row=0, column=4, padx=10, pady=10)

    ln_label = Label(input_frame, text="Last Name", background='#e0ffff')
    ln_label.grid(row=0, column=7, padx=10, pady=10)
    ln_entry = Entry(input_frame)
    ln_entry.grid(row=0, column=8, padx=10, pady=10)

    hd_label = Label(input_frame, text="Hire Date", background='#e0ffff')
    hd_label.grid(row=1, column=0, padx=10, pady=10)
    hd_entry = Entry(input_frame)
    hd_entry.grid(row=1, column=1, padx=10, pady=10)

    sd_label = Label(input_frame, text="Separation Date", background='#e0ffff')
    sd_label.grid(row=1, column=3, padx=10, pady=10)
    sd_entry = Entry(input_frame)
    sd_entry.grid(row=1, column=4, padx=10, pady=10)

    rfs_label = Label(input_frame, text="Reason for Separation", background='#e0ffff')
    rfs_label.grid(row=1, column=7, padx=10, pady=10)
    rfs_entry = Entry(input_frame)
    rfs_entry.grid(row=1, column=8, padx=10, pady=10)

    pswd_label = Label(input_frame, text="Password", background='#e0ffff')
    pswd_label.grid(row=2, column=0, padx=10, pady=10)
    pswd_entry = Entry(input_frame)
    pswd_entry.grid(row=2, column=1, padx=10, pady=10)

    ut_label = Label(input_frame, text="User Type", background='#e0ffff')
    ut_label.grid(row=2, column=3, columnspan=3, padx=10, pady=10)
    ut_entry = Entry(input_frame)
    ut_entry.grid(row=2, column=4, columnspan=4, padx=10, pady=10)

    staff_tree.bind('<ButtonRelease-1>', select_record)

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