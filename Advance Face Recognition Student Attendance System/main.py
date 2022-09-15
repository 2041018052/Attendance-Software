from logging import root
from time import strftime
from tkinter import *
from tkinter import ttk
import tkinter
from turtle import back
from PIL import Image, ImageTk
from attendance import attendance
from student import student
from train_data import trainData
from face_recognition import face_detection
from attendance import attendance
from developer import developer
from help import help
from time import strftime
from datetime import datetime
import os


class faceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x820+0+0")
        self.root.title("Advance Face Recognition Student Attendance System")
        self.root.wm_iconbitmap("logo.ico")

        # background image
        img1 = Image.open("Images\image7.jpg")
        img1 = img1.resize((1920, 820), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1920, height=820)

        # title
        title = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=(
            "fantasy", 35, "bold"), bg="black", fg="red")
        title.place(x=0, y=0, width=1550, height=50)

        #-----------------------time-----------------------------------#
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title, font=('fantasy', 14, 'bold'),
                    bg='black', fg='white')
        lbl.place(x=0, y=(-15), width=110, height=50)
        time()

        # student button
        img2 = Image.open("Images\image9.png")
        img2 = img2.resize((220, 220), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1 = Button(bg_img, image=self.photoimg2,
                    command=self.student_panel, cursor="hand2")
        b1.place(x=285, y=100, width=220, height=220)

        b1_name = Button(bg_img, text="Student Panel", command=self.student_panel, font=(
            "fantasy", 20, "bold"), bg="black", fg="red", cursor="hand2")
        b1_name.place(x=285, y=320, width=220, height=40)

        # Face Detection button
        img3 = Image.open("Images\image11.gif")
        img3 = img3.resize((220, 220), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b2 = Button(bg_img, command=self.faceDetect,
                    image=self.photoimg3, cursor="hand2")
        b2.place(x=535, y=100, width=220, height=220)

        b2_name = Button(bg_img, command=self.faceDetect, text="Face Detector", font=(
            "fantasy", 20, "bold"), bg="black", fg="red", cursor="hand2")
        b2_name.place(x=535, y=320, width=220, height=40)

        # Attendance button
        img4 = Image.open("Images\image12.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b3 = Button(bg_img, command=self.Attendance,
                    image=self.photoimg4, cursor="hand2")
        b3.place(x=785, y=100, width=220, height=220)

        b3_name = Button(bg_img, command=self.Attendance, text="Attendance", font=(
            "fantasy", 20, "bold"), bg="black", fg="red", cursor="hand2")
        b3_name.place(x=785, y=320, width=220, height=40)

        # Help and support button
        img5 = Image.open("Images\image13.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b4 = Button(bg_img, command=self.Help,
                    image=self.photoimg5, cursor="hand2")
        b4.place(x=1035, y=100, width=220, height=220)

        b4_name = Button(bg_img, command=self.Help, text="Help Desk", font=(
            "fantasy", 20, "bold"), bg="black", fg="red", cursor="hand2")
        b4_name.place(x=1035, y=320, width=220, height=40)

        # Data train button
        img6 = Image.open("Images\image14.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b6 = Button(bg_img, command=self.train_dataset,
                    image=self.photoimg6, cursor="hand2")
        b6.place(x=285, y=450, width=220, height=220)

        b6_name = Button(bg_img, command=self.train_dataset, text="Data Train", font=(
            "fantasy", 20, "bold"), bg="black", fg="red", cursor="hand2")
        b6_name.place(x=285, y=670, width=220, height=40)

        # dataset button
        img7 = Image.open("Images\image15.png")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b6 = Button(bg_img, command=self.open_img,
                    image=self.photoimg7, cursor="hand2")
        b6.place(x=535, y=450, width=220, height=220)

        b6_name = Button(bg_img, command=self.open_img, text="Dataset", font=(
            "fantasy", 20, "bold"), bg="black", fg="red", cursor="hand2")
        b6_name.place(x=535, y=670, width=220, height=40)

        # Developers button
        img8 = Image.open("Images\image16.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b7 = Button(bg_img, command=self.Developer,
                    image=self.photoimg8, cursor="hand2")
        b7.place(x=785, y=450, width=220, height=220)

        b7_name = Button(bg_img, command=self.Developer, text="Developer", font=(
            "fantasy", 20, "bold"), bg="black", fg="red", cursor="hand2")
        b7_name.place(x=785, y=670, width=220, height=40)

        # Exit button
        img9 = Image.open("Images\image17.png")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b8 = Button(bg_img, command=self.exit,
                    image=self.photoimg9, cursor="hand2")
        b8.place(x=1035, y=450, width=220, height=220)

        b8_name = Button(bg_img, command=self.exit, text="Exit", font=(
            "fantasy", 20, "bold"), bg="black", fg="red", cursor="hand2")
        b8_name.place(x=1035, y=670, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    def exit(self):
        self.exit = tkinter.messagebox.askyesno(
            "Exit", "Are you sure want to exit this software?", parent=self.root)
        if self.exit > 0:
            self.root.destroy()
        else:
            return

    #==========================Function Button==========================#

    # student_panel

    def student_panel(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)

    # train data
    def train_dataset(self):
        self.new_window = Toplevel(self.root)
        self.app = trainData(self.new_window)

    # face detection
    def faceDetect(self):
        self.new_window = Toplevel(self.root)
        self.app = face_detection(self.new_window)

    # attendance
    def Attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = attendance(self.new_window)

    # developer
    def Developer(self):
        self.new_window = Toplevel(self.root)
        self.app = developer(self.new_window)

    # helpdesk
    def Help(self):
        self.new_window = Toplevel(self.root)
        self.app = help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = faceRecognitionSystem(root)
    root.mainloop()
