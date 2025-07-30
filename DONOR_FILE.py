import mysql.connector as ms

myconnect= ms.connect(host="localhost", user="root", password="aadya@06" , database="aadya_invest")




#TO DISPLAY ALL THE SAVED RECORDS OF THE DONOR UNDER TREATMENT 

def show_donor():
    mycursor=myconnect.cursor()
    query=("SELECT* FROM DONOR;")
    mycursor.execute(query)
    record=mycursor.fetchall()
    print("THE DONOR DATA\n",record)
    for line in record:
        print("*----------*----------*---------*--------*---------*")
        print("Donor_ID:",line[0])
        print("Name:",line[1])
        print("Age:",line[2])
        print("Organ Donated:",line[3])
        print("Blood_group:",line[4])
        print("Date_Donated:",line[5])
        print("*---------*--------*---------*-------*---------*-----*")



# TO ADD NEW DATA INTO THE DONOR FILE
def add_donor():
    mycursor = myconnect.cursor()
    myID=int(input("ENTER DONOR ID :"))
    myname=input("ENTER DONOR NAME :")
    myage = int(input("ENTER DONOR AGE: "))
    organ = input("ENTER THE ORGAN DONATED: ")
    bgroup=input("ENTER THE BLOOD GROUP OF THE DONOR:")
    date = input("ENTER THE DATE OF DONATION : ")


    query = '''INSERT INTO DONOR(DONOR_ID , NAME_OF_THE_DONOR, AGE , ORGAN_DONATED , Blood_group , DATE_DONATED)
            VALUES(%s , %s , %s , %s , %s , %s)'''
    vals = (myID, myname, myage , organ , bgroup , date)

    mycursor.execute(query, vals)
    myconnect.commit()
    mycursor.close()
    print(" ALL DONE !!! ALL RECORDS ADDED TO THE FINAL TABLE ")



#TO SEARCH FOR THE RECORDS OF A DONOR USING THE NAME ENTERED BY THE USER

def search_donor(dname):
    mycursor=myconnect.cursor()
    query=("SELECT* FROM DONOR WHERE NAME_OF_THE_DONOR=%s ")
    mycursor.execute(query,(dname,))
    mydata=mycursor.fetchall()
    for line in mydata:
        print("*----------*----------*---------*--------*---------*")
        print("Donor_ID:",line[0])
        print("Name:",line[1])
        print("Age:",line[2])
        print("Organ Donated:",line[3])
        print("Blood_group:",line[4])
        print("Date_Donated:",line[5])
        print("*---------*--------*---------*-------*---------*-----*")
    mycursor.close()

#TO SEARCH FOR THE RECORDS OF A DONOR USING THE DONOR ID ENTERED BY THE USER

def search_id(DID):
    mycursor=myconnect.cursor()
    query=("SELECT* FROM DONOR WHERE Donor_ID=%s")
    mycursor.execute(query,(DID,))
    mydata=mycursor.fetchall()
    for line in mydata:
        print("*----------*----------*---------*--------*---------*")
        print("Donor_ID:",line[0])
        print("Name:",line[1])
        print("Age:",line[2])
        print("Organ Donated:",line[3])
        print("Blood_group:",line[4])
        print("Date_Donated:",line[5])
        print("*---------*--------*---------*-------*---------*-----*")
    mycursor.close()




#TO UPDATE THE ORGAN REQUIREMENT AND BLOOD GROUP OF THE DONOR USING THE DONOR ID 

def update_organ(DID,org,bgroup):
    mycursor=myconnect.cursor()
    query="UPDATE DONOR SET ORGAN_DONATED=%s,Blood_group=%s WHERE Donor_ID=%s"
    mycursor.execute(query,(org,bgroup,DID))
    print("UPDATED!!!")
    myconnect.commit()
    mycursor.close()



#TO DELETE THE RECORDS OF A DONOR USING THE DONOR ID ENTERED BY THE USER 

def del_donor(DID):
    flag=0
    mycursor=myconn.cursor()
    while True:
        flag=1
        query=("DELETE FROM DONOR WHERE Donor_ID=%s")
        mycursor.execute(query,(DID,))
        myconn.commit()
    if flag ==1:
        print("RECORDS OF THE DONOR WITH DONOR ID ",DID," HAS BEEN DELETED")
    else:
        print("RECORD OF THE DONOR WITH DONOR ID",DID,"NOT FOUND")
    
    mycursor.close()





