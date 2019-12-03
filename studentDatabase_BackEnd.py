import sqlite3
# backend

def studentData():
    con=sqlite3.connect("student.db")
    cur= con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, StdID text, Firstname text, Lastname text,Dob text, Age text,Gender text, Addresst text,Mobile text)")
    con.commit()
    con.close()

def addstdrecord(StdID , Firstname ,Lastname ,Dob, Age ,Gender , Addresst,Mobile ):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES(NULL, ?,?,?,?,?,?,?,?)", (StdID , Firstname ,Lastname ,Dob, Age ,Gender , Addresst,Mobile))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return rows

def deleterec(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?",(id,))
    con.commit()
    con.close()

def searchData(StdID="" , Firstname="" ,Lastname="" ,Dob="", Age="" ,Gender="", Addresst="",Mobile="" ):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID=? OR Firstname=? OR Lastname=? OR Dob=? OR Age=? OR Gender=? OR Addresst=? OR Mobile=?",(StdID , Firstname ,Lastname ,Dob, Age ,Gender , Addresst,Mobile))
    rows=cur.fetchall()
    con.close()
    return rows

def updateData(StdID="" , Firstname="" ,Lastname="" ,Dob="", Age="" ,Gender="", Addresst="",Mobile="" ):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET  StdID=? , Firstname=? , Lastname=? , Dob=? , Age=? , Gender=? , Addresst=? , Mobile=?, WHERE id=?",(StdID , Firstname ,Lastname ,Dob, Age ,Gender , Addresst,Mobile))
    con.commit()
    con.close()

studentData()