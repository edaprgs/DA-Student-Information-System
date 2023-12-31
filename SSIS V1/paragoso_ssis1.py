# Eda Grace J. Paragoso 2021-1574 
#======================================== STUDENT INFORMATION SYSTEM V.1 ========================================#
import tkinter
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk 
import tkinter.messagebox as tkMessageBox
import customtkinter

customtkinter.set_appearance_mode("light") 
customtkinter.set_default_color_theme("green") 

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("SSIS version 1.0")
        self.geometry("800x600+0+0")
        self.resizable(False, False)

    # configure grid layout
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=0)
    # header frame 
        self.header_frame = customtkinter.CTkFrame(self)
        self.header_frame.grid(row=0,column=0,padx=10,pady=30)
        self.header_label = customtkinter.CTkLabel(self.header_frame,text="STUDENT INFORMATION SYSTEM",font=("Arial",22,"bold"),fg_color="palegreen4",text_color="white",width=700,height=55)
        self.header_label.configure(corner_radius=10,bg_color="gray92")
        self.header_label.grid(row=0,column=0)
    # tabview
        self.tabview = customtkinter.CTkTabview(self,width=700,height=450)
        self.tabview.configure(segmented_button_fg_color="palegreen3",segmented_button_selected_color="palegreen2",segmented_button_unselected_color="palegreen3",segmented_button_unselected_hover_color="palegreen2",text_color="black")
        self.tabview.grid(row=1,column=0)
        self.tabview.add("Add Course")
        self.tabview.add("Add Student")
        self.tabview.add("List")

#======================================== ADD COURSE TABVIEW ========================================#       
    # add course form
        self.addcourse_label = customtkinter.CTkLabel(self.tabview.tab("Add Course"),text="ADD COURSE:",font=("Arial",14,"bold"))
        self.addcourse_label.place(x=50,y=65)
        self.course_label = customtkinter.CTkLabel(self.tabview.tab("Add Course"),text="Course:",font=("Arial",14))
        self.course_label.place(x=50,y=110)
        self.course_entry = customtkinter.CTkEntry(self.tabview.tab("Add Course"),placeholder_text="e.g. BACHELOR OF SCIENCE IN COMPUTER SCIENCE",placeholder_text_color="palegreen4",border_color="palegreen4",width=470,height=30)
        self.course_entry.place(x=160,y=110)
        self.savecourse_btn = customtkinter.CTkButton(self.tabview.tab("Add Course"),text="Add Course",text_color=("black","white"),fg_color="palegreen2",hover_color="palegreen1",border_width=1,border_color="palegreen3",width=90,command=self.add_course)
        self.savecourse_btn.place(x=540,y=160)
    
