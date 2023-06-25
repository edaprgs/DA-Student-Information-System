# Eda Grace J. Paragoso 2021-1574 
#======================================== STUDENT INFORMATION SYSTEM V.2 ========================================#
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk 
import tkinter.messagebox as tkMessageBox
import customtkinter
import sqlite3

customtkinter.set_appearance_mode("light") 
customtkinter.set_default_color_theme("blue") 

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("SSIS version 2.0")
        self.geometry("800x600+0+0")
        self.resizable(False, False)    
        
        conn = sqlite3.connect('studentdata.db')
        cursor = conn.cursor()
    # create student table 
        create_studenttable = '''CREATE TABLE IF NOT EXISTS student_data(student_id TEXT NOT NULL PRIMARY KEY,last_name TEXT NOT NULL,first_name TEXT NOT NULL,middle_name TEXT NOT NULL,
                        gender TEXT NOT NULL,year_level TEXT NOT NULL,course TEXT NOT NULL,contact_number INTEGER,registration_date TEXT DEFAULT CURRENT_TIMESTAMP)'''
        conn.execute(create_studenttable)
    # create course table 
        create_coursetable = '''CREATE TABLE IF NOT EXISTS courses(course_code TEXT NOT NULL PRIMARY KEY,course TEXT NOT NULL)'''
        conn.execute(create_coursetable)
        conn.commit()
        conn.close()
    # configure grid layout
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=0)
    # header frame 
        self.header_frame = customtkinter.CTkFrame(self)
        self.header_frame.grid(row=0,column=0,padx=10,pady=30)
        self.header_label = customtkinter.CTkLabel(self.header_frame,text="STUDENT INFORMATION SYSTEM",font=("Arial",22,"bold"),fg_color="LightSkyBlue4",text_color="white",width=700,height=55)
        self.header_label.configure(corner_radius=10,bg_color="white smoke")
        self.header_label.grid(row=0,column=0)
    # tabview
        self.tabview = customtkinter.CTkTabview(self,width=700,height=450)
        self.tabview.configure(fg_color="azure2",segmented_button_fg_color="LightSkyBlue3",segmented_button_selected_color="LightSkyBlue4",segmented_button_unselected_color="LightSkyBlue3",segmented_button_unselected_hover_color="LightSkyBlue4",text_color="white")
        self.tabview.grid(row=1,column=0)
        self.tabview.add("Add Course")
        self.tabview.add("Add Student")
        self.tabview.add("List")

