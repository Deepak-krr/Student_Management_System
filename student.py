from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow 
import mysql.connector
from tkinter import messagebox




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        
        # Variables
        self.var_dep=StringVar() 
        self.var_course=StringVar() 
        self.var_year=StringVar() 
        self.var_sem=StringVar() 
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phn=StringVar()
        self.var_addr=StringVar()
        self.var_t_name=StringVar()


        
        # 1st Top img
        img_1= Image.open(r"college_images\7th.jpg")
        img_1= img_1.resize((450,160),Image.LANCZOS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)
        
        self.btn_1=Button(self.root,image=self.photoimg_1,cursor="hand2")
        self.btn_1.place(x=0,y=0,width=452,height=160)


        # 2nd Top Img
        img_2= Image.open(r"college_images\6th.jpg")
        img_2= img_2.resize((452,160),Image.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        
        self.btn_2=Button(self.root,image=self.photoimg_2,cursor="hand2")
        self.btn_2.place(x=452,y=0,width=452,height=160)
        

        # 3rd Top Img
        img_3= Image.open(r"college_images\5th.jpg")
        img_3= img_3.resize((452,160),Image.LANCZOS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)
         
        self.btn_3=Button(self.root,image=self.photoimg_3,cursor="hand2")
        self.btn_3.place(x=904,y=0,width=452,height=160)
        

        # Background img
        img_4= Image.open(r"college_images\university.jpg")
        img_4= img_4.resize((1356,605),Image.LANCZOS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        bg_lbl=Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=160,width=1356,height=605)
               

        # Bg_lbl Title
        lbl_title=Label(bg_lbl,text="Student Management System",font=("times new roman",28,"bold"),fg="blue",bg="white")
        lbl_title.place(x=0,y=0,width=1356,height=45)


        # Manage Frame
        manage_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
        manage_frame.place(x=5,y=48,width=1340,height=470)


        # --------left DataFrame--------
        DataLeftFrame=LabelFrame(manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        DataLeftFrame.place(x=10,y=3,width=511,height=460)

        
        # left DataFrame img
        img_5= Image.open(r"college_images\3rd.jpg")
        img_5= img_5.resize((496,100),Image.LANCZOS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        my_img_left=Label(DataLeftFrame,image=self.photoimg_5,bd=2,relief=RIDGE)
        my_img_left.place(x=3,y=3,width=496,height=100)


        # Current course LabelFrame Information
        std_lbl_info_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Current Course Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        std_lbl_info_frame.place(x=2,y=100,width=496,height=100)


        # Labels & Combobox       
        
        # Department
        label_dept=Label(std_lbl_info_frame,text="Department",font=("aerial",10,"bold"),bg="white")
        label_dept.grid(row=0,column=0,padx=2,sticky=W)
       
        Combo_dept=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_dep,font=("aerial",10,"bold"),width=17,state="readonly")
        Combo_dept["value"]=("Select Department","Computer","IT","Civil","Mechanical","Electronics & Telecom","Others")
        Combo_dept.current(0)
        Combo_dept.grid(row=0,column=1,padx=2,pady=5,sticky=W) 

        # Course
        label_course=Label(std_lbl_info_frame,text="Courses:",font=("aerial",10,"bold"),bg="white")
        label_course.grid(row=0,column=2,padx=2,pady=5,sticky=W)
        
        Combo_course=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_course,font=("aerial",10,"bold"),width=17,state="readonly")
        Combo_course["value"]=("Select Course","FE","SE","TE","BE")
        Combo_course.current(0)
        Combo_course.grid(row=0,column=3,padx=2,pady=5,sticky=W)


        # Year
        label_year=Label(std_lbl_info_frame,text="Years:",font=("aerial",10,"bold"),bg="white")
        label_year.grid(row=1,column=0,padx=2,pady=8,sticky=W)

        Combo_year=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_year,font=("aerial",10,"bold"),width=17,state="readonly")
        Combo_year["value"]=("Select Year","2019-2020","2020-2021","2021-2022","2022-2023")
        Combo_year.current(0)
        Combo_year.grid(row=1,column=1,padx=2,sticky=W)


        # Semester
        label_semester=Label(std_lbl_info_frame,text="Semesters:",font=("aerial",10,"bold"),bg="white")
        label_semester.grid(row=1,column=2,padx=2,pady=5,sticky=W)

        Combo_semester=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_sem,font=("aerial",10,"bold"),width=17,state="readonly")
        Combo_semester["value"]=("Select Semester","First","Second")
        Combo_semester.current(0)
        Combo_semester.grid(row=1,column=3,padx=2,pady=5,sticky=W)


        # Student class LabelFrame Information
        std_lbl_class_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Student Class Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        std_lbl_class_frame.place(x=2,y=198,width=496,height=196)


        # Labels 
        
        # StudentId
        label_Std_id=Label(std_lbl_class_frame,text="StudentID:",font=("aerial",10,"bold"),bg="white")
        label_Std_id.grid(row=0,column=0,padx=2,sticky=W)

        # EntryLabel for Std ID
        std_id_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_std_id,font=("aerial",10,"bold"),width=16)
        std_id_entry.grid(row=0,column=1,padx=2,pady=5,sticky=W)
        
        
        # Student Name
        label_std_name=Label(std_lbl_class_frame,text="Student Name:",font=("aerial",10,"bold"),bg="white")
        label_std_name.grid(row=0,column=2,padx=2,pady=5,sticky=W)

        # EntryLevel for Std Name
        std_name_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_std_name,font=("aerial",10,"bold"),width=16)
        std_name_entry.grid(row=0,column=3,padx=2,pady=5,sticky=W)
        

        # Class Division
        label_cls_div=Label(std_lbl_class_frame,text="Class Division:",font=("aerial",10,"bold"),bg="white")
        label_cls_div.grid(row=1,column=0,padx=2,pady=5,sticky=W)

        # Entrylevel for Class div
        Combo_cls_div=ttk.Combobox(std_lbl_class_frame,textvariable=self.var_div,font=("aerial",10,"bold"),width=14,state="readonly")
        Combo_cls_div["value"]=("Select Division","A","B","C","D")
        Combo_cls_div.current(0)
        Combo_cls_div.grid(row=1,column=1,padx=2,pady=5,sticky=W)
        

        # Roll No
        label_roll_no=Label(std_lbl_class_frame,text="Roll No:",font=("aerial",10,"bold"),bg="white")
        label_roll_no.grid(row=1,column=2,padx=2,pady=5,sticky=W)

        # Entrylevel for Roll no
        std_roll_no_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_roll,font=("aerial",10,"bold"),width=16)
        std_roll_no_entry.grid(row=1,column=3,padx=2,pady=5,sticky=W)


         # Gender
        label_gender=Label(std_lbl_class_frame,text="Gender:",font=("aerial",10,"bold"),bg="white")
        label_gender.grid(row=2,column=0,padx=2,pady=5,sticky=W)

        # Combobox level for Gender
        Combo_gender=ttk.Combobox(std_lbl_class_frame,textvariable=self.var_gender,font=("aerial",10,"bold"),width=14,state="readonly")
        Combo_gender["value"]=("Select Gender","Male","Female","Other")
        Combo_gender.current(0)
        Combo_gender.grid(row=2,column=1,padx=2,pady=5,sticky=W)


        # DOB
        label_dob=Label(std_lbl_class_frame,text="DOB:",font=("aerial",10,"bold"),bg="white")
        label_dob.grid(row=2,column=2,padx=2,pady=5,sticky=W)

        # Entrylevel for DOB
        std_dob_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_dob,font=("aerial",10,"bold"),width=16)
        std_dob_entry.grid(row=2,column=3,padx=2,pady=5,sticky=W)

        
        # Email
        label_mail_id=Label(std_lbl_class_frame,text="Email:",font=("aerial",10,"bold"),bg="white")
        label_mail_id.grid(row=3,column=0,padx=2,pady=5,sticky=W)

        # Entrylevel for Email
        std_mail_id_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_email,font=("aerial",10,"bold"),width=16)
        std_mail_id_entry.grid(row=3,column=1,padx=2,pady=5,sticky=W)


        # Phone No
        label_phn_no=Label(std_lbl_class_frame,text="Phone No:",font=("aerial",10,"bold"),bg="white")
        label_phn_no.grid(row=3,column=2,padx=2,pady=5,sticky=W)

        # Entrylevel for Phone No
        std_phn_no_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_phn,font=("aerial",10,"bold"),width=16)
        std_phn_no_entry.grid(row=3,column=3,padx=2,pady=5,sticky=W)


        # Address
        label_addr=Label(std_lbl_class_frame,text="Address:",font=("aerial",10,"bold"),bg="white")
        label_addr.grid(row=4,column=0,padx=2,pady=5,sticky=W)

        
        # Entrylevel for Address
        std_addr_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_addr,font=("aerial",10,"bold"),width=16)
        std_addr_entry.grid(row=4,column=1,padx=2,pady=5,sticky=W)


        # Teacher Name
        label_fac_name=Label(std_lbl_class_frame,text="Teacher Name:",font=("aerial",10,"bold"),bg="white")
        label_fac_name.grid(row=4,column=2,padx=2,pady=5,sticky=W)

        # Entrylevel for Teacher Name
        std_fac_name_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_t_name,font=("aerial",10,"bold"),width=16)
        std_fac_name_entry.grid(row=4,column=3,padx=2,pady=5,sticky=W)

        # Button Frame
        btn_frame=Frame(DataLeftFrame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=396,width=496,height=26)
        
        btn_frm_sv=Button(btn_frame,text="Save",command=self.add_data,font=("aerial",9,"bold"),width=16,fg="white",bg="blue")
        btn_frm_sv.grid(row=0,column=0,padx=2) 

        btn_frm_upd=Button(btn_frame,text="Update",command=self.update_data,font=("aerial",9,"bold"),width=16,fg="white",bg="blue")
        btn_frm_upd.grid(row=0,column=1,padx=2)
        
        btn_frm_del=Button(btn_frame,text="Delete",command=self.delete_data,font=("aerial",9,"bold"),width=16,fg="white",bg="blue")
        btn_frm_del.grid(row=0,column=2,padx=2) 

        btn_frm_res=Button(btn_frame,text="Reset",command=self.reset_data,font=("aerial",9,"bold"),width=16,fg="white",bg="blue")
        btn_frm_res.grid(row=0,column=3,padx=2)


        # --------Right DataFrame----------
        DataRightFrame=LabelFrame(manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        DataRightFrame.place(x=528,y=3,width=795,height=460)

        # Img_1 RightFrame
        img_6= Image.open(r"college_images\clg.jpg")
        img_6= img_6.resize((780,160),Image.LANCZOS)
        self.photoimg_6=ImageTk.PhotoImage(img_6)

        my_img_right=Label(DataRightFrame,image=self.photoimg_6,bd=2,relief=RIDGE)
        my_img_right.place(x=0,y=0,width=780,height=160)


        # Right SearchFrame
        search_frame=LabelFrame(DataRightFrame,bd=4,relief=RIDGE,padx=2,text="Search Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        search_frame.place(x=0,y=162,width=780,height=55)

        search_by=Label(search_frame,text="Search By",font=("aerial",10,"bold"),fg="white",bg="black")
        search_by.grid(row=0,column=0,padx=5,sticky=W)
        
        # Search
        self.var_combo_search=StringVar()

        # Combobox
        Combo_search_by=ttk.Combobox(search_frame,textvariable=self.var_combo_search,font=("aerial",10,"bold"),width=22,state="readonly")
        Combo_search_by["value"]=("Select Option","Roll_No","Phone","Std_Id","Std_Name")
        Combo_search_by.current(0)
        Combo_search_by.grid(row=0,column=1,padx=2,pady=5,sticky=W)


        # EntryField
        self.var_search=StringVar()
        search_entry=ttk.Entry(search_frame,textvariable=self.var_search,font=("aerial",10,"bold"),width=21)
        search_entry.grid(row=0,column=2,padx=5,sticky=W)

        # button Right
        btn_search=Button(search_frame,command=self.search_data,text="Search",font=("aerial",9,"bold"),width=21,fg="white",bg="blue")
        btn_search.grid(row=0,column=3,padx=5) 

        btn_showAll=Button(search_frame,command=self.fetch_data,text="Show All",font=("aerial",9,"bold"),width=21,fg="white",bg="blue")
        btn_showAll.grid(row=0,column=4,padx=5)

        
        # STUDENT TABLE & Scroll Bar
        tbl_frame=Frame(DataRightFrame,bd=4,relief=RIDGE)
        tbl_frame.place(x=0,y=220,width=780,height=210)

        scroll_x=ttk.Scrollbar(tbl_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tbl_frame,orient=VERTICAL)
        self.std_tbl=ttk.Treeview(tbl_frame,columns=("Dept","Course","Years","Semester","Std_Id","Std_Name","Std_Div","Roll_No","Gender","DOB","Email","Phone","Address","Teacher"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)                      

        scroll_x.config(command=self.std_tbl.xview)
        scroll_y.config(command=self.std_tbl.yview)

        self.std_tbl.heading("Dept",text="Department")
        self.std_tbl.heading("Course",text="Course")
        self.std_tbl.heading("Years",text="Year")
        self.std_tbl.heading("Semester",text="Semester")
        self.std_tbl.heading("Std_Id",text="StudentId")
        self.std_tbl.heading("Std_Name",text="Student Name")
        self.std_tbl.heading("Std_Div",text="Class Div")
        self.std_tbl.heading("Roll_No",text="Roll No")
        self.std_tbl.heading("Gender",text="Gender")
        self.std_tbl.heading("DOB",text="DOB")
        self.std_tbl.heading("Email",text="Email")
        self.std_tbl.heading("Phone",text="Phone No")
        self.std_tbl.heading("Address",text="Address")
        self.std_tbl.heading("Teacher",text="Teacher Name")

        self.std_tbl["show"]="headings"

        self.std_tbl.column("Dept",width=150)
        self.std_tbl.column("Course",width=150)
        self.std_tbl.column("Years",width=150)
        self.std_tbl.column("Semester",width=150)
        self.std_tbl.column("Std_Id",width=150)
        self.std_tbl.column("Std_Name",width=150)
        self.std_tbl.column("Std_Div",width=150)
        self.std_tbl.column("Roll_No",width=150)
        self.std_tbl.column("Gender",width=150)
        self.std_tbl.column("DOB",width=150)
        self.std_tbl.column("Email",width=150)
        self.std_tbl.column("Phone",width=150)
        self.std_tbl.column("Address",width=150)
        self.std_tbl.column("Teacher",width=150)

        self.std_tbl.pack(fill=BOTH,expand=1)
        self.std_tbl.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        

    def add_data(self):
        if (self.var_dep.get()=="" or self.var_email.get()=="" or self.var_std_id.get()=="" or self.var_course.get()=="" or self.var_year.get()=="" or self.var_sem.get()=="" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phn.get()=="" or self.var_addr.get()=="" or self.var_t_name.get()==""):
           messagebox.showerror("Error","All fields are Mandatory") 
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),
                                                                                                           self.var_course.get(),
                                                                                                           self.var_year.get(),
                                                                                                           self.var_sem.get(),
                                                                                                           self.var_std_id.get(),
                                                                                                           self.var_std_name.get(),
                                                                                                           self.var_div.get(),
                                                                                                           self.var_roll.get(),
                                                                                                           self.var_gender.get(),
                                                                                                           self.var_dob.get(),
                                                                                                           self.var_email.get(),
                                                                                                           self.var_phn.get(),
                                                                                                           self.var_addr.get(),
                                                                                                           self.var_t_name.get()))
                
                conn.commit()
                self.fetch_data
                conn.close()
                messagebox.showinfo("successful","Student has been added",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due to {str(e)}",parent=self.root)

    #Fetch Function
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
        my_cursur=conn.cursor()
        my_cursur.execute("Select * from student")    
        data=my_cursur.fetchall()    
        if len(data)!=0:
            self.std_tbl.delete(*self.std_tbl.get_children())
            for i in data:
                self.std_tbl.insert("",END,values=i)
            conn.commit()
        conn.close()

    # Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.std_tbl.focus()
        content=self.std_tbl.item(cursor_row)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phn.set(data[11])
        self.var_addr.set(data[12])
        self.var_t_name.set(data[13]) 

    # Update 
    def update_data(self):
        if (self.var_std_id==""):
            messagebox.showerror("Error","All fields are Mandatory") 
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure you want to update student Info",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dept=%s, Course=%s, Years=%s, Semester=%s, Std_Name=%s, Std_Div=%s, Roll_no=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s where Std_Id=%s",(
                                                                                                           self.var_dep.get(),
                                                                                                           self.var_course.get(),
                                                                                                           self.var_year.get(),
                                                                                                           self.var_sem.get(),
                                                                                                           
                                                                                                           self.var_std_name.get(),
                                                                                                           self.var_div.get(),
                                                                                                           self.var_roll.get(),
                                                                                                           self.var_gender.get(),
                                                                                                           self.var_dob.get(),
                                                                                                           self.var_email.get(),
                                                                                                           self.var_phn.get(),
                                                                                                           self.var_addr.get(),
                                                                                                           self.var_t_name.get(),
                                                                                                           self.var_std_id.get()))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Sucess","Student Info Updated Sucessfully",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due to {str(e)}",parent=self.root)
                
    # Delete
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are Mandatory",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Are you sure you want to delete student Info",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
                    my_cursor=conn.cursor()       
                    sql="delete from student where Std_Id=%s"
                    value=(self.var_std_id.get(),)
                    my_cursor.execute(sql,value)  
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student Info Deleted Successfully",parent=self.root)
            except Exception as e: 
                messagebox.showerror("Error",f"Due to {str(e)}",parent=self.root) 

    # Reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phn.set("")
        self.var_addr.set("")
        self.var_t_name.set("")

    # search Data   
    def search_data(self):
        if self.var_combo_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please Select an option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where "+str(self.var_combo_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.std_tbl.delete(*self.std_tbl.get_children())
                    for i in data:
                        self.std_tbl.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Due to {str(e)}",parent=self.root)

                 

if __name__ == "__main__" :
    root=Tk()
    obj=Student(root)
    root.mainloop()

    


