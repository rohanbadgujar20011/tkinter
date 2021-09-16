from tkinter import *
import tkinter.messagebox as tsmg
import random
import time
import re
from datetime import datetime

root=Tk()
root.title("ATM")
root.geometry("733x600")
root.minsize(733, 600)
root.maxsize(733, 600)

def search(m):
    def check_Transation(m):
        root3.destroy()
        root4 = Tk()
        root4.title("ATM")
        root4.geometry("733x600")
        root4.minsize(733, 600)

        Label(root4,text="Name:-{}".format(m[0]),font="SegoeUI 20 bold").place(x=100,y=30)

        Label(root4, text="Transation Status:  {} transation till now".format(len(m)-6), font="SegoeUI 15 ").place(x=100, y=70)
        Label(root4, text="Date---------------Time----------Widrawal----------Balance", font="SegoeUI 10 bold").place( x=100, y=120)

        q = 150
        for i in range(6,len(m)):
            p=100

            Label(root4,text=m[i],font=("Arial", 10)).place(x=p,y=q)
            q+=30
        root4.mainloop()

    def check_balance(m):
        tsmg.showinfo("Balance", f"Your account Has {m[4]}")
        ra = root3.place_slaves()
        for x in ra:
            x.destroy()
        Label(root3, text="Thank you Visit Again", font="SegoeUI 30 bold").place(x=200, y=250)

    def confirm(a,l,li,t):
        if(int(a)==int(l)):

            # print(li)
            f = open("ATM.txt", "r")
            q = 0

            for x in f:
                l1 = x.rstrip().split("  ")

                if li[0] in t:
                    if li[1] in t:
                        if li[2] in t:
                            q = 1
                            m = t
                            f.close()
                            break
            if q==1:
                n="  ".join(m)
                m[2]=a
                p="  ".join(m)
                with open("ATM.txt", 'r+') as f:
                    text = f.read()

                    text = re.sub(n, p, text)

                    f.seek(0)
                    f.write(text)
                    f.truncate()





    def Pin_Change(li,t):
        root3.destroy()
        root4 = Tk()
        root4.title("ATM")
        root4.geometry("733x600")
        root4.minsize(733, 600)
        root4.maxsize(733, 600)
        Label(root4, text="Enter New Pin", font="SegoeUI 20 bold").place(x=100, y=100)
        Label(root4, text="Confirme Pin", font="SegoeUI 20 bold").place(x=100, y=200)
        pin=StringVar()
        Con_Pin=StringVar()
        pin_e=Entry(root4,textvariable=pin,width=50).place(x=400,y=108)
        Con_Pin_e = Entry(root4, textvariable=Con_Pin, width=50).place(x=400, y=208)

        Button(root4,text="Ok",command=lambda:[confirm(pin.get(),Con_Pin.get(),li,t)],font=("Arial", 20)).place(x=250,y=308)
        '''with open("ATM.txt", 'r+') as f:
            text = f.readline()


            text = re.sub(t, m, text)

            f.seek(0)
            f.write(text)
            f.truncate()'''


    def withdrawal(m):
        root3.destroy()
        root4 = Tk()
        root4.title("ATM")
        root4.geometry("733x600")
        root4.minsize(733, 600)
        root4.maxsize(733, 600)
        def checkif(a):
            if int(m[4])>=int(a):
                v=int(m[4])-int(a)
                time.sleep(1)
                tsmg.showinfo("collect", f"Collect Your Cash...")
                tsmg.showinfo("Welcome", f"Account Balance is {v}")
                now = datetime.now()
                s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
                tu = s2.split(", ")
                tu.append(a + "Rs")
                tu.append(str(v) + "Rs")
                tu = "----------".join(tu)

                l = "  ".join(m)
                m[4] = str(v)
                m.append(tu)
                o = "  ".join(m)
                with open("ATM.txt", 'r+') as f:
                    text = f.read()
                    text = re.sub(l, o, text)
                    f.seek(0)
                    f.write(text)
                    f.truncate()



                    print("done")
            else:
                tsmg.showinfo("Welcome", f"Sorry Not enough Balance")


            ra = root4.place_slaves()
            for x in ra:
                x.destroy()
            Label(root4,text="Thank you Visit Again",font="SegoeUI 30 bold").place(x=200,y=250)



        p=StringVar()
        Label(root4,text="Enter Your Amount:-",font="SegoeUI 20 bold").place(x=100,y=100)
        p1=Entry(root4,textvariable=p,width=50).place(x=400,y=105)
        Button(root4, text="Confirm",command=lambda :[checkif(p.get())],font=("Arial", 20)).place(x=300, y=400)



        root4.mainloop()


    li=m.split("  ")

    f = open("ATM.txt", "r")
    q = 0

    for x in f:
        l1 = x.rstrip().split("  ")



        if li[0] in l1:
            if li[1] in l1:
                if li[2] in l1:
                    q=1
                    m=l1
                    break


    if q==1:
        root.destroy()
        root3 = Tk()
        root3.title("ATM")
        root3.geometry("733x600")
        root3.minsize(733, 600)
        root3.maxsize(733, 600)
        Label(root3,text="Welcome Back {}".format(l1[0]),font="SegoeUI 20 bold",fg="red").place(x=150,y=50)
        Label(root3, text = "Banking Transation", font = "SegoeUI  30 bold ").place(x=200, y=100)
        Button(root3,text="withdrawal",command=lambda :[withdrawal(m)],font=("Arial", 20)).place(x=270,y=200)
        Button(root3, text="Pin Change",command=lambda:[Pin_Change(li,m)] ,font=("Arial", 20)).place(x=270, y=300)
        Button(root3, text="Check Balance", command=lambda:[check_balance(m)],font=("Arial", 20)).place(x=260, y=400)
        Button(root3, text="Check Transation", command=lambda: [check_Transation(m)], font=("Arial", 20)).place(x=260, y=500)
        root3.mainloop()

    else:
        tsmg.showinfo("Account not found", f"Check your details")



