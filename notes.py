#Code writer:Mr ahmad akhshan

#import
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
#window and frame
window =Tk()
window.title("app Tk")
window.geometry("750x600")
window.resizable(width=False,height=False)
frame1=Frame(window)
frame2=Frame(window)
frame3=Frame(window)
frame1.pack()
frame2.pack()
frame3.pack()
#list and x
file=[]
sar_list=[]
save_t=[]
tik=False
#def
def save_text():
    global sar_list
    if str(entry_name.get()) in sar_list and var.get()==0:
        eror()
    else:
        if str(entry_name.get()) in sar_list:
            del file [sar_list.index(str(entry_name.get()))]
            
        save_t.append(str(entry_name.get()))
        sar_list.append(str(entry_name.get()))
        save_t.append(text_t.get(1.0,END))
        file.extend([save_t])
        write_text(file)
        del save_t[0:]
        print(sar_list)
        print(file)
        print(save_t)
def write_text(enter_new_taxt):
    with open('a.CSV','w',newline='') as acsvw:
        write_t=csv.writer(acsvw)
        write_t.writerows(enter_new_taxt)
def eror():
    messagebox.showerror( 'eror','The name is duplicate. If you want to save this text in another text with the same name, check the option at the bottom of the page.')
def opntext():
    x=file[sar_list.index(str(combobox.get()))]
    text_t.delete(1.0,END)
    text_entry.set(x[0])
    text_t.insert(INSERT,x[1])
#read file#Code writer:Mr ahmad akhshan

with open ('a.CSV') as a_csv:
    r=csv.reader(a_csv)
    for i in r:
        file.append(i)
        sar_list.append(i[0])
    sar_list.append('new text')
#tk library
#frame1
combobox=ttk.Combobox(frame1,font=(60),values=sar_list)
combobox.set("new text")
combobox.grid(row=0,column=0)
button_show=Button(frame1,text='open',font=(60),command=opntext)
button_show.grid(row=0,column=1)
#frame2
Label(frame2,text='name text',font=(40)).grid(row=0,column=0)
text_entry=StringVar()
entry_name=Entry(frame2,font=(40),textvariable=text_entry)
entry_name.grid(row=0,column=1)
#frame3

text_t=Text(frame3,font=(40))
text_t.grid(row=0,column=0)
Button(frame3,text='save',font=(40),command=save_text).grid(row=1,column=0)
var=IntVar()
Checkbutton(frame3,text='Save text in another text with the same name',variable=var).grid(row=2,column=0)
#mainloop
#The name is duplicate. If you want to save this text in another text with the same name, check the option at the bottom of the page.
#Are you sure you want to save your text in another text with the same name?
window.mainloop() #Code writer:Mr ahmad akhshan