#======================================== ADD COURSE TABVIEW ========================================#       
    # add course form
        self.addcourse_label = customtkinter.CTkLabel(self.tabview.tab("Add Course"),text="ADD COURSE:",font=("Arial",14,"bold"))
        self.addcourse_label.place(x=50,y=30)
        self.coursecode_label = customtkinter.CTkLabel(self.tabview.tab("Add Course"),text="Course Code:",font=("Arial",14))
        self.coursecode_label.place(x=50,y=75)
        self.coursecode_entry = customtkinter.CTkEntry(self.tabview.tab("Add Course"),placeholder_text="e.g. BSCS",placeholder_text_color="LightSkyBlue4",border_color="LightSkyBlue4",width=150,height=30)
        self.coursecode_entry.place(x=160,y=75)
        self.course_label = customtkinter.CTkLabel(self.tabview.tab("Add Course"),text="Course:",font=("Arial",14))
        self.course_label.place(x=50,y=130)
        self.course_entry = customtkinter.CTkEntry(self.tabview.tab("Add Course"),placeholder_text="e.g. BACHELOR OF SCIENCE IN COMPUTER SCIENCE",placeholder_text_color="LightSkyBlue4",border_color="LightSkyBlue4",width=475,height=30)
        self.course_entry.place(x=160,y=130)
    # add course information
        self.savecourse_btn = customtkinter.CTkButton(self.tabview.tab("Add Course"),text="Add Course",text_color=("black","white"),fg_color="LightSkyBlue3",border_width=2,hover= True,hover_color= "LightSkyBlue4",corner_radius=10,border_color= "LightSkyBlue3",width=100,height=30,command=self.add_course)
        self.savecourse_btn.place(x=535,y=185)
        
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
        self.studentID_entry = customtkinter.CTkEntry(self.tabview.tab("Add Student"),placeholder_text="e.g. 2021-1574",placeholder_text_color="LightSkyBlue4",border_color="LightSkyBlue4",width=130,height=30)
        self.studentID_entry.place(x=160,y=75)
    # student name
        self.fName_entry = customtkinter.CTkEntry(self.tabview.tab("Add Student"),placeholder_text="e.g. EDA GRACE",placeholder_text_color="LightSkyBlue4",border_color="LightSkyBlue4",width=160,height=30)
        self.fName_entry.place(x=160,y=135)
        self.mName_entry = customtkinter.CTkEntry(self.tabview.tab("Add Student"),placeholder_text="e.g. JUTBA",placeholder_text_color="LightSkyBlue4",border_color="LightSkyBlue4",width=160,height=30)
        self.mName_entry.place(x=160,y=195)
        self.lName_entry = customtkinter.CTkEntry(self.tabview.tab("Add Student"),placeholder_text="e.g. PARAGOSO",placeholder_text_color="LightSkyBlue4",border_color="LightSkyBlue4",width=160,height=30)
        self.lName_entry.place(x=160,y=255)
    # student course
        conn = sqlite3.connect('studentdata.db')
        cursor = conn.cursor()
        course_insert_query = '''SELECT DISTINCT course_code as class FROM courses'''
        course = cursor.execute(course_insert_query)
        course_list = [r for r, in course] # create a list
        conn.commit()
        conn.close()
        self.course_var = tkinter.StringVar(value="Select")
        self.course_option = customtkinter.CTkOptionMenu(self.tabview.tab("Add Student"),fg_color="LightSkyBlue4",button_color="LightSkyBlue3",button_hover_color="LightSkyBlue3",text_color="white",dropdown_fg_color="azure2",dropdown_hover_color="LightSkyBlue3",width=300,values=course_list,variable=self.course_var)
        self.course_option.place(x=160,y=315)
    # student year level
        self.ylevel_var = tkinter.StringVar(value="Select")
        self.ylevel_option = customtkinter.CTkOptionMenu(self.tabview.tab("Add Student"),fg_color="LightSkyBlue4",button_color="LightSkyBlue3",button_hover_color="LightSkyBlue3",text_color="white",dropdown_fg_color="azure2",dropdown_hover_color="LightSkyBlue3",width=170,values=["1ST YEAR","2ND YEAR","3RD YEAR","4TH YEAR"],variable=self.ylevel_var)
        self.ylevel_option.place(x=460,y=110)
     # student gender
        self.gender_var = tkinter.StringVar()
        self.female_rbtn = customtkinter.CTkRadioButton(self.tabview.tab("Add Student"),text="FEMALE",border_color="LightSkyBlue4",variable=self.gender_var,value="FEMALE")
        self.female_rbtn.place(x=460,y=170)
        self.male_rbtn = customtkinter.CTkRadioButton(self.tabview.tab("Add Student"),text="MALE",border_color="LightSkyBlue4",variable=self.gender_var,value="MALE")
        self.male_rbtn.place(x=565,y=170)
    # student contact number
        self.contactnum_entry = customtkinter.CTkEntry(self.tabview.tab("Add Student"),placeholder_text="e.g. 09351454490",placeholder_text_color="LightSkyBlue4",border_color="LightSkyBlue4",width=170,height=30)
        self.contactnum_entry.place(x=460,y=225)
    # add student information
        self.savebtn = customtkinter.CTkButton(self.tabview.tab("Add Student"),text="Add Student",text_color=("black","white"),fg_color="LightSkyBlue3",border_width=2,hover= True,hover_color= "LightSkyBlue4",corner_radius=10,border_color= "LightSkyBlue3",width=100,height=30,command=self.add_student)
        self.savebtn.place(x=528,y=315)

#======================================== LIST TABVIEW ========================================#
        self.studenttab_btn = customtkinter.CTkButton(self.tabview.tab("List"),text="LIST OF STUDENTS",fg_color="LightSkyBlue3",hover_color="LightSkyBlue4",text_color="black",font=("Arial",13,"bold"),corner_radius=10,width=195,height=45,command=self.display_studentlist)
        self.studenttab_btn.place(x=260,y=125)
        self.coursetab_btn = customtkinter.CTkButton(self.tabview.tab("List"),text="LIST OF COURSES",fg_color="LightSkyBlue3",hover_color="LightSkyBlue4",text_color="black",font=("Arial",13,"bold"),corner_radius=10,width=195,height=45,command=self.display_courselist)
        self.coursetab_btn.place(x=260,y=200)

