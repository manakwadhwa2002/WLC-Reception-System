import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

# Creating a Window

root = Tk()
root.geometry('900x680+100+5')
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
        messagebox.showinfo('Error','Please Enter '+f.get()+' !!!')
    else:
        try: 
            if f.get() == 'Client Name':
                conn = sqlite3.connect('wlc_administration_system.db')
                myCursor = conn.cursor()
                myCursor.execute('SELECT * FROM client WHERE first_name like (?)',['%'+g.get()+'%'])
                pc = myCursor.fetchall()
                myCursor.close()
                conn.close()
                if pc:
                    insert(pc)#messagebox.showinfo('Found!','Record Found')
                else:
                    messagebox.showinfo('Error','Oops! no record found :(')
            elif f.get() == 'Client ID':
                conn = sqlite3.connect('wlc_administration_system.db')
                myCursor = conn.cursor()
                myCursor.execute('SELECT * FROM client WHERE unique_id like (?)',['%'+g.get()+'%'])
                pc = myCursor.fetchall()
                myCursor.close()
                conn.close()
                if pc:
                    insert(pc)#messagebox.showinfo('Found!','Record Found')
                else:
                    messagebox.showinfo('Error','Oops! no record found :(')
            elif f.get() == 'Client Phone Number':
                conn = sqlite3.connect('wlc_administration_system.db')
                myCursor = conn.cursor()
                myCursor.execute('SELECT * FROM client WHERE unique_id like (?)',['%'+g.get()+'%'])
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
        listtree.insert('', 'end', text = row[0], values = (row[1]+'  '+row[2], row[3], row[8]))


# Logo 
logo = ImageTk.PhotoImage(Image.open('Logo(200x200).png'))
logo_label = Label(root, image=logo)
logo_label.pack() # Placing Logo


# Heading 
Label(root, text='Find Client', font=('Verdana', 32)).place(x=325,y=200)


# Lables
Label(root, text='Search By', font=('TimesNewRoman', 16)).place(x=150, y=275)
Label(root, text='Enter', font=('TimesNewRoman', 16)).place(x=150, y=310)

# Entry Widgets 
ttk.Combobox(root, textvariable=f, values=['Client Name','Client ID','Client Phone Number'], width=45, state='readonly').place(x=350, y=275)
Entry(root, textvariable=g, font=('TimesNewRoman', 16), width=25, bd=0, bg='#E2E2E2').place(x=350, y=310)


# Find Button
search=ImageTk.PhotoImage(Image.open('new-search.png'))
Button(root, image=search, bd=0, command=get).place(x=700, y=309)


# Seting Up Treeview
listtree = ttk.Treeview(root, height=12,columns=('Client Name', 'Client Phone Number', 'Client of'))
listtree.place(x= 50, y=375)
listtree.heading('#0',text='Client ID')
listtree.heading('Client Name', text='Client Name')
listtree.heading('Client Phone Number', text='Client Phone Number')
listtree.heading('Client of', text='Client of')
listtree.column('#0', anchor='n')
listtree.column('Client Name', anchor='center')
listtree.column('Client Phone Number', anchor='center')
listtree.column('Client of', anchor='center')
ttk.Style().configure('Treeview', font=('TimesNewRoman', 12))

# Copyright Label
Label(root, text="Manak Wadhwa | © Copyright 2020 - Wadhwa Legal Consultancy", font=('Verdana', 11, 'bold')).place(x=200, y=655)


root.mainloop()