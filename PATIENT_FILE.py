import mysql.connector as ms

myconn = ms.connect(host="localhost", user="root", password="aadya@06", database="aadya_invest")


#TO DISPLAY ALL THE SAVED RECORDS OF THE PATIENTS UNDER TREATMENT 

def show_patient():
    mycursor=myconn.cursor()
    query=("SELECT* FROM PATIENT;")
    mycursor.execute(query)
    record=mycursor.fetchall()
    print("THE PATIENT DATA\n",record)
    for tule in record:
        print("*----------*----------*---------*--------*---------*")
        print("Patient_ID:",tule[0])
        print("Name:",tule[1])
        print("Age:",tule[2])
        print("Gender:",tule[3])
        print("Organ Required for Transplantation:",tule[4])
        print("Blood Group Of the Patient:",tule[5])
        print("*---------*--------*---------*-------*---------*-----*")
        



# TO ADD NEW DATA INTO THE PATIENT FILE
def add_patient():
    mycursor = myconn.cursor()
    myID=int(input("ENTER PATIENT ID :"))
    myname=input("ENTER PATIENT NAME :")
    myage = int(input("ENTER PATIENT AGE: "))
    mygender = input("ENTER PATIENT GENDER: ")
    organ = input("ENTER THE ORGAN REQUIRED FOR TRANSPLANTATION: ")
    gblood = input("ENTER THE BLOOD GROUP OF THE PATEINT : ")


    query = '''INSERT INTO patient(Patient_ID , NAME_OF_THE_PATIENT , AGE , GENDER , Organ_Required , Blood_group)
            VALUES(%s , %s , %s , %s , %s , %s )'''
    vals = (myID, myname, myage, mygender, organ , gblood)

    mycursor.execute(query, vals)
    myconn.commit()
    mycursor.close()
    print(" ALL DONE !!! ALL RECORDS ADDED TO THE FINAL TABLE ")



#TO SEARCH FOR THE RECORDS OF A PATIENT USING THE NAME ENTERED BY THE USER

def search_patient(pname):
    mycursor=myconn.cursor()
    query=("SELECT* FROM PATIENT WHERE NAME_OF_THE_PATIENT = %s")
    mycursor.execute(query,(pname,))
    mydata=mycursor.fetchall()
    for tule in mydata:
        print("*----------*----------*---------*--------*---------*")
        print("Patient_ID:",tule[0])
        print("Name:",tule[1])
        print("Age:",tule[2])
        print("Gender:",tule[3])
        print("Organ Required for Transplantation:",tule[4])
        print("Blood Group Of the Patient:",tule[5])
        print("*---------*--------*---------*-------*---------*-----*")
    
    mycursor.close()




#TO SEARCH FOR THE RECORDS OF A PATIENT USING THE PATIENT ID ENTERED BY THE USER

def search_Patient_id(PID):
    mycursor=myconn.cursor()
    query=("SELECT* FROM PATIENT WHERE Patient_ID=%s")
    mycursor.execute(query,(PID,))
    mydata=mycursor.fetchall()
    for tule in mydata:
        print("*----------*----------*---------*--------*---------*")
        print("Patient_ID:",tule[0])
        print("Name:",tule[1])
        print("Age:",tule[2])
        print("Gender:",tule[3])
        print("Organ Required for Transplantation:",tule[4])
        print("Blood Group Of the Patient:",tule[5])
        print("*---------*--------*---------*-------*---------*-----*")

    mycursor.close()




#TO UPDATE THE ORGAN REQUIREMENT AND BLOOD GROUP OF THE PATIENT USING THE PATIENT ID 

def update_organ(PID,org):
    mycursor=myconn.cursor()
    query="UPDATE Patient SET Organ_Required=%s WHERE Patient_ID=%s"
    mycursor.execute(query,(org ,PID ))
    print("UPDATED!!!")
    myconn.commit()
    mycursor.close()


#TO DELETE THE RECORDS OF A PATIENT USING THE PATIENT ID ENTERED BY THE USER 

def del_patient(PID):
    flag=0
    mycursor=myconn.cursor()
    for i in range(1):
        flag=1
        query=("DELETE FROM Patient WHERE Patient_ID=%s")
        mycursor.execute(query,(PID,))
    if flag ==1:
        print("RECORDS OF THE PATIENT WITH PATIENT ID ",PID," HAS BEEN DELETED")
    else:
        print("RECORD OF THE PATIENT WITH PATIENT ID",PID,"NOT FOUND")
    myconn.commit()
    mycursor.close()