#======================================== TABLE STYLE ========================================#
    def table_style(self):
        style=ttk.Style()
        style.theme_use("vista")
        style.configure("Treeview",bg="lightgray",fg="white",rowheight=35,fieldbackground="lightgray")
        style.configure("Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 12)) # Modify the font of the body
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
        style.map("Treeview",background=[("selected","LightSkyBlue4")])

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
        conn = sqlite3.connect('studentdata.db')
        cursor = conn.cursor()
    # get the student info from the input fields
        student_id = self.studentID_entry.get()
        last_name = self.lName_entry.get().upper()
        first_name = self.fName_entry.get().upper()
        middle_name = self.mName_entry.get().upper()
        selected_gender = str(self.gender_var.get())
        selected_ylevel = str(self.ylevel_var.get())
        selected_course = str(self.course_var.get())
        contactnum = self.contactnum_entry.get()
    # input in database
        if student_id=='' or last_name=='' or first_name=='' or middle_name=='' or selected_gender=='' or selected_ylevel=='' or selected_course=='' or contactnum=='': tkMessageBox.showwarning("Warning","Please fill the empty field!")
        else:
            if self.student_exists(cursor, student_id):
                tkMessageBox.showerror("Error", "There is already a student with the same student ID in the system!")
            else:
                data_insert_query = '''INSERT INTO student_data (student_id,last_name,first_name,middle_name,gender,year_level,course,contact_number) VALUES (?,?,?,?,?,?,?,?)'''
                data_insert_tuple = (student_id,last_name,first_name,middle_name,selected_gender,selected_ylevel,selected_course,contactnum)
                cursor.execute(data_insert_query,data_insert_tuple)
                conn.commit()
                tkMessageBox.showinfo("Message","Student information added successfully")
        conn.close()
        self.clear_student_inputs()

    # Check if a student with the same ID already exists in the database
    def student_exists(self, cursor, student_id):
        conn = sqlite3.connect('studentdata.db')
        cursor = conn.cursor()
        query = '''SELECT * FROM student_data WHERE student_id = ?'''
        cursor.execute(query, (student_id,))
        conn.commit()
        if cursor.fetchone():
            return True
        conn.close()
        return False
        
#======================================== DISPLAY LIST OF STUDENTS ========================================#
    def display_studentlist(self):
    # list of students frame
        self.studentlist_frame = customtkinter.CTkFrame(self.tabview.tab("List"),width=680,height=390,fg_color="transparent")
        self.studentlist_frame.grid(row=1,column=0)
        self.studentlist_label = tk.Label(self.studentlist_frame,text="STUDENTS LIST",font=("Arial",12,"bold"),fg="black",bg="azure2")
        self.studentlist_label.place(x=38,y=15)
    # a button to access the list of courses
        self.courselist_btn = customtkinter.CTkButton(self.studentlist_frame,text="List of Courses",fg_color="LightSkyBlue3",hover_color="LightSkyBlue4",text_color="black",corner_radius=10,width=65,height=30,command=self.display_courselist)
        self.courselist_btn.place(x=25,y=350)
    # student list table
        self.table_style()
        self.table_frame = tk.Frame(self.studentlist_frame,bg="white",relief=GROOVE)
        self.table_frame.place(x=30,y=50,width=795,height=370)
        self.y_scroll = customtkinter.CTkScrollbar(self.table_frame,orientation=VERTICAL)
        self.x_scroll = customtkinter.CTkScrollbar(self.table_frame,orientation=HORIZONTAL)
        self.student_table = ttk.Treeview(self.table_frame,columns=("Student ID","Name","Gender","Year Level","Course","Contact No.","Registration Date"),xscrollcommand=self.x_scroll.set,yscrollcommand=self.y_scroll.set)
        self.y_scroll.configure(command=self.student_table.yview)
        self.x_scroll.configure(command=self.student_table.xview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.x_scroll.pack(side=BOTTOM,fill=X)
    # columns
        self.student_table['columns'] = ("Student ID","Last Name","First Name","Middle Name","Gender","Year Level","Course","Contact No.","Registration Date")
        self.student_table.column("#0",width=0,stretch=NO)
        self.student_table.column("Student ID",anchor=CENTER,width=100)
        self.student_table.column("Last Name",anchor=CENTER,width=200)
        self.student_table.column("First Name",anchor=CENTER,width=200)
        self.student_table.column("Middle Name",anchor=CENTER,width=200)
        self.student_table.column("Gender",anchor=CENTER,width=70)
        self.student_table.column("Year Level",anchor=CENTER,width=100)
        self.student_table.column("Course",anchor=CENTER,width=200)
        self.student_table.column("Contact No.",anchor=CENTER,width=110)
        self.student_table.column("Registration Date",anchor=CENTER,width=150)
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
        self.student_table.heading("Registration Date",text="Registration Date",anchor=CENTER)
        self.student_table.pack(fill=BOTH,expand=True)
    # to fetch data from database and display in the table
        conn = sqlite3.connect('studentdata.db')
        cursor = conn.cursor()
        display_data_query = cursor.execute("SELECT * FROM student_data ORDER BY last_name  ")
        fetch = display_data_query.fetchall()
        for data in fetch:
            self.student_table.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]))
        conn.commit()
        conn.close()
    # search student
        self.searchstudent_var = StringVar()
        self.search_label = customtkinter.CTkLabel(self.studentlist_frame,text="Search:")
        self.search_label.place(x=460,y=5)
        self.search_entry1 = customtkinter.CTkEntry(self.studentlist_frame,textvariable=self.searchstudent_var,placeholder_text="e.g. 2021-1574",placeholder_text_color="LightSkyBlue4",border_color="LightSkyBlue4", width=145)
        self.search_entry1.place(x=510,y=5)
        self.search_entry1.bind("<Key>",self.display_searchstudent)
    # delete student
        self.deletestudent_btn = customtkinter.CTkButton(self.studentlist_frame,text="Delete Student",text_color="white",fg_color="red2",border_width=2,hover= True,hover_color= "red",corner_radius=10,border_color= "red2",width=5,height=30,command=self.delete_student_data)
        self.deletestudent_btn.place(x=555,y=350)
    # edit student 
        self.editstudent_btn = customtkinter.CTkButton(self.studentlist_frame,text="Edit Student",text_color=("black","white"),fg_color="yellow2",border_width=2,hover= True,hover_color= "yellow",corner_radius=10,border_color= "yellow2",width=5,height=30,command=self.edit_student_data)
        self.editstudent_btn.place(x=450,y=350)
    # update student list
        self.updatestudent_btn = customtkinter.CTkButton(self.studentlist_frame,text="Update List",text_color=("black","white"),fg_color="cadetblue2",border_width=2,hover= True,hover_color= "cadetblue1",corner_radius=10,border_color= "cadetblue2",width=5,height=30,command=self.update_student_table)
        self.updatestudent_btn.place(x=350,y=350)