def new_account():


    def file(p):
        f = open("ATM.txt", 'a')
        f.write(p)
        f.close()
        tsmg.showinfo("welcome", f"Account created")
    def id():

        r = random.randint(1, 1000)
        l = 0
        u = open("login.txt")
        for j in u:
            o1 = j.lower().rstrip().split()

            if r in o1:

                l += 1
        if l == 0:

            return r
        else:
            id()


    root.destroy()
    root_1 = Tk()
    root_1.title("Search contact")
    root_1.geometry("733x600")
    root_1.minsize(733, 600)
    root_1.maxsize(733, 600)
    f2 = Frame(root_1, bg="white")
    f2.pack()
    Y = id()
    a = Label(root_1,text="Your account number is {}".format(Y),font="SegoeUI  15 bold ").place(x=180,y=50)

    Name = Label(root_1, text="Name                      :-", font="SegoeUI  15 bold ")
    Name.place(x=170, y=100)
    M_number = Label(root_1, text="Mobile no               :-", font="SegoeUI  15 bold ")
    M_number.place(x=170, y=150)
    Label(root_1, text="Pin Number             :- ", font="SegoeUI  15 bold ").place(x=170, y=200)
    Label(root_1, text="Email adress           :-", font="SegoeUI  15 bold ").place(x=170, y=250)
    Label(root_1, text="Minimum_ amount   :-", font="SegoeUI  15 bold ").place(x=170, y=300)

    Name = StringVar()
    M_no = StringVar()
    Pin_n = StringVar()
    Em_a = StringVar()
    M_A = StringVar()
    s = Entry(root_1, textvariable=Name, width=50)
    s.place(x=400, y=108)
    M_no_e = Entry(root_1, textvariable=M_no, width=50)
    M_no_e.place(x=400, y=158)
    pin_e = Entry(root_1, textvariable=Pin_n,show='*' ,width=50)
    pin_e.place(x=400, y=208)
    Em_e= Entry(root_1, textvariable=Em_a, width=50)
    Em_e.place(x=400, y=258)
    M_A_e = Entry(root_1, textvariable=M_A, width=50)
    M_A_e.place(x=400, y=308)


    bu = Button(root_1, text="Submit",command=lambda: file(s.get() + "  " + M_no_e.get() + "  " + pin_e.get() + "  " +Em_e.get() + "  " +M_A_e.get() + "  "+str(Y) + "\n"),font=("Arial", 15)).place(x=280, y=400)


if __name__ == '__main__':
    Label(root, text="ATM ", pady=40, padx=100, font="SegoeUI  30 bold ").place(x=200,y=10)
    Label(root,text="Enter pin:-",font="SegoeUI 15 bold",pady=5).place(x=200,y=150)
    pi=StringVar()
    M_n=StringVar()
    acoo=StringVar()
    pin_1=Entry(root,textvariable=pi,show='*',width=50).place(x=400,y=163)
    Label(root,text="Mobile number",font="SegoeUI 15 bold",pady=5).place(x=200,y=250)
    m_n_1=Entry(root,textvariable=M_n,width=50).place(x=400,y=262)
    Label(root, text="Account Number", font="SegoeUI 15 bold", pady=5).place(x=200, y=350)
    A= Entry(root, textvariable=acoo, width=50).place(x=400, y=362)
    Button(root,text="CONFIRM",command=lambda:[search(pi.get()+"  "+M_n.get()+"  "+acoo.get())],font="SegoeUI 18 ",pady=5).place(x=320,y=430)


    b=Button(root,text="New account",font="SegoeUI 18 bold",command = new_account,pady=5).place(x=300,y=500)

    root.mainloop()