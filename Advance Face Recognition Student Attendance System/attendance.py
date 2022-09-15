from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import csv
from tkinter import filedialog

mydata = []
myDataList = []


class attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x820+0+0")
        self.root.title("Attendance Panel")
        self.root.wm_iconbitmap("logo.ico")

        # variables for all fields:
        self.var_dep = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_status = StringVar()

        # background image
        img1 = Image.open("Images\image21.png")
        img1 = img1.resize((1600, 800), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1600, height=800)

        title = Label(bg_img, text="Attendance Panel", font=(
            "fantasy", 45, "bold"), bg="black", fg="red")
        title.place(x=0, y=0, width=1600, height=70)

        #=========================================Left frame====================================#

        # left side frame
        left_frame = LabelFrame(bg_img, bd=5, relief=GROOVE, text="Student Details", font=(
            "times new roman", 25, "bold",))
        left_frame.place(x=10, y=100, width=700, height=670)

        # left image
        img2 = Image.open("Images\image18.jpg")
        img2 = img2.resize((680, 120), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        left_img = Label(left_frame, image=self.photoimg2)
        left_img.place(x=0, y=0, width=680, height=130)

        # detail frame
        detail_frame = Frame(left_frame, bd=2, relief=GROOVE)
        detail_frame.place(x=5, y=135, width=680, height=480)

        # Student id
        StudentId_label = Label(detail_frame, text="Student ID:", font=(
            "times new roman", 14, "bold"))
        StudentId_label.grid(row=0, column=0, padx=10, sticky=W)

        StudentId_entry = ttk.Entry(
            detail_frame, textvariable=self.var_id, width=20, font=("times new roman", 14))
        StudentId_entry.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        # Roll No
        Rollno_label = Label(detail_frame, text="Roll No:", font=(
            "times new roman", 14, "bold"))
        Rollno_label.grid(row=0, column=2, padx=10, sticky=W)

        Rollno_entry = ttk.Entry(
            detail_frame, textvariable=self.var_roll, width=17, font=("times new roman", 14))
        Rollno_entry.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        # student name
        StudentName_label = Label(detail_frame, text="Student Name:", font=(
            "times new roman", 14, "bold"))
        StudentName_label.grid(row=1, column=0, padx=10, sticky=W)

        StudentName_entry = ttk.Entry(
            detail_frame, textvariable=self.var_name, width=20, font=("times new roman", 14))
        StudentName_entry.grid(row=1, column=1, padx=5, pady=10, sticky=W)

        # Department
        dep_label = Label(detail_frame, text="Department",
                          font=("times new roman", 14, "bold"))
        dep_label.grid(row=1, column=2, padx=10, sticky=W)

        dep_combo = ttk.Combobox(detail_frame, textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer Science Engineering", "Computer Science and Information technology",
                               "Mechanical Engineering", "Civil Engineering", "Electrical and Electronics Engineering")
        dep_combo.current(0)
        dep_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # time
        time_label = Label(detail_frame, text="Time:", font=(
            "times new roman", 14, "bold"))
        time_label.grid(row=2, column=0, padx=10, sticky=W)

        time_entry = ttk.Entry(
            detail_frame, textvariable=self.var_time, width=20, font=("times new roman", 14))
        time_entry.grid(row=2, column=1, padx=5, pady=10, sticky=W)

        # date
        date_label = Label(detail_frame, text="Date:", font=(
            "times new roman", 14, "bold"))
        date_label.grid(row=2, column=2, padx=10, sticky=W)

        date_entry = ttk.Entry(
            detail_frame, textvariable=self.var_date, width=17, font=("times new roman", 14))
        date_entry.grid(row=2, column=3, padx=5, pady=10, sticky=W)

        # attendance status
        attendance_label = Label(detail_frame, text="Attendance Status:",
                                 font=("times new roman", 14, "bold"))
        attendance_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        attendance_combo = ttk.Combobox(detail_frame, textvariable=self.var_status, font=(
            "times new roman", 12, "bold"), width=20, state="readonly")
        attendance_combo["values"] = (
            "Select Status", "Present", "Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=3, column=1, padx=2, pady=10, sticky=W)

        # button frame1
        button1_frame = Frame(detail_frame, bd=2, relief=GROOVE)
        button1_frame.place(x=5, y=250, width=665, height=50)

        # import csv button
        import_csv_button = Button(button1_frame, command=self.importCSV, text="IMPORT CSV", width=50, font=(
            "times new roman", 17, "bold"), bg="black", fg="red")
        import_csv_button.grid(row=0, column=0)

        # button frame2
        button2_frame = Frame(detail_frame, bd=2, relief=GROOVE)
        button2_frame.place(x=5, y=300, width=665, height=50)

        # export csv button
        export_csv_button = Button(button2_frame, command=self.exportCSV, text="EXPORT CSV", width=50, font=(
            "times new roman", 17, "bold"), bg="black", fg="red")
        export_csv_button.grid(row=0, column=0)

        # button frame3
        button3_frame = Frame(detail_frame, bd=2, relief=GROOVE)
        button3_frame.place(x=5, y=350, width=665, height=50)

        # update button
        update_button = Button(button3_frame, command=self.updateData, text="UPDATE", width=50, font=(
            "times new roman", 17, "bold"), bg="black", fg="red")
        update_button.grid(row=0, column=0)

        # button frame4
        button4_frame = Frame(detail_frame, bd=2, relief=GROOVE)
        button4_frame.place(x=5, y=400, width=665, height=50)

        # reset button
        reset_button = Button(button4_frame, command=self.reset, text="RESET", width=50, font=(
            "times new roman", 17, "bold"), bg="black", fg="red")
        reset_button.grid(row=0, column=0)

        note_label = Label(detail_frame, text="NOTE: Re-import the csv file after updating the details.",
                           font=("times new roman", 10, "bold"), fg="red")
        note_label.place(x=10, y=200, width=665, height=20)

        #-------------------------------------Right side frame-------------------------------#
        # right side frame
        right_frame = LabelFrame(bg_img, bd=5, relief=GROOVE, text="Attendance Details", font=(
            "times new roman", 25, "bold"))
        right_frame.place(x=720, y=100, width=800, height=670)

        # table frame
        table_frame = Frame(right_frame, bd=2, relief=GROOVE)
        table_frame.place(x=5, y=5, width=780, height=600)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendance_table = ttk.Treeview(table_frame, column=("StudentID", "Roll No", "Student Name",
                                             "Department", "Time", "Date", "Attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("StudentID", text="StudentID")
        self.attendance_table.heading("Roll No", text="Roll No")
        self.attendance_table.heading("Student Name", text="Student Name")
        self.attendance_table.heading("Department", text="Department")
        self.attendance_table.heading("Time", text="Time")
        self.attendance_table.heading("Date", text="Date")
        self.attendance_table.heading("Attendance", text="Attendance")
        self.attendance_table["show"] = "headings"

        self.attendance_table.column("StudentID", width=100)
        self.attendance_table.column("Roll No", width=100)
        self.attendance_table.column("Student Name", width=100)
        self.attendance_table.column("Department", width=100)
        self.attendance_table.column("Time", width=100)
        self.attendance_table.column("Date", width=100)
        self.attendance_table.column("Attendance", width=100)

        self.attendance_table.pack(fill=BOTH, expand=True)
        self.attendance_table.bind("<ButtonRelease>", self.getCursor)

    #----------------------------------------Fetch data--------------------------------#

    def fetchData(self, rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("", END, values=i)

    #--------------------------------------import csv-----------------------------------------#
    def importCSV(self):
        global mydata
        mydata.clear()
        filenm = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
            ("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
        with open(filenm) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #----------------------------------------------export csv-----------------------------------#
    def exportCSV(self):
        try:
            if len(mydata) == 0:
                messagebox.showerror(
                    "Error", "No data found to export", parent=self.root)
                return False
            file2 = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
                ("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
            with open(file2, mode="w", newline="") as myfile:
                ex_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    ex_write.writerow(i)
                messagebox.showinfo("Export CSV", "Data has been exported to " +
                                    os.path.basename(file2)+" successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror(
                "Error", f"Error:{str(es)}", parent=self.root)

    #---------------------------------------get cursor------------------------------------#

    def getCursor(self, event=""):
        cursorFocus = self.attendance_table.focus()
        content = self.attendance_table.item(cursorFocus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_roll.set(data[1]),
        self.var_name.set(data[2]),
        self.var_dep.set(data[3]),
        self.var_time.set(data[4]),
        self.var_date.set(data[5]),
        self.var_status.set(data[6])

    #----------------------------------------Reset Function-----------------------------------#

    def reset(self):
        self.var_dep.set("Select Department")
        self.var_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_status.set("Select Status")

    #----------------------------------------Update button-------------------------------------#

    def updateData(self):
        if self.var_dep.get() == "Select Department" or self.var_id.get() == "" or self.var_name == "" or self.var_roll.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you want to update this student details?", parent=self.root)
                if Update > 0:
                    with open("Attendance report\Attendance.csv", "r+", newline="\n") as f:
                        myDataList = f.readlines()
                        name_list = []
                        for line in myDataList:
                            entry = line.split((","))
                            name_list.append(entry[0])

                        for i in name_list:
                            if i == self.var_id.get():
                                ex_write = csv.writer(
                                    open("Attendance report\Attendance.csv", "w"))
                                edit = (
                                    self.var_id.get(),
                                    self.var_roll.get(),
                                    self.var_name.get(),
                                    self.var_dep.get(),
                                    self.var_time.get(),
                                    self.var_date.get(),
                                    self.var_status.get()
                                )
                                ex_write.writerow(edit)

                else:
                    if not Update:
                        return

                messagebox.showinfo(
                    "Success", "Student details has been Successfully updated", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = attendance(root)
    root.mainloop()
