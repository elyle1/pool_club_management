# Import Required Module
from tkinter import *
from tkinter.ttk import *
import poolclub_staff_gui
import maintenance_gui
import day_read_gui
import week_read_gui
import daily_report_gui
import weekly_report_gui
import poolchem_supp_gui
import staff_schedule_gui
 
# Create Root Object
root = Tk()

# Set Title, Geometry(widthxheight), and background color
root.title('Pool Club Management')
root.geometry('550x450')
root.configure(bg ='coral')

# Create style Object
style = Style()

style.configure('TFrame', background='#ff7f50')
style.configure('TButton', font =
               ('calibri', 12, 'bold'),
                    borderwidth = '0')
style.configure('TLabel', background='#ff7f50', font=('Arial', 11))

# Changes will be reflected
# by the movement of mouse.
style.map('TButton', foreground = [('active', '!disabled', 'green')],
                     background = [('active', 'black')])

header_label = Label(root, text="Pool Club Management")
header_label.config(font=('arial', 18, 'bold'))
header_label.grid(row=0, column=0, padx=100, pady=10)

# label
label1 = Label(root, text="Options")
label1.config(font=('calibri', 14, 'bold', 'underline'))
label1.grid(row=1, column=0, padx= 100)

# Staff Button
btn1 = Button(root, text ="Staff Organization", command=poolclub_staff_gui.display)
btn1.grid(row=2, column=0, padx=100)
 
# Maintenance Button
btn2 = Button(root, text="Schedule Maintenance", command=maintenance_gui.display)
btn2.grid(row=3, column=0, padx=100)

# Daily Readings Button
btn3 = Button(root, text="Daily Readings", command=day_read_gui.display)
btn3.grid(row=4, column=0, padx=100)

# Weekly Readings Button
btn4 = Button(root, text="Weekly Readings", command=week_read_gui.display)
btn4.grid(row=5, column=0, padx=100)
 
# Pool Chemical Supply Button
btn5 = Button(root, text="Pool Chemical Supply", command=poolchem_supp_gui.display)
btn5.grid(row=6, column=0, padx=100)

# Staff Scheduling Button
btn6 = Button(root, text="Staff Scheduling", command=staff_schedule_gui.display)
btn6.grid(row=7, column=0, padx=100)

# Execute Tkinter
root.mainloop()
