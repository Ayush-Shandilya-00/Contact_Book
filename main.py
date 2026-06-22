# This is a Project potray Contact_Book based on CRUD(Create,Read,Update,Delete)

Contact_Book ={}
print("─── ✧ CONTACT MANAGER ✧ ───")
print("")
print("    ✦ 1. Add Contact")
print("    ✦ 2. Search Contact")
print("    ✦ 3. Update Contact")
print("    ✦ 4. Delete Contact")
print("    ✦ 5. Quit")
print("")

choice = input("Enter any choice from Menu: ")

while True:
    
    if choice == 1:
        add = str(input("Enter Contact Name: "))
        add1 = int(input("Enter Contact Number: "))
        Contact_Book[add]= add1

        print("─── ✧ CONTACT MANAGER ✧ ───")
        print("")
        print("    ✦ 1. Add Contact")
        print("    ✦ 2. Search Contact")
        print("    ✦ 3. Update Contact")
        print("    ✦ 4. Delete Contact")
        print("    ✦ 5. Quit")
        print("")
        
        choice = input("Enter any choice from Menu: ")
    
    elif choice == 2:
        search_name = input("Enter Contact name to Search: ")

        if search_name in Contact_Book:
            phone = Contact_Book[search_name]
            print(f"Contact Found : Name: {search_name} and NUmber: {phone}")

        else:
            print("Contact Not Found!")

            
        print("─── ✧ CONTACT MANAGER ✧ ───")
        print("")
        print("    ✦ 1. Add Contact")
        print("    ✦ 2. Search Contact")
        print("    ✦ 3. Update Contact")
        print("    ✦ 4. Delete Contact")
        print("    ✦ 5. Quit")
        print("")
        
        choice = input("Enter any choice from Menu: ")

    elif choice ==3:
        print("")
        print("──┤ MENU FOR Update IN CONTACT BOOK ├──")
        print("")
        print("  1) Updating Name of Contact")
        print("  2) Updating Number of the Contact")
        print("")
        choice1= input("Choose any option from Menu for Updating: ")

        if choice1 == "1":
            old_name = input("Enter the current Contact Name: ")
            if old_name in Contact_Book:
                new_name = input("Enter new Name to Update: ")

               
                Contact_Book[new_name] = Contact_Book.pop(old_name)
                print(" Contact Name Updated Successfully!")
            else:
                print(" Contact Name Not Found!")

        elif choice1 == "2":
            search_name = input("Enter the Contact Name to change their number: ")
            if search_name in Contact_Book:
                new_phone = input("Enter new Number to Update: ")


                Contact_Book[search_name] = new_phone
                print(" Contact Number Updated Successfully!")
            else:
                print(" Contact Name Not Found!")
        else:
            print(" Invalid Choice inside Update Menu!")


        print("─── ✧ CONTACT MANAGER ✧ ───")
        print("")
        print("    ✦ 1. Add Contact")
        print("    ✦ 2. Search Contact")
        print("    ✦ 3. Update Contact")
        print("    ✦ 4. Delete Contact")
        print("    ✦ 5. Quit")
        print("")
        
        choice = input("Enter any choice from Menu: ")


    elif choice == 4:
        remove_contact= input("Enter Name of the Contact to Remove: ")

        if remove_contact in Contact_Book:
            del Contact_Book[remove_contact]
            print("Contact Deleted Successfully!") 

        else:
            print("Invalid")
    
        
        print("─── ✧ CONTACT MANAGER ✧ ───")
        print("")
        print("    ✦ 1. Add Contact")
        print("    ✦ 2. Search Contact")
        print("    ✦ 3. Update Contact")
        print("    ✦ 4. Delete Contact")
        print("    ✦ 5. Quit")
        print("")
        
        choice = input("Enter any choice from Menu: ")
    
    elif choice == 5:
        print("!QUIT! Thank you for using Contact Manager.")
        break

    else:
        print("Invaid choice please pick a number from 1 to 5!")
break