from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import faceRecognitionSystem


def main():
    window = Tk()
    app = login_window(window)
    window.mainloop()


class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login page")
        self.root.geometry("1920x820+0+0")
        self.root.wm_iconbitmap("logo.ico")

        # variables
        self.var_user = StringVar()
        self.var_pass = StringVar()
        self.var_ques = StringVar()
        self.var_ans = StringVar()
        self.var_reset = StringVar()

        # background image
        img1 = Image.open("Images\image25.jpg")
        img1 = img1.resize((1920, 820), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1920, height=820)

        frame = Frame(self.root, bg="black")
        frame.place(x=600, y=200, width=400, height=450)

        # Login image
        img2 = Image.open("Images\image26.jpg")
        img2 = img2.resize((100, 100), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        login_img = Label(frame, image=self.photoimg2)
        login_img.place(x=150, y=0, width=100, height=100)

        # title
        title = Label(bg_img, text="WELCOME TO FACE RECOGNITION ATTENDANCE SYSTEM", font=(
            "fantasy", 35, "bold"), bg="black", fg="red")
        title.place(x=0, y=0, width=1550, height=50)

        # Login title
        title_lbl = Label(frame, text="Login Page", font=(
            "times new roman", 20, "bold"), bg="black", fg="white")
        title_lbl.place(x=102, y=100, width=200, height=50)

        # username
        username_lbl = Label(frame, text="Username: ", font=(
            "times new roman", 15, "bold"), bg="black", fg="white")
        username_lbl.place(x=20, y=170, width=150, height=30)

        username_entry = ttk.Entry(
            frame, textvariable=self.var_user, width=20, font=("times new roman", 14))
        username_entry.place(x=180, y=170, width=150, height=30)

        # password
        password_lbl = Label(frame, text="Password: ", font=(
            "times new roman", 15, "bold"), bg="black", fg="white")
        password_lbl.place(x=20, y=220, width=150, height=30)

        password_entry = ttk.Entry(
            frame, textvariable=self.var_pass, width=20, font=("times new roman", 14))
        password_entry.place(x=180, y=220, width=150, height=30)

        # login button
        login_button = Button(frame, command=self.login, text="LOGIN", width=15, font=(
            "times new roman", 15, "bold"), relief=RIDGE, bg="red", fg="white", activeforeground="white", activebackground="red")
        login_button.place(x=145, y=275, width=120, height=40)

        # register button
        login_button = Button(frame, command=self.registerWindow, text="New User? Register", width=15, font=(
            "times new roman", 12, "bold"), borderwidth=0, bg="black", fg="white", activeforeground="white", activebackground="black")
        login_button.place(x=30, y=335, width=170)

        # forgot password button
        forgot_button = Button(frame, command=self.forgot_password, text="Forgot Password?", width=15, font=(
            "times new roman", 12, "bold"), borderwidth=0, bg="black", fg="white", activeforeground="white", activebackground="black")
        forgot_button.place(x=20, y=365, width=170)

    def registerWindow(self):
        self.window1 = Toplevel(self.root)
        self.app = register_window(self.window1)

    def login(self):
        if self.var_user.get() == "" or self.var_pass.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="9631921702@sql", database="login_data")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from register where Email=%s and Password=%s", (
                    self.var_user.get(),
                    self.var_pass.get()
                ))
                row = my_cursor.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid username and password")
                else:
                    self.window2 = Toplevel(self.root)
                    self.app = faceRecognitionSystem(self.window2)
                conn.commit()
                conn.close()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error:{str(es)}", parent=self.root)

    # reset button
    def reset_pass(self):
        if self.var_ques.get() == "Select Question":
            messagebox.showerror(
                "Error", "Select the Security Question", parent=self.root2)
        elif self.var_ans.get() == "":
            messagebox.showerror(
                "Error", "Enter the valid Security Answer", parent=self.root2)
        elif self.var_reset.get() == "":
            messagebox.showerror(
                "Error", "Password Cannot be empty", parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="9631921702@sql", database="login_data")
                my_cursor = conn.cursor()
                query1 = (
                    "select * from register where Email=%s and `Security Question`=%s and `Security Answer`=%s")
                value = (self.var_user.get(),
                         self.var_ques.get(), self.var_ans.get())
                my_cursor.execute(query1, value)
                row = my_cursor.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Enter the valid Security Answer", parent=self.root2)
                else:
                    query2 = ("update register set Password=%s where Email=%s")
                    value1 = (self.var_reset.get(), self.var_user.get())
                    my_cursor.execute(query2, value1)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo(
                        "Reset", "Your Password has been Reset, Please login with your new Password")
                    self.root2.destroy()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error:{str(es)}", parent=self.root)

    #-------------------------------------------Forgot password window-----------------------------#
    def forgot_password(self):
        if self.var_user.get() == "":
            messagebox.showerror(
                "Error", "Enter a valid username", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="9631921702@sql", database="login_data")
                my_cursor = conn.cursor()
                query = ("select * from register where Email=%s")
                value = (self.var_user.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row == None:
                    messagebox.showerror(
                        "Error", "Enter a valid username", parent=self.root)
                else:
                    conn.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forgot password")
                    self.root2.geometry("350x450+610+170")
                    self.root2.wm_iconbitmap("logo.ico")

                    title_lbl = Label(self.root2, text="Forgot Password", font=(
                        "fantasy", 25, "bold"), bg="black", fg="white")
                    title_lbl.place(x=5, y=5, height=70, width=340)

                    # security question
                    question_lbl = Label(self.root2, text="Security Question:", font=(
                        "times new roman", 18, "bold"),  fg="black")
                    question_lbl.place(x=20, y=85, width=200, height=30)

                    question_combo = ttk.Combobox(self.root2, textvariable=self.var_ques, font=(
                        "times new roman", 12, "bold"), state="readonly")
                    question_combo["values"] = (
                        "Select Question", "Your Birth Place", "Your Pet Name", "Your Favourite Sport", "Your Favourite Dish")
                    question_combo.current(0)
                    question_combo.place(x=18, y=115, width=300, height=30)

                    # answer
                    answer_lbl = Label(self.root2, text="Security Answer: ", font=(
                        "times new roman", 18, "bold"), fg="black")
                    answer_lbl.place(x=18, y=150, width=200, height=30)

                    answer_entry = ttk.Entry(
                        self.root2, textvariable=self.var_ans, width=50, font=("times new roman", 14))
                    answer_entry.place(x=18, y=180, width=300, height=30)

                    # password
                    password_lbl = Label(self.root2, text="New Password: ", font=(
                        "times new roman", 18, "bold"), fg="black")
                    password_lbl.place(x=11, y=215, width=200, height=30)

                    password_entry = ttk.Entry(
                        self.root2, textvariable=self.var_reset, width=50, font=("times new roman", 14))
                    password_entry.place(x=18, y=245, width=300, height=30)

                    # button
                    login_button = Button(self.root2, command=self.reset_pass, text="RESET", width=25, font=(
                        "times new roman", 20, "bold"), relief=RIDGE, borderwidth=2,  cursor='hand2', bg="black", fg="red")
                    login_button.place(x=18, y=285, width=300, height=50)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error:{str(es)}", parent=self.root)


#--------------------------------------------Register Class------------------------------------#
class register_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Register page")
        self.root.geometry("1920x820+0+0")
        self.root.wm_iconbitmap("logo.ico")

        # variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_question = StringVar()
        self.var_answer = StringVar()
        self.var_password = StringVar()
        self.var_confirm = StringVar()
        self.var_check = IntVar()

        # background image
        img1 = Image.open("Images\image29.jpg")
        img1 = img1.resize((1920, 820), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1920, height=820)

        frame = Frame(self.root, bg="white")
        frame.place(x=350, y=150, width=850, height=450)

        # register image
        img2 = Image.open("Images\image31.png")
        img2 = img2.resize((300, 50), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        login_img = Label(frame, image=self.photoimg2)
        login_img.place(x=280, y=0, width=300, height=50)

        #=======================entry field=========================#

        # full name
        fname_lbl = Label(frame, text="First Name: ", font=(
            "times new roman", 18, "bold"), bg="white", fg="black")
        fname_lbl.place(x=130, y=80, width=150, height=30)

        fname_entry = ttk.Entry(
            frame, textvariable=self.var_fname, width=50, font=("times new roman", 14))
        fname_entry.place(x=130, y=110, width=250, height=30)

        # Last name
        lname_lbl = Label(frame, text="Last Name: ", font=(
            "times new roman", 18, "bold"), bg="white", fg="black")
        lname_lbl.place(x=480, y=80, width=150, height=30)

        lname_entry = ttk.Entry(
            frame, textvariable=self.var_lname, width=50, font=("times new roman", 14))
        lname_entry.place(x=480, y=110, width=250, height=30)

        # contact No
        contact_lbl = Label(frame, text="Contact Number: ", font=(
            "times new roman", 18, "bold"), bg="white", fg="black")
        contact_lbl.place(x=130, y=145, width=200, height=30)

        contact_entry = ttk.Entry(
            frame, textvariable=self.var_contact, width=50, font=("times new roman", 14))
        contact_entry.place(x=130, y=185, width=250, height=30)

        # email
        email_lbl = Label(frame, text="Email: ", font=(
            "times new roman", 18, "bold"), bg="white", fg="black")
        email_lbl.place(x=480, y=145, width=100, height=30)

        email_entry = ttk.Entry(
            frame, textvariable=self.var_email, width=50, font=("times new roman", 14))
        email_entry.place(x=480, y=185, width=250, height=30)

        # security question
        question_lbl = Label(frame, text="Security Question:", font=(
            "times new roman", 18, "bold"), bg="white", fg="black")
        question_lbl.place(x=130, y=220, width=200, height=30)

        question_combo = ttk.Combobox(frame, textvariable=self.var_question, font=(
            "times new roman", 12, "bold"), state="readonly")
        question_combo["values"] = (
            "Select Question", "Your Birth Place", "Your Pet Name", "Your Favourite Sport", "Your Favourite Dish")
        question_combo.current(0)
        question_combo.place(x=130, y=255, width=250, height=30)

        # answer
        answer_lbl = Label(frame, text="Security Answer: ", font=(
            "times new roman", 18, "bold"), bg="white", fg="black")
        answer_lbl.place(x=480, y=220, width=200, height=30)

        answer_entry = ttk.Entry(
            frame, textvariable=self.var_answer, width=50, font=("times new roman", 14))
        answer_entry.place(x=480, y=255, width=250, height=30)

        # password
        password_lbl = Label(frame, text="Password: ", font=(
            "times new roman", 18, "bold"), bg="white", fg="black")
        password_lbl.place(x=130, y=290, width=130, height=30)

        password_entry = ttk.Entry(
            frame, textvariable=self.var_password, width=50, font=("times new roman", 14))
        password_entry.place(x=130, y=320, width=250, height=30)

        # confirm password
        confirm_lbl = Label(frame, text="Confirm Password: ", font=(
            "times new roman", 18, "bold"), bg="white", fg="black")
        confirm_lbl.place(x=480, y=290, width=210, height=30)

        confirm_entry = ttk.Entry(
            frame, textvariable=self.var_confirm, width=50, font=("times new roman", 14))
        confirm_entry.place(x=480, y=320, width=250, height=30)

        #--------------------------------checkbox------------------------------#

        check_btn = Checkbutton(frame, variable=self.var_check, text="I Agree to all The Terms And Conditions", font=(
            "times new roman", 14, 'bold'), bg="white", activebackground="white", onvalue=1, offvalue=0)
        check_btn.place(x=130, y=355)

        # button
        # register image
        img3 = Image.open("Images\image32.png")
        img3 = img3.resize((200, 40), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        register_button = Button(frame, command=self.register_data, image=self.photoimg3, width=25, font=(
            "times new roman", 15, "bold"), relief=RIDGE, borderwidth=0, bg="white", activebackground="white", cursor='hand2')
        register_button.place(x=220, y=390, width=200, height=50)

        # login image
        img4 = Image.open("Images\image33.jpg")
        img4 = img4.resize((200, 40), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        login_button = Button(frame, command=self.loginWindow, image=self.photoimg4, width=25, font=(
            "times new roman", 15, "bold"), relief=RIDGE, borderwidth=0, bg="white", activebackground="white", cursor='hand2')
        login_button.place(x=480, y=390, width=200, height=50)

    #------------------------------------Function declaration-------------------------------------#

    def register_data(self):
        if self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_email.get() == "" or self.var_password.get() == "" or self.var_confirm.get() == "" or self.var_contact.get() == "" or self.var_answer.get() == "" or self.var_question.get() == "Select Question":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        elif self.var_password.get() != self.var_confirm.get():
            messagebox.showerror(
                "Error", "Password and Confirm Password must be same", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror(
                "Error", "You must agree to all the terms and conditions")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="9631921702@sql", database="login_data")
                my_cursor = conn.cursor()
                query = ("select * from register where Email=%s")
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "User already exist, Please login")
                else:
                    my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_question.get(),
                        self.var_answer.get(),
                        self.var_password.get()
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo(
                        "Success", "You have been registered successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error:{str(es)}", parent=self.root)

    def loginWindow(self):
        self.root.destroy()


if __name__ == '__main__':
    main()
