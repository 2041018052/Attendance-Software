from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x820+0+0")
        self.root.title("About Developer")
        self.root.wm_iconbitmap("logo.ico")

        # background image
        img1 = Image.open("Images\image24.png")
        img1 = img1.resize((1600, 800), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1600, height=800)

        title = Label(bg_img, text="Developer Information", font=(
            "fantasy", 45, "bold"), bg="black", fg="red")
        title.place(x=0, y=0, width=1600, height=70)

        # developer image
        img2 = Image.open("Images\image1.jpeg")
        img2 = img2.resize((500, 600), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        developer_img = Label(self.root, image=self.photoimg2)
        developer_img.place(x=30, y=100, width=500, height=600)

        # INFORMATION FRAME
        information_frame = Frame(bg_img, bd=2, relief=GROOVE)
        information_frame.place(x=535, y=100, width=500, height=600)

        lbl1 = Label(information_frame, text="ABOUT ME:-\n\nHello everyone!!! My name is Sudhanshu\nRanjan. I am the developer of this\nAdvanced Face Recognition\nSystem Sofware.\nI have build this software using Python,\nTkinter, OpenCV and MySQL Database.\nI am currently learning Machine learning\nand Artificial intelligence.\nI am a 3rd year CSE student in ITER,\nSOA University\nWatch out me on:\nInstagram: sudhanshuranjan_052\nLinkedIn: Sudhanshu Ranjan\nEmail: sudhanshu.ppps@gmail.com",
                     font=("fantasy", 17, "bold"), bg="darkblue", fg="red")
        lbl1.place(x=0, y=0, width=500, height=600)


if __name__ == "__main__":
    root = Tk()
    obj = developer(root)
    root.mainloop()