#======================================== ADD STUDENT TABVIEW ========================================#
    # add student form
        self.addstudent_label = customtkinter.CTkLabel(self.tabview.tab("Add Student"),text="ADD STUDENT:",font=("Arial",14,"bold"))
        self.addstudent_label.place(x=50,y=30)
        self.studentID_label = customtkinter.CTkLabel(self.tabview.tab("Add Student"),text="Student ID:",font=("Arial",14))
        self.studentID_label.place(x=50,y=75)
        self.fName_label = customtkinter.CTkLabel(self.tabview.tab("Add Student"),text="First Name:",font=("Arial",14))
        self.fName_label.place(x=50,y=135)
        self.mName_label = customtkinter.CTkLabel(self.tabview.tab("Add Student"),text="Middle Name:",font=("Arial",14))
        self.mName_label.place(x=50,y=195)
        self.lName_label = customtkinter.CTkLabel(self.tabview.tab("Add Student"),text="Last Name:",font=("Arial",14))
        self.lName_label.place(x=50,y=255)
        self.course_label = customtkinter.CTkLabel(self.tabview.tab("Add Student"),text="Course:",font=("Arial",14))
        self.course_label.place(x=50,y=315)
        self.ylevel_label = customtkinter.CTkLabel(self.tabview.tab("Add Student"),text="Year Level:",font=("Arial",14))
        self.ylevel_label.place(x=360,y=110)
        self.gender_label = customtkinter.CTkLabel(self.tabview.tab("Add Student"),text="Gender:",font=("Arial",14))
        self.gender_label.place(x=360,y=165)
        self.contactnum_label = customtkinter.CTkLabel(self.tabview.tab("Add Student"),text="Contact No.",font=("Arial",14))
        self.contactnum_label.place(x=360,y=225)
    # add student user-inputs
    # student ID
        self.studentID_entry = customtkinter.CTkEntry(self.tabview.tab("Add Student"),placeholder_text="e.g. 2021-1574",placeholder_text_color="palegreen4",border_color="palegreen4",width=160,height=30)
        self.studentID_entry.place(x=160,y=75)
    # student name
        self.fName_entry = customtkinter.CTkEntry(self.tabview.tab("Add Student"),placeholder_text="e.g. EDA GRACE",placeholder_text_color="palegreen4",border_color="palegreen4",width=160,height=30)
        self.fName_entry.place(x=160,y=135)
        self.mName_entry = customtkinter.CTkEntry(self.tabview.tab("Add Student"),placeholder_text="e.g. JUTBA",placeholder_text_color="palegreen4",border_color="palegreen4",width=160,height=30)
        self.mName_entry.place(x=160,y=195)
        self.lName_entry = customtkinter.CTkEntry(self.tabview.tab("Add Student"),placeholder_text="e.g. PARAGOSO",placeholder_text_color="palegreen4",border_color="palegreen4",width=160,height=30)
        self.lName_entry.place(x=160,y=255)
    # student course
        with open("courses.txt", "r") as f:
            course_list = f.read().splitlines()
        self.course_var = tkinter.StringVar(value="Select")
        self.course_option = customtkinter.CTkOptionMenu(self.tabview.tab("Add Student"),dynamic_resizing=FALSE,width=300,values=course_list,fg_color="palegreen4",dropdown_fg_color="palegreen4",dropdown_hover_color="palegreen3",button_color="palegreen3",button_hover_color="palegreen3",text_color="white",dropdown_text_color="white",variable=self.course_var)
        self.course_option.place(x=160,y=315)
    # student year level
        self.ylevel_var = tkinter.StringVar(value="Select")
        self.ylevel_option = customtkinter.CTkOptionMenu(self.tabview.tab("Add Student"),width=170,values=["1ST YEAR","2ND YEAR","3RD YEAR","4TH YEAR"],fg_color="palegreen4",dropdown_fg_color="palegreen4",dropdown_hover_color="palegreen3",button_color="palegreen3",button_hover_color="palegreen3",text_color="white",dropdown_text_color="white",variable=self.ylevel_var)
        self.ylevel_option.place(x=460,y=110)
    # student gender
        self.gender_var = tkinter.StringVar()
        self.female_rbtn = customtkinter.CTkRadioButton(self.tabview.tab("Add Student"),text="FEMALE",border_color="palegreen4",variable=self.gender_var,value="FEMALE")
        self.female_rbtn.place(x=460,y=170)
        self.male_rbtn = customtkinter.CTkRadioButton(self.tabview.tab("Add Student"),text="MALE",border_color="palegreen4",variable=self.gender_var,value="MALE")
        self.male_rbtn.place(x=565,y=170)
    # student contact number
        self.contactnum_entry = customtkinter.CTkEntry(self.tabview.tab("Add Student"),placeholder_text="e.g. 09351454490",placeholder_text_color="palegreen4",border_color="palegreen4",width=170,height=30)
        self.contactnum_entry.place(x=460,y=225)
    # add student information
        self.savebtn = customtkinter.CTkButton(self.tabview.tab("Add Student"),text="Add Student",text_color=("black","white"),fg_color="palegreen2",hover_color="palegreen1",border_width=1,border_color="palegreen3",width=90,command=self.add_student)
        self.savebtn.place(x=540,y=315)

#======================================== LIST TABVIEW ========================================#
        self.studenttab_btn = customtkinter.CTkButton(self.tabview.tab("List"),text="List of Students",font=("Arial",14,"bold"),fg_color="palegreen4",hover_color="palegreen3",width=180,height=40,command=self.display_studentlist)
        self.studenttab_btn.place(x=260,y=120)
        self.coursetab_btn = customtkinter.CTkButton(self.tabview.tab("List"),text="List of Courses",font=("Arial",14,"bold"),fg_color="palegreen4",hover_color="palegreen3",width=180,height=40,command=self.display_courselist)
        self.coursetab_btn.place(x=260,y=180)

