from tkinter import *
import tkinter.messagebox
from tkinter import messagebox, Toplevel, Button, Tk, Menu
import math

root = Tk()
root.title('My Calcu')

#=========================Menu & Function============================#
def iExit():
    iExit = tkinter.messagebox.askyesno("My Calcu","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Standard():
    root.resizable(width=False,height=False)
    root.geometry("335x433+0+0")

def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("428x598+0+0")

calc = Frame(root)
calc.grid()


menubar = Menu(root)
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File',menu=file)
file.add_command(label="Standard", command=Standard)
file.add_command(label="Scientific", command=Scientific)
file.add_separator()
file.add_command(label="Exit", command=iExit)

edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_separator()
edit.add_command(label="Paste")

help = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help)
help.add_command(label="View Help")

root.config(menu=menubar)

#GUI logic here

#width x height
root.geometry("335x433")
#root.geometry("340x450+0+0")
root.resizable(width=False,height=False)
root.configure(background="powder blue")
root.maxsize(width=428,height=598)
#root.minsize(width=340,height=433)
root.iconbitmap("cal1.ico")
root.configure(bg='white')


def click(number):
    global operator
    operator += str(number)
    tex.set(operator)

def cmexp():
    global operator
    try:
        result = math.exp(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
         messagebox.showinfo("Notification", "Something Wrong", parent=root)

def cmpw():
    global operator
    try:
        result = eval(tex.get()) ** 2
        operator = str(result)
        tex.set(operator)

    except:
         messagebox.showinfo("Notification", "Something Wrong", parent=root)

def cmfct():
    global operator
    try:
        result = math.factorial(eval(tex.get()))
        operator = str(result)
        tex.set(operator)

    except:
         messagebox.showinfo("Notification", "Something Wrong", parent=root)

def cme():
    global operator
    try:
        result = math.e * eval(tex.get())
        operator = str(result)
        tex.set(operator)

    except:
         messagebox.showinfo("Notification", "Something Wrong", parent=root)

def cmpi():
    global operator
    try:
        result = eval(tex.get()) * math.pi
        operator = str(result)
        tex.set(operator)

    except:
         messagebox.showinfo("Notification", "Something Wrong", parent=root)

def clear():
    global operator
    operator = ''
    tex.set(operator)

def equal():
    global operator
    try:
       result = eval(operator)
       operator = str(result)
       tex.set(result)
    except:
       messagebox.showinfo("Notification","Something Wrong",parent=root)

def cmsin():
    global operator
    try:
        result = math.sin(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", "Something Wrong", parent=root)

def cmtan():
    global operator
    try:
        result = math.tan(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", "Something Wrong", parent=root)

def cmcos():
    global operator
    try:
        result = math.cos(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", "Something Wrong", parent=root)

def cmsqrt():
    global operator
    try:
        result = math.sqrt(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", "Something Wrong", parent=root)

def cmlog():
    global operator
    try:
        result = math.log(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", "Something Wrong", parent=root)

def cmsq():
    global operator
    try:
       result = eval(operator)
       operator = str(result)
       tex.set(result)
    except:
       messagebox.showinfo("Notification","Something Wrong",parent=root)

def cmlog10():
    global operator
    try:
        result = math.log10(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", "Something Wrong", parent=root)

def cmcsh():
    global operator
    try:
        result = math.cosh(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", "Something Wrong", parent=root)

def cmsnh():
    global operator
    try:
        result = math.sinh(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", "Something Wrong", parent=root)

def cmtnh():
    global operator
    try:
        result = math.tanh(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", "Something Wrong", parent=root)

#===========================cursor==================================
def on_enter7(e):
    btn7.configure(bg='pink')

def on_leave7(e):
    btn7.configure(bg='powder blue')

def on_enter8(e):
    btn8.configure(bg='pink')

def on_leave8(e):
    btn8.configure(bg='powder blue')

def on_enter9(e):
    btn9.configure(bg='pink')

def on_leave9(e):
    btn9.configure(bg='white')

def on_enteradd(e):
    btnadd.configure(bg='pink')

def on_leaveadd(e):
    btnadd.configure(bg='powder blue')

def on_enter4(e):
    btn4.configure(bg='pink')

def on_leave4(e):
    btn4.configure(bg='white')

def on_enter5(e):
    btn5.configure(bg='pink')

def on_leave5(e):
    btn5.configure(bg='powder blue')

def on_enter6(e):
    btn6.configure(bg='pink')

def on_leave6(e):
    btn6.configure(bg='powder blue')

def on_entersub(e):
    btnsub.configure(bg='pink')

def on_leavesub(e):
    btnsub.configure(bg='white')

def on_enter1(e):
    btn1.configure(bg='pink')

def on_leave1(e):
    btn1.configure(bg='powder blue')

def on_enter2(e):
    btn2.configure(bg='pink')

def on_leave2(e):
    btn2.configure(bg='white')

def on_enter3(e):
    btn3.configure(bg='pink')

def on_leave3(e):
    btn3.configure(bg='powder blue')

def on_enterdiv(e):
    btndiv.configure(bg='pink')

def on_leavediv(e):
    btndiv.configure(bg='powder blue')

def on_enterclear(e):
    btnclear.configure(bg='pink')

def on_leaveclear(e):
    btnclear.configure(bg='powder blue')

def on_enter0(e):
    btn0.configure(bg='pink')

def on_leave0(e):
    btn0.configure(bg='powder blue')

def on_enterequal(e):
    btnequal.configure(bg='pink')

def on_leaveequal(e):
    btnequal.configure(bg='white')

def on_entermul(e):
    btnmul.configure(bg='pink')

def on_leavemul(e):
    btnmul.configure(bg='powder blue')

def on_entercos(e):
    btncos.configure(bg='pink')

def on_leavecos(e):
    btncos.configure(bg='powder blue')

def on_entersin(e):
    btnsin.configure(bg='pink')

def on_leavesin(e):
    btnsin.configure(bg='powder blue')

def on_entertan(e):
    btntan.configure(bg='pink')

def on_leavetan(e):
    btntan.configure(bg='white')

def on_entersqrt(e):
    btnsqrt.configure(bg='pink')

def on_leavesqrt(e):
    btnsqrt.configure(bg='powder blue')

def on_enterlog(e):
    btnlog.configure(bg='pink')

def on_leavelog(e):
    btnlog.configure(bg='powder blue')

def on_entere(e):
    btne.configure(bg='pink')

def on_leavee(e):
    btne.configure(bg='white')

def on_enterpi(e):
    btnpi.configure(bg='pink')

def on_leavepi(e):
    btnpi.configure(bg='white')

def on_enterpow(e):
    btnpow.configure(bg='pink')

def on_leavepow(e):
    btnpow.configure(bg='powder blue')

def on_enterfct(e):
    btnfct.configure(bg='pink')

def on_leavefct(e):
    btnfct.configure(bg='powder blue')

def on_enterexp(e):
    btnexp.configure(bg='pink')

def on_leaveexp(e):
    btnexp.configure(bg='white')

def on_entercom(e):
    btncom.configure(bg='pink')

def on_leavecom(e):
    btncom.configure(bg='powder blue')

def on_enterlog10(e):
    btnlog10.configure(bg='pink')

def on_leavelog10(e):
    btnlog10.configure(bg='powder blue')

def on_entercsh(e):
    btncsh.configure(bg='pink')

def on_leavecsh(e):
    btncsh.configure(bg='white')

def on_entersnh(e):
    btnsnh.configure(bg='pink')

def on_leavesnh(e):
    btnsnh.configure(bg='powder blue')

def on_entertnh(e):
    btntnh.configure(bg='pink')

def on_leavetnh(e):
    btntnh.configure(bg='powder blue')

tex = StringVar()
operator = ''


entry1 = Entry(root,bg='white',font=('arial',18,'italic bold'),bd='30',justify='right',textvariable=tex)
entry1.grid(row=0,columnspan=4)
entry1.insert(0,'0')

btnblnk = Label(root,bg='white',text='Scientific',font=('arial',9,'bold'),bd=6,padx=15,pady=18,activebackground="red",activeforeground="white")
btnblnk.grid(row=0,column=4)

btn7 = Button(root,bg='powder blue',text='7',font=('arial',17,'italic bold'),bd=6,padx=22,pady=17,command=lambda : click(7),activebackground="red",activeforeground="white")
btn7.grid(row=1,column=0)

btn7.bind('<Enter>',on_enter7)
btn7.bind('<Leave>',on_leave7)

btn8 = Button(root,bg='powder blue',text='8',font=('arial',17,'italic bold'),bd=6,padx=20,pady=17,command=lambda : click(8),activebackground="red",activeforeground="white")
btn8.grid(row=1,column=1)

btn8.bind('<Enter>',on_enter8)
btn8.bind('<Leave>',on_leave8)

btn9 = Button(root,text='9',font=('arial',17,'italic bold'),bd=6,padx=20,pady=17,command=lambda : click(9),activebackground="red",activeforeground="white")
btn9.grid(row=1,column=2)

btn9.bind('<Enter>',on_enter9)
btn9.bind('<Leave>',on_leave9)

btnadd = Button(root,bg='powder blue',text='+',font=('arial',17,'italic bold'),bd=6,padx=20,pady=17,command=lambda : click('+'),activebackground="red",activeforeground="white")
btnadd.grid(row=1,column=3)

btnadd.bind('<Enter>',on_enteradd)
btnadd.bind('<Leave>',on_leaveadd)


btn4 = Button(root,text='4',font=('arial',17,'italic bold'),bd=6,padx=21,pady=17,command=lambda : click(4),activebackground="red",activeforeground="white")
btn4.grid(row=2,column=0)

btn4.bind('<Enter>',on_enter4)
btn4.bind('<Leave>',on_leave4)

btn5 = Button(root,bg='powder blue',text='5',font=('arial',17,'italic bold'),bd=6,padx=20,pady=17,command=lambda : click(5),activebackground="red",activeforeground="white")
btn5.grid(row=2,column=1)

btn5.bind('<Enter>',on_enter5)
btn5.bind('<Leave>',on_leave5)

btn6 = Button(root,bg='powder blue',text='6',font=('arial',17,'italic bold'),bd=6,padx=20,pady=17,command=lambda : click(6),activebackground="red",activeforeground="white")
btn6.grid(row=2,column=2)

btn6.bind('<Enter>',on_enter6)
btn6.bind('<Leave>',on_leave6)

btnsub = Button(root,text='-',font=('arial',17,'italic bold'),bd=6,padx=22,pady=17,command=lambda : click('-'),activebackground="red",activeforeground="white")
btnsub.grid(row=2,column=3)

btnsub.bind('<Enter>',on_entersub)
btnsub.bind('<Leave>',on_leavesub)

btn1 = Button(root,bg='powder blue',text='1',font=('arial',17,'italic bold'),bd=6,padx=22,pady=17,command=lambda : click(1),activebackground="red",activeforeground="white")
btn1.grid(row=3,column=0)

btn1.bind('<Enter>',on_enter1)
btn1.bind('<Leave>',on_leave1)

btn2 = Button(root,text='2',font=('arial',17,'italic bold'),bd=6,padx=20,pady=17,command=lambda : click(2),activebackground="red",activeforeground="white")
btn2.grid(row=3,column=1)

btn2.bind('<Enter>',on_enter2)
btn2.bind('<Leave>',on_leave2)

btn3 = Button(root,bg='powder blue',text='3',font=('arial',17,'italic bold'),bd=6,padx=20,pady=17,command=lambda : click(3),activebackground="red",activeforeground="white")
btn3.grid(row=3,column=2)

btn3.bind('<Enter>',on_enter3)
btn3.bind('<Leave>',on_leave3)

btndiv = Button(root,bg='powder blue',text='/',font=('arial',17,'italic bold'),bd=6,padx=23,pady=17,command=lambda : click('/'),activebackground="red",activeforeground="white")
btndiv.grid(row=3,column=3)

btndiv.bind('<Enter>',on_enterdiv)
btndiv.bind('<Leave>',on_leavediv)

btnclear = Button(root,bg='powder blue',text='C',font=('arial',17,'italic bold'),bd=6,padx=20,pady=17, command=clear,activebackground="red",activeforeground="white")
btnclear.grid(row=4,column=0)

btnclear.bind('<Enter>',on_enterclear)
btnclear.bind('<Leave>',on_leaveclear)

btn0 = Button(root,bg='powder blue',text='0',font=('arial',17,'italic bold'),bd=6,padx=20,pady=17,command=lambda : click(0),activebackground="red",activeforeground="white")
btn0.grid(row=4,column=1)

btn0.bind('<Enter>',on_enter0)
btn0.bind('<Leave>',on_leave0)

btnequal = Button(root,text='=',font=('arial',17,'italic bold'),bd=6,padx=20,pady=17,command=equal,activebackground="red",activeforeground="white")
btnequal.grid(row=4,column=2)

btnequal.bind('<Enter>',on_enterequal)
btnequal.bind('<Leave>',on_leaveequal)

btnmul = Button(root,bg='powder blue',text='*',font=('arial',17,'italic bold'),bd=6,padx=21,pady=17,command=lambda : click('*'),activebackground="red",activeforeground="white")
btnmul.grid(row=4,column=3)

btnmul.bind('<Enter>',on_entermul)
btnmul.bind('<Leave>',on_leavemul)

btncos = Button(root,text='cos',bg='powder blue',font=('arial',15,'bold'),bd=6,padx=15,pady=18,activebackground="red",activeforeground="white",command=cmcos)
btncos.grid(row=1,column=4)

btncos.bind('<Enter>',on_entercos)
btncos.bind('<Leave>',on_leavecos)

btnsin = Button(root,bg='powder blue',text='sin',font=('arial',15,'bold'),bd=6,padx=17,pady=18,activebackground="red",activeforeground="white", command=cmsin)
btnsin.grid(row=2,column=4)

btnsin.bind('<Enter>',on_entersin)
btnsin.bind('<Leave>',on_leavesin)

btntan = Button(root,text='tan',font=('arial',15,'bold'),bd=6,padx=17,pady=18,activebackground="red",activeforeground="white", command=cmtan)
btntan.grid(row=3,column=4)

btntan.bind('<Enter>',on_entertan)
btntan.bind('<Leave>',on_leavetan)

btnsqrt = Button(root,bg='powder blue',text='sqrt',font=('arial',15,'bold'),bd=6,padx=14,pady=17,activebackground="red",activeforeground="white",command=cmsqrt)
btnsqrt.grid(row=4,column=4)

btnsqrt.bind('<Enter>',on_entersqrt)
btnsqrt.bind('<Leave>',on_leavesqrt)

btnlog = Button(root,text='log',bg='powder blue',font=('arial',15,'bold'),bd=6,padx=18,pady=17,activebackground="red",activeforeground="white",command=cmlog)
btnlog.grid(row=5,column=4)

btnlog.bind('<Enter>',on_enterlog)
btnlog.bind('<Leave>',on_leavelog)

btne = Button(root,text='e',font=('arial',17,'bold'),bd=6,padx=23,pady=16,activebackground="red",activeforeground="white",command=cme)
btne.grid(row=6,column=4)

btne.bind('<Enter>',on_entere)
btne.bind('<Leave>',on_leavee)

btnpi = Button(root,text='pi',font=('arial',15,'bold'),bd=6,padx=20,pady=16,activebackground="red",activeforeground="white",command=cmpi)
btnpi.grid(row=5,column=3)

btnpi.bind('<Enter>',on_enterpi)
btnpi.bind('<Leave>',on_leavepi)

btnfct = Button(root,text='fct',bg='powder blue',font=('arial',15,'bold'),bd=6,padx=17,pady=16,activebackground="red",activeforeground="white",command=cmfct)
btnfct.grid(row=5,column=2)

btnfct.bind('<Enter>',on_enterfct)
btnfct.bind('<Leave>',on_leavefct)

btnpow = Button(root,text='pow',bg='powder blue',font=('arial',15,'bold'),bd=6,padx=10,pady=15,activebackground="red",activeforeground="white",command=cmpw)
btnpow.grid(row=5,column=1)

btnpow.bind('<Enter>',on_enterpow)
btnpow.bind('<Leave>',on_leavepow)

btnexp = Button(root,text='exp',font=('arial',15,'bold'),bd=6,padx=13,pady=15,activebackground="red",activeforeground="white",command=cmexp)
btnexp.grid(row=5,column=0)

btnexp.bind('<Enter>',on_enterexp)
btnexp.bind('<Leave>',on_leaveexp)

btnlog10 = Button(root,bg='powder blue',text='log10',font=('arial',15,'bold'),bd=6,padx=5.5,pady=16,activebackground="red",activeforeground="white", command = cmlog10)
btnlog10.grid(row=6,column=0)

btnlog10.bind('<Enter>',on_enterlog10)
btnlog10.bind('<Leave>',on_leavelog10)

btncsh = Button(root,text='cosh',font=('arial',15,'bold'),bd=6,padx=8,pady=17,activebackground="red",activeforeground="white", command=cmcsh)
btncsh.grid(row=6,column=1)

btncsh.bind('<Enter>',on_entercsh)
btncsh.bind('<Leave>',on_leavecsh)

btnsnh = Button(root,text='sinh',bg='powder blue',font=('arial',15,'bold'),bd=6,padx=8,pady=17,activebackground="red",activeforeground="white",command=cmsnh)
btnsnh.grid(row=6,column=2)

btnsnh.bind('<Enter>',on_entersnh)
btnsnh.bind('<Leave>',on_leavesnh)

btntnh = Button(root,text='tanh',bg='powder blue',font=('arial',15,'italic bold'),bd=6,padx=8,pady=17,activebackground="red",activeforeground="white", command=cmtnh)
btntnh.grid(row=6,column=3)

btntnh.bind('<Enter>',on_entertnh)
btntnh.bind('<Leave>',on_leavetnh)


root.mainloop()