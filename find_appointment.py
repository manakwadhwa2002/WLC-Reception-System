import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

# Creating a Window

root = Tk()
root.geometry('1250x680+50+5')
root.title('Find Client - Wadhwa Legal Consultancy System')
root.iconbitmap('favicon.ico')
root.resizable(False, False)



# Defininf Variables
g = StringVar()
f = StringVar()


# Defining Functions
def get():
    if len(f.get()) == 0:
        messagebox.showinfo('Error','Please Select a Search Domain !!!')
    elif len(g.get()) == 0:
        messagebox.showinfo('Error','Please Enter'+f.get()+' !!!')
    else:
        try: 
            if f.get() == 'Appointment ID':
                conn = sqlite3.connect('wlc_administration_system.db')
                myCursor = conn.cursor()
                myCursor.execute('SELECT * FROM bookings WHERE booking_id like (?)',['%'+g.get()+'%'])
                pc = myCursor.fetchall()
                myCursor.close()
                conn.close()
                if pc:
                    insert(pc)#messagebox.showinfo('Found!','Record Found')
                else:
                    messagebox.showinfo('Error','Oops! no record found :(')
            elif f.get() == 'Client Name':
                conn = sqlite3.connect('wlc_administration_system.db')
                myCursor = conn.cursor()
                myCursor.execute('SELECT * FROM bookings WHERE client_name like (?)',['%'+g.get()+'%'])
                pc = myCursor.fetchall()
                myCursor.close()
                conn.close()
                if pc:
                    insert(pc)#messagebox.showinfo('Found!','Record Found')
                else:
                    messagebox.showinfo('Error','Oops! no record found :(')
            elif f.get() == 'Appointment Date':
                conn = sqlite3.connect('wlc_administration_system.db')
                myCursor = conn.cursor()
                myCursor.execute('SELECT * FROM bookings WHERE date like (?)',['%'+g.get()+'%'])
                pc = myCursor.fetchall()
                myCursor.close()
                conn.close()
                if pc:
                    insert(pc)#messagebox.showinfo('Found!','Record Found')
                else:
                    messagebox.showinfo('Error','Oops! no record found :(')
            elif f.get() == 'Appointment Time':
                conn = sqlite3.connect('wlc_administration_system.db')
                myCursor = conn.cursor()
                myCursor.execute('SELECT * FROM bookings WHERE time_slot like (?)',['%'+g.get()+'%'])
                pc = myCursor.fetchall()
                myCursor.close()
                conn.close()
                if pc:
                    insert(pc)#messagebox.showinfo('Found!','Record Found')
                else:
                    messagebox.showinfo('Error','Oops! no record found :(')                        
        except:
            messagebox.showinfo('Error','Something Went Wrong !!!')            

def insert(data):
    for row in data:
        listtree.insert('', 'end', text = row[0], values = (row[2], row[7], row[6], row[4], row[5]))


# Logo 
logo = ImageTk.PhotoImage(Image.open('Logo(200x200).png'))
logo_label = Label(root, image=logo)
logo_label.pack() # Placing Logo


# Heading 
Label(root, text='Find Appointment', font=('Verdana', 32)).place(x=425,y=200)


# Lables
Label(root, text='Search By', font=('TimesNewRoman', 16)).place(x=350, y=275)
Label(root, text='Enter', font=('TimesNewRoman', 16)).place(x=350, y=310)

# Entry Widgets 
ttk.Combobox(root, textvariable=f, values=['Appointment ID','Client Name', 'Appointment Date', 'Appointment Time'], width=55, state='readonly').place(x=550, y=275)
Entry(root, textvariable=g, font=('TimesNewRoman', 16), width=30, bd=0, bg='#E2E2E2').place(x=550, y=310)


# Find Button
search=ImageTk.PhotoImage(Image.open('new-search.png'))
Button(root, image=search, bd=0, command=get).place(x=950, y=309)


# Seting Up Treeview
listtree = ttk.Treeview(root, height=12,columns=('Client Name', 'Fee Status', 'Appointment With', 'Appointment Date', 'Appointment Time'))
listtree.place(x= 25, y=375)
#vsb = ttk.Scrollbar(root, orient='horizontal', command=listtree.xview)
#vsb.pack()
listtree.heading('#0',text='Appointment ID')
listtree.heading('Client Name', text='Client Name')
listtree.heading('Fee Status', text='Fee Status')
listtree.heading('Appointment With', text='Appointment With')
listtree.heading('Appointment Date', text='Appointment Date')
listtree.heading('Appointment Time', text='Appointment Time')
#listtree.heading('Client Phone Number', text='Client Phone Number')
listtree.column('#0', anchor='n')
listtree.column('Client Name', anchor='center')
listtree.column('Fee Status', anchor='center')
listtree.column('Appointment With', anchor='center')
listtree.column('Appointment Date', anchor='center')
listtree.column('Appointment Time', anchor='center')
#listtree.column('Client Phone Number', anchor='center')
ttk.Style().configure('Treeview', font=('TimesNewRoman', 12))

# Copyright Label
Label(root, text="Manak Wadhwa | © Copyright 2020 - Wadhwa Legal Consultancy", font=('Verdana', 11, 'bold')).place(x=425, y=655)

root.mainloop()