import sqlite3 as sql

sex= ""; sno=0; sna=''; crs="";
conn = sql.connect("student.db")
cursor = conn.cursor()
#cursor.execute('''Drop table tbl_stud''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tbl_stud (
                    stud_no TEXT ,
                    stud_name TEXT,
                    course TEXT,
                    sex TEXT)''')
class Students:
    def __init__(self,sno,sna,crs,sex): #,crs
        self.sno = sno
        self.sna = sna
        self.crs = crs
        self.sex = sex
    def add_rec(self,cmd):
        cursor.execute(cmd,(self.sno,self.sna,self.crs,self.sex)) 
        conn.commit()

def main():
    conn = sql.connect("student.db")
    cursor = conn.cursor()
    ans = 'y'
    while ans == 'y':
        sno = input('student no.: ')
        sna = input('student name: ')
        crs = input ("course: ")
        sex = input("sex (M/F): ")


        if sex == 'F':
            sex = 'Female'
        else: sex = 'Male'

        stud = Students(sno,sna,crs,sex)

        cmd = 'insert into tbl_stud(stud_no,stud_name,course,sex) values(?,?,?,?)'
        stud.add_rec(cmd)
        ans = input('input again[y/n]?: ')
    conn.close()
    view_rec()

def view_rec():
    conn = sql.connect("student.db")
    cursor = conn.cursor()
    cursor = conn.execute('select * from tbl_stud')
    for record in cursor:
        print('student no.: ',record[0])
        print('student name: ',record[1])
        print('course: ',record[2])
        print('sex: ',record[3])
        #print('course: ',record[4])
        print()

main()

