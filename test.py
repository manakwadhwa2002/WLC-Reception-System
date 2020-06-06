# Start  Testing From Here #

from tkinter import *

root = Tk()


def check():
    f_name = Entry(root)
    f_name.pack()
    
    for i in range(1):
        f_name.insert(0, i)







Button(root, text='Check', command=check).pack()

root.mainloop()


'''
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()

g = StringVar()
f = StringVar()


ttk.Combobox(root, textvariable=f, values=['Name','ID']).pack()
Entry(root, textvariable=g).pack()
ent1 = Label(root)


def get():
    if f.get() == 'Name':
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
    elif f.get() == 'ID':
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

def insert(data):
    for row in data:
        listtree.insert('', 'end', text = row[0], values = (row[1]+'  '+row[2], row[3], row[8]))



listtree = ttk.Treeview(root, height=11,columns=('Client Name', 'Client Phone Number', 'Client of'))
listtree.pack()
listtree.heading('#0',text='Client ID')
listtree.heading('Client Name', text='Client Name')
listtree.heading('Client Phone Number', text='Client Phone Number')
listtree.heading('Client of', text='Client of')
listtree.column('#0', anchor='n')
listtree.column('Client Name', anchor='center')
listtree.column('Client Phone Number', anchor='center')
listtree.column('Client of', anchor='center')


Button(root, text='Get', command=get).pack()



root.mainloop()
'''
'''
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()

g = StringVar()
f = StringVar()


ttk.Combobox(root, textvariable=f, values=['Name','ID']).pack()
Entry(root, textvariable=g).pack()
ent1 = Label(root)


def get():
    if f.get() == 'Name':
        conn = sqlite3.connect('wlc_administration_system.db')
        myCursor = conn.cursor()
        myCursor.execute('SELECT * FROM client WHERE first_name like (?)',['%'+g.get()+'%'])
        pc = myCursor.fetchall()
        myCursor.close()
        conn.close()
        if pc:
            print(pc)#messagebox.showinfo('Found!','Record Found')
        else:
            messagebox.showinfo('Error','Oops! no record found :(')
    elif f.get() == 'ID':
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

def insert(data):
    for row in data:
        ent1.config('', 'end')



Button(root, text='Get', command=get).pack()



root.mainloop()
'''
'''
import sqlite3
from tkinter import *

root = Tk()

g = StringVar()

Entry(root, textvariable=g).pack()
label1 = Label(root)
label1.pack()

def get():
    conn = sqlite3.connect('wlc_administration_system.db')
    myCursor = conn.cursor()
    myCursor.execute('SELECT unique_id, first_name, phone_number FROM client')
    pc = myCursor.fetchall()
    myCursor.close()
    conn.close()
    return pc

def replace():
    label1.config(text=str(get()))
    

Button(root, text='Get Data', command=replace).pack()

root.mainloop()
'''
'''
from reportlab.pdfgen import canvas
import qrcode
from tkinter import *
from tkinter import messagebox

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=1,
    border=6,
)

qr.add_data('Appointment Booked :).\n Below are the Details:\n\n   Client Name : Manak\n   Client ID : 45676545\n   Client Ph. No. : 9878967564\n\nBelow are the Appointment Details:\n\n   Appointment No. : 98785676\n   Appointment Date : Mon, 26 May 2020\n   Appointment Time : 10:00 AM\n   Appointment With : Sr. Adv. Vinod Wadhwa \n\nBelow are the Invoice Details\n\n   Fees Status : Paid\n   Invoice Number : 1234567654432')
qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color='white')
img.save('Test.png')
'''
'''
from reportlab.pdfgen import canvas
import qrcode
from tkinter import *
from tkinter import messagebox


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=2,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

pdf = canvas.Canvas('Test QR.pdf')
pdf.drawInlineImage(img, 0, 0)
pdf.save()
'''
'''
from tkinter import *
from tkinter import messagebox
import os
import pyqrcode

window = Tk()
window.title("QR Code Generator")

def generate():
    if len(Subject.get())!=0 :
        global qr,photo
        qr = pyqrcode.create(Subject.get())
        photo = BitmapImage(data = qr.xbm(scale=2))
    else:
        messagebox.showinfo("Please Enter some Subject")
    try:
        showcode()
    except:
        pass

def showcode():
    imageLabel.config(image = photo)
    subLabel.config(text="QR of " + Subject.get())

def save():
    dir = os.getcwd() + "\\QR Codes"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get())!=0:
            qr.png(os.path.join(dir,name.get()+".png"),scale=8)
        else:
            messagebox.showinfo("Please enter a File Name")
    except:
        messagebox.showinfo("Generate the QR code first!")

Sub = Label(window,text="Enter subject")
Sub.grid(row =0,column =0,sticky=N+S+W+E)

FName = Label(window,text="Enter FileName")
FName.grid(row =1,column =0,sticky=N+S+W+E)

Subject = StringVar()
SubEntry = Entry(window,textvariable = Subject)
SubEntry.grid(row =0,column =1,sticky=N+S+W+E)

name = StringVar()
nameEntry = Entry(window,textvariable = name)
nameEntry.grid(row =1,column =1,sticky=N+S+W+E)

button = Button(window,text = "Generate",width=15,command = generate)
button.grid(row =0,column =3,sticky=N+S+W+E)

imageLabel = Label(window)
imageLabel.grid(row =2,column =1,sticky=N+S+W+E)

subLabel = Label(window,text="")
subLabel.grid(row =3,column =1,sticky=N+S+W+E)

saveB = Button(window,text="Save as PNG",width=15) # command=save
saveB.grid(row =1,column =3,sticky=N+S+W+E)

#making this resposnsive
Rows = 3
Columns = 3

for row in range(Rows+1):
    window.grid_rowconfigure(row,weight=1)

for col in range(Columns+1):
    window.grid_columnconfigure(col,weight=1)

 
window.mainloop()
'''

