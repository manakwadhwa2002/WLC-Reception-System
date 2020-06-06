import random
from tkinter import *
from tkinter import Tk, Label, ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import os
import sys

# Creating an Empty list in which numbers will be appended later



# Establishing Data Base Connection

conn = sqlite3.connect('wlc_administration_system.db')
myCursor = conn.cursor()
myCursor.execute("SELECT unique_id FROM client")
pc = myCursor.fetchall()
myCursor.close()
conn.close()

# Looping throught List which contains Tuples & Then Looping through Data Inside Tuples
all_id = []
  
for d in pc:
    for g in d:
        all_id.append(int(g))


# Creating a Window 
root = Tk()
root.geometry("1250x700+60+0")
root.title('New Client Registration - Wadhwa Legal Consultancy System')
root.iconbitmap('favicon.ico')
root.resizable(False, False)

# Defining Variabes

a = StringVar()
b = StringVar()
c = StringVar()
e = StringVar()
f = StringVar()
h = StringVar()
j = StringVar()
k = StringVar()
l = StringVar()
m = StringVar()
v = StringVar()
s = StringVar()
t = StringVar()
aa = StringVar()
# DataBase Table Check

conn = sqlite3.connect('wlc_administration_system.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS client 
(
	unique_id	TEXT,
	first_name	TEXT,
	last_name	TEXT,
	phone_number	TEXT,
	email	TEXT,
	address	TEXT,
	city	TEXT,
	city_pincode	TEXT,
	client_of	TEXT,
	case_category	TEXT,
	case_court	TEXT,
	case_city	TEXT,
	case_subject	TEXT
)''')
conn.commit()

# Display Labels 

logo = ImageTk.PhotoImage(Image.open('Logo(200x200).png'))
logo_label = Label(root, image=logo)

name_label_1 = Label(root, text="Client Id:", font=('Verdana', 16))
label = Label(root, font=('Verdana', 16, 'bold')) # On giving text variable to yhis column it doesn't display the text

name_label_2 = Label(root, text="First Name:", font=('Verdana', 16))
entry_label_2 = Entry(root, textvariable=b, bd=0, bg='#E2E2E2', width=20, font=('TimesNewRoman', 16))

name_label_3 = Label(root, text="Last Name:", font=('Verdana', 16))
entry_label_3 = Entry(root, textvariable=c, bd=0, bg='#E2E2E2', width=20, font=('TimesNewRoman', 16))

name_label_4 = Label(root, text="Phone No:", font=('Verdana', 16))
entry_label_4 = Entry(root, textvariable=e, bd=0, bg='#E2E2E2', width=20, font=('TimesNewRoman', 16))

name_label_5 = Label(root, text="Email Id:", font=('Verdana', 16))
entry_label_5 = Entry(root, textvariable=f, bd=0, bg='#E2E2E2', width=20, font=('TimesNewRoman', 16))

name_label_6 = Label(root, text="Address:", font=('Verdana', 16))
entry_label_6 = Entry(root, textvariable=h, bd=0, bg='#E2E2E2', width=20, font=('TimesNewRoman', 16))

name_label_7 = Label(root, text="City:", font=('Verdana', 16))
entry_label_7 = Entry(root, textvariable=j, bd=0, bg='#E2E2E2', width=20, font=('TimesNewRoman', 16))

name_label_8 = Label(root, text="City Pincode:", font=('Verdana', 16))
entry_label_8 = Entry(root, textvariable=k, bd=0, bg='#E2E2E2', width=20, font=('TimesNewRoman', 16))

name_label_9 = Label(root, text="Client Of:", font=('Verdana', 16))
entry_label_9 = ttk.Combobox(root, textvariable=l, values=["Sr. Adv. Vinod Wadhwa", "Prof. O.P. Wadhwa"], width=37,state="readonly")

name_label_10 = Label(root, text="Case Category:", font=('Verdana', 16))
entry_label_10 = ttk.Combobox(root, textvariable=m, values=["Criminal Defense", "Personal Injury", "Family Law", "Civil Law", "Service Matters", "RTI Matters"], width=37,state="readonly")

name_label_11 = Label(root, text="Case in Court:", font=('Verdana', 16))
entry_label_11 = ttk.Combobox(root, textvariable=v, values=["Delhi High Court", "Punjab & Haryana High Court", "Dwarka District Court", "Not Defined Yet", "Other"], width=37,state="readonly")

name_label_12 = Label(root, text="Case in City", font=('Verdana', 16))
entry_label_12 = Entry(root, textvariable=s, bd=0, bg='#E2E2E2', width=20, font=('TimesNewRoman', 16))

name_label_13 = Label(root, text="Case Subject:", font=('Verdana', 16))
entry_label_13 = Entry(root, textvariable=t, bd=0, bg='#E2E2E2', width=20, font=('TimesNewRoman', 16))

#name_label_14 = Label(root, text="Case State", font=('Verdana', 16))
#entry_label_14 = ttk.Combobox(root, textvariable=, values=["Delhi High Court", "Punjab & Haryana High Court", "Dwarka District Court", "Not Defined Yet", "Other"], width=37,state="readonly")

#############################################################################################

# Place Labels
# Packing The Logo

logo_label.pack()

# Placing Read Only Label

name_label_1.place(x=425, y=225)
label.place(x=725, y=225)

# Column 1 of Editable Lables

# Row 1
name_label_2.place(x= 100, y=300)
entry_label_2.place(x= 300, y=305)

# Row 2
name_label_4.place(x= 100, y=360)
entry_label_4.place(x= 300, y=365)

# Row 3
name_label_6.place(x= 100, y=420)
entry_label_6.place(x=300, y=425)

#Row 4
name_label_8.place(x= 100, y=480)
entry_label_8.place(x= 300, y=485)

# Row 5
name_label_10.place(x= 100, y=540)
entry_label_10.place(x= 300, y=545)

# Row 6
name_label_12.place(x= 100, y=600)
entry_label_12.place(x= 300, y=605)


#  Column 2 of Editable Lables

# Row 1
name_label_3.place(x= 700, y=300)
entry_label_3.place(x= 900, y=305)

# Row 2
name_label_5.place(x= 700, y=360)
entry_label_5.place(x= 900, y=365)

# Row 3
name_label_7.place(x= 700, y=420)
entry_label_7.place(x= 900, y=425)

# Row 4
name_label_9.place(x= 700, y=480)
entry_label_9.place(x= 900, y=485)

# Row 5
name_label_11.place(x= 700, y=540)
entry_label_11.place(x= 900, y=545)

# Row 6
name_label_13.place(x= 700, y=600)
entry_label_13.place(x= 900, y=605)

##############################################################################################
# Defining a Verifying Function
def verify():
    if len(b.get()) == 0:
        messagebox.showinfo('Error','First Name is Required !!!')
    elif len(c.get()) == 0:
        messagebox.showinfo('Error','Last Name is Required !!!')
    elif len(f.get()) == 0:
        messagebox.showinfo('Error','Email ID is Required !!!')
    elif len(h.get()) == 0:
        messagebox.showinfo('Error','Address is Required !!!')
    elif len(j.get()) == 0:
        messagebox.showinfo('Error','City is Required !!!')
    elif len(k.get()) == 0:
        messagebox.showinfo('Error','City Pincode is Required !!!')
    elif len(l.get()) == 0:
        messagebox.showinfo('Error','Client Of is Required !!!')
    elif len(m.get()) == 0:
        messagebox.showinfo('Error','Case Category is Required !!!')
    elif len(v.get()) == 0:
        messagebox.showinfo('Error','Case in Court is Required !!!')
    elif len(s.get()) == 0:
        messagebox.showinfo('Error','Case in City is Required !!!')                    
    elif len(t.get()) == 0:
        messagebox.showinfo('Error','Case Subject is Required !!!')        
    elif len(e.get()) != 10:
        messagebox.showinfo('Error','Phone Number Must be of 10 digits')  
    else:
        insert_client()    


# Defining Function to Insert Client

def insert_client():
    ent1 = a
    ent2 = b.get()
    ent3 = c.get()
    ent4 = e.get()
    ent5 = f.get()
    ent6 = h.get() 
    ent7 = j.get()
    ent8 = k.get()
    ent9 = l.get()
    ent10 = m.get()
    ent11 = v.get()
    ent12 = s.get()
    ent13 = t.get()
    conn = sqlite3.connect('wlc_administration_system.db')
    with conn:
        myCursor = conn.cursor()
        myCursor.execute("INSERT INTO client(unique_id, first_name, last_name, phone_number, email, address, city, city_pincode, client_of, case_category, case_court, case_city, case_subject) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(ent1, ent2, ent3, ent4, ent5, ent6,ent7, ent8, ent9,ent10, ent11, ent12,ent13,))
        if True:
            messagebox.showinfo('Success','Client Data Inserted Sucessfully ! :)')
            ask = messagebox.askyesno('Add New', 'Do you want to add another client ?')
            if ask:
                root.destroy()
                os.system('%s %s' % (py, 'reg_new_client.py'))
            else:
                root.destroy()  
        else:
            messagebox.showinfo('Error','Something Went Wrong Please\ntry again !!! :( ')    

conn.close()

# Display Button
Button(root, text='Add New Client', bd=0, bg='skyblue', fg='black', padx=25, font=('Romanesco', 16), command=verify).place(x=575, y=650)

##############################################################################################

# Defining Read Only Functions
def find_unique_id():
    i = 0
    while i < 1000000:
        n = random.randint(1,999999)
        if n in all_id:
            i += 1
        else:
            i == i
            break
    return n 

a = find_unique_id()
def replace():
    label.config(text=str(a))

replace()

root.mainloop()