#======================================== UPDATE STUDENT LIST ON THE TABLE ========================================#
    def update_student_table(self):
        conn = sqlite3.connect('studentdata.db')
        cursor = conn.cursor() 
    # clearing current display data
        self.student_table.delete(*self.student_table.get_children())
        display_data_query = cursor.execute("SELECT * FROM student_data ORDER BY last_name ASC")
        fetch = display_data_query.fetchall()
        for data in fetch:
            self.student_table.insert('', 'end', values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8]))
        conn.commit()
        conn.close()
    
#======================================== SEARCH STUDENT ========================================#
    def display_searchstudent(self,ev):
        conn = sqlite3.connect('studentdata.db')
        cursor = conn.cursor() 
        if self.searchstudent_var.get() != "":      
    # clearing current display data
            self.student_table.delete(*self.student_table.get_children())
            display_search_query = cursor.execute("SELECT * FROM student_data WHERE student_id LIKE ? or last_name LIKE ? or first_name LIKE ? or gender LIKE ? or course LIKE ?", ('%' + str(self.searchstudent_var.get()) + '%','%' + str(self.searchstudent_var.get()) + '%','%' + str(self.searchstudent_var.get()) + '%','%' + str(self.searchstudent_var.get()) + '%','%' + str(self.searchstudent_var.get()) + '%',))
    # fetch all matching records
            fetch = display_search_query.fetchall()
    # loop for displaying all records 
            for data in fetch:
                self.student_table.insert('', 'end', values=(data))
                conn.commit()
            conn.close()

