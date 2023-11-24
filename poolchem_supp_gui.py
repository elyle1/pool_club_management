from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import poolchem_supp_api

def display():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Prof3SSi0nalPiupzzxk",
    database="poolclub"
    )

    def clear_entries():
        id_entry.delete(0, END)
        cn_entry.delete(0, END)
        ap_entry.delete(0, END)
        dp_entry.delete(0, END)
        au_entry.delete(0, END)
        du_entry.delete(0, END)
        ao_entry.delete(0, END)

    def select_record(e):
        clear_entries()
        selected = chem_tree.focus()
        values = chem_tree.item(selected, 'values')
        id_entry.insert(0, values[0])
        cn_entry.insert(0, values[1])
        ap_entry.insert(0, values[2])
        dp_entry.insert(0, values[3])
        au_entry.insert(0, values[4])
        du_entry.insert(0, values[5])
        ao_entry.insert(0, values[6])

    def generateTree():
        chem_tree.delete(*chem_tree.get_children())
        sql = "SELECT * FROM poolclub.pool_chemical_supply"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        for x in myresult:
            chem_tree.insert(parent='', index='end', text='', values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6]))
        mydb.commit()

    def addRecord():
        results = [id_entry.get(), cn_entry.get(), ap_entry.get(), dp_entry.get(), au_entry.get(), du_entry.get(), ao_entry.get()]
        poolchem_supp_api.addPoolChemical(results)
        generateTree()
        clear_entries()

    def removeRecord():
        results = [id_entry.get(), cn_entry.get(), ap_entry.get(), dp_entry.get(), au_entry.get(), du_entry.get(), ao_entry.get()]
        poolchem_supp_api.removePoolChemical(results)
        generateTree()
        clear_entries()

    def updateRecord():
        results = [id_entry.get(), cn_entry.get(), ap_entry.get(), dp_entry.get(), au_entry.get(), du_entry.get(), ao_entry.get()]
        poolchem_supp_api.updatePoolChemical(results)
        generateTree()
        clear_entries()

    def displayRecords():
        top = Toplevel()
        top.title("Display Filter")
        display_label = ttk.Label(top, text="Please check the variables you wish to filter by.").pack()
        checkID = ttk.Checkbutton(top, text="Chemical ID").pack()

    root = Tk()
    label = ttk.Label(root, text="Pool Chemical Supply", background='#ff7f50')
    label.config(font=('Arial', 18, 'bold'))
    label.pack()
    mycursor = mydb.cursor()

    root.title('Pool Club Manager - Pool Chemical Supply')
    root.resizable(True, True)
    root.configure(background = '#ff7f50')

    style = ttk.Style()
    style.configure('TFrame', background='ff7f50')
    style.configure('TButton', background='#ff7f50')
    style.configure('TLabel', background='#ff7f50', font=('Arial', 11))
    
    pandedwindow = ttk.PanedWindow(root, orient=HORIZONTAL)
    pandedwindow.pack(fill=BOTH, expand=True)
    
    treeframe = Frame(root)
    treeframe.pack(pady = 10)

    scrollbar = ttk.Scrollbar(treeframe)
    scrollbar.pack(side=RIGHT, fill=Y)

    chem_tree = ttk.Treeview(treeframe, yscrollcommand=scrollbar.set, selectmode='extended')
    chem_tree.pack()

    scrollbar.config(command = chem_tree.yview)

    chem_tree['columns']=("Chemical ID", "Chemical Name", "Amount Purchased", "Date Purchased", "Amount Used", "Date Used", "Amount On-hand")
    chem_tree.column("#0", width=0, stretch=NO)
    chem_tree.heading("#0", text="", anchor=W)
    chem_tree.column("Chemical ID", anchor=W, width=80)
    chem_tree.heading("Chemical ID", text="Chemical ID", anchor=W)
    chem_tree.column("Chemical Name", anchor=W, width=100)
    chem_tree.heading("Chemical Name", text="Chemical Name", anchor=W)
    chem_tree.column("Amount Purchased", anchor=W, width=120)
    chem_tree.heading("Amount Purchased", text="Amount Purchased", anchor=W)
    chem_tree.column("Date Purchased", anchor=W, width=100)
    chem_tree.heading("Date Purchased", text="Date Purchased", anchor=W)
    chem_tree.column("Amount Used", anchor=W, width=80)
    chem_tree.heading("Amount Used", text="Amount Used", anchor=W)
    chem_tree.column("Date Used", anchor=W, width=100)
    chem_tree.heading("Date Used", text="Date Used", anchor=W)
    chem_tree.column("Amount On-hand", anchor=W, width=120)
    chem_tree.heading("Amount On-hand", text="Amount On-hand", anchor=W)

    generateTree()

    input_frame = LabelFrame(root, text="Record", background='#e0ffff')
    input_frame.pack(fill='x', expand='yes', pady=10)

    id_label = Label(input_frame, text="Chemical ID", background='#e0ffff')
    id_label.grid(row=0, column=0, padx=10, pady=10)
    id_entry = Entry(input_frame)
    id_entry.grid(row=0, column=1, padx=10, pady=10)

    cn_label = Label(input_frame, text="Chemical Name", background='#e0ffff')
    cn_label.grid(row=0, column=3, padx=10, pady=10)
    cn_entry = Entry(input_frame)
    cn_entry.grid(row=0, column=4, padx=10, pady=10)

    ap_label = Label(input_frame, text="Amount Purchased", background='#e0ffff')
    ap_label.grid(row=0, column=7, padx=10, pady=10)
    ap_entry = Entry(input_frame)
    ap_entry.grid(row=0, column=8, padx=10, pady=10)

    dp_label = Label(input_frame, text="Date Purchased", background='#e0ffff')
    dp_label.grid(row=1, column=0, padx=10, pady=10)
    dp_entry = Entry(input_frame)
    dp_entry.grid(row=1, column=1, padx=10, pady=10)

    au_label = Label(input_frame, text="Amount Used", background='#e0ffff')
    au_label.grid(row=1, column=3, padx=10, pady=10)
    au_entry = Entry(input_frame)
    au_entry.grid(row=1, column=4, padx=10, pady=10)

    du_label = Label(input_frame, text="Date Used", background='#e0ffff')
    du_label.grid(row=1, column=7, padx=10, pady=10)
    du_entry = Entry(input_frame)
    du_entry.grid(row=1, column=8, padx=10, pady=10)

    ao_label = Label(input_frame, text="Amount On-hand", background='#e0ffff')
    ao_label.grid(row=2, column=0, padx=10, pady=10)
    ao_entry = Entry(input_frame)
    ao_entry.grid(row=2, column=1, padx=10, pady=10)

    chem_tree.bind('<ButtonRelease-1>', select_record)

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