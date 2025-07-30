import mysql.connector as ms

myconn = ms.connect(host="localhost", user="root", password="aadya@06", database="MYSAMPLE")


# INSERT DATA
def insert_patient():
    mycursor=myconn.cursor()
    query='''INSERT INTO PATIENT (Patient_ID , Name , AGE , GENDER , Organ_Required ,Blood_group) \
       VALUES(881, 'Gautam Mishra', 56, 'Male', 'Liver', ' O+'),
(882, 'Madhuri Park', 64, 'Female', 'Kidney', 'AB+'),
(883, 'Catalina Martin', 35, 'Female', 'Heart', 'B-'),
(884, 'Aaron Blackford ', 39, 'Male', 'Kidney', 'O+'),
(885, 'Helena Hoang', 28, 'Female', 'Liver', 'A+'),
(886, 'Cristina B ', 40, 'Male', ' Kidney', ' B+');'''
    mycursor.execute(query)
    print("DATA SUCCESSFULLY INSERTED IN THE PATIENT TABLE ")
    myconn.commit()
    mycursor.close()

def insert_donor():
    mycursor=myconn.cursor()
    query='''INSERT INTO DONOR(DONOR_ID , Name , AGE , ORGAN_DONATED ,Blood_group,DATE_DONATED) \
VALUES(441, 'Khaled Hosseini', 58, 'Kidney', 'AB+','2023-11-16'),
(442, 'Joanna Trollope', 29, 'Liver', 'O+','2023-6-15'),
(443, 'Alfred Lerner', 46, 'Kidney', 'A+', '2023-4-23'),
(444, 'Daoud Wahab', 50, 'Liver', 'B-', '2023-9-13'),
(445, 'Sandy Chun', 48, 'Liver', 'B+', '2023-7-8'),
(446, 'Todd Dray', 39, 'Heart', 'O+','2023-8-17'),
(447, 'Dori Heck', 61, 'Kidney', 'AB+','2023-11-18'),
(448, 'Robert Heck ', 44, 'Kidney', 'B+','2023-12-9');'''
    mycursor.execute(query)
    print("DATA SUCCESSFULLY INSERTED IN THE DONOR TABLE ")
    myconn.commit()
    mycursor.close()
    
def insert_hospital():
    mycursor=myconn.cursor()
    query='''INSERT INTO HOSPITALS (H_ID , Name ,Address , Contact_no)VALUES (100, 'MUNICH HOSPITAL', 'Munich-Germany', 1110467),
     (200, 'KOÇ UNI HOSPITAL', 'Istanbul Turkey', 39567885),
    (300, 'MEDICNA HOSPITAL', 'Istanbul- Turkey', 56985090),
     (400, 'GLENLES HOSPITAL', 'Chennai-India', 72524598),
    (500, 'ICHILOV HOSPITAL', 'Tel Aviv, Israel', 68902452);'''
    mycursor.execute(query)
    print("DATA SUCCESSFULLY INSERTED IN THE HOSPITAL TABLE ")
    myconn.commit()
    mycursor.close()

def insert_doctor():
    mycursor=myconn.cursor()
    query='''INSERT INTO DOCTOR (Doc_ID, H_ID ,Name_of_the_doctor , CONTACT_NO)VALUES ('661', 300, 'Elena', 87250132),
    ('662', 200, 'Gerald', 59804532),
    ('663', 500, 'Lina', 98345710),
    ('664', 100, 'Kabir', 3455543),
    ('665', 500, 'Issabella', 34576558),
    ('666', 300, 'Theo', 56829904),
    ('667', 400, 'Rajesh', 56450132);'''
    mycursor.execute(query)
    print("DATA SUCCESSFULLY INSERTED IN THE DOCTOR TABLE ")
    myconn.commit()
    mycursor.close()

def insert_reporting():
    mycursor=myconn.cursor()
    query='''INSERT INTO REPORTING(SERIAL_NUM , Patient_ID , Donor_ID , Doc_ID , H_ID)  VALUES(1 , 881 , 446 , 200 ,661) ,
    (2,882,444,500,669) ,
    (3,883,442,100,664) ,
    (4,884,446,400,666),
    (5,885,443,300,662) ,
    (6,886,448,400,665);'''
    mycursor.execute(query)
    print("DATA SUCCESSFULLY INSERTED IN THE REPORTING TABLE ")
    myconn.commit()
    mycursor.close()

insert_hospital()
insert_patient()
insert_donor()
insert_doctor()
inser_reporting()


