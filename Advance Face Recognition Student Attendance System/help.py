from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x820+0+0")
        self.root.title("Help Panel")
        self.root.wm_iconbitmap("logo.ico")

        # background image
        img1 = Image.open("Images\image23.jpg")
        img1 = img1.resize((1600, 800), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1600, height=800)

        title = Label(bg_img, text="Help Desk", font=(
            "fantasy", 45, "bold"), bg="black", fg="red")
        title.place(x=0, y=0, width=1600, height=70)

        lbl1 = Label(bg_img, text="Watch out me for any queries or help on:\nInstagram: sudhanshuranjan_052\nLinkedIn: Sudhanshu Ranjan\nEmail: sudhanshu.ppps@gmail.com",
                     font=("fantasy", 17, "bold"), bg="darkblue", fg="red")
        lbl1.place(x=530, y=450, width=535, height=150)


if __name__ == "__main__":
    root = Tk()
    obj = help(root)
    root.mainloop()
