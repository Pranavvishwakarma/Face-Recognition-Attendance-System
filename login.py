from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import student_detail

from tkinter import*
import tkinter
from tkinter import ttk  #Containes style toolkit
from PIL import Image,ImageTk  # pil-pillow
import os
from student_detail import Student
from facial_recognition import Face_Recognition
from train import Train
from attendance import Attendance
from developer import Developer
from help import Help 
import pyttsx3
from time import strftime


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()
   

class Login_Window:

    def __init__(self, root):

        self.root = root
        self.root.title("login")
        self.root.geometry("1530x790+0+0")

        self.bg = ImageTk.PhotoImage(
            file=r"D:\MY MINOR PROJECT\MY MINOR PROJECT\Images\face.pdf")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open(r"D:\MY MINOR PROJECT\MY MINOR PROJECT\img.png")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=(
            "times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # label
        username = lbl = Label(frame, text="Username", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser = ttk.entry = Entry(
            frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = lbl = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=215)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        # # icon images
        # img2=Image.open("Pranav.jpg")
        # img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        # self.photoimage2=ImageTk.PhotoImage(img1)
        # lbling1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        # lbling1.place(x=610,y=323,width=25,height=25)

        # img3=Image.open("Pranav.jpg")
        # img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        # self.photoimage3=ImageTk.PhotoImage(img1)
        # lbling1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        # lbling1.place(x=650,y=397,width=25,height=25)

        # Login button
        loginbtn = Button(frame,command=self.login, text="login", font=("times new roman", 10, "bold"), bd=3,
                          relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="black")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # # Register button
        registerbtn = Button(frame, text="New user register",command=self.rigister_window, font=("times new roman", 10, "bold"), borderwidth=0,
                             relief=RIDGE, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

        # # Forgot password
        registerbtn = Button(frame, text="forget password",command=self.forgot_password, font=("times new roman", 10, "bold"), borderwidth=0,
                             relief=RIDGE, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=10, y=370, width=160)
    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=register(self.new_window) 

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
                messagebox.showerror("Error", "all field requird")

        elif self.txtuser.get() == "Pranav" and self.txtpass.get() == "piemr":

            messagebox.showinfo(
                "Success", "Welcome to Face Recognition Attendance System")
        else:
            conn = mysql.connector.connect(
                host='localhost', user='root', password='abc', database='register', auth_plugin='mysql_native_password')
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(self.txtuser.get(),
                                                                                        self.txtpass.get()))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel()
                    self.app=Face_Recognition_System(self.new_window)
                else:
                     if not open_main:
                            return
            conn.commit()
            conn.close()

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the name",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(
                host='localhost', user='root', password='abc', database='register', auth_plugin='mysql_native_password')
            my_cursor = conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer")
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been reset , please login new password",parent=self.root2)
    
    def forgot_password(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the mail address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="abc",database="register",auth_plugin='mysql_native_password')
            my_cursur=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursur.execute(query,value)
            row=my_cursur.fetchone()
            # print(row)

            if row ==None:
                messagebox.showerror("My Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget password")
                self.root2.geometry("340x450+610+170")
                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="black")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your pet name","Your school name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                
                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman" ,15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)


    
