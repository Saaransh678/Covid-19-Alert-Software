import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
from csv import DictWriter
from csv import DictReader
import os
win = tk.Tk()
nb = ttk.Notebook(win)
s = ttk.Style()
s.configure('TNotebook.Tab', font=('URW Gothic L','11','bold') )

page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
page3 = ttk.Frame(nb)
win.title('Covid-19 Alert!')
win.wm_iconbitmap('coro.ico')
#########################################################################################################################################3
labels=['Enter Your Name : ','Flat no./Room no. : ','Temperature : ']
info={}
infonam={}
nb.add(page1,text='Register')
nb.add(page2,text='Check for room')
nb.add(page3,text='Check for Resident')
nb.pack(expand=True, fill='both')
for i in range(len(labels)):
    cur_label='label'+str(i)
    cur_label=ttk.Label(page1,text = labels[i])
    cur_label.grid(row=i+1,column=0,sticky=tk.W)
symbol=ttk.Label(page1,text='°F')
symbol.grid(row=2+1,column=2,sticky=tk.W)
name_var=tk.StringVar()
name_entry=ttk.Entry(page1,width=16,textvariable=name_var)
name_entry.grid(row=0+1,column=1,sticky=tk.W, padx=4,pady=4)
flat_var=tk.StringVar()
flat_entry=ttk.Entry(page1,width=16,textvariable=flat_var)
flat_entry.grid(row=1+1,column=1,sticky=tk.W, padx=4,pady=4)
temp_var=tk.StringVar()
temp_entry=ttk.Entry(page1,width=16,textvariable=temp_var)
temp_entry.grid(row=2+1,column=1,sticky=tk.W, padx=4,pady=4)
def submit():
    name=name_var.get()
    flat=flat_var.get()
    temp=temp_var.get()
    if name == '' or flat == '' or temp == '':
        mbox.showerror('Error', 'Please fill all the Details')
    else:
        try:
            temp=float(temp)
        except ValueError:
            mbox.showerror('Error','Only digits are allowed in this field')
        else: 
            with open('Data.csv','a',newline='') as f:
                dict_writer=DictWriter(f,fieldnames=['Name','FlatNo','Temp'])
                if os.stat('Data.csv').st_size==0:
                    dict_writer.writeheader()
                dict_writer.writerow({'Name':name,'FlatNo':flat,'Temp':temp})
            mbox.showinfo('Registration Information','Registered Successfully')
        name_entry.delete(0,tk.END)
        flat_entry.delete(0,tk.END)
        temp_entry.delete(0,tk.END)

submit_btn=ttk.Button(page1, text='Submit',command=submit)
submit_btn.grid(row=3+1,columnspan=2)
#########################################################################################################################################
def check():
    checkin=check_var.get()
    if checkin == '':
        mbox.showerror('Error', 'Please Enter the Flat/Room no.')
    else:
        accum=0.0
        cunt=0
        with open('Data.csv','r') as f:
            csv_reader = DictReader(f)
            for row in csv_reader:
                if(row['FlatNo']==checkin):
                    accum=accum+float(row['Temp'])
                    cunt=cunt+1
            if cunt == 0:
                mbox.showinfo('Information','No Information is available for entered Flat/room')
            else:
                avg=accum/cunt
                if avg>=100.4:
                    mbox.showwarning('Information',f'The Residents of this flat or room has an average temperature of {avg} °F, Maybe a COVID-19 patient')
                else:
                    mbox.showinfo('Information',f'The Residents of this flat or room has an average temperature of {avg} °F, which is normal')
        check_entry.delete(0,tk.END)
        
        


Checkroom_label=ttk.Label(page2,text='Enter the flat/room no.')
Checkroom_label.grid(row=2,column=3, padx=4,pady=4)
check_var=tk.StringVar()
check_entry=ttk.Entry(page2,width=16,textvariable=check_var)
check_entry.grid(row=2,column=4, padx=4,pady=4)
check_btn=ttk.Button(page2, text='Check',command=check)
check_btn.grid(row=3+1,column=3,columnspan=2)
###################################################################################################################################
def check1():
    checkin1=check1_var.get()
    if checkin1 == '':
        mbox.showerror('Error', 'Please Enter the Name of Resident')
    else:
        Note=0.0
        with open('Data.csv','r') as f:
            csv_reader = DictReader(f)
            for row in csv_reader:
                if(row['Name']==checkin1):
                    Note=float(row['Temp'])
        if Note == 0.0:
            mbox.showinfo('Information','No Information is available for the given person')
        else:
            if Note>=100.4:
                mbox.showwarning('Information',f'The person has a high fever of {Note} °F, Maybe a COVID-19 patient')
            else:
                mbox.showinfo('Information','The person is normal and has no fever.')
            check1_entry.delete(0,tk.END)
            

Checkresident_label=ttk.Label(page3,text='Enter the Name of Resident')
Checkresident_label.grid(row=2,column=5, padx=4,pady=4)
check1_var=tk.StringVar()
check1_entry=ttk.Entry(page3,width=16,textvariable=check1_var)
check1_entry.grid(row=2,column=6, padx=4,pady=4)
check1_btn=ttk.Button(page3, text='Check',command=check1)
check1_btn.grid(row=3+1,column=5,columnspan=2)
win.mainloop()