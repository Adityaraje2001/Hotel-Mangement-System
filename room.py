from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime

from mysql.connector import cursor

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x500+240+250")
        #==v
        self.var_conatct=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        
        

        #===title==
        lb1_title=Label(self.root,text="ROOM BOOKING",font=("Arial",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lb1_title.place(x=0,y=0,width=1295,height=50)

    #=====logo=======
        img2=Image.open(r"C:\Users\desai\OneDrive\Desktop\hotel mangement\hotel_images\logohotel.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)
    
    #======label frame====
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="RoomBooking Details",font=("Arial",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=425,height=490)
    #===label and entries==
    #===cust Contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("Arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_conatct,width=20,font=("Arial",13,"bold"))
        enty_contact.grid(row=0,column=1)
        #==Fetch DATa BUtton==
        btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("Arial",8,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=347,y=4)
    #===Check IN 
        check_in_date=Label(labelframeleft,text="Check in Date",font=("Arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_data=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=20,font=("Arial",13,"bold"))
        txtcheck_in_data.grid(row=1,column=1)
    #===Check Out===
        lb1_Check_out=Label(labelframeleft,text="Check out Date",font=("Arial",12,"bold"),padx=2,pady=6)
        lb1_Check_out.grid(row=2,column=0,sticky=W)

        txt_Check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=20,font=("Arial",13,"bold"))
        txt_Check_out.grid(row=2,column=1)
    #===Room Type==
        label_RoomType=Label(labelframeleft,font=("Arial",12,"bold"),text="Room Type",padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)
        conn=mysql.connector.connect(host="localhost",username="root",password="@Di302001",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("Arial",12,"bold"),width=20,state="readonly")
        combo_RoomType["value"]=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=4,column=1)
    #===Available Room==
        lb1RoomAvailable=Label(labelframeleft,text="Available Room",font=("Arial",12,"bold"),padx=2,pady=6)
        lb1RoomAvailable.grid(row=4,column=0,sticky=W)

        #txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=22,font=("Arial",13,"bold"))
        #txtRoomAvailable.grid(row=4,column=1)
        conn=mysql.connector.connect(host="localhost",username="root",password="@Di302001",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("Arial",12,"bold"),width=20,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=3,column=1)
    #==Meals==
        lb1Meal=Label(labelframeleft,text="Meals",font=("Arial",12,"bold"),padx=2,pady=6)
        lb1Meal.grid(row=5,column=0,sticky=W)

        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,width=20,font=("Arial",13,"bold"))
        txtMeal.grid(row=5,column=1)
    #No of DAYS===
        lb1NoofDays=Label(labelframeleft,text="No of DAYS",font=("Arial",12,"bold"),padx=2,pady=6)
        lb1NoofDays.grid(row=6,column=0,sticky=W)

        txtNoofDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=20,font=("Arial",13,"bold"))
        txtNoofDays.grid(row=6,column=1)
    #==Paid Tax==
        lb1NoofDays=Label(labelframeleft,text="Paid Tax",font=("Arial",12,"bold"),padx=2,pady=6)
        lb1NoofDays.grid(row=7,column=0,sticky=W)

        txtNoofDays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=20,font=("Arial",13,"bold"))
        txtNoofDays.grid(row=7,column=1)
    #==Sub Total==
        lb1NoofDays=Label(labelframeleft,text="Sub Total",font=("Arial",12,"bold"),padx=2,pady=6)
        lb1NoofDays.grid(row=8,column=0,sticky=W)

        txtNoofDays=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=20,font=("Arial",13,"bold"))
        txtNoofDays.grid(row=8,column=1)
    #===Toatl==
        lb1IdNumber=Label(labelframeleft,text="Total",font=("Arial",12,"bold"),padx=2,pady=6)
        lb1IdNumber.grid(row=9,column=0,sticky=W)

        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_total,width=20,font=("Arial",13,"bold"))
        txtIdNumber.grid(row=9,column=1)

    #==Bill Button==
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("Arial",12,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)


    #====btn=====
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("Arial",12,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("Arial",12,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("Arial",12,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("Arial",12,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)
        #===RightSide Image===
        img3=Image.open(r"C:\Users\desai\OneDrive\Desktop\hotel mangement\hotel_images\bed.jpg")
        img3=img3.resize((520,300),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=520,height=200)


        #===table frame search system==
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text=" View Customer Details",font=("Arial",12,"bold"),padx=2,)
        Table_frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Table_frame,font=("Arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W)

        self.serch_var=StringVar()
        combo_Search=ttk.Combobox(Table_frame,textvariable=self.serch_var,font=("Arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Conatact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        #self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_frame,width=24,font=("Arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)
        btnSearch=Button(Table_frame,text="Search",font=("Arial",12,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowall=Button(Table_frame,text="Showall",command=self.fetch_data,font=("Arial",12,"bold"),bg="black",fg="gold",width=10)
        btnShowall.grid(row=0,column=4,padx=1)

        #==Show DATa
        details_table=Frame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,columns=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfDays"),xscrollcommand=scroll_x.set ,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Conatact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room-Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfDays",text="NoOfDays")
        
        
        self.room_table["show"]="headings"
        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfDays",width=100)
        

        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #===add data
    def add_data(self):
        if self.var_conatct.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","Fill all fields",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="@Di302001",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_conatct.get(),
                                                                                    self.var_checkin.get(),
                                                                                    self.var_checkout.get(),
                                                                                    self.var_roomtype.get(),
                                                                                    self.var_roomavailable.get(),
                                                                                    self.var_meal.get(),
                                                                                    self.var_noofdays.get()
                                                                                    
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()                                                                
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning","Some thing went wrong:{str(es)}",parent=self.root)
    
    #==Fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@Di302001",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #==get cursor

    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]
        self.var_conatct.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

    #==Update
    def update(self):
        if self.var_conatct.get()=="":
            messagebox.showerror("Error","Please Enter Mobile No",parent=self.root)
        else:    
            conn=mysql.connector.connect(host="localhost",username="root",password="@Di302001",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtypel=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(
                                                                                                                                        
                                                                                                                                       self.var_checkin.get(),
                                                                                                                                       self.var_checkout.get(),
                                                                                                                                       self.var_roomtype.get(),
                                                                                                                                       self.var_roomavailable.get(),
                                                                                                                                       self.var_meal.get(),
                                                                                                                                       self.var_noofdays.get(),

                                                                                                                                       self.var_conatct.get()
                                                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer deatils updated",parent=self.root)
    #==Delete==
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this room details",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="@Di302001",database="management")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_conatct.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    #===Reset==
    def reset(self):
        self.var_conatct.set(""),
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
        
    #===Search==
    def search(self):
    
        conn=mysql.connector.connect(host="localhost",username="root",password="@Di302001",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where "+ str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
               self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
       
    #===All Data Fetch==
    def Fetch_contact(self):
        if self.var_conatct.get()=="":
            messagebox.showerror("Error","Please Enter the Contact No",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="@Di302001",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_conatct.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)
                #==Nmae

                lb1Name=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lb1Name.place(x=0,y=0)

                lb1=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lb1.place(x=90,y=0)
                #===Gender
                conn=mysql.connector.connect(host="localhost",username="root",password="@Di302001",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_conatct.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lb1Gender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lb1Gender.place(x=0,y=30)
            
                lb1=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lb1.place(x=90,y=30)
                #===Idproof
                conn=mysql.connector.connect(host="localhost",username="root",password="@Di302001",database="management")
                my_cursor=conn.cursor()
                query=("select Idproof from customer where Mobile=%s")
                value=(self.var_conatct.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lb1Idproof=Label(showDataframe,text="Idproof:",font=("arial",12,"bold"))
                lb1Idproof.place(x=0,y=60)

                lb2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lb2.place(x=90,y=60)

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Luxury"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Duplex"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

            
            









if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()       