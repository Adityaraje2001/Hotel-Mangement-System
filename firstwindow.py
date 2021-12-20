from logging import root
from os import curdir
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import random
import time
import datetime
from hotel import HotelManagementSystem



def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()
class Login_Window:
    def __init__(self,root):
        #self.var_email=StringVar()
        #self.var_password=StringVar()
        self.root=root
        self.root.title("Welcome")
        self.root.geometry("1550x800+0+0")
        self.bg=ImageTk.PhotoImage(file=r"b2.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        title=Label(frame,text="Welcome",font=("Arial ",20,"bold"),bg="black",fg="Red").place(x=120,y=30)

        useraname=lbl=Label(frame,text="Email Id",font=("Arial",15,"bold"),bg="black",fg="white")
        useraname.place(x=60,y=145)

        self.txtuser=Entry(frame,font=("Arial",15),bg="lightgray",)
        self.txtuser.place(x=60,y=180,width=250)

        
        password=Label(frame,text="Password",font=("Arial",15,"bold"),bg="black",fg="white")
        password.place(x=60,y=250)
        self.txtpass=Entry(frame,font=("Arial",15),bg="lightgray",)
        self.txtpass.place(x=60,y=280,width=250)

        loginbtn=Button(frame,text="Login",command=self.login,font=("Arial",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=120,y=320,width=100,height=35)

        registerbtn=Button(frame,text="New user",command=self.rigister_window,font=("Arial",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="black")
        registerbtn.place(x=110,y=350,width=120,height=35)

        forgetbtn=Button(frame,text="forget Password",font=("Arial",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="black")
        forgetbtn.place(x=110,y=380,width=120,height=35)

    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome to Hotel Grand Resort")
        else: 
            conn=mysql.connector.connect(host="localhost",user="root",password="@Di302001",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from new_table where email=%s and password=%s",(
                                                                              self.txtuser.get(),
                                                                              self.txtpass.get()
                                                                                  
                                                                           ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
                messagebox.showinfo("Success","Welcome to Hotel Grand Resort")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main > 0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Form")
        self.root.geometry("1600x900+0+0")

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        #===BgImage==
        self.bg=ImageTk.PhotoImage(file="b2.png")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

       #==Register Frame==
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        register_lbl=Label(frame,text="Register Here",font=("Arial",20,"bold"),bg="white",fg="Red").place(x=50,y=30)

        
        fname=Label(frame,text="First Name",font=("Arial",15,"bold"),bg="white",fg="gray")
        fname .place(x=100,y=100)
        fname_entry=Entry(frame,textvariable=self.var_fname,font=("Arial",15),bg="lightgray",)
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="last Name",font=("Arial",15,"bold"),bg="white",fg="gray")
        l_name.place(x=370,y=100)
        self.txt_lname=Entry(frame,textvariable=self.var_lname,font=("Arial",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)

        contact=Label(frame,text="Contact",font=("Arial",15,"bold"),bg="white",fg="gray")
        contact.place(x=50,y=170)
        self.txt_contact=Entry(frame,textvariable=self.var_contact,font=("Arial",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Mail Id",font=("Arial",15,"bold"),bg="white",fg="gray")
        email.place(x=370,y=170)
        self.txt_email=Entry(frame,textvariable=self.var_email,font=("Arial",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)

        security_Q=Label(frame,text="Security Question",font=("Arial",15,"bold"),bg="white",fg="gray")
        security_Q.place(x=50,y=240)
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("Arial",13),state='readonly',justify=CENTER)
        self.combo_security_Q['values']=("Select","Your first pet name","Your Birth Place","Your Best Friend Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        answer=Label(frame,text="answer",font=("Arial",15,"bold"),bg="white",fg="gray")
        answer.place(x=370,y=240)
        
        self.txt_answer=Entry(frame,textvariable=self.var_securityA,font=("Arial",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)

        pswd=Label(frame,text="Password",font=("Arial",15,"bold"),bg="white",fg="gray")
        pswd.place(x=50,y=310)
        self.txt_pswd=Entry(frame,textvariable=self.var_pass,font=("Arial",15),bg="lightgray")
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("Arial",15,"bold"),bg="white",fg="gray")
        confirm_pswd.place(x=370,y=310)
        self.txt_confirm_pswd=Entry(frame,textvariable=self.var_confpass,font=("Arial",15),bg="lightgray")
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        btn=Button(frame,text="Submit",command=self.register_data).place(x=50,y=420)
        btn=Button(frame,text="Sign In").place(x=370,y=420)

    #====function====
    def register_data(self):
        if self.var_fname.get()==""  or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Invalid Password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="@Di302001",database="management")
            cur=conn.cursor()
            query=("select * from new_table where email=%s")
            value=(self.var_email.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                cur.execute("insert into new_table values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                      ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Sucessfully")



if __name__=="__main__":
    main()