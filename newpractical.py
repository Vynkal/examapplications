from tkinter import *
import sqlite3
root=Tk()
conn=sqlite3.connect("newproject.db")
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS student(first_name text NOT NULL PRIMARY KEY,middle_name text NOT NULL,last_name text NOT NULL,mother_name text NOT NULL,highest_qualification text NOT NULL,dob text NOT NULL,email text,mob_no text NOT NULL,username text NOT NULL,password text NOT NULL)")
def login():
    conn=sqlite3.connect("newproject.db")
    c=conn.cursor()
    c.execute("SELECT OID FROM student WHERE username=? AND password=?",(username.get(),password.get(),))
    row=c.fetchone()
    if row:
        
        log=Tk()
        #first name
        query="select first_name FROM student WHERE username=?;"
        c.execute(query,(username.get(),))
        first=c.fetchone()
        first_name=Label(log,text="first name").grid(row=0,column=0)
        first_name=Entry(log,)
        first_name.grid(row=0,column=1)
        first_name.insert(0,first)
        #middle name
        query="select middle_name FROM student WHERE username=?;"
        c.execute(query,(username.get(),))
        middle=c.fetchone()
        middle_name=Label(log,text="middle name").grid(row=2,column=0)
        middle_name=Entry(log,)
        middle_name.grid(row=2,column=1)
        middle_name.insert(0,middle)
        #last name
        query="select last_name FROM student WHERE username=?;"
        c.execute(query,(username.get(),))
        last=c.fetchone()
        last_name=Label(log,text="last name").grid(row=3,column=0)
        last_name=Entry(log,)
        last_name.grid(row=3,column=1)
        last_name.insert(0,last)
        #mother name
        query="select mother_name FROM student WHERE username=?;"
        c.execute(query,(username.get(),))
        mother=c.fetchone()
        mother_name=Label(log,text="mother name").grid(row=4,column=0)
        mother_name=Entry(log,)
        mother_name.grid(row=4,column=1)
        mother_name.insert(0,mother)
        #qualification
        query="select highest_qualification FROM student WHERE username=?;"
        c.execute(query,(username.get(),))
        qualification=c.fetchone()
        highest_qualification=Label(log,text="highest_qualification").grid(row=5,column=0)
        highest_qualification=Entry(log,)
        highest_qualification.grid(row=5,column=1)
        highest_qualification.insert(0,qualification)
        #dob
        query="select dob FROM student WHERE username=?;"
        c.execute(query,(username.get(),))
        dob=c.fetchone()
        do=Label(log,text="dob").grid(row=6,column=0)
        do=Entry(log,)
        do.grid(row=6,column=1)
        do.insert(0,dob)
        #email
        query="select email FROM student WHERE username=?;"
        c.execute(query,(username.get(),))
        mail=c.fetchone()
        email=Label(log,text="email ").grid(row=7,column=0)
        email=Entry(log,)
        email.grid(row=7,column=1)
        email.insert(0,mail)
        #phone no
        query="select mob_no FROM student WHERE username=?;"
        c.execute(query,(username.get(),))
        mob=c.fetchone()
        phone=Label(log,text="mob no").grid(row=8,column=0)
        phone=Entry(log,)
        phone.grid(row=8,column=1)
        phone.insert(0,mob)
        def update():
            conn=sqlite3.connect("newproject.db")
            c=conn.cursor()
            query="UPDATE  student SET first_name=? WHERE username=?;"
            conn.execute(query,(first_name.get(),username.get()))
            query="UPDATE  student SET middle_name=? WHERE username=?;"
            conn.execute(query,(middle_name.get(),username.get()))
            query="UPDATE  student SET last_name=? WHERE username=?;"
            conn.execute(query,(last_name.get(),username.get()))
            query="UPDATE  student SET mother_name=? WHERE username=?;"
            conn.execute(query,(mother_name.get(),username.get()))
            query="UPDATE  student SET highest_qualification=? WHERE username=?;"
            conn.execute(query,(highest_qualification.get(),username.get()))
            query="UPDATE  student SET dob=? WHERE username=?;"
            conn.execute(query,(do.get(),username.get()))
            query="UPDATE  student SET email=? WHERE username=?;"
            conn.execute(query,(email.get(),username.get()))
            query="UPDATE  student SET mob_no=? WHERE username=?;"
            conn.execute(query,(phone.get(),username.get()))
            conn.commit()
            conn.close()
            return
        update=Button(log,text="update",command=update)
        update.grid(row=9,column=1)
                  
    else:
        l=Label(root,text="enter correct credential").grid()
    
    conn.commit()
    conn.close()
    return
def adminlogin():
    def adlogin():
        def adupdate():
            usernam=Entry(ad,)
            usernam.grid(row=0,column=1)
            
            return
        
        def addeluser():
            def ad_del():
                conn=sqlite3.connect("newproject.db")
                c=conn.cursor()
                query="DELETE FROM student WHERE mob_no=?"
                c.execute(query,(usernam.get(),))
                conn.commit()
                conn.close()
                
                return
            
            usernam=Entry(ad,text="mob no")
            usernam.grid(row=6,column=2)
            ad_del=Button(ad,text="Delete",command=ad_del).grid(row=6,column=3)
            
            return
        
        if usernam.get()=="Admin" and passwor.get()=="Admin@@123":
            conn=sqlite3.connect("newproject.db")
            c=conn.cursor()
            c.execute("SELECT * FROM student")
            x=c.fetchall()
            ##adupdate=Button(ad,text="upate",command=adupdate).grid(row=5,column=1)
            deluser=Button(ad,text="del user",command=addeluser).grid(row=6,column=1)
            u=Label(ad,text=x).grid(row=4,column=0)
            conn.commit()
            conn.close()
        return
    
    ad=Tk()
    user=Label(ad,text="username").grid(row=0,column=0)
    passw=Label(ad,text="password").grid(row=1,column=0)
    usernam=Entry(ad,)
    passwor=Entry(ad,)
    usernam.grid(row=0,column=1)
    passwor.grid(row=1,column=1)
    logi=Button(ad,text="Login",command=adlogin).grid(row=2,column=1)
    
    return
