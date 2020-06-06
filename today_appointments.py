from tkinter import *
from tkinter import Tk, Label
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
import datetime as dt
from reportlab.pdfgen import canvas
from sqlite3 import Error
import os,sys

root = Tk()
root.geometry('1000x700+100+0')
root.title("Today's Appointments - Wadhwa Legal Consultancy System")


# Defining Text Variables
d = StringVar()

# Predefined Non Changable Fixed commands
logo_image = 'Logo Small White BG.jpg'

# Logo
logo = ImageTk.PhotoImage(Image.open('Logo(200x200).png'))
logo_label = Label(root, image=logo)
logo_label.pack()


# Heading
Label(root, text='Today(s) Appointments', font=('Romanesco', 32)).pack()

# Lables
Label(root, text='For Consultant', font=('TimesNewRoman', 16)).place(x=200, y=300)
ttk.Combobox(root, textvariable=d, values=['Sr. Adv. Vinod Wadhwa', 'Prof. OP Wadhwa'], state='readonly',width=45).place(x=400, y=305)

def verify():
    if len(d.get()) == 0:
        messagebox.showinfo('Error','Please Select a Consultant !!!')
    else:
        printing()    

def printing():
    global pc
    conn = sqlite3.connect('wlc_administration_system.db')
    myCursor = conn.cursor()
    myCursor.execute('SELECT * FROM bookings WHERE consultant_name like (?) AND fee_status = ?',[d.get(), 'PAID'])
    pc = myCursor.fetchall()
    myCursor.close()
    conn.close()
    if pc:
        generate()
    else:
        messagebox.showinfo('Oops!',"No Appointment's today !!!")    



def generate():
    today = f"{dt.datetime.now():%a, %d %b %Y}"
    fileName = d.get()+' appointments for '+today+'.pdf'
    saveFileto = "D:\\Mani Bhai\\Files\\Website\\Python Projects\\WLC Application\\Conusltants Appointments\\"+fileName
    fileTitle = "Appointments List of "+d.get()+' for '+today
    ack = d.get()+" Today's Appointments"

    # Canvas
    pdf = canvas.Canvas(saveFileto)

    # PDF Title 
    pdf.setTitle(fileTitle)

    # Placing Image for PDF Main Page
    pdf.drawInlineImage(logo_image, 200, 625)

    # Placing Heading 
    pdf.setFont("Times-Roman", 34)
    pdf.drawString(20, 575, ack)

    # Seprating Line
    pdf.line(0, 550, 700, 550)

    # Placing Column Headings
    pdf.setFont("Times-Roman", 18)
    pdf.drawString(25, 525, 'Client Name')
    pdf.drawString(175, 525, 'Time')
    pdf.drawString(275, 525, 'Service Name')
    pdf.drawString(450, 525, 'Case Subject')

    # Seprating Line 2
    pdf.line(0, 515, 700, 515)

    # Vertical Lines to seprate columns
    pdf.line(140, 550, 140, 0)
    pdf.line(250, 550, 250, 0)
    pdf.line(400, 550, 400, 0)

    # Making Lines
    x = 40
    x1 = 165
    x2 = 275
    x3 = 425
    y = 490
    y1 = 480
    pdf.setFont('Times-Roman', 14)
    for row in pc:
        pdf.drawString(x, y, row[2])
        pdf.drawString(x1, y, row[5])
        pdf.drawString(x2, y, row[10])
        pdf.drawString(x3, y, row[11])
        pdf.line(0, y1, 700, y1)
        x = x
        y -= 25
        y1 -= 25


    # Saving PDF
    pdf.save()




Button(root, text='Print Today(s) Appointments', font=('TimesNewRoman', 16), bd=0, bg='skyblue', padx=50, command=verify).place(x=300, y=600)


root.mainloop()