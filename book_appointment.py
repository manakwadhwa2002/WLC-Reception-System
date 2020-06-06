# Importing Required Libraries

import random
from tkinter import *
from tkinter import Tk, Label
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from sqlite3 import Error
import os
import datetime as dt
from reportlab.pdfgen import canvas
import qrcode
py=sys.executable

# Creating Window
root = Tk()
root.geometry('1000x685+200+5')
#root.state('zoomed')
root.title('Book Appointment - Wadhwa Legal Consultancy System')# Window Title
root.canvas = Canvas(width=800, height=600)
root.iconbitmap('favicon.ico') # Logo in the Title Bar
root.resizable(False, False)
logo = ImageTk.PhotoImage(Image.open('Logo(200x200).png'))
logo_label = Label(root, image=logo)


# Predefined Non Changable Fixed commands

title = "WLC Appointment Acknowledgement"
logo_image = 'Logo Small White BG.jpg'
head_client = "Client Details"
head_app = "Appointment Details"
head_invoice = "Invoice Details"
head_inst = "Instructions"
app_num = "Appointment Number"
def_apt_num = "WLC/APT/"
client_name = "Client Name"
client_id = "Client ID"
client_ph_num = "Client Ph. No."
app_date = "Appointment Date"
app_time_slot = "Appointment Time"
con_name = "Consultant Name"
inv_num =  "Receipt Number"
fee_stat = "Fees Status"
paid_amt = "Paid Amount"
inst1 = "1.   You need to reach our Office (Office Address, Office Address Street, Office Address City,"
inst2 = "Pin ,ETC). At Least 20 minutes before your appointment and report at the Reception Desk."
inst3 = "2.   If you have not paid the fees then please pay it online via the e-mail link or pay at the"
inst4 = "reception desk before your appointment other wise your appointment will be cancelled."
def_colon = ":"

appointment_date = f"{dt.datetime.now():%a, %d %b %Y}"

# Defining Variables
e = StringVar() 
g = StringVar()
h = StringVar()
i = StringVar()
j = StringVar()
k = StringVar()
l = StringVar()
q = StringVar()
r = StringVar()


# Labels
logo_label.pack()
Label(root, text='Book Appointment', font=('Romanesco', 32,'bold')).pack()

# Row 0
Label(root, text='Appointment ID  :', font=('Verdana', 14, 'bold')).place(x=300, y=300)
Label(root, text='WLC / APT / ', font=('TimesNewRoman', 16)).place(x=510, y=300)
label = Label(root, font=('TimesNewRoman', 16))
label.place(x=635, y=300)

# Row 1
Label(root, text='Client ID', font=('Verdana')).place(x=50, y=360)
Label(root, text='Client Name', font=('Verdana')).place(x=550, y=360)

# Row 2
Label(root, text='Phone Number', font=('Verdana')).place(x=50, y=420)
Label(root, text='Consultant Name', font=('Verdana')).place(x=550, y=420)

# Row 3
Label(root, text='Time Slot', font=('Verdana')).place(x=50, y=480)
Label(root, text='Appointment Date', font=('Verdana')).place(x=550, y=480)

# Row 4
Label(root, text='Service Name', font=('Verdana')).place(x=50, y=540)
Label(root, text='Case Subject', font=('Verdana')).place(x=550, y=540)

# Entry 
Entry(root, textvariable=e, font=('TimesNewRoman', 15), bd=0, bg='#E2E2E2').place(x= 225, y= 360)
Entry(root, textvariable=g, font=('TimesNewRoman', 15), bd=0, bg='#E2E2E2').place(x= 725, y= 360)
Entry(root, textvariable=h, font=('TimesNewRoman', 15), bd=0, bg='#E2E2E2').place(x= 225, y= 420)
Entry(root, textvariable=q, font=('TimesNewRoman', 15), bd=0, bg='#E2E2E2').place(x= 725, y= 540)

