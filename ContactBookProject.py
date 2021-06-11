import os
import fnmatch


def contact_book_menu():
    dashes = "-"
    title = " CONTACT BOOK MENU "
    print("||            {:15}            ||".format(dashes * 25 + title + dashes * 25))
    print("||    {:10}|   {:9}  |   {:9}   |   {:10}   |   {:8}   |   {:7}   ||".format("ADD [1]", "VIEW [2]",
                                                                                        "MODIFY [3]", "DELETE [4]",
                                                                                        "HELP [5]", "EXIT [6]"))
    print("|| {:1} ||".format(dashes * 91))
    print("", end='\n')

    cb_menu = input("Please Select Key Number >>  ")
    print("", end='\n')

    if cb_menu == "6":
        exit("Thank you, always update your contacts and keep in touch!")
    elif cb_menu == "1":
        cb_add_new()
    elif cb_menu == "2":
        cb_view_menu()
    elif cb_menu == "3":
        cb_modify()
    elif cb_menu == "4":
        cb_delete()
    elif cb_menu == "5":
        cb_help()

    else:
        print('''
Invalid Key Number, choose only from the menu!
        ''')

    print("", end='\n')


def cb_view_menu():
    category = input("""
Search by name ---------->  Press [1]
View entire directory---->  Press [2]
""")

    if category == "1":
        cb_search_name()
    elif category == "2":
        cb_view_directory()
    else:
        cb_view_menu()


def cb_add_new():
    l_name = input("Last Name: ")
    f_name = input("First Name: ")
    if os.path.exists(l_name + " " + f_name + ".txt"):
        print("Contact name exists, do you want to overwrite it?")
        overwrite = input("Yes, Press [1]. If No, Press [2]")

        if overwrite == "1":
            print("", end='\n')
            f_name_change = input("Enter New First Name: ")
            l_name_change = input("Enter New Last Name: ")
            mid_name_change = input("Middle Name: ")
            m_number_change = input("Mobile Number: ")
            dept_change = input("Department: ")
            email_add_change = input("Email Address: ")
            lines = [f_name_change, mid_name_change, l_name_change, dept_change, m_number_change, email_add_change]
            with open(l_name + " " + f_name + '.txt', "w") as file_handler:
                for line in lines:
                    file_handler.write(f'{line}\n')
            file_handler.close()

            print("", end='\n')
            print(l_name+", "+f_name+" "+mid_name_change[0]+". data overwritten!")

            print("", end='\n')

            os.rename(l_name + " " + f_name + ".txt", l_name_change + " " + f_name_change + '.txt')

        elif overwrite == "2":
            print("", end='\n')

    else:
        mid_name = input("Middle Name: ")
        m_number = input("Mobile Number: ")
        department = input("Department: ")
        email_add = input("Email Address: ")
        lines = [f_name, mid_name, l_name, department, m_number, email_add]
        with open(l_name + " " + f_name + '.txt', "w") as file_handler:
            for line in lines:
                file_handler.write(f'{line}\n')
        file_handler.close()
        print("", end='\n')
        print(l_name + ", " + f_name + " " + mid_name[0] + ". is added!")
        print("", end='\n')


def cb_search_name():
    l_name = input("Last Name: ")
    f_name = input("First Name: ")
    name_search = open(l_name + " " + f_name + ".txt", "r")
    if name_search.mode == 'r':
        contents = name_search.readlines()
        print("", end='\n')
        print("------------ Contact information -------------")
        print("", end='\n')
        print("{}{}".format(" FIRST NAME:     ", contents[0][0:]), end=" ")
        print("{}{}".format("MIDDLE NAME:    ", contents[1][0:]), end=" ")
        print("{}{}".format("LAST NAME:      ", contents[2][0:]), end=" ")
        print("{}{}".format("DEPARTMENT:     ", contents[3][0:]), end=" ")
        print("{}{}".format("CONTACT NUMBER: ", contents[4][0:]), end=" ")
        print("{}{}".format("EMAIL ADDRESS:  ", contents[5][0:]), end=" ")
        print("", end='\n' * 2)


def cb_view_directory():
    print("", end='\n')
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.txt'):
            print(file)
    print("", end='\n')
    print("Total contacts in the directory: ", len(fnmatch.filter(os.listdir('.'), '*.txt')))
    print("", end='\n')