def register():
    reg=Tk()
    #submit form
    def submit():
        first_name
        middle_name
        last_name
        mother_name
        highest_qualification
        dob
        email
        mob_no
        username
        password
        conn=sqlite3.connect("newproject.db")
        c=conn.cursor()
        c.execute("INSERT INTO student VALUES(:first_name,:middle_name,:last_name,:mother_name,:highest_qualification,:dob,:email,:mob_no,:username,:password)",

                    {
                        "first_name":first_name.get(),
                        "middle_name":middle_name.get(),
                        "last_name":last_name.get(),
                        "mother_name":mother_name.get(),
                        "highest_qualification":highest_qualification.get(),
                        "dob":dob.get(),
                        "email":email.get(),
                        "mob_no":mob_no.get(),
                        "username":username.get(),
                        "password":password.get(),
                        }

                  )
        first_name.delete(0,END)
        middle_name.delete(0,END)
        last_name.delete(0,END)
        mother_name.delete(0,END)
        highest_qualification.delete(0,END)
        dob.delete(0,END)
        email.delete(0,END)
        mob_no.delete(0,END)
        username.delete(0,END)
        password.delete(0,END)
        conn.commit()
        conn.close()
        return
    #clear entry key
    def clear():
        first_name.delete(0,END)
        middle_name.delete(0,END)
        last_name.delete(0,END)
        mother_name.delete(0,END)
        highest_qualification.delete(0,END)
        dob.delete(0,END)
        email.delete(0,END)
        mob_no.delete(0,END)
        username.delete(0,END)
        password.delete(0,END)
        return
    #label of registration entry key
    first_name=Label(reg,text="first name").grid(row=0,column=0)
    middle_name=Label(reg,text="middle name").grid(row=1,column=0)
    last_name=Label(reg,text="last name").grid(row=2,column=0)
    mother_name=Label(reg,text="mother name").grid(row=3,column=0)
    highest_qualification=Label(reg,text="highest qualification").grid(row=4,column=0)
    dob=Label(reg,text="date of birth").grid(row=5,column=0)
    email=Label(reg,text="email id").grid(row=6,column=0)
    mob_no=Label(reg,text="mob no").grid(row=7,column=0)
    username=Label(reg,text="username").grid(row=8,column=0)
    password=Label(reg,text="password").grid(row=9,column=0)
    #entry point in registration
    first_name=Entry(reg,)
    middle_name=Entry(reg,)
    last_name=Entry(reg,)
    mother_name=Entry(reg,)
    highest_qualification=Entry(reg,)
    dob=Entry(reg,)
    email=Entry(reg,)
    mob_no=Entry(reg,)
    username=Entry(reg,)
    password=Entry(reg,)
    #grid of entry
    first_name.grid(row=0,column=1)
    middle_name.grid(row=1,column=1)
    last_name.grid(row=2,column=1)
    mother_name.grid(row=3,column=1)
    highest_qualification.grid(row=4,column=1)
    dob.grid(row=5,column=1)
    email.grid(row=6,column=1)
    mob_no.grid(row=7,column=1)
    username.grid(row=8,column=1)
    password.grid(row=9,column=1)
    #submit and clear bottons
    submit=Button(reg,text="submit",command=submit)
    submit.grid(row=10,column=1)
    clear=Button(reg,text="clear",command=clear)
    clear.grid(row=11,column=1)
    
    
    return

def forgetuser():
    
    use=Tk()
    mob=Label(use,text="mob no").grid(row=0,column=0)
    mo=Entry(use,)
    mo.grid(row=0,column=1)
    def user():
        conn=sqlite3.connect("newproject.db")
        c=conn.cursor()
        query="SELECT username FROM student WHERE mob_no=?"
        c.execute(query,(mo.get(),))
        username=c.fetchone()
        l=Label(use,text=username).grid()
        conn.commit()
        conn.close()
    but=Button(use,text="show user",command=user).grid(row=1,column=1)
    
    
    return
def forgetpass():
    pas=Tk()
    user=Label(pas,text="username").grid(row=0,column=0)
    a=Entry(pas,)
    a.grid(row=0,column=1)
    def passw():
        b=Entry(pas,)
        b.grid(row=2,column=1)
        def chpass():
                conn=sqlite3.connect("newproject.db")
                c=conn.cursor()
                pa=b.get()
                us=a.get()
                query="UPDATE student SET password=? WHERE username=?;"
                c.execute(query,(pa,us,))
                conn.commit()
                conn.close()
                return
       
        bu=Button(pas,text="update password",command=chpass).grid(row=3,column=1)
        return
    bt=Button(pas,text="next",command=passw).grid(row=1,column=1)
    
    return
user=Label(root,text="username").grid(row=0,column=0)
passw=Label(root,text="password").grid(row=1,column=0)
username=Entry(root,)
password=Entry(root,)
username.grid(row=0,column=1)
password.grid(row=1,column=1)
login=Button(root,text="Login",command=login).grid(row=2,column=1)
register=Button(root,text="Register",command=register).grid(row=2,column=2)
forgetuser=Button(root,text="forget username",command=forgetuser).grid(row=12,column=1)
forgetpass=Button(root,text="forget password",command=forgetpass).grid(row=13,column=1)
adminlogin=Button(root,text="AdminLogin",command=adminlogin).grid(row=14,column=1)

conn.commit()
conn.close()
root.mainloop()
