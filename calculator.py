from tkinter import *
#Code writer:Mr ahmad akhshan
#window..................
w =Tk()
w.title("app Tk")
w.geometry("520x487")
w.resizable(width=False,height=False)

#frame.................
window2=Frame(w)
window2.pack()
window=Frame(w)
window.pack()

#def...................
entry_t_two=""

def button(number):
    global entry_t_two
    global text_entry
    entry_t_two=entry.get() + number
    text_entry.set(entry_t_two)

#def clear.............
def c():
    global text_entry
    text_entry.set("")

#def mohasebe..........
def mohasebe():
    global text_entry
    global tx
    global ltx
    global ltxv
    global moh
    moh=""
    tx=text_entry.get()
    ltx=len(tx)
    for i in range(0,ltx):
        ltxv=tx[i]
        if ltxv in ("1","2","3","4","5","6","7","8","9",".","+","-"):
            moh= moh+ ltxv
        elif ltxv in ("^","%","^2","√","÷","×"):
            if ltxv=="^":
                moh+="**"
            if ltxv=="^2":
                moh+="**2"
            if ltxv=="√":
                moh+="**0.5"
            if ltxv=="÷":
                moh+="/"
            if ltxv=="×":
                moh+="*"
            if ltxv=="%":
                moh+="*0.01"
        else:
            moh="eror!!!"
    text_entry.set(eval(moh))

#one clear................
txoc=""
ntxoc=str()
atxoc=""
def one_clear():
    global txoc
    global ntxoc
    global atxoc
    txoc=text_entry
    ntxoc = len(txoc.get())
    ntxoc-=1
    atxoc = txoc.get()[:ntxoc]
    text_entry.set(atxoc)

#entry....................
text_entry=StringVar()
entry=Entry(window,bd=30,font=("Tahoma",32),textvariable=text_entry)
entry.grid(row=0, column=0, columnspan=4)

#Code writer:Mr ahmad akhshan

#Button..................

#row1....................
rw1=2

by=Button(window,text="x^y",font=(30),height=2,width=12,bd=8,command=lambda:button("^"))
by.grid(row=rw1,column=0)

da=Button(window,text="%",font=(30),height=2,width=12,bd=8,command=lambda:button("%"))
da.grid(row=rw1,column=1)

c=Button(window,text="c",font=(30),height=2,width=12,bd=8,command=c)
c.grid(row=rw1,column=2)

co=Button(window,text="←",font=(30),height=2,width=12,bd=8,command=one_clear)
co.grid(row=rw1,column=3)

#row2....................
rw2=3

b2=Button(window,text="x^2",font=(30),height=2,width=12,bd=8,command=lambda:button("^2"))
b2.grid(row=rw2,column=0)

r=Button(window,text="√",font=(30),height=2,width=12,bd=8,command=lambda:button("√"))
r.grid(row=rw2,column=1)

t=Button(window,text="÷",font=(30),height=2,width=12,bd=8,command=lambda:button("÷"))
t.grid(row=rw2,column=2)

z=Button(window,text="×",font=(30),height=2,width=12,bd=8,command=lambda:button("×"))
z.grid(row=rw2,column=3)

#row3...................
rw3=4

B7=Button(window,text="7",font=(30),height=2,width=12,bd=8,command=lambda:button("7"))
B7.grid(row=rw3,column=0)

B8=Button(window,text="8",font=(30),height=2,width=12,bd=8,command=lambda:button("8"))
B8.grid(row=rw3,column=1)

B9=Button(window,text="9",font=(30),height=2,width=12,bd=8,command=lambda:button("9"))
B9.grid(row=rw3,column=2)

m=Button(window,text="-",font=(30),height=2,width=12,bd=8,command=lambda:button("-"))
m.grid(row=rw3,column=3)
#Code writer:Mr ahmad akhshan

#row4...........................
rw4=5

B4=Button(window,text="4",font=(30),height=2,width=12,bd=8,command=lambda:button("4"))
B4.grid(row=rw4,column=0)

B5=Button(window,text="5",font=(30),height=2,width=12,bd=8,command=lambda:button("5"))
B5.grid(row=rw4,column=1)

B6=Button(window,text="6",font=(30),height=2,width=12,bd=8,command=lambda:button("6"))
B6.grid(row=rw4,column=2)

j=Button(window,text="+",font=(30),height=2,width=12,bd=8,command=lambda:button("+"))
j.grid(row=rw4,column=3)

#row5...................................
rw5=6

b1=Button(window,text="1",font=(30),height=2,width=12,bd=8,command=lambda:button("1"))
b1.grid(row=rw5,column=0)

b2=Button(window,text="2",font=(30),height=2,width=12,bd=8,command=lambda:button("2"))
b2.grid(row=rw5,column=1)

b3=Button(window,text="3",font=(30),height=2,width=12,bd=8,command=lambda:button("3"))
b3.grid(row=rw5,column=2)

h=Button(window,text="=",font=(30),height=5,width=12,bd=8,command=mohasebe)
h.grid(row=rw5,column=3,rowspan=2)

#row6...............................
rw6=7

gh=Button(window,text="+/-",font=(30),height=2,width=12,bd=8,command=lambda:button("-"))
gh.grid(row=rw6,column=0)

b0=Button(window,text="0",font=(30),height=2,width=12,bd=8,command=lambda:button("0"))
b0.grid(row=rw6,column=1)

d=Button(window,text=".",font=(30),height=2,width=12,bd=8,command=lambda:button("."))
d.grid(row=rw6,column=2)

#end....................
window.mainloop()
#Code writer:Mr ahmad akhshan
