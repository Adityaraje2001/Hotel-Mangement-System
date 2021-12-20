
from tkinter import*
from PIL import Image,ImageTk 
from customer import Cust_Win
from room import Roombooking
from details import DeatailsRoom


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")



        #======== 1st img ============
        img1=Image.open(r"C:\Users\desai\OneDrive\Desktop\hotel mangement\hotel_images\hotel1.png")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
        
        #=====logo=======
        img2=Image.open(r"C:\Users\desai\OneDrive\Desktop\hotel mangement\hotel_images\logohotel.png")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)
        
        #===title==
        lb1_title=Label(self.root,text="Hotel MANAGEMENT SYSTEM",font=("Arial",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lb1_title.place(x=0,y=140,width=1550,height=50)

        #======frame===
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #====menu===
        lb1_menu=Label(main_frame,text="MENU",font=("Arial",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lb1_menu.place(x=0,y=0,width=230)

        #===btnframe===
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=120)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("Arial",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=1,column=0,pady=1)

        room_btn=Button(btn_frame,text="room",command=self.roombooking,width=22,font=("Arial",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=2,column=0,pady=1)

        details_btn=Button(btn_frame,text="details",command=self.details_room,width=22,font=("Arial",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=3,column=0,pady=1)

        '''report_btn=Button(btn_frame,text="report",width=22,font=("Arial",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="logout",width=22,font=("Arial",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)'''
  
    
    #=====right img==
    
        img3=Image.open(r"C:\Users\desai\OneDrive\Desktop\hotel mangement\hotel_images\slide3.jpg")
        img3=img3.resize((1310,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=225,y=0,width=1310,height=590)
        
#===down img
        img4=Image.open(r"C:\Users\desai\OneDrive\Desktop\hotel mangement\hotel_images\down.jpg")
        img4=img4.resize((230,400),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=155,width=230,height=210)
        

        img5=Image.open(r"C:\Users\desai\OneDrive\Desktop\hotel mangement\hotel_images\food.jpg")
        img5=img5.resize((230,250),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=355,width=230,height=230)
        
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)   

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)
    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DeatailsRoom(self.new_window)




if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()