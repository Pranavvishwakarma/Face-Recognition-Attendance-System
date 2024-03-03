from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

import os
from time import strftime
from datetime import datetime
import numpy as np
import face_recognition
# import pyttsx3

# engine = pyttsx3.init()

# engine.say("Please Wait for recognition")
# engine.runAndWait()


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl = Label(self.root,text="FACE RECOGNITION",font=("times new roman", 35, "bold"), bg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # 1st imageE:\prd year\MY MINOR PROJECT\MY MINOR PROJECT\Images\training1.jpg
        img_top = Image.open("Images/face_rec_1.jpg")
        img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # 2nd image
        img_bottom = Image.open("Images/face_recog_2.png")
        img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # button
        b1_1 = Button(f_lbl, text="RECOGNIZE", command=self.recognize_attendence, cursor="hand2", font=(
            "times new roman", 18, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=365, y=620, width=200, height=40)


# attendance  #########################33

        # to avoid repeat


    def mark_attendance(self,i,n,d):

        with open("./Pranav.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((n not in name_list) and (d not in name_list) and (i not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{d},{dtString},{d1},Present")


# face recognition  #################3

    def recognize_attendence(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord = []
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w+20,y+h+20),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h+20,x:x+w+20])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="abc",database="face_recognizer",auth_plugin='mysql_native_password')
                # conn=mysql.connector.connect(host="localhost",username="root",password="Keshav@123",database="mydata")
                my_cursor=conn.cursor()

                # my_cursor.execute("select student_id from student where Student_Id="+str(id))
                # i = my_curs
                # or.fetchone()
                # n=str(i)

                my_cursor.execute("select Student_Id from student where Student_Id="+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)
                

                my_cursor.execute("select name from student where Student_Id="+str(id))
                n = my_cursor.fetchone()
                n="+".join(n)

                # n="+".join(n)

                # my_cursor.execute("select Roll from student where Student_Id="+str(id))
                # r=my_cursor.fetchone()
                # r = str(r)
                # r = "+".join(r)

                my_cursor.execute("select dep from student where Student_Id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)
                # d=str(d)

                # new code for accuracy calculation
                # img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                # result = id.predict(img)

                if predict<500:
                    # # if result[1] < 500:
                    #     # confidence=int((100*(1-predict/300)))
                    #     # str2 = str(confidence)
                    #     # confidence = int(100 * (1 - (result[1])/300))
                    #     #display_string = (confidence)+'% confidence it is user'
                    #     #cv2.putText(img,display_string(250, 250), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
                    cv2.putText(img,f"Accuracy:{confidence}%",(x,y-100),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),3)

                if confidence>77:
                    cv2.putText(img,f"Roll:{i}",(x, y-55),cv2.FONT_HERSHEY_COMPLEX, 0.8,(255, 255, 255),3)
                    cv2.putText(img,f"Name:{n}",(x, y-30),cv2.FONT_HERSHEY_COMPLEX, 0.8,(255, 255, 255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),3)

                    self.mark_attendance(i,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w+20,y+h+20),(0,0,255),3)

                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),3)

                coord = [x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord = draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            _,img = video_cap.read()
            img=recognize(img,clf,faceCascade)
            #speak_va("Welcome to Face Recognition World")
            cv2.imshow("Welcome to face Recognition",img)

            if (cv2.waitKey(1)==ord('q')):
                     break
        video_cap.release()
        cv2.destroyAllWindows()
    # def recognize_attendence(self):
    #     recognizer = cv2.face.LBPHFaceRecognizer_create()  
    #     #recognizer.read("TrainingImageLabel"+os.sep+"Trainner.yml")
    #     recognizer.read('classifier.xml')
    #     harcascadePath = "Cascades\haarcascade_frontalface_default.xml"
    #     faceCascade = cv2.CascadeClassifier(harcascadePath)
    #     font = cv2.FONT_HERSHEY_SIMPLEX
        

    #     # start realtime video capture
    #     cam = cv2.VideoCapture(0)
    #     cam.set(3, 640) 
    #     cam.set(4, 480) 
    #     minW = 0.1 * cam.get(3)
    #     minH = 0.1 * cam.get(4)

    #     while True:
    #         ret,img = cam.read()
    #         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #         faces = faceCascade.detectMultiScale(gray, 1.2,5,cv2.CASCADE_SCALE_IMAGE)
    #         for(x, y, w, h) in faces:
    #             cv2.rectangle(img, (x, y), (x+w, y+h), (10, 159, 255), 2)
    #             id,predict=recognizer.predict(gray[y:y+h,x:x+w])
    #             confidence=int((100*(1-predict/300)))

    #             conn = mysql.connector.connect(host="localhost", user="root", password="Pranav@123",database="face_recognizer", auth_plugin='mysql_native_password')
    # #             # conn=mysql.connector.connect(host="localhost",username="root",password="Keshav@123",database="mydata")
    #             my_cursor = conn.cursor()

    # #             # my_cursor.execute("select student_id from student where Student_Id="+str(id))
    # #             # i = my_curs
    # #             # or.fetchone()
    # #             # n=str(i)

    #             my_cursor.execute("select Student_Id from student where Student_Id="+str(id))
    #             i = my_cursor.fetchone()
    #             i = "+".join(i)

    #             my_cursor.execute("select Name from student where Student_Id="+str(id))
    #             n = my_cursor.fetchone()
    #             n = "+".join(n)
    # #             # n="+".join(n)

    # #             # my_cursor.execute("select Roll from student where Student_Id="+str(id))
    # #             # r=my_cursor.fetchone()
    # #             # r = str(r)
    # #             # r = "+".join(r)

    #             my_cursor.execute("select Dep from student where Student_Id="+str(id))
    #             d = my_cursor.fetchone()
    #             d = "+".join(d)

                
    #             if confidence>77:
    #                 cv2.putText(img,f"ID:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
    #                 cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
    #                 cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
    #                 self.mark_attendance(i,n,d)                
    #             else:
    #                 cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    #                 cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)


    #         cv2.imshow("Welcome to Face Recognition",img)
    
    #         if (cv2.waitKey(1)==ord('q')):
    #             break
        
    #     cam.release()
    #     cv2.destroyAllWindows()

        

 



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
