from sqlite3.dbapi2 import connect
from tkinter import *
from tkinter.font import BOLD
import time, sys
from tkinter import ttk, messagebox
import sqlite3
from admin_dashboard import admin_dashboard


#GUI
class Admin_Login:


        def __init__(self,root):
                self.root=root
                self.root.geometry('1200x550+50+50')
                self.root.title(' PRISM Taxi Booking Service"')
                self.root.config(bg='white')

#Icon
                photo_icon = PhotoImage(file='Image/small.png')
                self.root.iconphoto(False,photo_icon)
# Display Left to right    #top corner
                self.photo_bg0= PhotoImage(file='Image/small.png')
                self.photo_bg_label0 =Label(self.root,image=self.photo_bg0).place(x=0,y=0,width=100,height=100)

                self.photo_bg1= PhotoImage(file='Image/small.png')
                self.photo_bg_label1 =Label(self.root,image=self.photo_bg1).place(x=110,y=0,width=100,height=100)

                self.photo_bg2= PhotoImage(file='Image/small.png')
                self.photo_bg_label2 =Label(self.root,image=self.photo_bg2).place(x=220,y=0,width=100,height=100)

                self.photo_bg3= PhotoImage(file='Image/small.png')
                self.photo_bg_label3 =Label(self.root,image=self.photo_bg3).place(x=330,y=0,width=100,height=100)

                self.photo_bg4= PhotoImage(file='Image/small.png')
                self.photo_bg_label4 =Label(self.root,image=self.photo_bg4).place(x=440,y=0,width=100,height=100)

                self.photo_bg5= PhotoImage(file='Image/small.png')
                self.photo_bg_label5 =Label(self.root,image=self.photo_bg5).place(x=550,y=0,width=100,height=100)

                self.photo_bg6= PhotoImage(file='Image/small.png')
                self.photo_bg_label6 =Label(self.root,image=self.photo_bg6).place(x=660,y=0,width=100,height=100)

                self.photo_bg7= PhotoImage(file='Image/small.png')
                self.photo_bg_label7 =Label(self.root,image=self.photo_bg7).place(x=770,y=0,width=100,height=100)

                self.photo_bg8= PhotoImage(file='Image/small.png')
                self.photo_bg_label8 =Label(self.root,image=self.photo_bg8).place(x=880,y=0,width=100,height=100)

                self.photo_bg9= PhotoImage(file='Image/small.png')
                self.photo_bg_label9 =Label(self.root,image=self.photo_bg9).place(x=990,y=0,width=100,height=100)

                self.photo_bg10= PhotoImage(file='Image/small.png')
                self.photo_bg_label10 =Label(self.root,image=self.photo_bg10).place(x=1100,y=0,width=100,height=100)


#Display Top to bottom Left corner
        

                self.photo_bg11= PhotoImage(file='Image/small.png')
                self.photo_bg_label11 =Label(self.root,image=self.photo_bg11).place(x=0,y=110,width=100,height=100)

                self.photo_bg12= PhotoImage(file='Image/small.png')
                self.photo_bg_label12 =Label(self.root,image=self.photo_bg12).place(x=0,y=220,width=100,height=100)

                self.photo_bg13= PhotoImage(file='Image/small.png')
                self.photo_bg_label13 =Label(self.root,image=self.photo_bg13).place(x=0,y=330,width=100,height=100)

                self.photo_bg14= PhotoImage(file='Image/small.png')
                self.photo_bg_label14 =Label(self.root,image=self.photo_bg14).place(x=0,y=440,width=100,height=100)

                self.photo_bg15= PhotoImage(file='Image/small.png')
                self.photo_bg_label15 =Label(self.root,image=self.photo_bg15).place(x=0,y=550,width=100,height=100)

                self.photo_bg16= PhotoImage(file='Image/small.png')
                self.photo_bg_label16 =Label(self.root,image=self.photo_bg16).place(x=0,y=660,width=100,height=100)

       