#======================================== DELETE STUDENT ========================================#
    def delete_student_data(self):
        if not self.student_table.selection():
            tkMessageBox.showerror("Error", "No item selected. Please select a student from the table.")
            return
        
        decision = tkMessageBox.askquestion("Warning","Are you sure you want to delete the selected student?")
        if decision != 'yes':
            return
        else:
            try:
                selected_item = self.student_table.selection()[0]
                delete_data = str(self.student_table.item(selected_item)['values'][0])
                conn = sqlite3.connect('studentdata.db')
                cursor = conn.cursor() 
                cursor.execute("DELETE FROM student_data WHERE student_id = '" + str(delete_data)+"'")
                conn.commit()
                tkMessageBox.showinfo("Message", "The student is deleted successfully!")
                conn.close()
            except:
                tkMessageBox.showerror("Error","An error has occured")
                return
        self.update_student_table()

#======================================== UPDATE STUDENT RECORD ========================================#
    def update_student_data(self):
        decision = tkMessageBox.askquestion("Warning", "Are you sure you want to make changes in the student information?")
        if decision != 'yes':
            tkMessageBox.showinfo("Message", "The changes have not been saved")
            return
        conn = sqlite3.connect('studentdata.db')
        cursor = conn.cursor()
        selected_id = self.student_table.focus()
        id_details = str(self.student_table.item(selected_id)['values'][0])
        student_id = str(id_details)
        cursor.execute('''UPDATE student_data SET last_name = :last_name,first_name = :first_name,middle_name = :middle,
            gender = :gender,year_level = :year_level,course = :course,contact_number = :contact WHERE student_id = :student_id''',
                {'last_name': self.lName_entry.get().upper(),'first_name': self.fName_entry.get().upper(),'middle': self.mName_entry.get().upper(),
                    'gender': self.gender_var.get(),'year_level': self.ylevel_var.get(),'course': self.course_var.get(),'contact': self.contactnum_entry.get(),'student_id': student_id})
        conn.commit()
        conn.close()
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

        conn = sqlite3.connect('studentdata.db')
        cursor = conn.cursor()
        selected_id = self.student_table.focus()
        id_details = str(self.student_table.item(selected_id)['values'][0])
        cursor.execute("SELECT * FROM student_data WHERE student_id = '" + str(id_details)+"'")
        data = cursor.fetchall()
    # global variables for the entries
        global fName_entry; global mName_entry; global lName_entry; global gender_var; global ylevel_var; global course_var; global contactnum_entry
    # edit student form
        self.studentinfo_label = customtkinter.CTkLabel(self.edit_window,text="Student Information:",font=("Arial",14,"bold"))
        self.studentinfo_label.place(x=50,y=50)
        self.fName_label = customtkinter.CTkLabel(self.edit_window,text="First Name:",font=("Arial",14))
        self.fName_label.place(x=50,y=110)
        self.mName_label = customtkinter.CTkLabel(self.edit_window,text="Middle Name:",font=("Arial",14))
        self.mName_label.place(x=50,y=170)
        self.lName_label = customtkinter.CTkLabel(self.edit_window,text="Last Name:",font=("Arial",14))
        self.lName_label.place(x=50,y=230)
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
        self.fName_entry = customtkinter.CTkEntry(self.edit_window,placeholder_text="e.g. EDA GRACE",placeholder_text_color="LightSkyBlue4",border_color="LightSkyBlue4",width=160,height=30)
        self.fName_entry.place(x=160,y=110)
        self.mName_entry = customtkinter.CTkEntry(self.edit_window,placeholder_text="e.g. JUTBA",placeholder_text_color="LightSkyBlue4",border_color="LightSkyBlue4",width=160,height=30)
        self.mName_entry.place(x=160,y=170)
        self.lName_entry = customtkinter.CTkEntry(self.edit_window,placeholder_text="e.g. PARAGOSO",placeholder_text_color="LightSkyBlue4",border_color="LightSkyBlue4",width=160,height=30)
        self.lName_entry.place(x=160,y=230)
    # student course
        cursor.execute("SELECT DISTINCT course_code FROM courses")
        course_list = [r[0] for r in cursor.fetchall()]
        conn.close()
        self.course_option = customtkinter.CTkComboBox(self.edit_window, fg_color="LightSkyBlue4", button_color="LightSkyBlue3", button_hover_color="LightSkyBlue3", text_color="white", dropdown_fg_color="azure2", dropdown_hover_color="LightSkyBlue3", width=350, values=course_list, variable=self.course_var)
        self.course_option.place(x=120, y=290)
    # student gender
        self.gender_var = tkinter.StringVar()
        self.female_rbtn = customtkinter.CTkRadioButton(self.edit_window,text="FEMALE",border_color="LightSkyBlue4",variable=self.gender_var,value="FEMALE")
        self.female_rbtn.place(x=480,y=115)
        self.male_rbtn = customtkinter.CTkRadioButton(self.edit_window,text="MALE",border_color="LightSkyBlue4",variable=self.gender_var,value="MALE")
        self.male_rbtn.place(x=590,y=115)
    # student year level
        self.ylevel_var = tkinter.StringVar()
        self.ylevel_option = customtkinter.CTkOptionMenu(self.edit_window,fg_color="LightSkyBlue4",button_color="LightSkyBlue3",button_hover_color="LightSkyBlue3",text_color="white",dropdown_fg_color="azure2",dropdown_hover_color="LightSkyBlue3",width=175,values=["1ST YEAR","2ND YEAR","3RD YEAR","4TH YEAR"],variable=self.ylevel_var)
        self.ylevel_option.place(x=480,y=170)
    # student contact number
        self.contactnum_entry = customtkinter.CTkEntry(self.edit_window,placeholder_text="e.g. 09351454490",placeholder_text_color="LightSkyBlue4",border_color="LightSkyBlue4",width=175,height=30)
        self.contactnum_entry.place(x=480,y=230)
    # a button to save student information
        self.savebtn = customtkinter.CTkButton(self.edit_window,text="Save Changes",text_color=("black","white"),fg_color="LightSkyBlue3",border_width=2,hover= True,hover_color= "LightSkyBlue4",corner_radius=10,border_color= "LightSkyBlue3",width=100,height=30,command=self.update_student_data)
        self.savebtn.place(x=552,y=290) 
    # loop through results 
        for selected_data in data:
            self.lName_entry.insert(0,selected_data[1])
            self.fName_entry.insert(0,selected_data[2])
            self.mName_entry.insert(0,selected_data[3])
            self.gender_var.set(selected_data[4])
            self.ylevel_var.set(selected_data[5])
            self.course_var.set(selected_data[6])
            self.contactnum_entry.insert(0,selected_data[7])

