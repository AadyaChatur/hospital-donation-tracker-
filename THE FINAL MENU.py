import PATIENT_FILE
import DONOR_FILE
import HOSPITAL
def main():
    ans = 'y'
    while ans.lower() == 'y':
        print(''' WELCOME TO श्रद्धया देयम् FOUNDATION SOFTWARE ASSISTANT
          HOW ARE YOU (GOOD/BAD) ?''')
        print('''THIS ALL WHAT YOU CAN DO :
              MAINPULATE ANY OF THE FOLOWING RECORDS 

              1)PATIENT RECORDS
              2)DONOR RECORDS
              3)HOSPITAL RECORDS ''')
        
        choice = int(input("Enter your choice\t"))
        
        print('''ALL SET ENTER YOUR CHOICE AND HERE WE GOOO!!''')
        
        if choice == 1:
            print("THIS WHAT YOU CAN DO WITH THE PATIENT RECORDS : ")
            print("1. DISPLAY ALL THE SAVED RECORDS OF THE PATIENTS UNDER TREATMENT")
            print("2. ADD NEW DATA INTO THE PATIENT RECORDS")
            print("3. SEARCH FOR THE RECORDS OF A PATIENT USING THE NAME ENTERED BY THE USER")
            print("4. SEARCH FOR THE RECORDS OF A PATIENT USING THE PATIENT ID ENTERED BY THE USER")
            print("5. UPDATE THE ORGAN REQUIREMENT AND BLOOD GROUP OF THE PATIENT USING THE PATIENT ID")
            print("6. DELETE THE RECORDS OF A PATIENT USING THE PATIENT ID ENTERED BY THE USER")
            print("7. EXIT")
            user_choice=int(input("Enter your choice: "))
            if user_choice==1:
                PATIENT_FILE.show_patient()
            elif user_choice==2:
                PATIENT_FILE.add_patient()
            elif user_choice==3:
                pname=input("ENTER NAME OF THE PATIENT IN THE FOLLOWING FORMAT 'Name'  ")
                PATIENT_FILE.search_patient(pname)
            elif user_choice==4:
                pID=int(input("ENTER PATIENT ID YOU WOULOD LIKE TO SEARCH FOR: "))
                PATIENT_FILE.search_Patient_id(pID)
            elif user_choice==5:
                ido=int(input("ENTER PATIENT ID YOU WOULD LIKE TO UPDATE DATA OF :"))
                neworg=input("ENTER THE UPDATION ORGAN:")
                PATIENT_FILE .update_organ(ido , neworg)
            elif user_choice==6:
                pID=int(input("ENTER PATIENT ID YOU WOULOD LIKE DELETE RECORD OF : "))
                PATIENT_FILE .del_patient(pID)
            elif user_choice==7:
                break

        elif choice == 2:
            print("THIS WHAT YOU CAN DO WITH THE DONOR RECORDS : ")
            print("1. DISPLAY ALL THE SAVED RECORDS OF THE ORGAN DONATIONG DONORS")
            print("2. ADD NEW DATA INTO THE DONOR FILE")
            print("3. SEARCH FOR THE RECORDS OF A DONOR USING THE NAME ENTERED BY THE USER")
            print("4. SEARCH FOR THE RECORDS OF A DONOR USING THE DONOR ID ENTERED BY THE USER")
            print("5. UPDATE THE ORGAN REQUIREMENT AND BLOOD GROUP OF THE DONOR USING THE DONOR ID")
            print("6. DELETE THE RECORDS OF A DONOR USING THE DONOR ID ENTERED BY THE USER ")
            print("7. EXIT")
            
            user_choice=int(input("Enter your choice: "))
            if user_choice==1:
                DONOR_FILE.show_donor()
            elif user_choice==2:
                DONOR_FILE.add_donor()
            elif user_choice==3:
                name=input("ENTER THE NAME OF THE DONOR YOU WOULD LIKE TO SEARCH FOR :")
                DONOR_FILE.search_donor(name)
            elif user_choice==4:
                ip=int(input("ENTER THE ID OF THE PATIENT YOU WOULD LIKE TO SEARCH FOR :"))
                DONOR_FILE.search_id(ip)
            elif user_choice==5:
                dID=int(input("ENTER DONOR ID YOU WOULOD LIKE TO UPDATE RECORD OF : "))
                org=input("ENTER NEW ORGAN RECORD")
                bgroup=input("ENTER NEW BLOOD GROUP RECORD ")
                DONOR_FILE.update_organ(dID,org,bgroup)

            elif user_choice==6:
                dID=int(input("ENTER DONOR ID YOU WOULOD LIKE TO DELETE RECORD OF : "))
                DONOR_FILE.del_donor(dID)
            elif user_choice==7:
                break
        elif choice == 3:
            print("THIS WHAT YOU CAN DO WITH THE HOSPITAL RECORDS : ")
            print("1. DISPLAY ALL THE SAVED RECORDS OF THE HOSPITALS")
            print("2. ADD NEW DATA INTO THE HOSPITAL FILE")
            print("3. SEARCH FOR THE RECORDS OF A HOSPITAL USING THE NAME ENTERED BY THE USER")
            print("4. SEARCH FOR THE RECORDS OF A HOSPITAL USING THE HOSPITAL ID ENTERED BY THE USER")
            print("5. DELETE THE RECORDS OF A HOSPITAL USING THE HOSPITAL ID ENTERED BY THE USER ")
            print("6. EXIT")
            user_choice=int(input("Enter your choice: "))
            if user_choice==1:
                HOSPITAL.show_hospital()
            elif user_choice==2:
                HOSPITAL.add_hospital()
            elif user_choice==3:
                hame=input("ENTER THE NAME OF THE HOSPITAL YOU WOULD LIKE TO SEARCH FOR ")
                HOSPITAL.search_hospital(hame)
            elif user_choice==4:
                ID=int(input("ENTER THE HOSPITAL ID YOU WOULD LIKE TO SEACH FOR "))
                HOSPITAL.search_id(ID)
            elif user_choice==5:
                ID=int(input("ENTER HOSPITAL ID YOU WOULOD LIKE DELETE RECORD OF : "))
                HOSPITAL.del_hose(ID)
            elif user_choice==6:
                break


        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

        
        ans = input("Do you want to continue? y/n")

if __name__ == "__main__":
    main()