# Display Left to right Bottom corner 

                self.photo_bg21= PhotoImage(file='Image/small.png')
                self.photo_bg_label21=Label(self.root,image=self.photo_bg21).place(x=0,y=660,width=100,height=100)

                self.photo_bg22= PhotoImage(file='Image/small.png')
                self.photo_bg_label22 =Label(self.root,image=self.photo_bg22).place(x=110,y=660,width=100,height=100)

                self.photo_bg23= PhotoImage(file='Image/small.png')
                self.photo_bg_label23 =Label(self.root,image=self.photo_bg23).place(x=220,y=660,width=100,height=100)

                self.photo_bg24= PhotoImage(file='Image/small.png')
                self.photo_bg_label24 =Label(self.root,image=self.photo_bg24).place(x=330,y=660,width=100,height=100)

                self.photo_bg25= PhotoImage(file='Image/small.png')
                self.photo_bg_label25 =Label(self.root,image=self.photo_bg25).place(x=440,y=660,width=100,height=100)

                self.photo_bg26= PhotoImage(file='Image/small.png')
                self.photo_bg_label26 =Label(self.root,image=self.photo_bg26).place(x=550,y=660,width=100,height=100)

                self.photo_bg27= PhotoImage(file='Image/small.png')
                self.photo_bg_label27 =Label(self.root,image=self.photo_bg27).place(x=660,y=660,width=100,height=100)

                self.photo_bg28= PhotoImage(file='Image/small.png')
                self.photo_bg_label28 =Label(self.root,image=self.photo_bg28).place(x=770,y=660,width=100,height=100)

                self.photo_bg29= PhotoImage(file='Image/small.png')
                self.photo_bg_label29 =Label(self.root,image=self.photo_bg29).place(x=880,y=660,width=100,height=100)

                self.photo_bg30= PhotoImage(file='Image/small.png')
                self.photo_bg_label30 =Label(self.root,image=self.photo_bg30).place(x=990,y=660,width=100,height=100)

                self.photo_bg31= PhotoImage(file='Image/small.png')
                self.photo_bg_label31 =Label(self.root,image=self.photo_bg31).place(x=1100,y=660,width=100,height=100)
        
#Display  top to bottom right corner 

                self.photo_bg32= PhotoImage(file='Image/small.png')
                self.photo_bg_label32 =Label(self.root,image=self.photo_bg32).place(x=1100,y=110,width=100,height=100)

                self.photo_bg33= PhotoImage(file='Image/small.png')
                self.photo_bg_label33 =Label(self.root,image=self.photo_bg33).place(x=1100,y=220,width=100,height=100)

                self.photo_bg34= PhotoImage(file='Image/small.png')
                self.photo_bg_label34 =Label(self.root,image=self.photo_bg34).place(x=1100,y=330,width=100,height=100)

                self.photo_bg35= PhotoImage(file='Image/small.png')
                self.photo_bg_label35 =Label(self.root,image=self.photo_bg35).place(x=1100,y=440,width=100,height=100)

                self.photo_bg36= PhotoImage(file='Image/small.png')
                self.photo_bg_label36 =Label(self.root,image=self.photo_bg36).place(x=1100,y=550,width=100,height=100)

                self.photo_bg37= PhotoImage(file='Image/small.png')
                self.photo_bg_label37 =Label(self.root,image=self.photo_bg37).place(x=1100,y=660,width=100,height=100)

#Admin login back ground photo
                self.photo_login_bg= PhotoImage(file="Image/taxi_back_login.png")
                self.photo_login_bg_label = Label (self.root ,image=self.photo_login_bg).place(x=100,y=100,width=1000,height=550)

# username and password Label
                admin_ID_label= Label (self.root,text='Admin ID :- ',fg='Black',bg ='yellow',font=("Times New Roman",30,"bold")).place(x=130,y=130)
                Password_label=Label (self.root,text='Password        :-',fg='Black',bg = 'yellow',font=("Times New Roman",30,"bold")).place(x=130,y=210)

# Variables
                self.var_admin_ID = StringVar()
                self.var_password_admin = StringVar()
# Text box
                txt_admin=Entry(self.root, textvariable=self.var_admin_ID,bg = 'yellow',font=("Times New ROman",34)).place(x=450,y=130)
                txt_Passowrd=Entry(self.root, textvariable=self.var_password_admin,show='*',bg ="yellow",font=("Times New ROman",34)).place(x=450,y=210)

#Login button
                Login_btn = Button(self.root,text="Login ",command = self.admin_login,font=("Times New Roman",40,'bold'),bg="black",fg="yellow",cursor='hand2', ).place(x=400,y=340,width=400,height=90)
        
        
        def admin_login(self):

                con= sqlite3.connect(database=r'taxi_booking_data.db')
                cur = con.cursor()
                
                
                find_user = (" SELECT * from admin where admin_ID =? and password_admin=?")
                cur.execute(find_user,[self.var_admin_ID.get(),self.var_password_admin.get()])
                result =cur.fetchall()
                if self.var_admin_ID.get() == "" or self.var_password_admin.get()== "":
                        messagebox.showerror("Error"," You must enter the Admin ID and Passowrd",parent = self.root)

                elif result:

                        
                        messagebox.showinfo("Login","SUccessfully Login", parent = self.root)
                        self.var_admin_ID.set("")
                        self.var_password_admin.set("")
                                
                        self.Booking_page()

                else :
                        messagebox.showerror("Error"," Please Input valid Admin ID or Password",parent = self.root)

        
               
        def Booking_page(self):
                
                self.Trip = Toplevel (self.root)
                self.Newobject = admin_dashboard(self.Trip)

con = sqlite3.connect(database=r'taxi_booking_data.db')
cur = con.cursor()
def connection():
        con.commit
connection
if __name__ =='__main__':
    root=Tk()
    obj= Admin_Login(root)
    root.mainloop()
