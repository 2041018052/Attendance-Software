from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x820+0+0")
        self.root.title("Student Panel")
        self.root.wm_iconbitmap("logo.ico")

        # variables for all fields:
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_stu_name = StringVar()
        self.var_sec = StringVar()
        self.var_email = StringVar()
        self.var_roll = StringVar()
        self.var_dob = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_combo = StringVar()
        self.var_entry = StringVar()

        # background image
        img1 = Image.open("Images\image7.jpg")
        img1 = img1.resize((1920, 820), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1920, height=820)

        title = Label(bg_img, text="STUDENT PANEL", font=(
            "fantasy", 35, "bold"), bg="black", fg="red")
        title.place(x=0, y=0, width=1550, height=50)

        #----------------------------------------Left side frame----------------------------------#

        # left side frame
        left_frame = LabelFrame(bg_img, bd=5, relief=GROOVE, text="Student Details", font=(
            "times new roman", 25, "bold",))
        left_frame.place(x=10, y=60, width=660, height=710)

        # left image
        img2 = Image.open("Images\image18.jpg")
        img2 = img2.resize((650, 120), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        left_img = Label(left_frame, image=self.photoimg2)
        left_img.place(x=0, y=0, width=650, height=130)

        # current course information
        current_course_frame = LabelFrame(
            left_frame, bd=2, relief=GROOVE, text="Current Course Information", font=("times new roman", 17, "bold",))
        current_course_frame.place(x=5, y=135, width=640, height=130)

        # Department
        dep_label = Label(current_course_frame, text="Department",
                          font=("times new roman", 14, "bold"))
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "Computer Science Engineering", "Computer Science and Information technology",
                               "Mechanical Engineering", "Civil Engineering", "Electrical and Electronics Engineering")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # course
        course_label = Label(current_course_frame, text="Course",
                             font=("times new roman", 14, "bold"))
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "times new roman", 12, "bold"), state="readonly")
        course_combo["values"] = (
            "Select Course", "CSE3541", "CSE4049", "CSE3034", "CSE3142", "CSE3731", "CSE2733")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # year
        year_label = Label(current_course_frame, text="Year",
                           font=("times new roman", 14, "bold"))
        year_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), state="readonly")
        year_combo["values"] = (
            "Select Year", "First Year", "Second Year", "Third Year", "Fourth Year")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semester
        sem_label = Label(current_course_frame, text="Semester",
                          font=("times new roman", 14, "bold"))
        sem_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem, font=(
            "times new roman", 12, "bold"), state="readonly")
        sem_combo["values"] = (
            "Select Semester", "Even Semester", "Odd Semester")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # student information
        student_information_frame = LabelFrame(
            left_frame, bd=2, relief=GROOVE, text="Student Information", font=("times new roman", 17, "bold",))
        student_information_frame.place(x=5, y=270, width=640, height=390)

        # Student id
        StudentId_label = Label(student_information_frame, text="Student ID:", font=(
            "times new roman", 14, "bold"))
        StudentId_label.grid(row=0, column=0, padx=10, sticky=W)

        StudentId_entry = ttk.Entry(
            student_information_frame, textvariable=self.var_id, width=15, font=("times new roman", 14))
        StudentId_entry.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        # student name
        StudentName_label = Label(student_information_frame, text="Student Name:", font=(
            "times new roman", 14, "bold"))
        StudentName_label.grid(row=0, column=2, padx=10, sticky=W)

        StudentName_entry = ttk.Entry(
            student_information_frame, textvariable=self.var_stu_name, width=19, font=("times new roman", 14))
        StudentName_entry.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        # section
        Section_label = Label(student_information_frame, text="Section:", font=(
            "times new roman", 14, "bold"))
        Section_label.grid(row=1, column=0, padx=10, sticky=W)

        Section_entry = ttk.Entry(
            student_information_frame, textvariable=self.var_sec, width=15, font=("times new roman", 14))
        Section_entry.grid(row=1, column=1, padx=5, pady=10, sticky=W)

        # Email
        Email_label = Label(student_information_frame,
                            text="Email:", font=("times new roman", 14, "bold"))
        Email_label.grid(row=1, column=2, padx=10, sticky=W)

        Email_entry = ttk.Entry(
            student_information_frame, textvariable=self.var_email, width=19, font=("times new roman", 14))
        Email_entry.grid(row=1, column=3, padx=5, pady=10, sticky=W)

        # Roll no
        Rollno_label = Label(student_information_frame, text="Roll No:", font=(
            "times new roman", 14, "bold"))
        Rollno_label.grid(row=2, column=0, padx=10, sticky=W)

        Rollno_entry = ttk.Entry(
            student_information_frame, textvariable=self.var_roll, width=15, font=("times new roman", 14))
        Rollno_entry.grid(row=2, column=1, padx=5, pady=10, sticky=W)

        # DOB
        DOB_label = Label(student_information_frame, text="DOB:",
                          font=("times new roman", 14, "bold"))
        DOB_label.grid(row=2, column=2, padx=10, sticky=W)

        DOB_entry = ttk.Entry(student_information_frame,
                              textvariable=self.var_dob, width=19, font=("times new roman", 14))
        DOB_entry.grid(row=2, column=3, padx=5, pady=10, sticky=W)

        # Gender
        gender_label = Label(student_information_frame, text="Gender:", font=(
            "times new roman", 14, "bold"))
        gender_label.grid(row=3, column=0, padx=10, sticky=W)

        gender_combo = ttk.Combobox(student_information_frame, textvariable=self.var_gender, width=13, font=(
            "times new roman", 14), state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=3, column=1, padx=5, pady=10, sticky=W)

        # phone no
        Phone_no_label = Label(student_information_frame, text="Phone No:", font=(
            "times new roman", 14, "bold"))
        Phone_no_label.grid(row=3, column=2, padx=10, sticky=W)

        Phone_no_entry = ttk.Entry(
            student_information_frame, textvariable=self.var_phone, width=19, font=("times new roman", 14))
        Phone_no_entry.grid(row=3, column=3, padx=5, pady=10, sticky=W)

        # Address
        Address_label = Label(student_information_frame, text="Address:", font=(
            "times new roman", 14, "bold"))
        Address_label.grid(row=4, column=0, padx=10, sticky=W)

        Address_entry = ttk.Entry(
            student_information_frame, textvariable=self.var_address, width=15, font=("times new roman", 14))
        Address_entry.grid(row=4, column=1, padx=5, pady=10, sticky=W)

        # Teacher name
        Teacher_name_label = Label(student_information_frame, text="Teacher Name:", font=(
            "times new roman", 14, "bold"))
        Teacher_name_label.grid(row=4, column=2, padx=10, sticky=W)

        Teacher_name_entry = ttk.Entry(
            student_information_frame, textvariable=self.var_teacher, width=19, font=("times new roman", 14))
        Teacher_name_entry.grid(row=4, column=3, padx=5, pady=10, sticky=W)

        # radio button
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            student_information_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0, padx=10)

        radiobtn2 = ttk.Radiobutton(
            student_information_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1, padx=10)

        note_label = Label(student_information_frame, text="NOTE:- Student ID must be sequential and start from 1", font=(
            "times new roman", 10, "bold"),  fg="red")
        note_label.place(x=5,y=257,width=305,height=20)

        # button frame1
        btn_frame1 = Frame(student_information_frame, bd=2, relief=GROOVE)
        btn_frame1.place(x=6, y=275, width=623, height=40)

        # save button
        save_button = Button(btn_frame1, command=self.add_data, text="Save", width=15, font=(
            "times new roman", 13, "bold"), bg="black", fg="red")
        save_button.grid(row=0, column=0)

        # delete button
        delete_button = Button(btn_frame1, command=self.delete_data, text="Delete", width=15, font=(
            "times new roman", 13, "bold"), bg="black", fg="red")
        delete_button.grid(row=0, column=1)

        # update button
        update_button = Button(btn_frame1, command=self.update_data, text="Update", width=15, font=(
            "times new roman", 13, "bold"), bg="black", fg="red")
        update_button.grid(row=0, column=2)

        # reset button
        reset_button = Button(btn_frame1, command=self.reset_data, text="Reset", width=15, font=(
            "times new roman", 13, "bold"), bg="black", fg="red")
        reset_button.grid(row=0, column=3)

        # button frame2
        btn_frame2 = Frame(student_information_frame, bd=2, relief=GROOVE)
        btn_frame2.place(x=6, y=315, width=623, height=35)

        # add_sample button
        add_photo_button = Button(btn_frame2, command=self.generate_dataset, text="Take Photo Sample", width=30, font=(
            "times new roman", 13, "bold"), bg="black", fg="red")
        add_photo_button.grid(row=0, column=0)

        # update_sample button
        update_photo_button = Button(btn_frame2, command=self.generate_dataset, text="Update Photo Sample", width=30, font=(
            "times new roman", 13, "bold"), bg="black", fg="red")
        update_photo_button.grid(row=0, column=1)

        #-------------------------------------Right side frame-------------------------------#
        # right side frame
        right_frame = LabelFrame(bg_img, bd=5, relief=GROOVE, text="Search Student", font=(
            "times new roman", 25, "bold"))
        right_frame.place(x=680, y=60, width=830, height=710)

        # right image
        img3 = Image.open("Images\image19.png")
        img3 = img3.resize((820, 120), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        right_img = Label(right_frame, image=self.photoimg3)
        right_img.place(x=0, y=0, width=820, height=130)

        #------------------------------------Search System-----------------------------------------#

        search_frame = LabelFrame(right_frame, bd=2, relief=GROOVE,
                                  text="Search System", font=("times new roman", 17, "bold"))
        search_frame.place(x=5, y=135, width=810, height=70)

        searchby_label = Label(search_frame, text="Search By:", font=(
            "times new roman", 13, "bold"), bg="black", fg="red")
        searchby_label.grid(row=0, column=0, padx=10, sticky=W)

        search_combo = ttk.Combobox(search_frame, textvariable=self.var_combo, font=(
            "times new roman", 13, "bold"), state="readonly")
        search_combo["values"] = (
            "Select", "Roll No", "Phone No", "Student ID")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(
            search_frame, textvariable=self.var_entry, width=20, font=("times new roman", 14))
        search_entry.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        search_button = Button(search_frame, command=self.search, text="Search", width=14, font=(
            "times new roman", 12, "bold"), bg="black", fg="red")
        search_button.grid(row=0, column=3, padx=5)

        showall_button = Button(search_frame, command=self.show, text="Show All", width=14, font=(
            "times new roman", 12, "bold"), bg="black", fg="red")
        showall_button.grid(row=0, column=4, padx=5)

        #======================= Table frame============================#
        table_frame = LabelFrame(right_frame, bd=2, relief=GROOVE,
                                 text="Search Result", font=("times new roman", 17, "bold"))
        table_frame.place(x=5, y=210, width=810, height=400)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("Department", "Course", "Year", "Semester", "StudentID", "Student Name", "Section", "Email",
                                          "Roll No", "DOB", "Gender", "Phone No", "Address", "Teacher Name", "Photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("StudentID", text="StudentID")
        self.student_table.heading("Student Name", text="Student Name")
        self.student_table.heading("Section", text="Section")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Roll No", text="Roll No")
        self.student_table.heading("DOB", text="Date of Birth")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Phone No", text="Phone No")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Teacher Name", text="Teacher Name")
        self.student_table.heading("Photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("Department", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("StudentID", width=100)
        self.student_table.column("Student Name", width=100)
        self.student_table.column("Section", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Roll No", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Phone No", width=100)
        self.student_table.column("Address", width=200)
        self.student_table.column("Teacher Name", width=100)
        self.student_table.column("Photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    #=======================================Function declaration===========================#

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_id.get() == "" or self.var_stu_name == "" or self.var_roll.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="9631921702@sql", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_id.get(),
                    self.var_stu_name.get(),
                    self.var_sec.get(),
                    self.var_email.get(),
                    self.var_roll.get(),
                    self.var_dob.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student details has been added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error:{str(es)}", parent=self.root)

    #==========================Fetch data=================================#

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="9631921702@sql", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    #========================GET cursor=================#

    def get_cursor(self, event):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_stu_name.set(data[5]),
        self.var_sec.set(data[6]),
        self.var_email.set(data[7]),
        self.var_roll.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_gender.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #=============================update function=======================================#

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_id.get() == "" or self.var_stu_name == "" or self.var_roll.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you want to update this student details?", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="9631921702@sql", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Department=%s, Course=%s, Year=%s,Semester=%s,`Student Name`=%s,Section=%s,Email=%s,`Roll No`=%s,DOB=%s,Gender=%s,`Phone No`=%s,Address=%s,`Teacher Name`=%s,PhotoSampleStatus=%s where StudentID=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_stu_name.get(),
                        self.var_sec.get(),
                        self.var_email.get(),
                        self.var_roll.get(),
                        self.var_dob.get(),
                        self.var_gender.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_id.get()
                    ))
                else:
                    if not Update:
                        return

                messagebox.showinfo(
                    "Success", "Student details has been Successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error:{str(es)}", parent=self.root)

    #=================================Delete functio=======================#

    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror(
                "Errro", "Select a Student First", parent=self.root)
        else:
            try:
                Delete = messagebox.askyesno(
                    "Delete", "Do you want to delete this student details?", parent=self.root)
                if Delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="9631921702@sql", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where StudentID=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Student details has been Successfully Deleted", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error:{str(es)}", parent=self.root)

    #===============================Reset Function======================#

    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_id.set(""),
        self.var_stu_name.set(""),
        self.var_sec.set(""),
        self.var_email.set(""),
        self.var_roll.set(""),
        self.var_dob.set(""),
        self.var_gender.set("Select Gender"),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set(""),

    #==========================================Generate photo sample=====================================#

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_id.get() == "" or self.var_stu_name == "" or self.var_roll.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="9631921702@sql", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set Department=%s, Course=%s, Year=%s,Semester=%s,`Student Name`=%s,Section=%s,Email=%s,`Roll No`=%s,DOB=%s,Gender=%s,`Phone No`=%s,Address=%s,`Teacher Name`=%s,PhotoSampleStatus=%s where StudentID=%s", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_stu_name.get(),
                    self.var_sec.get(),
                    self.var_email.get(),
                    self.var_roll.get(),
                    self.var_dob.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_id.get() == id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Loading predefined frontal face file
                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for(x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, user_frame = cap.read()
                    if face_cropped(user_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(user_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + \
                            str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo(
                    "Result", "Generating datasets completed!!!")

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error:{str(es)}", parent=self.root)

    #---------------------------------------Search system-------------------------------------#

    def search(self):
        try:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="9631921702@sql", database="face_recognizer")
            my_cursor = conn.cursor()
            value = (self.var_entry.get(),)
            if self.var_combo.get() == "Roll No":
                query1 = ("select * from student where `Roll No`=%s")
                my_cursor.execute(query1, value)
                data = my_cursor.fetchall()

                if len(data) != 0:
                    self.student_table.delete(
                        *self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                else:
                    self.student_table.delete(
                        *self.student_table.get_children())
                    conn.commit()
                conn.close()

            elif self.var_combo.get() == "Phone No":
                query2 = ("select * from student where `Phone No`=%s")
                my_cursor.execute(query2, value)
                data = my_cursor.fetchall()

                if len(data) != 0:
                    self.student_table.delete(
                        *self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                else:
                    self.student_table.delete(
                        *self.student_table.get_children())
                    conn.commit()
                conn.close()

            elif self.var_combo.get() == "Student ID":
                query3 = ("select * from student where StudentID=%s")
                my_cursor.execute(query3, value)
                data = my_cursor.fetchall()

                if len(data) != 0:
                    self.student_table.delete(
                        *self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                else:
                    self.student_table.delete(
                        *self.student_table.get_children())
                    conn.commit()
                conn.close()

        except Exception as es:
            messagebox.showerror(
                "Error", f"Error:{str(es)}", parent=self.root)

    #--------------------------------------------Show all-----------------------------------------#

    def show(self):
        self.var_combo.set("Select")
        self.var_entry.set("")
        conn = mysql.connector.connect(
            host="localhost", username="root", password="9631921702@sql", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()