class register:
    
    def __init__(self, root):

        self.root = root
        self.root.title("login")
        self.root.geometry("1530x790+0+0")

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        self.bg = ImageTk.PhotoImage(
            file=r"D:\MY MINOR PROJECT\MY MINOR PROJECT\Images\face.pdf")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        self.bg = ImageTk.PhotoImage(
            file=r"D:\MY MINOR PROJECT\MY MINOR PROJECT\Images\face.pdf")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=50, y=100, width=470, height=550)

        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

        # ++++++++++

        fname = Label(frame, text="First Name", font=(
            "times new roman", 20, "bold"), bg="white")
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(
            frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=(
            "times new roman", 20, "bold"), bg="white")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(
            frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        contact = Label(frame, text="Contact No", font=(
            "times new roman", 20, "bold"), bg="white")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(
            frame,textvariable=self.var_contact , font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        Email = Label(frame, text="Email", font=(
            "times new roman", 20, "bold"), bg="white")
        Email.place(x=370, y=170)

        self.txt_Email = ttk.Entry(
            frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_Email.place(x=370, y=200, width=250)

        # security_Q=Label(frame,text="Select ")
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your pet name","Your school name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        pswd = Label(frame, text="Password", font=(
            "times new roman", 20, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=300)

        self.txt_pswd = ttk.Entry(
            frame, textvariable=self.var_pass, font=("times new roman", 15, "bold"))
        self.txt_pswd.place(x=50, y=340, width=250)

        pswd = Label(frame, text="Confirm Password", font=(
            "times new roman", 20, "bold"), bg="white", fg="black")
        pswd.place(x=370, y=300)

        self.txt_contact = ttk.Entry(
            frame, textvariable=self.var_confpass, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=370, y=340, width=250)

        img = Image.open(r"register.png")
        img = img.resize((200, 55), Image.Resampling.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame,command=self.register_data,image=self.photoimage, borderwidth=0,
                    cursor="hand2", font=("times new roman", 15, "bold"))
        b1.place(x=10, y=420, width=200)

        img1 = Image.open(r"login.png")
        img1 = img1.resize((200, 50), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame,command=self.login_window,image=self.photoimage1, borderwidth=0,
                    cursor="hand2", font=("times new roman", 15, "bold"))
        b1.place(x=330, y=420, width=200)
    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=register(self.new_window) 

    def login_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Login_Window(self.new_window)

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email == "" or self.var_contact.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "password & confirm must be same")
        else:
            conn = mysql.connector.connect(
                host='localhost', user='root', password='abc', database='register', auth_plugin='mysql_native_password')
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row!= None:
                messagebox.showerror("Error", "already register")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
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
            messagebox.showinfo("Success", "Register Successfully")

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        # geometry set
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        

        img=Image.open("Images\help.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)   #High level img to Low level img
        self.photoimg=ImageTk.PhotoImage(img)

        first_lb=Label(self.root, image=self.photoimg)
        first_lb.place(x=0,y=0,width=500,height=130)


        img1=Image.open("Images\PIEMR-BUILDING.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)   #High level img to Low level img
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_lb=Label(self.root, image=self.photoimg1)
        first_lb.place(x=500,y=0,width=500,height=130)


        img2=Image.open("Images/face_rec_1.jpg")
        img2=img2.resize((530,130),Image.Resampling.LANCZOS)   #High level img to Low level img
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_lb=Label(self.root, image=self.photoimg2)
        first_lb.place(x=1000,y=0,width=530,height=130)


        # img3=Image.open("Images/logo.jpg")
        # img3=img3.resize((130,130),Image.ANTIALIAS)   #High level img to Low level img
        # self.photoimg3=ImageTk.PhotoImage(img3)

        # first_lb=Label(self.root, image=self.photoimg3)
        # first_lb.place(x=1400,y=0,width=130,height=130)



        #Bg Image
        bg=Image.open("Images/face.pdf")
        bg=bg.resize((1530,710),Image.Resampling.LANCZOS)   #High level img to Low level img
        self.photoimg_bg=ImageTk.PhotoImage(bg)

        bg_image=Label(self.root, image=self.photoimg_bg)
        bg_image.place(x=0,y=130,width=1530,height=710)


        title_lb=Label(bg_image,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("PT Serif",35,"bold"),bg="#faffc7",fg="#f7520f")
        title_lb.place(x=0,y=0,width=1530,height=50)

        # ==============time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lb,font=('time new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
             #Student Button
        std_1=Image.open("Images/std_1.jpg")
        std_1=std_1.resize((220,220),Image.Resampling.LANCZOS)   #High level img to Low level img
        self.photoimg_std_1=ImageTk.PhotoImage(std_1)

        b1=Button(bg_image,image=self.photoimg_std_1,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width =220,height=220)

        b1_txt=Button(bg_image,text="Student Details",command=self.student_details,cursor="hand2",font=("PT Serif",15,"bold"),bg="#040229",fg="white")
        b1_txt.place(x=200,y=300,width =220,height=40)


        #Detect Face
        face_1=Image.open("Images/face_detect.jpg")
        face_1=face_1.resize((220,220),Image.Resampling.LANCZOS)   #High level img to Low level img
        self.photoimg_face=ImageTk.PhotoImage(face_1)

        b1=Button(bg_image,image=self.photoimg_face,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width =220,height=220)

        b1_txt=Button(bg_image,text="Face Recognizer",command=self.face_data,cursor="hand2",font=("PT Serif",15,"bold"),bg="#040229",fg="white")
        b1_txt.place(x=500,y=300,width =220,height=40)



        #Attendance 
        att=Image.open("Images/att.png")
        att=att.resize((220,220),Image.Resampling.LANCZOS)   #High level img to Low level img
        self.photoimg_att=ImageTk.PhotoImage(att)

        b1=Button(bg_image,command=self.attendance_data,image=self.photoimg_att,cursor="hand2")
        b1.place(x=800,y=100,width =220,height=220)

        b1_txt=Button(bg_image,text="Attendance",command=self.attendance_data,cursor="hand2",font=("PT Serif",15,"bold"),bg="#040229",fg="white")
        b1_txt.place(x=800,y=300,width =220,height=40)


        #Help Desk
        help=Image.open("Images/help_d.jpg")
        help=help.resize((220,220),Image.Resampling.LANCZOS)   #High level img to Low level img
        self.photoimg_help=ImageTk.PhotoImage(help)

        b1=Button(bg_image,image=self.photoimg_help,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width =220,height=220)

        b1_txt=Button(bg_image,text="Help Desk",command=self.help_data,cursor="hand2",font=("PT Serif",15,"bold"),bg="#040229",fg="white")
        b1_txt.place(x=1100,y=300,width =220,height=40)


        #Training the algo
        train=Image.open("Images/training.jpg")
        train=train.resize((220,220),Image.Resampling.LANCZOS)   #High level img to Low level img
        self.photoimg_train=ImageTk.PhotoImage(train)

        b1=Button(bg_image,image=self.photoimg_train,command=self.train_data,cursor="hand2")
        b1.place(x=200,y=380,width =220,height=220)

        b1_txt=Button(bg_image,text="Training data",command=self.train_data,cursor="hand2",font=("PT Serif",15,"bold"),bg="#040229",fg="white")
        b1_txt.place(x=200,y=580,width =220,height=40)


        #Data library
        photos=Image.open("Images/store.jpg")
        photos=photos.resize((220,220),Image.Resampling.LANCZOS)   #High level img to Low level img
        self.photoimg_photos=ImageTk.PhotoImage(photos)

        b1=Button(bg_image,command=self.open_img,image=self.photoimg_photos,cursor="hand2")
        b1.place(x=500,y=380,width =220,height=220)

        b1_txt=Button(bg_image,command=self.open_img,text="Image Library",cursor="hand2",font=("PT Serif",15,"bold"),bg="#040229",fg="white")
        b1_txt.place(x=500,y=580,width =220,height=40)


        #Developer info/Contact
        Dev=Image.open("Images/dev1.jpg")
        Dev=Dev.resize((220,220),Image.Resampling.LANCZOS)   #High level img to Low level img
        self.photoimg_Dev=ImageTk.PhotoImage(Dev)

        b1=Button(bg_image,image=self.photoimg_Dev,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width =220,height=220)

        b1_txt=Button(bg_image,text="Contact Developer",command=self.developer_data,cursor="hand2",font=("PT Serif",15,"bold"),bg="#040229",fg="white")
        b1_txt.place(x=800,y=580,width =220,height=40)


        #Exit Button
        Exit=Image.open("Images/exit.png")
        Exit=Exit.resize((220,220),Image.Resampling.LANCZOS)   #High level img to Low level img
        self.photoimg_Exit=ImageTk.PhotoImage(Exit)

        b1=Button(bg_image,image=self.photoimg_Exit,cursor="hand2",command=self.isExit)
        b1.place(x=1100,y=380,width =220,height=220)

        b1_txt=Button(bg_image,text="Exit",command=self.isExit,cursor="hand2",font=("PT Serif",15,"bold"),bg="#040229",fg="white")
        b1_txt.place(x=1100,y=580,width =220,height=40)




    




#############################Function buttons ###################
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def open_img(self):
        os.startfile("data")


    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def isExit(self):
        self.isExit=tkinter.messagebox.askyesno("Face recognition system","Are you sure want to exit?")
        if self.isExit>0:
            self.root.destroy()
        else:
            return


            
    

     
                
                
         



if __name__ == "__main__":
    main()
    