#======================================== TABLE STYLE ========================================#
    def table_style(self):
        style=ttk.Style()
        style.theme_use("vista")
        style.configure("Treeview",bg="white",fg="black",rowheight=35,fieldbackground="white")
        style.configure("Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 12)) # Modify the font of the body
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
        style.map("Treeview",background=[("selected","palegreen4")])

#======================================== ADD STUDENT ========================================#
    def clear_student_inputs(self):
        self.studentID_entry.delete(0, END)
        self.fName_entry.delete(0, END)
        self.mName_entry.delete(0, END)
        self.lName_entry.delete(0, END)
        self.gender_var.set(None)
        self.ylevel_var.set('Select')
        self.course_var.set('Select')
        self.contactnum_entry.delete(0, END)

    def add_student(self):
    # get the student info from the input fields
        student_id = self.studentID_entry.get()
        last_name = self.lName_entry.get().upper()
        first_name = self.fName_entry.get().upper()
        middle_name = self.mName_entry.get().upper()
        selected_gender = str(self.gender_var.get())
        selected_ylevel = str(self.ylevel_var.get())
        selected_course = str(self.course_var.get())
        contactnum = self.contactnum_entry.get()
    # input in the file
        if student_id=='' or last_name=='' or first_name=='' or middle_name=='' or selected_gender=='' or selected_ylevel=='' or selected_course=='' or contactnum=='': tkMessageBox.showwarning("Warning","Please fill the empty field!")
        else:
            if self.student_exists(student_id):
                tkMessageBox.showerror("Error", "There is already a student with the same student ID in the system!")
            else:
                student_record = f"\n{student_id}|{last_name}|{first_name}|{middle_name}|{selected_gender}|{selected_ylevel}|{selected_course}|{contactnum}"
                with open("students.txt", "a") as f:
                    f.write(student_record)
                tkMessageBox.showinfo("Message", "The student information has been successfully added!")
        self.clear_student_inputs()

    def student_exists(self, student_id):
        with open("students.txt", "r") as f:
            for line in f:
                if line.startswith(student_id + "|"):
                    return True
        return False
        
#======================================== DISPLAY LIST OF STUDENTS ========================================#
    def display_studentlist(self):
    # list of students frame
        self.studentlist_frame = customtkinter.CTkFrame(self.tabview.tab("List"),width=680,height=390,fg_color="transparent")
        self.studentlist_frame.grid(row=1,column=0)
        self.studentlist_label = tk.Label(self.studentlist_frame,text="STUDENTS LIST",font=("Arial",12,"bold"),bg="grey85")
        self.studentlist_label.place(x=38,y=15)
    # a button to access the list of courses
        self.courselist_btn = customtkinter.CTkButton(self.studentlist_frame,text="List of Courses",text_color=("black"),fg_color="palegreen2",hover_color="palegreen1",border_width=1,border_color="palegreen3",width=65,height=30,command=self.display_courselist)
        self.courselist_btn.place(x=25,y=350)
    # student list table
        self.table_style()
        self.table_frame = tk.Frame(self.studentlist_frame,bg="white",relief=GROOVE)
        self.table_frame.place(x=30,y=50,width=795,height=370)
        self.y_scroll = customtkinter.CTkScrollbar(self.table_frame,orientation=VERTICAL,button_color="palegreen4",button_hover_color="palegreen3")
        self.x_scroll = customtkinter.CTkScrollbar(self.table_frame,orientation=HORIZONTAL,button_color="palegreen4",button_hover_color="palegreen3")
        self.student_table = ttk.Treeview(self.table_frame,columns=("Student ID","Last Name","First Name","Middle Name","Gender","Year Level","Course","Contact No."),yscrollcommand=self.y_scroll.set,xscrollcommand=self.x_scroll.set)
        self.y_scroll.configure(command=self.student_table.yview)
        self.x_scroll.configure(command=self.student_table.xview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.x_scroll.pack(side=BOTTOM,fill=X)
    # columns
        self.student_table['columns'] = ("Student ID","Last Name","First Name","Middle Name","Gender","Year Level","Course","Contact No.")
        self.student_table.column("#0",width=0,stretch=NO)
        self.student_table.column("Student ID",anchor=CENTER,width=100)
        self.student_table.column("Last Name",anchor=CENTER,width=200)
        self.student_table.column("First Name",anchor=CENTER,width=200)
        self.student_table.column("Middle Name",anchor=CENTER,width=200)
        self.student_table.column("Gender",anchor=CENTER,width=75)
        self.student_table.column("Year Level",anchor=CENTER,width=100)
        self.student_table.column("Course",anchor=CENTER,width=500)
        self.student_table.column("Contact No.",anchor=CENTER,width=110)
    # headings
        self.student_table.heading("#0",text="",anchor=W)
        self.student_table.heading("Student ID",text="Student ID",anchor=CENTER)
        self.student_table.heading("Last Name",text="Last Name",anchor=CENTER)
        self.student_table.heading("First Name",text="First Name",anchor=CENTER)
        self.student_table.heading("Middle Name",text="Middle Name",anchor=CENTER)
        self.student_table.heading("Gender",text="Gender",anchor=CENTER)
        self.student_table.heading("Year Level",text="Year Level",anchor=CENTER)
        self.student_table.heading("Course",text="Course",anchor=CENTER)
        self.student_table.heading("Contact No.",text="Contact No.",anchor=CENTER)
        self.student_table.pack(fill=BOTH,expand=True)
    # to fetch data from the file and display in the table
        with open("students.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                data = line.strip().split("|")
                if len(data) >= 2:
                    student_id = data[0]
                    last_name = data[1]
                    first_name = data[2]
                    middle_name = data[3]
                    selected_gender = data[4]
                    selected_ylevel = data[5]
                    selected_course = data[6]
                    contactnum = data[7]
                    self.student_table.insert("", tk.END, values=(student_id, last_name, first_name, middle_name, selected_gender, selected_ylevel, selected_course, contactnum))
    # search student
        self.searchstudent_var = StringVar()
        self.search_label = customtkinter.CTkLabel(self.studentlist_frame,text="Search:")
        self.search_label.place(x=460,y=5)
        self.search_entry1 = customtkinter.CTkEntry(self.studentlist_frame,textvariable=self.searchstudent_var,placeholder_text="e.g. 2021-1574",placeholder_text_color="palegreen4",border_color="palegreen4", width=145)
        self.search_entry1.place(x=510,y=5)
        self.search_entry1.bind("<Key>",self.display_searchstudent)
    # delete student
        self.deletestudent_btn = customtkinter.CTkButton(self.studentlist_frame,text="Delete Student",text_color=("white","white"),fg_color="red2",hover_color="red",width=70,command=self.delete_student_data)
        self.deletestudent_btn.place(x=560,y=350)
    # edit student 
        self.editstudent_btn = customtkinter.CTkButton(self.studentlist_frame,text="Edit Student",text_color=("black"),fg_color="palegreen2",hover_color="palegreen1",border_width=1,border_color="palegreen3",width=70,command=self.edit_student_data)
        self.editstudent_btn.place(x=465,y=350)
    # update student list
        self.updatestudent_btn = customtkinter.CTkButton(self.studentlist_frame,text="Update List",text_color=("black"),fg_color="palegreen2",hover_color="palegreen1",border_width=1,border_color="palegreen3",width=70,command=self.update_student_table)
        self.updatestudent_btn.place(x=375,y=350)

#======================================== UPDATE STUDENT LIST ON THE TABLE ========================================#
    def update_student_table(self):
        with open("students.txt", "r") as f:
            student_data = [line.strip().split("|") for line in f]

        self.student_table.delete(*self.student_table.get_children())

        for data in student_data:
            if len(data) >= 2:
                student_id = data[0]
                last_name = data[1]
                first_name = data[2]
                middle_name = data[3]
                selected_gender = data[4]
                selected_ylevel = data[5]
                selected_course = data[6]
                contactnum = data[7]

                values = (student_id, last_name, first_name, middle_name, selected_gender, selected_ylevel, selected_course, contactnum)
                self.student_table.insert("", tk.END, values=values)

#======================================== SEARCH STUDENT ========================================#
    def display_searchstudent(self, ev):
        if self.searchstudent_var.get() != "":
    # Clearing current display data
            self.student_table.delete(*self.student_table.get_children())
    # Read students.txt and filter the matching students
            with open('students.txt', 'r') as f:
                students = [line.strip().split('|') for line in f.readlines()]
                matching_students = [student for student in students if any(self.searchstudent_var.get().upper() in field.upper() for field in student)]
            for student in matching_students:
                self.student_table.insert(parent='', index='end', text='', values=student)

#======================================== DELETE STUDENT ========================================#
    def delete_student_data(self):
        if not self.student_table.selection():
            tkMessageBox.showerror("Error", "No item selected. Please select a student from the table.")
            return
        decision = tkMessageBox.askquestion("Warning", "Are you sure you want to delete the selected student?")
        if decision != 'yes':
            return
        selected_item = self.student_table.selection()[0]
        delete_data = str(self.student_table.item(selected_item)['values'][0])
        try:
            with open('students.txt', 'r') as f:
                lines = f.readlines()

            with open('students.txt', 'r') as f:
                lines = f.readlines()
    # Remove the selected student's data
                new_lines = []
                for line in lines:
                    if delete_data not in line.strip():
                        new_lines.append(line)
    # Write the remaining data back to the file
                with open('students.txt', 'w') as f:
                    f.write("".join(new_lines).strip())
                tkMessageBox.showinfo("Message", "Student information deleted successfully!")
        except:
            tkMessageBox.showerror("Error", "An error has occurred!")
            return
        self.update_student_table()

# ======================================== UPDATE STUDENT RECORD ========================================
    def update_student_data(self):
        decision = tkMessageBox.askquestion("Warning", "Are you sure you want to make changes in the student information?")
        if decision != 'yes':
            tkMessageBox.showinfo("Message", "The changes have not been saved")
            return
        selected_id = self.student_table.focus()
        id_details = str(self.student_table.item(selected_id)['values'][0])
        student_id = str(id_details).strip()
    # Open the file and read its contents
        with open("students.txt", "r") as f:
            data = f.readlines()
    # Update the student record in the file data
        for i in range(len(data)):
            line = data[i].strip()
            if line.startswith(student_id):
                # Split the line into student info
                student_info = line.split("|")
                student_info[1] = self.lName_entry.get().upper()
                student_info[2] = self.fName_entry.get().upper()
                student_info[3] = self.mName_entry.get().upper()
                student_info[4] = self.gender_var.get()
                student_info[5] = self.ylevel_var.get()
                student_info[6] = self.course_var.get()
                student_info[7] = self.contactnum_entry.get()
                data[i] = "|".join(student_info) + "\n"
                break
    # Save the updated data back to the file
        with open("students.txt", "w") as f:
            f.writelines(data)
        tkMessageBox.showinfo("Message","The edited information has been updated successfully!")
        self.update_student_table()
        self.edit_window.destroy()

#======================================== EDIT STUDENT RECORD ========================================#
    def edit_student_data(self):
        if not self.student_table.selection():
            tkMessageBox.showerror("Error", "No item selected. Please select a student from the table.")
            return
        
        self.edit_window = Toplevel(self)
        self.edit_window.title("Edit Student Information")
        self.edit_window.geometry("890x470+0+0")

        selected_id = self.student_table.focus()
        id_details = str(self.student_table.item(selected_id)['values'][0])
        with open("students.txt", "r") as f:
            data = f.readlines()
    # global variables for the entries
        global fName_entry; global mName_entry; global lName_entry; global gender_var; global ylevel_var; global course_var; global contactnum_entry
    # edit student form
        self.studentinfo_label = customtkinter.CTkLabel(self.edit_window,text="Student Information:",font=("Arial",14,"bold"))
        self.studentinfo_label.place(x=50,y=50)
        self.lName_label = customtkinter.CTkLabel(self.edit_window,text="Last Name:",font=("Arial",14))
        self.lName_label.place(x=50,y=110)
        self.fName_label = customtkinter.CTkLabel(self.edit_window,text="First Name:",font=("Arial",14))
        self.fName_label.place(x=50,y=170)
        self.mName_label = customtkinter.CTkLabel(self.edit_window,text="Middle Name:",font=("Arial",14))
        self.mName_label.place(x=50,y=230)
        self.course_label = customtkinter.CTkLabel(self.edit_window,text="Course:",font=("Arial",14))
        self.course_label.place(x=50,y=290)
        self.gender_label = customtkinter.CTkLabel(self.edit_window,text="Gender:",font=("Arial",14))
        self.gender_label.place(x=380,y=110)
        self.ylevel_label = customtkinter.CTkLabel(self.edit_window,text="Year Level:",font=("Arial",14))
        self.ylevel_label.place(x=380,y=170)
        self.contactnum_label = customtkinter.CTkLabel(self.edit_window,text="Contact No.",font=("Arial",14))
        self.contactnum_label.place(x=380,y=230)
    # edit student user-inputs
    # student name
        self.lName_entry = customtkinter.CTkEntry(self.edit_window,placeholder_text="e.g. PARAGOSO",placeholder_text_color="palegreen4",border_color="palegreen4",width=160,height=30)
        self.lName_entry.place(x=160,y=110)
        self.fName_entry = customtkinter.CTkEntry(self.edit_window,placeholder_text="e.g. EDA GRACE",placeholder_text_color="palegreen4",border_color="palegreen4",width=160,height=30)
        self.fName_entry.place(x=160,y=170)
        self.mName_entry = customtkinter.CTkEntry(self.edit_window,placeholder_text="e.g. JUTBA",placeholder_text_color="palegreen4",border_color="palegreen4",width=160,height=30)
        self.mName_entry.place(x=160,y=230)
    # student course
        with open("courses.txt", "r") as f:
            courses = f.readlines()
            course_list = [course.strip() for course in courses]
    # Combine student course and additional courses on the course option
        self.course_option = customtkinter.CTkOptionMenu(self.edit_window, width=370,dynamic_resizing=False,values=course_list,fg_color="palegreen4",dropdown_fg_color="palegreen4",dropdown_hover_color="palegreen3",button_color="palegreen3",button_hover_color="palegreen3",text_color="white",dropdown_text_color="white",variable=self.course_var)
        self.course_option.place(x=160, y=290)
    # student gender
        self.gender_var = tkinter.StringVar()
        self.female_rbtn = customtkinter.CTkRadioButton(self.edit_window,text="FEMALE",border_color="palegreen4",variable=self.gender_var,value="FEMALE")
        self.female_rbtn.place(x=480,y=115)
        self.male_rbtn = customtkinter.CTkRadioButton(self.edit_window,text="MALE",border_color="palegreen4",variable=self.gender_var,value="MALE")
        self.male_rbtn.place(x=590,y=115)
    # student year level
        self.ylevel_var = tkinter.StringVar()
        self.ylevel_option = customtkinter.CTkOptionMenu(self.edit_window,width=175,values=["1ST YEAR","2ND YEAR","3RD YEAR","4TH YEAR"],fg_color="palegreen4",dropdown_fg_color="palegreen4",dropdown_hover_color="palegreen3",button_color="palegreen3",button_hover_color="palegreen3",text_color="white",dropdown_text_color="white",variable=self.ylevel_var)
        self.ylevel_option.place(x=480,y=170)
    # student contact number
        self.contactnum_entry = customtkinter.CTkEntry(self.edit_window,placeholder_text="e.g. 09351454490",placeholder_text_color="palegreen4",border_color="palegreen4",width=175,height=30)
        self.contactnum_entry.place(x=480,y=230)
    # a button to save student information
        self.savebtn = customtkinter.CTkButton(self.edit_window,text="Save Changes",text_color=("black","white"),fg_color="palegreen2",hover_color="palegreen1",border_width=1,border_color="palegreen3",width=80,command=self.update_student_data)
        self.savebtn.place(x=560,y=290) 
    # loop through results 
        for line in data:
            line = line.strip()
            if line.startswith(id_details):
    # Split the line into student info
                student_id, last_name, first_name, middle_name, selected_gender, selected_ylevel, selected_course, contactnum = line.split("|")
    # Clear the existing content of the entry fields before inserting new values
                self.lName_entry.delete(0, tkinter.END)
                self.fName_entry.delete(0, tkinter.END)
                self.mName_entry.delete(0, tkinter.END)
                self.contactnum_entry.delete(0, tkinter.END)
    # Insert the student info into the entry fields
                self.lName_entry.insert(0, last_name)
                self.fName_entry.insert(0, first_name)
                self.mName_entry.insert(0, middle_name)
                self.gender_var.set(selected_gender)
                self.ylevel_var.set(selected_ylevel)
                self.course_var.set(selected_course)
                self.contactnum_entry.insert(0, contactnum)
                break

#======================================== LIST OF COURSES ========================================#
    def display_courselist(self):
    # list of courses frame
        self.courselist_frame = customtkinter.CTkFrame(self.tabview.tab("List"),width=680,height=390,fg_color="transparent")
        self.courselist_frame.grid(row=1,column=0)
        self.courselist_label = tk.Label(self.courselist_frame,text="COURSES LIST",font=("Arial",12,"bold"),fg="black",bg="grey85")
        self.courselist_label.place(x=38,y=15)
    # a button to access the list of students
        self.studentlist_btn = customtkinter.CTkButton(self.courselist_frame,text="List of Students",fg_color="palegreen2",hover_color="palegreen1",text_color=("black"),border_width=1,border_color="palegreen3",width=65,height=30,command=self.display_studentlist)
        self.studentlist_btn.place(x=25,y=350)
    # course list table
        self.table_style()
        self.table_frame = tk.Frame(self.courselist_frame,bg="white",relief=GROOVE)
        self.table_frame.place(x=30,y=50,width=795,height=370)
        self.y_scroll = customtkinter.CTkScrollbar(self.table_frame,orientation=VERTICAL,button_color="palegreen4",button_hover_color="palegreen3")
        self.course_table = ttk.Treeview(self.table_frame,columns=("Course"),yscrollcommand=self.y_scroll.set)
        self.y_scroll.configure(command=self.course_table.yview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
    # columns
        self.course_table['columns'] = ("Course")
        self.course_table.column("#0",width=0,stretch=NO)
        self.course_table.column("Course",anchor=CENTER,width=280)
    # headings
        self.course_table.heading("#0",text="",anchor=W)
        self.course_table.heading("Course",text="Course",anchor=CENTER)
        self.course_table.pack(fill=BOTH,expand=True)
    # to fetch data from database and display in the table
        with open("courses.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                course = line.strip()
                self.course_table.insert("", tk.END, values=(course,)) 
    # search course
        self.searchcourse_var = StringVar()
        self.search_label = customtkinter.CTkLabel(self.courselist_frame,text="Search:")
        self.search_label.place(x=460,y=5)
        self.search_entry2 = customtkinter.CTkEntry(self.courselist_frame,textvariable=self.searchcourse_var,placeholder_text="e.g. BSCS",placeholder_text_color="palegreen4",border_color="palegreen4", width=145)
        self.search_entry2.place(x=510,y=5)
        self.search_entry2.bind("<Key>",self.display_searchcourse)
    # edit course
        self.editcourse_btn = customtkinter.CTkButton(self.courselist_frame,text="Edit Course",text_color=("black"),fg_color="palegreen2",hover_color="palegreen1",border_width=1,border_color="palegreen3",width=70,command=self.edit_course_data)
        self.editcourse_btn.place(x=475,y=350)
    # delete course
        self.deletecourse_btn = customtkinter.CTkButton(self.courselist_frame,text="Delete Course",text_color=("white","white"),fg_color="red2",hover_color="red",width=70,command=self.delete_course)
        self.deletecourse_btn.place(x=565,y=350)
    # update course list
        self.updatecourse_btn = customtkinter.CTkButton(self.courselist_frame,text="Update List",text_color=("black"),fg_color="palegreen2",hover_color="palegreen1",border_width=1,border_color="palegreen3",width=70,command=self.update_course_table)
        self.updatecourse_btn.place(x=385,y=350)

#======================================== ADD COURSE ========================================#
    def clear_course_inputs(self):
        self.course_entry.delete(0, END)

    def add_course(self):
    # get the course from the input field
        course = self.course_entry.get().upper()
    # input in the file
        if course=='': tkMessageBox.showwarning("Warning","Please fill the empty field!")
        else:
            if self.course_exists(course):
                tkMessageBox.showerror("Error", "The course cannot be added. It already exists!")
            else:
                course_record = f"\n{course}"
                with open("courses.txt", "a") as f:
                    f.write(course_record)
                tkMessageBox.showinfo("Message","Course added successfully!")
        self.clear_course_inputs()
    
    def course_exists(self, course):
        with open("courses.txt", "r") as f:
            for line in f:
                if line.strip().startswith(course):
                    return True
        return False

#======================================== UPDATE COURSE LIST ON THE TABLE ========================================#
    def update_course_table(self):
        with open("courses.txt", "r") as f:
            lines = f.readlines()
            self.course_table.delete(*self.course_table.get_children())
            for line in lines:
                course = line.strip()
                self.course_table.insert("", tk.END, values=(course,))
    
#======================================== SEARCH COURSE ========================================#
    def display_searchcourse(self,ev):
        if self.searchcourse_var.get() != "":
    # clearing current display data
            self.course_table.delete(*self.course_table.get_children())
        with open('courses.txt', 'r') as f:
            lines = f.readlines()
            matching_course = [course.strip() for course in lines if self.searchcourse_var.get().upper() in course.upper()]
    # update the table with the matching course
        for course in matching_course:
            self.course_table.insert(parent='', index='end', text='', values=(course,))

#======================================== DELETE COURSE ========================================#
    def check_students_enrolled(self,course):
        with open('students.txt', 'r') as f:
            lines = f.readlines()
        for line in lines:
            data = line.split('|')
            if data[6].strip() == course:
                return True
        return False
    
    def delete_course(self):
        if not self.course_table.selection():
            tkMessageBox.showerror("Error", "No item selected. Please select a course from the table.")
            return
        selected_item = self.course_table.selection()[0]
        delete_data = str(self.course_table.item(selected_item)['values'][0])
    # Check if there are students enrolled in the course
        if self.check_students_enrolled(delete_data):
            tkMessageBox.showwarning("Warning", "There are students enrolled in this course. Course cannot be deleted.")
            return
        decision = tkMessageBox.askquestion("Warning","Are you sure you want to delete the course selected?")
        if decision != 'yes':
            return
        else:
            try:
                with open('courses.txt', 'r') as f:
                    lines = f.readlines()
    # Remove the selected course's data
                new_lines = []
                for line in lines:
                    if delete_data not in line.strip():
                        new_lines.append(line)
    # Write the remaining data back to the file
                with open('courses.txt', 'w') as f:
                    f.write("".join(new_lines).strip())
                tkMessageBox.showinfo("Message","The course has been deleted successfully!")
            except:
                tkMessageBox.showerror("Error","An error has occured!")
                return
        self.update_course_table()

# ======================================== UPDATE COURSE RECORD ========================================
    def update_course_data(self):
        decision = tkMessageBox.askquestion("Warning", "Are you sure you want to make changes in the course information?")
        if decision != 'yes':
            tkMessageBox.showinfo("Message", "The changes have not been saved")
            return
        selected_code = self.course_table.focus()
        code_details = str(self.course_table.item(selected_code)['values'][0])

    # Open the file and read its contents
        with open("courses.txt", "r") as f:
            course_data = f.readlines()
    # Update the course record in the file data
        for i in range(len(course_data)):
            line = course_data[i].strip()
            if line.startswith(code_details):
                course_name = self.course_entry.get().upper()
                if self.coursename_exists(course_name):
                    tkMessageBox.showerror("Error", "The course cannot be added. It already exists!")
                else:
                    course_data[i] = course_name + "\n"
                    break
    # Save the updated data back to the file
        with open("courses.txt", "w") as f:
            f.writelines(course_data)
    # Open the students file and read its contents
        with open("students.txt", "r") as f:
            student_data = f.readlines()
    # Update the course name in the student records
        updated_student_data = []
        course_name = self.course_entry.get().upper()  
        for line in student_data:
            line = line.strip()
            student_info = line.split("|")
            if len(student_info) >= 7 and student_info[6] == code_details:
                student_info[6] = course_name 
            updated_student_data.append("|".join(student_info) + "\n") 
    # Save the updated data back to the students file
        with open("students.txt", "w") as f:
            f.writelines(updated_student_data) 
        tkMessageBox.showinfo("Message", "The changes have been saved successfully!")
        self.update_course_table()
        self.edit_window.destroy()

    def coursename_exists(self, course):
        with open("courses.txt", "r") as f:
            course_data = f.readlines()
        for line in course_data:
            if course in line.strip():
                return True
        return False

#======================================== EDIT COURSE RECORD ========================================#
    def edit_course_data(self):
        if not self.course_table.selection():
            tkMessageBox.showerror("Error", "No item selected. Please select a course from the table.")
            return
        
        self.edit_window = Toplevel(self)
        self.edit_window.title("Edit Course Information")
        self.edit_window.geometry("700x240+0+0")

        selected_code = self.course_table.focus()
        code_details = str(self.course_table.item(selected_code)['values'][0])
        
        with open("courses.txt", "r") as f:
            data = f.readlines()
    # global variables for the entries
        global course_entry
    # edit course form
        self.course_label = customtkinter.CTkLabel(self.edit_window,text="Course:",font=("Arial",12))
        self.course_label.place(x=25,y=50)
        self.course_entry = customtkinter.CTkEntry(self.edit_window,placeholder_text="e.g. BACHELOR OF SCIENCE IN COMPUTER SCIENCE",placeholder_text_color="palegreen4",border_color="palegreen4",width=450,height=30)
        self.course_entry.place(x=80,y=50)
    # save added course
        self.savecourse_btn = customtkinter.CTkButton(self.edit_window,text="Save Changes",text_color=("black"),fg_color="palegreen2",hover_color="palegreen1",border_width=1,border_color="palegreen3",width=80,command=self.update_course_data)
        self.savecourse_btn.place(x=435,y=100)    
    # loop through results 
        for line in data:
            line = line.strip()
            if line.startswith(code_details):
                course_name = line
                # Insert the course info into the entry fields
                self.course_entry.insert(0, course_name)
                break

if __name__ == "__main__":
    app = App()
    app.mainloop()
