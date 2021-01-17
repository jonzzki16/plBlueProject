def contact_book_menu():
    dashes = "-"
    title = " CONTACT BOOK MENU "
    print("||            {:15}            ||".format(dashes * 25+title+dashes * 25))
    print("||          {:10}|   {:9}   |   {:10}   |   {:10}   |   {:10}         ||".format("ADD [a]", "VIEW [v]",
                                                                                            "MODIFY [m]", "DELETE [d]",
                                                                                            "EXIT [x]"))
    print("|| {:1} ||".format(dashes * 91))

    cb_menu = input("Please select task >> ")
    if cb_menu.upper() == "X":
        exit("Thank you, always update your contacts and keep in touch!")
    elif cb_menu.upper() == "A":
        cb_add_modify()
    elif cb_menu.upper() == "V":
        cb_view_menu()
    elif cb_menu.upper() == "M":
        cb_modify()
    elif cb_menu.upper() == "D":
        cb_delete()
    else:
        print('''
Invalid keyword, choose only from menu!
        ''')

    contact_book_menu()


def cb_add_modify():
    f_name = input("First Name: ")
    l_name = input("Last Name: ")
    import os
    if os.path.exists(f_name+" "+l_name+".txt"):
        print("Contact name exists, do you want to overwrite it?")
        overwrite = input("Yes [Y] or No [N]")
        if overwrite.upper() == "Y":
            mid_name = input("Middle Name: ")
            m_number = input("Mobile Number: ")
            department = input("Department: ")
            email_add = input("Email Address: ")
            lines = [f_name, mid_name, l_name, department, m_number, email_add]
            with open(f_name+" "+l_name+'.txt', "w") as file_handler:
                for line in lines:
                    file_handler.write(f'{line}\n')
            file_handler.close()
            print("Contact data is modified!")
            contact_book_menu()
        elif overwrite.upper() == "N":
            contact_book_menu()

    else:
        mid_name = input("Middle Name: ")
        m_number = input("Mobile Number: ")
        department = input("Department: ")
        email_add = input("Email Address: ")
        lines = [f_name, mid_name, l_name, department, m_number, email_add]
        with open(f_name+" "+l_name+'.txt', "w") as file_handler:
            for line in lines:
                file_handler.write(f'{line}\n')
        file_handler.close()
        print(f_name+" "+l_name+" is added!")
        contact_book_menu()

    contact_book_menu()


def cb_search():
    f_name = input("First Name: ")
    l_name = input("Last Name: ")
    name_search = open(f_name+" "+l_name+".txt", "r")
    if name_search.mode == 'r':
        contents = name_search.readlines()
        print("{}{}{}{}{}{}".format("NAME: ", (contents[0]), "Middle Name: ", (contents[1]), "Last Name: ", (contents[2])), end="")
        print("{}{}".format("DEPARTMENT: ", contents[3]), end=" ")
        print("{}{}".format("CONTACT NUMBER: ", contents[4]), end=" ")
        print("{}{}".format("EMAIL ADDRESS: ", contents[5]), end=" ")

    contact_book_menu()


def cb_directory():
    import fnmatch
    import os

    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.txt'):
            print(file)


def cb_modify():
    import os
    f_name = input("First Name: ")
    l_name = input("Last Name: ")
    if os.path.exists(f_name+" "+l_name+".txt"):
        mid_name = input("Middle Name: ")
        m_number = input("Mobile Number: ")
        department = input("Department: ")
        email_add = input("Email Address: ")
        lines = [f_name, mid_name, l_name, department, m_number, email_add]
        with open(f_name+" "+l_name+'.txt', "w") as file_handler:
            for line in lines:
                file_handler.write(f'{line}\n')
        file_handler.close()
        print("Contact data is modified!")
        contact_book_menu()
    else:
        print("Contact does not exists!")
        contact_book_menu()


def cb_view_menu():
    category = input("Search by name, Press [N]. View entire directory, Press [D]")
    if category.upper() == "N":
        cb_search()
    elif category.upper() == "D":
        cb_directory()
    else:
        cb_view_menu()


def cb_delete():
    import os
    f_name = input("First Name: ")
    l_name = input("Last Name: ")
    if os.path.exists(f_name+" "+l_name+".txt"):
        os.remove(f_name+" "+l_name+".txt")
    else:
        print("The file does not exist")

    contact_book_menu()


while True:
    try:
        contact_book_menu()
    except FileNotFoundError:
        print("Name is not in the Directory")
        contact_book_menu()
