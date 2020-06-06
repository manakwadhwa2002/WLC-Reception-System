from tkinter import *
from tkinter import ttk
from tkinter import Tk, Label
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from sqlite3 import Error
import os


# Creating Window
root = Tk()
root.geometry('1200x725+100+0')
root.title('Update Client Record - Wadhwa Legal Consultancy System')
root.resizable(False, False)


# Defining Variables
b = StringVar()
c = StringVar()
d = StringVar()
e = StringVar()
f = StringVar()
g = StringVar()
h = StringVar()
j = StringVar()



# Logo
logo = ImageTk.PhotoImage(Image.open('Logo(200x200).png'))
logo_label = Label(root, image=logo)
logo_label.pack()

# Search Button Image
search_img=ImageTk.PhotoImage(Image.open('new-search.png'))

# Heading 
Label(root, text='Update Client Record', font=('Romanesco', 34)).place(x=485, y=200)

# First Label
Label(root, text='Enter Client ID   :', font=('TimesNewRoman', 16)).place(x=250, y=260)
Label(root, text='WLC / CLT / ', font=('TimesNewRoman', 16)).place(x=450, y=260)


# Entry Widget for Client ID
Entry(root, textvariable=b, bd=0, bg='#E2E2E2', font=('TimesNewRoman', 16), width=15).place(x=590, y=263)


# Defining Search Function
def search():
    if len(b.get()) == 0:
        messagebox.showinfo('Error','Please Enter Client ID !!!')
    else:    
        conn = sqlite3.connect('wlc_administration_system.db')
        myCursor = conn.cursor()
        myCursor.execute("SELECT * FROM client WHERE unique_id = ?",[b.get()])
        pc = myCursor.fetchall()
        myCursor.close()
        conn.close()
        if pc:
            messagebox.showinfo('Success','Client Record Found :)')
            for row in pc:
                entry_label_2.insert(0, row[1])
                entry_label_3.insert(0, row[2])
                entry_label_4.insert(0, row[3])
                entry_label_5.insert(0, row[4])
                entry_label_6.insert(0, row[5])
                entry_label_7.insert(0, row[6])
                entry_label_8.insert(0, row[7])
        else:
            messagebox.showinfo('Oops!','Client Record not Found :(')  

def update():
    conn = sqlite3.connect('wlc_administration_system.db')
    myCursor = conn.cursor()
    myCursor.execute("UPDATE client SET first_name=?, last_name=?, phone_number=?, email=?, address=?, city=?, city_pincode=? WHERE unique_id = ?",[c.get(), d.get(), e.get(), f.get(), g.get(), h.get(), j.get(), b.get()])
    conn.commit()
    myCursor.close()
    conn.close()
    if True:
        messagebox.showinfo('Success','Client Record Updated Successfully !!!')
    else:
        messagebox.showinfo('Error',"Failed to update Client Record !!!")



# Body Lables

name_label_2 = Label(root, text="First Name:", font=('Verdana', 16))
entry_label_2 = Entry(root, textvariable=c, bd=0, bg='#E2E2E2', width=20, font=('TimesNewRoman', 16))

name_label_3 = Label(root, text="Last Name:", font=('Verdana', 16))
entry_label_3 = Entry(root, textvariable=d, bd=0, bg='#E2E2E2', width=20, font=('TimesNewRoman', 16))

name_label_4 = Label(root, text="Phone No:", font=('Verdana', 16))
entry_label_4 = Entry(root, textvariable=e, bd=0, bg='#E2E2E2', width=20, font=('TimesNewRoman', 16))

name_label_5 = Label(root, text="Email Id:", font=('Verdana', 16))
entry_label_5 = Entry(root, textvariable=f, bd=0, bg='#E2E2E2', width=20, font=('TimesNewRoman', 16))

name_label_6 = Label(root, text="Address:", font=('Verdana', 16))
entry_label_6 = Entry(root, textvariable=g, bd=0, bg='#E2E2E2', width=20, font=('TimesNewRoman', 16))

name_label_7 = Label(root, text="City:", font=('Verdana', 16))
entry_label_7 = Entry(root, textvariable=h, bd=0, bg='#E2E2E2', width=20, font=('TimesNewRoman', 16))

name_label_8 = Label(root, text="City Pincode:", font=('Verdana', 16))
entry_label_8 = Entry(root, textvariable=j, bd=0, bg='#E2E2E2', width=20, font=('TimesNewRoman', 16))


# Column 1 of Editable Lables

# Row 1
name_label_2.place(x= 100, y=315)
entry_label_2.place(x= 300, y=320)

# Row 2
name_label_4.place(x= 100, y=375)
entry_label_4.place(x= 300, y=380)

# Row 3
name_label_6.place(x= 100, y=435)
entry_label_6.place(x=300, y=440)

#Row 4
name_label_8.place(x= 100, y=495)
entry_label_8.place(x= 300, y=500)


#  Column 2 of Editable Lables

# Row 1
name_label_3.place(x= 700, y=325)
entry_label_3.place(x= 900, y=330)

# Row 2
name_label_5.place(x= 700, y=385)
entry_label_5.place(x= 900, y=390)

# Row 3
name_label_7.place(x= 700, y=445)
entry_label_7.place(x= 900, y=450)


# Search Button
Button(root, image=search_img, command=search, bd=0).place(x=800,y=260)

# Button to Update
Button(root, text='Update', font=('TimesNewRoman', 18), bd=0, bg='skyblue', padx=50, command=update).place(x=500, y=600)


root.mainloop()