def cb_modify():
    l_name = input("Last Name: ")
    f_name = input("First Name: ")
    if os.path.exists(l_name + " " + f_name + ".txt"):
        modify_key = input("""

Enter key number to modify field
First Name   : [1]
Middle Name  : [2]
Last Name    : [3]
Department   : [4]
Mobile Number: [5]
Email Address: [6]
""")
        with open(l_name + " " + f_name + ".txt", 'r') as file:
            # read a list of lines into data
            contact_data = file.readlines()

            f_name_details = " First Name:     " + contact_data[0]
            m_name_details = "Middle Name:    " + contact_data[1]
            l_name_details = "Last Name:      " + contact_data[2]
            dept_details = "Department:     " + contact_data[3]
            contact_details = "Contact Number: " + contact_data[4]
            email_add_details = "Email Address:  " + contact_data[5]

        if modify_key == "1":
            f_name_change = input("Enter New First Name: ")

            print(f_name_details, end=" ")
            print(m_name_details, end=" ")
            print(l_name_details, end=" ")
            print(dept_details, end=" ")
            print(contact_details, end=" ")
            print(email_add_details, end=" ")

            contact_data[0] = f_name_change + '\n'
            # write everything back
            with open(l_name + " " + f_name + ".txt", 'w') as file:
                file.writelines(contact_data)

            print("", end='\n' * 2)
            print("First name changed to ", contact_data[0])
            print("", end='\n')

            os.rename(l_name + " " + f_name + ".txt", l_name + " " + f_name_change + '.txt')

            cb_modify_another()

        elif modify_key == "2":
            m_name_change = input("Enter New Middle Name: ")

            print(f_name_details, end=" ")
            print(m_name_details, end=" ")
            print(l_name_details, end=" ")
            print(dept_details, end=" ")
            print(contact_details, end=" ")
            print(email_add_details, end=" ")

            contact_data[1] = m_name_change + '\n'

            # write everything back
            with open(l_name + " " + f_name + ".txt", 'w') as file:
                file.writelines(contact_data)

            print("", end='\n' * 2)
            print("Middle name changed to ", contact_data[1])
            print("", end='\n')

            cb_modify_another()

        elif modify_key == "3":
            l_name_change = input("Enter New Last Name: ")

            print(f_name_details, end=" ")
            print(m_name_details, end=" ")
            print(l_name_details, end=" ")
            print(dept_details, end=" ")
            print(contact_details, end=" ")
            print(email_add_details, end=" ")

            contact_data[2] = l_name_change + '\n'

            # write everything back
            with open(l_name + " " + f_name + ".txt", 'w') as file:
                file.writelines(contact_data)

            print("", end='\n' * 2)
            print("Last name changed to ", contact_data[2])
            print("", end='\n')

            os.rename(l_name + " " + f_name + ".txt", l_name_change + " " + f_name + '.txt')

            print("", end='\n')
            cb_modify_another()

        elif modify_key == "4":
            department_transfer = input("Transfer to Department: ")
            print(f_name_details, end=" ")
            print(m_name_details, end=" ")
            print(l_name_details, end=" ")
            print(dept_details, end=" ")
            print(contact_details, end=" ")
            print(email_add_details, end=" ")

            contact_data[3] = department_transfer + '\n'

            # write everything back
            with open(l_name + " " + f_name + ".txt", 'w') as file:
                file.writelines(contact_data)

            print("", end='\n' * 2)
            print("Transferred to ", contact_data[3], " Department")
            print("", end='\n')

            cb_modify_another()

        elif modify_key == "5":

            contact_num_change = input("Enter New Contact Number: ")
            print(f_name_details, end=" ")
            print(m_name_details, end=" ")
            print(l_name_details, end=" ")
            print(dept_details, end=" ")
            print(contact_details, end=" ")
            print(email_add_details, end=" ")

            contact_data[4] = contact_num_change + '\n'

            # write everything back
            with open(l_name + " " + f_name + ".txt", 'w') as file:
                file.writelines(contact_data)

            print("", end='\n' * 2)
            print("Contact number updated to ", contact_data[4])
            print("", end='\n')

            cb_modify_another()

        elif modify_key == "6":
            change_email_add = input("Enter New Email Address: ")

            print(f_name_details, end=" ")
            print(m_name_details, end=" ")
            print(l_name_details, end=" ")
            print(dept_details, end=" ")
            print(contact_details, end=" ")
            print(email_add_details, end=" ")

            contact_data[5] = change_email_add + '\n'

            # write everything back
            with open(l_name + " " + f_name + ".txt", 'w') as file:
                file.writelines(contact_data)

            print("", end='\n' * 2)
            print("Email Address updated to ", contact_data[5])
            print("", end='\n')

            cb_modify_another()

    else:
        print("", end='\n')
        print("Contact does not exists, do you want to create it?")
        create = input("To create, Press [1] or hit the [ ENTER ] key to go back to the Main Menu")
        print("", end='\n' * 2)

        if create == "1":
            print("", end='\n')
            cb_add_new()
        else:
            print("", end='\n')


def cb_modify_another():
    print("", end='\n')
    modify_another = input("Modify another data, Press [1]. Go back to Main menu, Press [2]")
    if modify_another == "1":
        print("", end='\n')
        cb_modify()
    elif modify_another == "2":
        print("", end='\n')
    else:
        print("Wrong selection, try again!")
        print("", end='\n')
        cb_modify_another()


def cb_delete():
    l_name = input("Last Name: ")
    f_name = input("First Name: ")
    if os.path.exists(l_name + " " + f_name + ".txt"):
        os.remove(l_name + " " + f_name + ".txt")
        print(l_name + " " + f_name + " is deleted!")
    else:
        print("", end='\n')
        print("The file does not exist")

    print("", end='\n')


def cb_help():
    print(
        """     This contact book is dedicated for use by the Bosconians, Administration, Faculty, and Staff
of Don Bosco Technical College, Mandaluyong City. 

Upon using this program, user's agreed to the collection of personal pieces of information, such as Complete Name,
Contact Numbers, and Email Addresses.

   ----------------------------       
   About the Contact Book Menu: 
   ----------------------------   

      ADD    [1] - To create new contact. If contact exists, it will let the user's to overwrite exiting information.
      VIEW   [2] - Selecting View [2], proceeds to select between Search by Names or 
                                       View all the Contact list in the directory                       
      MODIFY [3] - Lets the user's to change the selected entries in the Contact Book
      DELETE [4] - This will delete a single contact in the directory
      HELP   [5] - Program guides and documentations
      EXIT   [6] - Closes the program

   ------------------------------------
      Created by: TeamBlue AY:2020-2021 
                  Jonald J. Anda - Team Leader/Project Engineer
                  Andrew Nazreth P. Conti - Co-Project Engineer
                  Markus Kyle Malicdem Realin - Rapporteur

      Program manuals:
      Tutorial on how to use the program:           
      """)


while True:
    try:
        contact_book_menu()

    except FileNotFoundError:
        print("", end='\n')
        print("Name is not in the Directory")
        print("", end='\n')
    except OSError:
        print("", end='\n')
        print("No names entered, Try again!")
        print("", end='\n')
