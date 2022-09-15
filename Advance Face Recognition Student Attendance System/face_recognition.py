from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class face_detection:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x820+0+0")
        self.root.title("Face Detection System")
        self.root.wm_iconbitmap("logo.ico")

        # background image
        img1 = Image.open("Images\image21.png")
        img1 = img1.resize((1600, 800), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1600, height=800)

        title = Label(bg_img, text="Face Detection System", font=(
            "fantasy", 45, "bold"), bg="black", fg="red")
        title.place(x=0, y=0, width=1600, height=70)

        # detect face button
        detect_button = Button(bg_img, command=self.face_detect, text="DETECT FACE", font=(
            "new times roman", 45, "bold"), cursor="hand2", bg="black", fg="red")
        detect_button.place(x=550, y=150, width=500, height=70)

        note_title = Label(bg_img, text="NOTE:- There should be trained dataset available before detecting the face", font=(
            "fantasy", 10, "bold"), bg="black", fg="red")
        note_title.place(x=550, y=225, width=500, height=20)

    #=======================================Attendance=====================================#

    def mark_attendance(self, result2, result4, result1, result3):
        with open("Attendance report\Attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])

            if((result2 not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d-%m-%Y")
                dt = now.strftime("%H:%M:%S")
                f.writelines(
                    f"\n{result2},{result4},{result1},{result3},{dt},{d1},Present")
            else:
                pass

    #=======================================Face Recognisation==============================#

    def face_detect(self):
        def draw_boundary(img, classifier, scaleFactor, miniNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, miniNeighbours)

            coordinates = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="9631921702@sql", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "select `Student Name` from student where StudentID="+str(id))
                result1 = my_cursor.fetchone()
                result1 = "+".join(result1)

                my_cursor.execute(
                    "select StudentID from student where StudentID="+str(id))
                result2 = my_cursor.fetchone()
                result2 = "+".join(result2)

                my_cursor.execute(
                    "select Department from student where StudentID="+str(id))
                result3 = my_cursor.fetchone()
                result3 = "+".join(result3)

                my_cursor.execute(
                    "select `Roll No` from student where StudentID="+str(id))
                result4 = my_cursor.fetchone()
                result4 = "+".join(result4)

                if confidence > 70:
                    cv2.putText(img, f"ID:{str(result2)}", (x, y-80),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 3)
                    cv2.putText(img, f"Roll No:{str(result4)}", (x, y-55),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 3)
                    cv2.putText(img, f"Student Name:{result1}", (x, y-30),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 3)
                    cv2.putText(img, f"Department:{result3}", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 3)
                    self.mark_attendance(result2, result4, result1, result3)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 3)

                coordinates = [x, y, w, h]

            return coordinates

        def recognize(img, clf, faceCascade):
            coordinates = draw_boundary(
                img, faceCascade, 1.1, 10, (0, 0, 0), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = face_detection(root)
    root.mainloop()
