import mysql.connector as ms
myconnection = ms.connect(host="localhost", user="root", password="aadya@06", database="aadya_invest")

def create_patient():
    mycursor=myconn.cursor()
    query='''CREATE TABLE PATIENT (Patient_ID int NOT NULL PRIMARY KEY,
    Name varchar(30) NOT NULL,
    AGE int DEFAULT NULL,
    GENDER varchar(6) NOT NULL,
    Organ_Required varchar(10) DEFAULT NULL,
    Blood_group varchar(4) DEFAULT NULL );'''
    mycursor.execute(query)
    print("PATIENT TABLE CREATED SUCCESSFULLY")
    myconn.commit()
    mycursor.close()



def create_donor():
    mycursor=myconn.cursor()
    query='''CREATE TABLE donor(Donor_ID int NOT NULL PRIMARY KEY,
    Name varchar(36) NOT NULL,
    AGE int DEFAULT NULL,
    ORGAN_DONATED varchar(10) DEFAULT NULL,
    Blood_group varchar(7) DEFAULT NULL,
    DATE_DONATED date DEFAULT NULL);'''
    mycursor.execute(query)
    print("DONOR TABLE CREATED SUCCESSFULLY")
    myconn.commit()
    mycursor.close()


def create_doctor() :
    mycursor=myconn.cursor()
    query='''CREATE TABLE doctor(Doc_ID varchar(6) NOT NULL PRIMARY KEY,
    H_ID int DEFAULT NULL,
    Name_of_the_doctor varchar(17) DEFAULT NULL,
    CONTACT_NO int DEFAULT NULL);'''
    mycursor.execute(query)
    print("DOCTOR TABLE CREATED SUCCESSFULLY")
    myconn.commit()
    mycursor.close()

def create_hospital():
    mycursor=myconn.cursor()
    query='''CREATE TABLE hospitals(H_ID varchar(6) NOT NULL PRIMARY KEY ,
    Name varchar(16) NOT NULL,
    Address varchar(19) DEFAULT NULL,
    Contact_no int DEFAULT NULL);'''
    mycursor.execute(query)
    print("HOSPITAL TABLE CREATED SUCCESSFULLY")
    myconn.commit()
    mycursor.close()

def create_reporting():
    mycursor=myconn.cursor()
    query='''CREATE TABLE REPORTING (SERIAL_NUM  INT NOT NULL PRIMARY KEY,
    Patient_ID INT,
    Donor_ID INT,
    Doc_ID INT,
    H_ID INT );'''

    mycursor.execute(query)
    print("REPORTING TABLE CREATED SUCCESSFULLY")
    myconn.commit()
    mycursor.close()


create_patient()
create_donor()
create_doctor()
create_hospital()
create_reporting()
