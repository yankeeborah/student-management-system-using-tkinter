from tkinter import *
from tkinter import ttk
from tkinter import font
import pymysql
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1535x800+0+0")

        title=Label(self.root,text="*Student Management System*",bd=10,relief=GROOVE,font=("calibri",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

    #variables
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

    
    
    #manage frame

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=680)
        m_title=Label(Manage_Frame,text="Manage Students",font=("calibri",30,"bold"),bg="crimson",fg="white")
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_Frame,text="Roll Number",bd=10,font=("calibri",15,"bold"),bg="crimson",fg="white")
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("calibri",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name",bd=10,font=("calibri",15,"bold"),bg="crimson",fg="white")
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("calibri",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email=Label(Manage_Frame,text="E-mail",bd=10,font=("calibri",15,"bold"),bg="crimson",fg="white")
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("calibri",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_gender=Label(Manage_Frame,text="Gender",bd=10,font=("calibri",15,"bold"),bg="crimson",fg="white")
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,width=18,textvariable=self.gender_var,font=("calibri",15,"bold"),state="readonly")
        combo_gender['values']=("males","female","other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10,sticky="w")


        lbl_contact=Label(Manage_Frame,text="Contact",bd=10,font=("calibri",15,"bold"),bg="crimson",fg="white")
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("calibri",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_DOB=Label(Manage_Frame,text="DOB",bd=10,font=("calibri",15,"bold"),bg="crimson",fg="white")
        lbl_DOB.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_DOB=Entry(Manage_Frame,textvariable=self.dob_var,font=("calibri",15,"bold"),bd=5,relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_add=Label(Manage_Frame,text="Address",bd=10,font=("calibri",15,"bold"),bg="crimson",fg="white")
        lbl_add.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_add=Text(Manage_Frame,width=26,height=5,font=("",10))
        self.txt_add.grid(row=7,column=1,padx=20,pady=10,sticky="w")

        #button 
        
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=20,y=600,width=410)

        addbtn=Button(btn_Frame,text="ADD",width=10,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_Frame,text="UPDATE",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        delbtn=Button(btn_Frame,text="DELETE",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_Frame,text="CLEAR",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)





        




    #detail frame

        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=1000,height=680)

        lblsearch=Label(Detail_Frame,text="Search By",bd=10,font=("calibri",15,"bold"),bg="crimson",fg="white")
        lblsearch.grid(row=0,padx=25)

        combo_Search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("calibri",15),state="readonly")
        combo_Search['values']=("Roll_no","Name","Contact")
        combo_Search.grid(row=0,column=1,padx=20,pady=10)

        txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=15,font=("calibri",15,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="SEARCH",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="SHOW ALL",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        #Table Frame

        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=50,y=70,width=900,height=550)


        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,column=("roll","name","email","gender","contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
       
        self.Student_table.heading("roll",text="Roll No")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="E-Mail")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("DOB",text="D.O.B")
        self.Student_table.heading("Address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name",width=155)
        self.Student_table.column("email",width=135)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("DOB",width=100)
        self.Student_table.column("Address",width=180)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)


        self.Student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()

    def add_student(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.contact_var.get()=="" or self.gender_var.get()=="" or self.dob_var.get()=="" :
            messagebox.showerror("Error","All fields are required")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.txt_add.get('1.0',END)
                                                                            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()  
    
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_add.delete("1.0",END)

    
    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents["values"]
        
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_add.delete("1.0",END)
        self.txt_add.insert(END,row[6])

    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",
                                                                       (self.name_var.get(),
                                                                        self.email_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.txt_add.get('1.0',END),
                                                                        self.Roll_No_var.get()
                                                                        ))

    
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()

        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()  



            




root=Tk()
ob=Student(root)
root.mainloop()