#======================================== LIST OF COURSES ========================================#
    def display_courselist(self):
    # list of courses frame
        self.courselist_frame = customtkinter.CTkFrame(self.tabview.tab("List"),width=680,height=390,fg_color="transparent")
        self.courselist_frame.grid(row=1,column=0)
        self.courselist_label = tk.Label(self.courselist_frame,text="COURSES LIST",font=("Arial",12,"bold"),fg="black",bg="azure2")
        self.courselist_label.place(x=38,y=15)
    # a button to access the list of students
        self.studentlist_btn = customtkinter.CTkButton(self.courselist_frame,text="List of Students",fg_color="LightSkyBlue3",hover_color="LightSkyBlue4",text_color="black",corner_radius=10,width=65,height=30,command=self.display_studentlist)
        self.studentlist_btn.place(x=25,y=350)
    # course list table
        self.table_style()
        self.table_frame = tk.Frame(self.courselist_frame,bg="white",relief=GROOVE)
        self.table_frame.place(x=30,y=50,width=795,height=370)
        self.y_scroll = customtkinter.CTkScrollbar(self.table_frame,orientation=VERTICAL)
        self.course_table = ttk.Treeview(self.table_frame,columns=("Course Code","Course"),yscrollcommand=self.y_scroll.set)
        self.y_scroll.configure(command=self.course_table.yview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
    # columns
        self.course_table['columns'] = ("Course Code","Course")
        self.course_table.column("#0",width=0,stretch=NO)
        self.course_table.column("Course Code",anchor=CENTER,width=10)
        self.course_table.column("Course",anchor=CENTER,width=280)
    # headings
        self.course_table.heading("#0",text="",anchor=W)
        self.course_table.heading("Course Code",text="Course Code",anchor=CENTER)
        self.course_table.heading("Course",text="Course",anchor=CENTER)
        self.course_table.pack(fill=BOTH,expand=True)
    # to fetch data from database and display in the table
        conn = sqlite3.connect('studentdata.db')
        cursor = conn.cursor()
        display_data_query = cursor.execute("SELECT * FROM courses ORDER BY course_code ASC")
        fetch = display_data_query.fetchall()
        for data in fetch:
            self.course_table.insert('', 'end', values=(data[0], data[1]))
        conn.commit()
        conn.close() 
    # search course
        self.searchcourse_var = StringVar()
        self.search_label = customtkinter.CTkLabel(self.courselist_frame,text="Search:")
        self.search_label.place(x=460,y=5)
        self.search_entry2 = customtkinter.CTkEntry(self.courselist_frame,textvariable=self.searchcourse_var,placeholder_text="e.g. BSCS",placeholder_text_color="LightSkyBlue4",border_color="LightSkyBlue4", width=145)
        self.search_entry2.place(x=510,y=5)
        self.search_entry2.bind("<Key>",self.display_searchcourse)
    # delete course
        self.deletecourse_btn = customtkinter.CTkButton(self.courselist_frame,text="Delete Course",text_color="white",fg_color="red2",border_width=2,hover= True,hover_color= "red",corner_radius=10,border_color= "red2",width=5,height=30,command=self.delete_course)
        self.deletecourse_btn.place(x=555,y=350)
    # edit course
        self.editcourse_btn = customtkinter.CTkButton(self.courselist_frame,text="Edit Course",text_color=("black","white"),fg_color="yellow2",border_width=2,hover= True,hover_color= "yellow",corner_radius=10,border_color= "yellow2",width=5,height=30,command=self.edit_course_data)
        self.editcourse_btn.place(x=450,y=350)
    # update course list
        self.updatecourse_btn = customtkinter.CTkButton(self.courselist_frame,text="Update List",text_color=("black","white"),fg_color="cadetblue2",border_width=2,hover= True,hover_color= "cadetblue1",corner_radius=10,border_color= "cadetblue2",width=5,height=30,command=self.update_course_table)
        self.updatecourse_btn.place(x=350,y=350)

#======================================== ADD COURSE ========================================#
    def clear_course_inputs(self):
        self.coursecode_entry.delete(0, END)
        self.course_entry.delete(0, END)

    def add_course(self):
        conn = sqlite3.connect('studentdata.db')
        cursor = conn.cursor()
    # get the course info from the input fields
        course_code = self.coursecode_entry.get().upper()
        course = self.course_entry.get().upper()
    # input in database
        if course_code=='' or course=='': tkMessageBox.showwarning("Warning","Fill the empty field!")
        else:
            if self.course_exists(cursor, course_code,course):
                tkMessageBox.showerror("Error", "The course cannot be added. It already exists!")
            else:
                data_insert_query = '''INSERT INTO courses (course_code,course) VALUES (?,?)'''
                data_insert_tuple = (course_code,course)
                tkMessageBox.showinfo("Message","Course added successfully")
                cursor.execute(data_insert_query,data_insert_tuple)
                conn.commit()
        conn.close()
        self.clear_course_inputs()
    
    # Check if a course with the same code already exists in the database
    def course_exists(self, cursor, course_code,course):
        conn = sqlite3.connect('studentdata.db')
        cursor = conn.cursor()
        query = '''SELECT * FROM courses WHERE course_code = ? or course = ?'''
        cursor.execute(query, (course_code,course))
        conn.commit()
        if cursor.fetchone():
            return True
        conn.close()
        return False

#======================================== UPDATE COURSE LIST ON THE TABLE ========================================#
    def update_course_table(self):
        conn = sqlite3.connect('studentdata.db')
        cursor = conn.cursor() 
    # clearing current display data
        self.course_table.delete(*self.course_table.get_children())
        display_data_query = cursor.execute("SELECT * FROM courses")
        fetch = display_data_query.fetchall()
        for data in fetch:
            self.course_table.insert('', 'end', values=(data[0],data[1]))
            conn.commit()
        conn.close()
    
#======================================== SEARCH COURSE ========================================#
    def display_searchcourse(self,ev):
        conn = sqlite3.connect('studentdata.db')
        cursor = conn.cursor() 
        if self.searchcourse_var.get() != "":
    # clearing current display data
            self.course_table.delete(*self.course_table.get_children())
            display_search_query = cursor.execute("SELECT * FROM courses WHERE course_code LIKE ? or course LIKE ?", ('%' + str(self.searchcourse_var.get()) + '%','%' + str(self.searchcourse_var.get()) + '%',))
    # fetch all matching records
            fetch = display_search_query.fetchall()
    # loop for displaying all records 
            for data in fetch:
                self.course_table.insert('', 'end', values=(data))
                conn.commit()
            conn.close()

#======================================== DELETE COURSE ========================================#
    def delete_course(self):
        if not self.course_table.selection():
            tkMessageBox.showerror("Error", "No item selected. Please select a course from the table.")
            return
        
        decision = tkMessageBox.askquestion("Warning", "Are you sure you want to delete the selected data?")
        if decision != 'yes':
            return
        else:
            selected_item = self.course_table.selection()[0]
            delete_data = str(self.course_table.item(selected_item)['values'][0])
            try:
                conn = sqlite3.connect('studentdata.db')
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) FROM student_data WHERE course = ?", (delete_data,))
                count = cursor.fetchone()[0]
                if count > 0:
                    tkMessageBox.showwarning("Warning", "There are students enrolled in this course. Course cannot be deleted.")
                    return
                cursor.execute("DELETE FROM courses WHERE course_code = ?", (delete_data,))
                conn.commit()
                conn.close()
                tkMessageBox.showinfo("Message", "The course has been deleted successfully!")
            except:
                tkMessageBox.showerror("Error", "An error has occurred")
                return
        self.update_course_table()

