def header():
    header_message = ('''~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~~=~=~=~=~=~=~=~=~=~=~=~~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
    ||   J. Anda- Lead, A.N. Conti- Proj. Engr., M.K. Realin - Rapporteur                BES241    ||
    ||   Blue Team - Contact Book                                               October 6, 2020    ||
    ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~~=~=~=~=~=~=~=~=~=~=~=~~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
    ||   
                                                                                              ||''')
    print("||        {:15}|      {:15}     |      {:15}     |   {:10}  ||".format("NAME", "CONTACT NUMBER",
                                                                                  "EMAIL ADDRESS", "DEPARTMENT"))
    print("|| __________________    +    __________________    +    __________________    +    _________  ||")


CB_NameList = {"Jonald Anda": "Jonald Anda"}
CB_Number = {'Jonald Anda': '09365984839'}
CB_Email = {'Jonald Anda': 'jjanda@one-bosco.org'}
CB_Department = {'Jonald Anda': 'BED'}


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
        cb_add()
    elif cb_menu.upper() == "V":
        cb_search()
    elif cb_menu.upper() == "M":
        cb_modify()
    elif cb_menu.upper() == "D":
        cb_delete()
    else:
        print('''
Invalid keyword, choose only from menu!
        ''')
        contact_book_menu()


def cb_add():
    name = input("Name: ")
    number = (input("Number: "))
    email = input("Email: ")
    department = (input("Department: "))
    a = {name: name}
    b = {name: number}
    c = {name: email}
    d = {name: department}
    CB_NameList.update(a)
    CB_Number.update(b)
    CB_Email.update(c)
    CB_Department.update(d)
    print("""
Contact added!
    """)
    contact_book_menu()


def cb_search():
    search_contact = input("Search name: ")
    if search_contact in CB_NameList:

        print("|| {:25} {:5}     {:13}     {:30}  ||".format("NAME", "DEPARTMENT",
                                                             "CONTACT NUMBER", "EMAIL ADDRESS"))
        print("|| __________________        __________     _____________      ______________                  ||")
        print(f"|| {CB_NameList[search_contact]:25}    {CB_Department[search_contact]:5}       "
              f"{CB_Number[search_contact]:13}      {CB_Email[search_contact]:30}  ||")
    else:
        print("Name not found!")
    contact_book_menu()


def cb_modify():
    modify_data = input("""
[N] >> to modify existing contact name
[D] >> to modify existing Contact Digits
[E] >> to modify existing Email Address
[X] >> Back to Main Menu

""")
    if modify_data.upper() == 'N':
        old_name = input("Enter name to change: ")
        if old_name in CB_NameList:
            new_name = input("Enter New Name: ")
            CB_NameList[new_name] = CB_NameList.pop(old_name)
            contact_book_menu()
        else:
            print("Name not f44ound!")
            contact_book_menu()

    elif modify_data.upper() == 'D':
        old_contact_digits = input("Enter Contact Digits to change: ")
        if old_contact_digits in CB_Number:
            new_contact_digits = input("Enter New Name: ")
            a = {old_contact_digits: new_contact_digits}
            CB_Number.update(a)
            for key in a:
                print(f"{old_contact_digits} is changed to {a[key]}")
            contact_book_menu()
        else:
            print("Contact Digits not found!")
            contact_book_menu()
    elif modify_data.upper() == 'E':
        old_email_address = input("Enter Email Address to change: ")
        if old_email_address in CB_Email:
            new_email_address = input("Enter New Email Address: ")
            a = {old_email_address: new_email_address}
            CB_Email.update(a)
            for key in a:
                print(f"{old_email_address} is changed to {a[key]}")
            contact_book_menu()
        else:
            print("Email Address not found!")
            contact_book_menu()
    elif modify_data.upper() == "X":
        contact_book_menu()
    else:
        print("""
Invalid keyword, Try Again!
""")
        cb_modify()


def cb_delete():
    delete_contact = str(input("Enter name to Delete:"))
    if delete_contact in CB_NameList:
        CB_NameList.pop(delete_contact)
        CB_Department.pop(delete_contact)
        CB_Number.pop(delete_contact)
        CB_Email.pop(delete_contact)
        print(f"{delete_contact} is Deleted")
        contact_book_menu()
    else:
        print("Name not found!")
        contact_book_menu()


def try_again():
    repeat = input("    Do you want to try again? [y] / [n] >> ")
    if repeat.upper() == "Y":
        contact_book_menu()
    elif repeat.upper() == "N":
        exit("Always keep in touch!")
    else:
        print("Wrong Input, choose YES [y] / NO [n] >> ")
        try_again()


contact_book_menu()
