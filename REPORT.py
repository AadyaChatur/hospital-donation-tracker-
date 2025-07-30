import mysql.connector as ms

myconn = ms.connect(host="localhost", user="root", password="aadya@06", database="aadya_invest")

def report():
    mycursor=myconn.cursor()
    print("श्रद्धया देयम् FOUNDATION")
    print("Patient reports")

    query = '''SELECT R.SERIAL_NUM , P.NAME_OF_THE_PATIENT , P.AGE ,P.GENDER ,P.Organ_Required , P.Blood_group , D.NAME_OF_THE_DONOR ,
D.AGE, D.Blood_group,D.DATE_DONATED ,doc.Name_of_the_doctor , doc.CONTACT_NO , H.Name_OF_THE_HOSPITAL , H.Address , H.Contact_no
FROM Patient P , Donor D ,
Doctor doc , Hospitals H , Reporting R
WHERE R. Patient_ID =P. Patient_ID AND R.Donor_ID=D.Donor_ID AND R.Doc_ID =doc.Doc_ID AND  R.H_ID=H.H_ID ;
'''
    mycursor.execute(query)
    data=mycursor.fetchall()
    for i in data:
        print("***************************************","SERIAL NUMBER",i[0],"****************************************************")
        print("PATIENT INFO")
        print("NAME OF THE PATIENT:",i[1] , "AGE:",i[2] ,"GENDER:",i[3] ,"Organ_Required:",i[4] ,"BLOOD GROUP:",i[5])
        print("_________________________________________________________________________________________________________")
        print("DONOR INFO")
        print("NAME_OF_THE_DONOR:",i[6] ,"AGE OF THE DONOR:",i[7] , "Blood_group OF THE DONOR:",i[8], "DATE_DONATED:",i[9])
        print("_________________________________________________________________________________________________________")
        print("DOCTOR INFO")
        print("NAME OF THE DOCTOR: ",i[10], "CONTACT NO:",i[11])
        print("_________________________________________________________________________________________________________")
        print("HOSPITAL INFO")
        print("NAME OF THE HOSPITAL :",i[12], "ADDRESS:",i[13],"CONTACT NUMBER OF HOSPITAL:",i[14])
        print("**************************************************************************************************************")
        

        
    mycursor.close()

    
report()