#======================================== UPDATE COURSE RECORD ========================================#
    def update_course_data(self):
        decision = tkMessageBox.askquestion("Warning", "Are you sure you want to make changes in the course information?")
        if decision != 'yes':
            tkMessageBox.showinfo("Message", "The changes have not been saved")
            return
        conn = sqlite3.connect('studentdata.db')
        cursor = conn.cursor()

        selected_code = self.course_table.focus()
        code_details = str(self.course_table.item(selected_code)['values'][0])
        course_data = str(code_details)
        new_course = self.course_entry.get().upper()
        if self.coursename_exists(cursor,new_course):
                tkMessageBox.showerror("Error", "The course cannot be added. It already exists!")
        else:
    # Update course in the courses table
            cursor.execute('''UPDATE courses SET course = :new_course WHERE course_code = :course_code''',{'new_course': new_course, 'course_code': course_data})
            tkMessageBox.showinfo("Message", "The changes have been saved successfully!")
            conn.commit()
        conn.close()    
        self.update_course_table()
        self.edit_window.destroy()
    
    def coursename_exists(self, cursor,course):
        conn = sqlite3.connect('studentdata.db')
        cursor = conn.cursor()
        query = '''SELECT * FROM courses WHERE course = ?'''
        cursor.execute(query, (course,))
        conn.commit()
        if cursor.fetchone():
            return True
        conn.close()
        return False

