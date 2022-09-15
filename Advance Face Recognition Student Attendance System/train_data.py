from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import cv2
import numpy as np

class trainData:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x820+0+0")
        self.root.title("Training Data System")
        self.root.wm_iconbitmap("logo.ico")

        # background image
        img1 = Image.open("Images\image7.jpg")
        img1 = img1.resize((1920, 820), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=1920,height=820)

        title = Label(bg_img,text="TRAIN DATA SET",font=("fantasy",45,"bold"),bg="black",fg="red")
        title.place(x=0,y=0,width=1600,height=50)

        #train button
        train_button = Button(bg_img,command=self.train_classifier,text="TRAIN DATA",font=("new times roman",45,"bold"),cursor="hand2",bg="black",fg="red")
        train_button.place(x=300,y=300,width=1000,height=70)

    def train_classifier(self):
        data_dir=("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L') #coverted to gray scale image
            imageNP = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training DataSet",imageNP)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)

        #============================Train classifier and save==============#

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed!!!",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = trainData(root)
    root.mainloop()
