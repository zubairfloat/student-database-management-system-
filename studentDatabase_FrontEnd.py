#Front End
from tkinter import*

import tkinter.messagebox

import studentDatabase_BackEnd

class Student:

    def __init__(self,root):
        self.root = root
        self.root.title("student management system")
        self.root.geometry("1500x800+20+20")
        self.root.configure(bg="#8D2752")

        StdID = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        Dob = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Addresst = StringVar()
        Mobile = StringVar()


        #=============================================================== Functions ==================================
        def stexit():
            stexit = tkinter.messagebox.askyesno("Student Database Management Systems ","Confirm if you want to exit")
            if stexit > 0:
                root.destroy()
                return
        def clearData():
            self.studentIDentry.delete(0,END)
            self.firstnameentry.delete(0, END)
            self.lastnameentry.delete(0,END)
            self.dateofBirthentry.delete(0,END)
            self.ageentry.delete(0,END)
            self.genderentry.delete(0,END)
            self.addressentry.delete(0,END)
            self.mobileentry.delete(0,END)


        def addData():
            if(len(StdID.get())!=0):
                studentDatabase_BackEnd.addstdrecord(StdID.get() , Firstname.get() ,Lastname.get() ,Dob.get(), Age.get() ,Gender.get() , Addresst.get(),Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get() , Firstname.get() ,Lastname.get() ,Dob.get(), Age.get() ,Gender.get() , Addresst.get(),Mobile.get()))


        def DisplayData():
            studentlist.delete(0,END)
            for row in studentDatabase_BackEnd.viewData():
                studentlist.insert(END,row,str(""))
        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            self.studentIDentry.delete(0,END)
            self.studentIDentry.insert(END,sd[1])

            self.firstnameentry.delete(0, END)
            self.firstnameentry.insert(END, sd[2])
            self.lastnameentry.delete(0,END)
            self.lastnameentry.insert(END, sd[3])
            self.dateofBirthentry.delete(0,END)
            self.dateofBirthentry.insert(END, sd[4])
            self.ageentry.delete(0,END)
            self.ageentry.insert(END, sd[5])
            self.genderentry.delete(0,END)
            self.genderentry.insert(END, sd[6])
            self.addressentry.delete(0,END)
            self.addressentry.insert(END, sd[7])
            self.mobileentry.delete(0,END)
            self.mobileentry.insert(END, sd[8])




        def DeleteData():
            if(len(StdID.get()) != 0):
                studentDatabase_BackEnd.deleterec(sd[0])
                clearData()
                DisplayData()

        def searchDatabase():
            studentlist.delete(0,END)
            for row in studentDatabase_BackEnd.searchData(StdID=StdID.get() ,Firstname= Firstname.get() ,Lastname=Lastname.get() ,Dob=Dob.get(), Age=Age.get() ,Gender=Gender.get() , Addresst=Addresst.get(),Mobile=Mobile.get()):
                studentlist.insert(END,row,str(""))

        def update():
            if (len(StdID.get())!=0):
                studentDatabase_BackEnd.deleterec(sd[0])
            if (len(StdID.get())!=0):
                studentDatabase_BackEnd.addstdrecord(StdID.get() , Firstname.get() ,Lastname.get() ,Dob.get(), Age.get() ,Gender.get() , Addresst.get(),Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get() , Firstname.get() ,Lastname.get() ,Dob.get(), Age.get() ,Gender.get() , Addresst.get(),Mobile.get()))



        #=============================================================== Frames =============================
        mainframe = Frame(self.root, width=1600,height=150, bd=10, relief= RIDGE,bg= "#9B2E52")
        mainframe.place(x=0,y=0)

        bottomframe = Frame(self.root, width=1600, height=120, relief=GROOVE,bd=10,bg="#F2F3F5")
        bottomframe.place(x=0, y=715)

        rightframe = Frame(self.root,width=600,height=570, bd=10,relief=GROOVE, bg="#F2F3F5")
        rightframe.place(x=1000,y=150)

        leftframe =Frame(self.root,widt=1000,height = 565, bd=10,relief=GROOVE, bg="#F2F3F5")
        leftframe.place(x=0,y=150)

        #======================================= main FRame ====================================================

        titlelable = Label(mainframe,pady=16, text= "Student Database Management System", font= ('arial', 63, 'bold'),fg="#7C2052", bg="#F2F3F5")
        titlelable.grid()

        #====================================== Left Frame ====================================================
        photo = PhotoImage(file="images/graduate.png")
        photoimage = photo.subsample(10, 10)
        a=Label( leftframe, bg="#F2F3F5",image= photoimage)
        a.image= photoimage
        a.place(x=40,y=0)
        self.stdinfolable = Label(leftframe, text= "Student Info",font= ('arial', 30, 'bold'))
        self.stdinfolable.place(x=130,y=5)

        self.studentinfoframe = Frame(leftframe,   width= 930,height=480,bg="#F2F3F5",relief=SUNKEN,bd=10)
        self.studentinfoframe.place(x=20, y=60)
        #======================================= student data entry =============================================
        photo2 = PhotoImage(file="images/ha.png")
        photoimage2 = photo2.subsample(13, 13)
        a = Label(self.studentinfoframe, image=photoimage2)
        a.image = photoimage2
        a.place(x=10, y=0)

        self.studentIDlabel = Label(self.studentinfoframe, text="Student Id :", font=('arial', 20, 'bold'), bg="#F2F3F5")
        self.studentIDlabel.place(x=80, y=2)
        self.studentIDentry = Entry(self.studentinfoframe,textvariable=StdID, width=30, font=('arial', 15, 'bold'))
        self.studentIDentry.place(x=300, y=5)

        photo2 = PhotoImage(file="images/ha.png")
        photoimage2 = photo2.subsample(13, 13)
        a = Label(self.studentinfoframe, image=photoimage2)
        a.image = photoimage2
        a.place(x=10, y=60)

        self.firstnametlabel = Label(self.studentinfoframe, text= "First Name  :",font= ('arial', 20, 'bold'),bg="#F2F3F5")
        self.firstnametlabel.place(x=80,y=60)
        self.firstnameentry = Entry(self.studentinfoframe, width=30, textvariable=Firstname, font= ('arial', 15, 'bold'))
        self.firstnameentry.place(x=300,y=65)

        photo2 = PhotoImage(file="images/ha.png")
        photoimage2 = photo2.subsample(13, 13)
        a = Label(self.studentinfoframe, image=photoimage2)
        a.image = photoimage2
        a.place(x=10, y=120)

        self.lastnamelabel = Label(self.studentinfoframe, text=" Last Name :", font=('arial', 20, 'bold'), bg="#F2F3F5")
        self.lastnamelabel.place(x=80, y=120)
        self.lastnameentry = Entry(self.studentinfoframe, width=30, textvariable=Lastname,font=('arial', 15, 'bold'))
        self.lastnameentry.place(x=300, y=125)

        photo2 = PhotoImage(file="images/ha.png")
        photoimage2 = photo2.subsample(13, 13)
        a = Label(self.studentinfoframe, image=photoimage2)
        a.image = photoimage2
        a.place(x=10, y=180)

        self.dateofBirthlabel = Label(self.studentinfoframe, text="Date of Birth  :", font=('arial', 20, 'bold'), bg="#F2F3F5")
        self.dateofBirthlabel.place(x=80, y=180)
        self.dateofBirthentry = Entry(self.studentinfoframe, width=30,textvariable=Dob, font=('arial', 15, 'bold'))
        self.dateofBirthentry.place(x=300, y=185)

        photo2 = PhotoImage(file="images/ha.png")
        photoimage2 = photo2.subsample(13, 13)
        a = Label(self.studentinfoframe, image=photoimage2)
        a.image = photoimage2
        a.place(x=10, y=240)

        self.agelabel = Label(self.studentinfoframe, text="Age :", font=('arial', 20, 'bold'), bg="#F2F3F5")
        self.agelabel.place(x=80, y=240)
        self.ageentry = Entry(self.studentinfoframe, width=30,textvariable=Age, font=('arial', 15, 'bold'))
        self.ageentry.place(x=300, y=245)

        photo2 = PhotoImage(file="images/ha.png")
        photoimage2 = photo2.subsample(13, 13)
        a = Label(self.studentinfoframe, image=photoimage2)
        a.image = photoimage2
        a.place(x=10, y=300)

        self.genderlabel = Label(self.studentinfoframe, text="Gender :", font=('arial', 20, 'bold'), bg="#F2F3F5")
        self.genderlabel.place(x=80, y=300)
        self.genderentry = Entry(self.studentinfoframe, width=30, textvariable=Gender, font=('arial', 15, 'bold'))
        self.genderentry.place(x=300, y=305)

        photo2 = PhotoImage(file="images/ha.png")
        photoimage2 = photo2.subsample(13, 13)
        a = Label(self.studentinfoframe, image=photoimage2)
        a.image = photoimage2
        a.place(x=10, y=360)

        self.addresslabel = Label(self.studentinfoframe, text="Address :", font=('arial', 20, 'bold'), bg="#F2F3F5")
        self.addresslabel.place(x=80, y=360)
        self.addressentry = Entry(self.studentinfoframe, width=30, textvariable=Addresst, font=('arial', 15, 'bold'))
        self.addressentry.place(x=300, y=365)

        photo2 = PhotoImage(file="images/ha.png")
        photoimage2 = photo2.subsample(13, 13)
        a = Label(self.studentinfoframe, image=photoimage2)
        a.image = photoimage2
        a.place(x=10, y=420)

        self.mobilelabel = Label(self.studentinfoframe, text="Mobile :", font=('arial', 20, 'bold'), bg="#F2F3F5")
        self.mobilelabel.place(x=80, y=420)
        self.mobileentry = Entry(self.studentinfoframe, width=30,textvariable=Mobile,font=('arial', 15, 'bold'))
        self.mobileentry.place(x=300, y=425)

        photo2 = PhotoImage(file="images/notes.png")
        photoimage2 = photo2.subsample(2, 2)
        a = Label(self.studentinfoframe, image=photoimage2)
        a.image = photoimage2
        a.place(x=700, y=30)

        photo2 = PhotoImage(file="images/Detail.png")
        photoimage2 = photo2.subsample(1, 1)
        a = Button(self.studentinfoframe, image=photoimage2)
        a.image = photoimage2
        a.place(x=650, y=200)
        #=========================================== Right Frame ================================================
        scrollbar = Scrollbar(rightframe,)
        scrollbar.place(x=530,y=60)

        studentlist = Listbox(rightframe,width=46,height=18,font=('arial',15,'bold'),yscrollcommand=scrollbar.set)
        studentlist.bind("<<ListboxSelect>>",StudentRec)
        studentlist.place(x=15,y=65)
        scrollbar.config(command = studentlist.yview)

        stddetailslable = Label(rightframe, text= "Student Details",font= ('arial', 30, 'bold'))
        stddetailslable.place(x=120,y=5)

        photo2 = PhotoImage(file="images/details.png")
        photoimage2 = photo2.subsample(4, 5)
        a = Label(rightframe, image=photoimage2)
        a.image = photoimage2
        a.place(x=40, y=0)
        #============================================ Button Sections =============================================

        addnewbutton = Button(bottomframe,text="Add New",fg="white",bg="#8D2752",font=('arial', 20, 'bold'),relief=SUNKEN, command= addData, bd=5,height=2,width=13)
        addnewbutton.place(x=0,y=5)

        displaybutton = Button(bottomframe, command= DisplayData,text="Display",fg="white",bg="#8D2752",font=('arial', 20, 'bold'),relief=SUNKEN, bd=5,height=2,width=13)
        displaybutton.place(x=223,y=5)

        clearbutton = Button(bottomframe,text="Clear",fg="white",bg="#8D2752",font=('arial', 20, 'bold'), command=clearData, relief=SUNKEN, bd=5,height=2,width=13)
        clearbutton.place(x=446,y=5)

        deletebutton = Button(bottomframe,command=DeleteData,text="Delete",fg="white",bg="#8D2752",font=('arial', 20, 'bold'),relief=SUNKEN, bd=5,height=2,width=13)
        deletebutton.place(x=667,y=5)

        searchbutton = Button(bottomframe,text="Search ",fg="white",bg="#8D2752",font=('arial', 20, 'bold'),relief=SUNKEN, bd=5,height=2,width=13,command=searchDatabase)
        searchbutton.place(x=892,y=5)

        updatebutton = Button(bottomframe,text="Update",fg="white",bg="#8D2752",font=('arial', 20, 'bold'),relief=SUNKEN, bd=5,height=2,width=13,command=update)
        updatebutton.place(x=1115,y=5)

        exitbutton = Button(bottomframe, command=stexit,text="Exit",fg="white",bg="#8D2752",font=('arial', 20, 'bold'),relief=SUNKEN, bd=5,height=2,width=13)
        exitbutton.place(x=1338,y=5)


if __name__== '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()