#======================================== EDIT COURSE RECORD ========================================#
    def edit_course_data(self):
        if not self.course_table.selection():
            tkMessageBox.showerror("Error", "No item selected. Please select a student from the table.")
            return
        
        self.edit_window = Toplevel(self)
        self.edit_window.title("Edit Course Information")
        self.edit_window.geometry("700x240+0+0")

        conn = sqlite3.connect('studentdata.db')
        cursor = conn.cursor()

        selected_code = self.course_table.focus()
        code_details = str(self.course_table.item(selected_code)['values'][0])
        cursor.execute("SELECT * FROM courses WHERE course_code = '" + str(code_details)+"'")
        data = cursor.fetchall()
    # global variables for the entries
        global course_entry
    # add course form
        self.course_label = customtkinter.CTkLabel(self.edit_window,text="Course:",font=("Arial",12))
        self.course_label.place(x=25,y=50)
        self.course_entry = customtkinter.CTkEntry(self.edit_window,placeholder_text="e.g. BACHELOR OF SCIENCE IN COMPUTER SCIENCE",placeholder_text_color="LightSkyBlue4",border_color="LightSkyBlue4",width=450,height=30)
        self.course_entry.place(x=80,y=50)
    # save added course
        self.savecourse_btn = customtkinter.CTkButton(self.edit_window,text="Save Changes",text_color=("black","white"),fg_color="LightSkyBlue3",border_width=2,hover= True,hover_color= "LightSkyBlue4",corner_radius=10,border_color= "LightSkyBlue3",width=100,height=30,command=self.update_course_data)
        self.savecourse_btn.place(x=426,y=100)    
    # loop through results 
        for selected_data in data:
            self.course_entry.insert(0,selected_data[1])

if __name__ == "__main__":
    app = App()
    app.mainloop()
