import pyfiglet
import mysql.connector as a

con = a.connect(host="localhost", user="root", passwd="12345", database="SCHOOL")

banner = pyfiglet.figlet_format("DIVINE SAINIK SCHOOL", font='bubble')
print(banner)

def aboutschool():
    print(banner)
    print("""                                             Aim of the school
              The main aim of the school is to provide comprehensive educational manner of speaking system to impart 
              impulse to the student's physical growth as well as his/her scientific thinking, emotional, spiritual and
              moral development.""")
    print("""                                             Rules & Regulations
             * A pupil will be eligible to appear in the session ending I Examination if he/she has completed 90% attendance.
             * Leave to a student for absence is granted only on an I application to The principal, through class Teacher 
               Submitted in Time definitely the same day, rarely the next day) duly attested by the Parent/Guardian.
             * The name of the student will be struck of the rolls of the school if he/she is absent for more than a week 
               continuous without sanction of leave.
             * Before leave inform and give the application.
             * Fee will be charged monthly.
             * Fee will be paid in advance 15th of every month.
             * Fee can also be paid with Late Payment of Rs.10/- on the last working day of the month. 
               There after the name will be struck off the register Readmission can be taken on payment of Rs.50/- 
               with the approval the principal.
             * If a child is with drawn in the mid-session six month's fees will be charged.""")
    print("""                                                
     
                                                             School Activities
               Divine Sainik School provides different activities for better development of your child. The activities are :

          * Co-Curicular activities
             Children are inquisitive by nature. They are extremely curious lot, always eager to know about everything around them, 
             therefore besides academics, in order to ensure development of curiosity and personality the school imparts
             ample opportunities to students in a wide variety of hobby and activity in quiescent surrounding as music 
             and dance, art and craft, painting and drawing, science exhibition, knowledge quotient.

          * Inter Class Activities
             The school has been divided into to groups namely Jr. Group (nursery to fifth) and Sr. Group 
             (Classes VI to onward) to make education more meaningful socially acceptable and for an all round growth
             and development such as physical, mental, emotional, spiritual etc.Inter class Literacy Activities are 
             organised on every Wednesday and Saturday of the week. The Inter Class Activities help in maintaining 
             discipline in the school.

          * Activities During The Session
             Literary Activities- Various Inter Class Activities such as : Debate, Extempore, Declamation, Quiz
             Competition, Essay Writing Competition,Art Competition and Assembly Song of Competition are organised 
             every month. G Inter Class Matches-Various Inter Class Matches such as Foot-ball, Handball, Khokho, Chess 
             and Carrom etc. are organised every month.""")

    print("""            Email:-info@divinesainikschool.com
            Website:-www.divinesainikschool.com
            Contact no.:0542-2371526""")
    print(">---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    main()
def ast():
    n=input("Student name:")
    c=input("Class:")
    r=input("Roll no.:")
    a=input("Address:")
    p=input("Phone:")
    data=(n,c,r,a,p)
    sql='insert into student values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    print(">---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    main()
def rst():
    c=input("Class:")
    r=input("Roll no.:")
    data=(c,r)
    sql='delete from student where CLASS=%s and ROLL=%s'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Deleted")
    print(">----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    main()
def addt():
    n=input("Teacher Name:")
    p=input("Subject:")
    s=input("Salary:")
    a=input("Address:")
    ph=input("Phone:")
    ac=input("ID:")
    data=(n,p,s,a,ph,ac)
    sql='insert into teacher values(%s,%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    print(">----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    main()
def remt():
    n=input("Teachers name:")
    ac=input("Account no.:")
    data=(n,ac)
    sql='delete from teacher where name=%s and acno=%s'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Deleted")
    print(">---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
    main()
def abclass():
    d=input("Date:")
    cl=input("Class:")
    ab=("Names of absent Student:")
    data=(d,cl,ab)
    sql="insert into cattendance values(%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
    main()
def abteacher():
    d=input("Date:")
    ab=("Names of Absent Teacher:")
    data=(d,ab)
    sql="insert into tattendance values(%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
    main()
def submitf():
    n=input("Student name:")
    c=input("Class:")
    r=input("Roll no.:")
    m=input("Month and Year:")
    f=input("Fees:")
    d=input("Date:")
    data=(n,c,r,m,f,d)
    sql='insert into fees values(%s,%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    print(">---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
    main()
def tpays():
    n=input("Teacher name:")
    m=input("Month:")
    p=input("YES/NO:")
    data=(n,m,p)
    sql='insert into salary values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfuly")
    print(">---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
    main()
def dclass():
    cl=input("Class:")
    data=(cl,)
    sql="select * from student where class=%s"
    c=con.cursor()
    c.execute(sql,data)
    d=c.fetchall()
    for i in d:
        print("NAME:",i[0])
        print("CLASS:", i[1])
        print("ROLL:", i[2])
        print("ADDRESS:", i[3])
        print("PHONE:", i[4])
        print(">----------------------------------------------------------------------------------------------------------------------")
    print(">---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
    main()
def dteacher():
    sql="select * from teacher"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print("NAME:",i[0])
        print("SUBJECT:", i[1])
        print("SALARY:", i[2])
        print("ADDRESS:", i[3])
        print("PHONE:", i[4])
        print("ID:",i[5])
        print(">-----------------------------------------------------------------------------------------------------------------------")
    print(">---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
    main()
def faci():
    print("""                                                     FACILITIES
           
              * Paying much attention to all subjects, classes will be allotted to expert teachers in particular subjects.
              * Four well ventilated labs for the subjects such as Physics, Chemistry, Biology, Computer Education gemmed by updated instruments.
              * Close circuite vigilance cameras in every room.
              * Huge playground for students and small parks for KG students.
              * Transportation facility available for both rural and urban areas.
              * Mandatory physical education for all believing in apt saying "Healthy bodies make healthy minds".
              * The Knowledge Bank- Library providing latest educational information tools to students.
              * Computer education-The indispensable part of today's modern world, starting from class III onwards to 
                make our students stand neck to neck with time.
              * privileges are blessed by able guidance and knowledge provided through expert teachers.
              * Apart from the regular curriculum, the school has facilities for outdoor games as football, volleyball, badminton etc. 
                to inculcate the spirit of overall development of the students in a big field by natural environment 
                under the guidance of trained sports teacher.
              * Apart from this, there are also facilities for indoor games like carrom, chess etc.
         """)
    print(">---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
    main()
def main():
    print("""
             1. About Divine Sainik School.
             2. Our Faculties.
             3. Display Students.
             4. Add Students.
             5. Add Teachers.
             6. Remove Student.
             7. Remove Teacher.
             8. Submit Fees.
             9. Pay Salary.
             10. Class Attendance.
             11. Teacher Attendance.
             12. Facilities.
        """)
    choice=input("Select a no. for viewing School Details\n")
    print(">----------------------------------------------------")
    if (choice=='1'):
        aboutschool()
    elif (choice=='2'):
        dteacher()
    elif (choice=='3'):
        dclass()
    elif (choice=='4'):
        ast()
    elif (choice=='5'):
        addt()
    elif (choice=='6'):
        rst()
    elif (choice=='7'):
        remt()
    elif (choice=='8'):
        submitf()
    elif (choice=='9'):
        tpays()
    elif (choice=='10'):
        abclass()
    elif (choice=='11'):
        abteacher()
    elif (choice=='12'):
        faci()
    else :
        print("wrong Choice.......")
        main()
def pswd():
    p=input("Password:")
    if p=="komal" :
        main()
    else:
        print("Wrong Password")
        pswd()
pswd()










