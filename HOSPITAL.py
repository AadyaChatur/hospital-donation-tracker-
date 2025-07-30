import mysql.connector as ms

myconn= ms.connect(host="localhost", user="root", password="aadya@06" , database="aadya_invest")


#TO DISPLAY ALL THE SAVED RECORDS OF THE HOSPITALS 

def show_hospital():
    mycursor=myconn.cursor()
    query=("SELECT* FROM HOSPITALS ;")
    mycursor.execute(query)
    record=mycursor.fetchall()
    print("THE HOSPITALS  DATA\n",record)
    for rec in record:
        print("*----------*----------*---------*--------*---------*")
        print("Hospital_ID:",rec[0])
        print("Name:",rec[1])
        print("Address:",rec[2])
        print("Contact_no:",rec[3])
        print("*---------*--------*---------*-------*---------*-----*")
        



# TO ADD NEW DATA INTO THE HOSPITAL FILE
def add_hospital():
    mycursor = myconn.cursor()
    myID=int(input("ENTER HOSPITALS  ID :"))
    myname=input("ENTER HOSPITALS  NAME :")
    myaddress =input("ENTER HOSPITALS ADDRESS: ")
    number = int(input("ENTER THE CONTACT NUMBER OF THE HOSPITAL: "))
    
    query = '''INSERT INTO HOSPITALS (H_ID , NAME_OF_THE_HOSPITAL , Address , Contact_no)
            VALUES(%s , %s , %s , %s )'''
    vals = (myID, myname, myaddress , number)

    mycursor.execute(query, vals)
    myconn.commit()
    mycursor.close()
    print(" ALL DONE !!! ALL RECORDS ADDED TO THE FINAL TABLE ")




#TO SEARCH FOR THE RECORDS OF A HOSPITALS  USING THE NAME ENTERED BY THE USER

def search_hospital(hname):
    mycursor=myconn.cursor()
    query=("SELECT* FROM HOSPITALS  WHERE NAME_OF_THE_HOSPITAL=%s ")
    mycursor.execute(query,(hname,))
    mydata=mycursor.fetchall()
    for rec in mydata:
        print("*----------*----------*---------*--------*---------*")
        print("Hospital_ID:",rec[0])
        print("Name:",rec[1])
        print("Address:",rec[2])
        print("Contact_no:",rec[3])
        print("*---------*--------*---------*-------*---------*-----*")
    myconn.commit()
    mycursor.close()



#TO SEARCH FOR THE RECORDS OF A HOSPITAL USING THE HOSPITAL ID ENTERED BY THE USER

def search_id(HID):
    mycursor=myconn.cursor()
    query=("SELECT* FROM HOSPITALS  WHERE H_ID=%s")
    mycursor.execute(query,(HID,))
    mydata=mycursor.fetchall()
    for rec in mydata:
        print("*----------*----------*---------*--------*---------*")
        print("Hospital_ID:",rec[0])
        print("Name:",rec[1])
        print("Address:",rec[2])
        print("Contact_no:",rec[3])
        print("*---------*--------*---------*-------*---------*-----*")
    myconn.commit()
    mycursor.close()


#TO DELETE THE RECORDS OF A HOSPITALS  USING THE HOSPITALS  ID ENTERED BY THE USER 

def del_hose(HID):
    flag=0
    mycursor=myconn.cursor()
    while True:
        flag=1
        query=("DELETE FROM HOSPITALS  WHERE H_ID=%s")
        mycursor.execute(query,(HID,))
        myconn.commit()
    if flag ==1:
        print("RECORDS OF THE HOSPITAL WITH HOSPITAL ID ",HID," HAS BEEN DELETED")
    else:
        print("RECORD OF THE HOSPITAL WITH HOSPITAL ID",HID,"NOT FOUND")
    mycursor.close()