'''
import qrcode
from PIL import Image

face = Image.open('D:\\Mani Bhai\\Files\\Website\\Python Projects\\WLC Application\\favicon.jpg')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=5
)
qr.add_data('HI!!!')
image = qr.make_image().convert('RGB')

pos = (image[0] - face.size[0] // 2, (image[1] - face.size[1]) // 2)

image.paste(face, pos)
image.save('Test QR')
'''

'''
data = "https://google.com"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save('Google Link')
'''

'''
from tkinter import *
import sqlite3

root=Tk()
root.geometry('410x450')
root.title("DataBase using Sqlite3 and Tkinter")

a=StringVar()
b=StringVar()

conn = sqlite3.connect('mysq.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS testuniqueid(id TEXT)")
conn.commit()



lab=Label(root,text='Id:',font=('none 13 bold'))
lab.place(x=0,y=0)

entname=Entry(root,width=20,font=('none 13 bold'),textvar=a)
entname.place(x=80,y=0)


def insert():  
   name1 = a.get()
   conn = sqlite3.connect('wlc_administration_system.db')
   with conn:
      cursor = conn.cursor()
      cursor.execute('INSERT INTO testuniqueid(id) VALUES(?)',(name1,))


conn.close()
   

but=Button(root,padx=2,pady=2,text='Submit',command=insert,font=('none 13 bold'))
but.place(x=60,y=100)   

root.mainloop()
'''
'''
def find_unique_id():
    i = 0
    while i < 12:
        n = random.randint(1,10)
        if n in back:
            i += 1
        else:
            i == i
            break
    return n 

def replace():
    label.config(text=str(find_unique_id()))

replace()
'''

'''
from tkinter import *
from tkinter import Tk, Label
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from sqlite3 import Error
import os
py=sys.executable


root = Tk()
root.geometry('1366x786')
root.state('zoomed')
root.title('Admin Login - Wadhwa Legal Consultancy System')# Window Title
root.canvas = Canvas(width=1366, height=768)
root.iconbitmap('favicon.ico') # Logo in the Title Bar
logo = ImageTk.PhotoImage(Image.open('Logo(300x300).png'))
logo_label = Label(root, image=logo)
a = StringVar()
b = StringVar()

def login():
    if(len(a.get())) < 0:
        messagebox.showinfo('Error',"Nothing in Username")
    elif(len(b.get())) < 0:
        messagebox.showinfo('Error',"Nothing in Password")
    else:
        try:
            conn = sqlite3.connect('wlc_administration_system.db')
            myCursor = conn.cursor()
            myCursor.execute("SELECT * FROM admin WHERE username=? AND password=?", [a.get(), b.get()])
            pc = myCursor.fetchall()
            myCursor.close()
            conn.close()
            if pc:
                messagebox.showinfo('Error', 'Username and password')
            else:
                messagebox.showinfo('Error', 'Username and password not found')
        except:
            messagebox.showinfo('Error',"Something Goes Wrong,Try restarting")

#################################
logo_label.pack()

Entry(root, textvariable=a).pack()
Entry(root, textvariable=b).pack()
Button(root, text="Test", command=login).pack()

root.mainloop()
'''
