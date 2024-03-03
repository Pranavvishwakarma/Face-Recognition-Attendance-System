from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
# from main import Face_Recognition


class register:

    def __init__(self, root):

        self.root = root
        self.root.title("login")
        self.root.geometry("1550x800+0+0")

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

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,font=("times new roman",15))
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
        b1 = Button(frame, image=self.photoimage1, borderwidth=0,
                    cursor="hand2", font=("times new roman", 15, "bold"))
        b1.place(x=330, y=420, width=200)
    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=register(self.new_window) 

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email == "" or self.var_contact.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "password & confirm must be same")
        else:
            conn = mysql.connector.connect(
                host='localhost', user='root', password='Pranav@123', database='register', auth_plugin='mysql_native_password')
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
            


if __name__ == "__main__":
    root = Tk()
    app = register(root)
    root.mainloop()