# Options (Drop Down)
ttk.Combobox(root, textvariable=i, values=["Sr. Adv. Vinod Wadhwa", "Prof. OP Wadhwa"], width=33,state="readonly").place(x=725, y=420)
ttk.Combobox(root, textvariable=j, values=["09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "01:00 PM", "02:00 PM", "03:00 PM", "04:00 PM", "05:00 PM", "06:00 PM", "07:00 PM", "08:00 PM"], width=33,state="readonly").place(x=225, y=480)
Label(root, text=f"{dt.datetime.now():%a, %d %b %Y}", fg="black", font=("Verdana", 14)).place(x=750,y=477)
ttk.Combobox(root, textvariable=r, values=["Criminal Defense", "Family Law", "Personal Injury", "Civil Law", "RTI Matters", "Service Matters"], width=33,state="readonly").place(x=225, y=540)


# Defining Function for Buttons
def verify():
    if len(e.get()) == 0:
        messagebox.showinfo('Error','Client Id is Required !!!')
    elif len(g.get()) == 0:
        messagebox.showinfo('Error','Client Name is Required !!!')
    elif len(h.get()) == 0:
        messagebox.showinfo('Error','Client Phone Number is Required !!!')
    elif len(h.get()) != 10:    
        messagebox.showinfo('Error','Please Check Client Phone Number !!!')
    elif len(i.get()) == 0:
        messagebox.showinfo('Error','Must Choose a Conusltant !!!')
    elif len(j.get()) == 0:
        messagebox.showinfo('Error','Must Choose a Time Slot !!!')
    elif len(q.get()) == 0:
        messagebox.showinfo('Error','Must Choose a Service Name !!!')
    elif len(r.get()) == 0:
        messagebox.showinfo('Error','Please Enter Case Subject !!!')            
    else:
        find_date = f"{dt.datetime.now():%a, %d %b %Y}"
        conn = sqlite3.connect('wlc_administration_system.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM bookings WHERE date=? AND time_slot=? AND consultant_name=?", [find_date, j.get(), i.get()])
        pc = cur.fetchall()
        cur.close()
        conn.close()
        if pc:
            messagebox.showinfo('Oops!','We already have an Appointment .\n Please Try to Book in some other slot !')
        else:
            insert()
            if True:
                generate()
        




def generate():
    # Generating Details and assigning it to variables

    fileName = str(df) + '.pdf'
    saveFileto = "D:\\Mani Bhai\\Files\\Website\\Python Projects\\WLC Application\\Generated Invoice(s)\\"+fileName
    fileTitle = "WLC / APT / "+str(df)
    get_name = str(g.get())
    get_id = str(e.get())
    get_ph_no = str(h.get())
    get_apt_num = str(df)
    get_apt_date = appointment_date
    get_apt_time = str(j.get())
    get_cons_name = str(i.get())
    get_rct_no = str(genr)
    get_fee_stat = "PAID"
    get_fee_amt = "Rs. 2000.00"

    # Generating QR Code
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=1,
    border=6,
    )
    qr.add_data('Appointment Booked :) \n Appointment Id :'+get_apt_num+'\n Client Id :'+get_id+'\n Fee Status :'+get_fee_stat)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Creating a Canvas for PDF
    pdf = canvas.Canvas(saveFileto)

    # Creating a title PDF
    pdf.setTitle(fileTitle)

    # Placing Image for PDF Main Page
    pdf.drawInlineImage(logo_image, 200, 600)

    # Placing Default Font
    pdf.setFont("Times-Roman", 34)
    pdf.drawString(35, 560, title)

    # Placing Full Length Line Before Client Heading
    pdf.line(0, 542, 700, 542)

    # Placing Client Heading
    pdf.setFont("Helvetica", 18)
    pdf.drawString(235, 520, head_client)
    pdf.line(245, 518, 333, 518) # Decor Line

    # Placing Full Length Line Before Appointment Details
    pdf.line(0, 400, 700, 400)

    # Placing Appointment Heading
    pdf.setFont("Helvetica", 18)
    pdf.drawString(225, 378, head_app)
    pdf.line(235, 376, 375, 376) # Decor Line

    # Placing Full Length Line Invoice Details
    pdf.line(0, 288, 700, 288)

    # Placing Invoice Heading
    pdf.setFont("Helvetica", 18)
    pdf.drawString(245, 266, head_invoice)
    pdf.line(252, 264, 355, 264) # Decor Line

    # Placing Full Length Line Instructions
    pdf.line(0, 166, 700, 166)

    # Placing Instructions Heading
    pdf.setFont("Helvetica", 18)
    pdf.drawString(245, 144, head_inst)
    pdf.line(252, 142, 330, 142) # Decor Line

    # Placing  Other details Default Text

    # 1. Client Name
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(100, 480, client_name)
    pdf.drawString(270, 480, def_colon)

    # 2. Client ID
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(100, 450, client_id)
    pdf.drawString(270, 450, def_colon)

    # 3. Client Phone Number
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(100, 420, client_ph_num)
    pdf.drawString(270, 420, def_colon)

    # 4. Appointment Number
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(20, 338, app_num)
    pdf.drawString(165, 338, def_colon)
    pdf.drawString(190, 338, def_apt_num)

    # 5. Appointment Date
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(20, 308, app_date)
    pdf.drawString(165, 308, def_colon)

    # 6. Appointment Time
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(350, 338, app_time_slot)
    pdf.drawString(480, 338, def_colon)

    # 7. Consultant Name
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(350, 308, con_name)
    pdf.drawString(480, 308, def_colon)   

    # 8. Invoice Number
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(20, 226, inv_num)
    pdf.drawString(165, 226, def_colon)

    # 9. Fees Status
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(20, 196, fee_stat)
    pdf.drawString(165, 196, def_colon)

    # 10. Fees Amount
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(350, 226, paid_amt)
    pdf.drawString(480, 226, def_colon)

    # 11. Instructions
    pdf.setFont("Times-Roman", 14)
    pdf.drawString(10, 106, inst1)
    pdf.drawString(15, 90, inst2)
    pdf.drawString(10, 65, inst3)
    pdf.drawString(15, 49, inst4)

    # Placing Other Details Got Text

    # 1. Get Client Name
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(325, 480, get_name)

    # 2. Get Client ID
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(325, 450, get_id)

    # 3. Get Client Phone Number
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(325, 420, get_ph_no)

    # 4. Get Appointment Number
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(270, 338, get_apt_num)

    # 5. Get Appointment Date
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(185, 308, get_apt_date)
    
    # 6. Get Appointment Time
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(500, 338, get_apt_time)

    #7. Get Consultant Name
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(430, 290, get_cons_name)

    # 8. Get Receipt Number
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(185, 226, get_rct_no)

    # 9. Get Fee Status
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(185, 196, get_fee_stat)

    # 10. Get Fee Amount
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(500, 226, get_fee_amt)

    # Adding QR Code to File 
    pdf.drawInlineImage(img, 500, 750)

    # Saving the created PDF File
    pdf.save()
    if True:
        messagebox.showinfo('Success','Invoice Generated Sucessfully')
        root.destroy()
    else:
        messagebox.showinfo('Error','Some Error Occured !!!')




def insert():
    ent1 = df
    ent2 = e.get()
    ent3 = g.get()
    ent4 = h.get()
    ent5 = i.get()
    ent6 = j.get()
    ent7 = f"{dt.datetime.now():%a, %d %b %Y}"
    ent8 = "PAID"
    ent9 = "Rs. 2000.00"
    ent10 = genr
    ent11 = q.get()
    ent12 = r.get()
    conn = sqlite3.connect('wlc_administration_system.db')
    while conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO bookings(booking_id, client_id, client_name, phone_number, date, time_slot, consultant_name, fee_status, fee_amount, invoice_num, service, case_subject) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(ent1, ent2, ent3, ent4, ent7, ent6, ent5, ent8, ent9, ent10, ent12, ent11,))
        conn.commit()
        if True:
            messagebox.showinfo('Success', 'Appointment has been booked :)')
            ask = messagebox.askyesno('Book Another','Do you want to book\n another appointment?')
            if ask:
                root.destroy()
                os.system("%s %s" % (py, 'book_appointment.py'))
                break
            else:
                root.destroy()  
                break  
        else:
            messagebox.showinfo('Error', 'Failed :(')           

def verify_find():
    if len(j.get()) == 0:
        messagebox.showinfo('Error','Please Select a Time Slot !!!')
    if len(i.get()) == 0:
        messagebox.showinfo('Error','Please Select a Consultant !!!')
    else:
        find()        


def find():
    find_date = f"{dt.datetime.now():%a, %d %b %Y}"
    conn = sqlite3.connect('wlc_administration_system.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookings WHERE date=? AND time_slot=?", [find_date, j.get()])
    pc = cur.fetchall()
    cur.close()
    conn.close()
    if pc:
        messagebox.showinfo('Oops!','We already have an Appointment .\n Please Try to Book in some other slot !')
    else:
        messagebox.showinfo('Success','You can Book Appointement in this slot :)')                


# Buttons

Button(root, text='Book Appointment', bd=0, bg='#003862', fg='white',font=('TimesNewRoman',16), padx=20, pady=5, command=verify).place(x=300, y=600)
Button(root, text='Search', bd=0, bg='#003862', fg='white',font=('TimesNewRoman',16), padx=20, pady=5, command=verify_find).place(x=600, y=600)

# Copyright Label

Label(root, text="Manak Wadhwa | © Copyright 2020 - Wadhwa Legal Consultancy", font=('Verdana', 11, 'bold')).place(x=275, y=660)

# Random Appointment Id Generator

# Establishing Connection 1
conn = sqlite3.connect('wlc_administration_system.db')
cur = conn.cursor()
cur.execute("SELECT booking_id FROM bookings")
pc = cur.fetchall()
cur.close()
conn.close()

# Establishing Connection 2
conn = sqlite3.connect('wlc_administration_system.db')
cur = conn.cursor()
cur.execute("SELECT invoice_num FROM bookings")
transactions = cur.fetchall()
cur.close()
conn.close()

# Verifying Results

all_id = []
for aax in pc:
    for aac in aax:
        all_id.append(int(aac))

all_trans = []
for afa in transactions:
    for aga in afa:
        all_trans.append(int(aga))

def find_unique_id():
    f = 0
    while f < 1000000:
        n = random.randint(1,999999)
        if n in all_id:
            f += 1
        else:
            f = f
            break    
    return n

df = find_unique_id()

def transaction_id():
    trans = 0
    while trans < 1000000000:
        opp = random.randint(1, 999999999)
        if opp in all_trans:
            trans += 1
        else:
            trans = trans
            break
    return opp 

genr = transaction_id()           


def replace():
    label.config(text=str(df))

replace()

root.mainloop()