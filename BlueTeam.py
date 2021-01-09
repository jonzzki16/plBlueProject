# Blue team, Andrew Nazreth P. Conti, Jonald J. Anda (CPE). Marcus Kyle Realin (ECE)
print()
print('Contact Book Commands')
print('- Enter "display" - to display a contact information.')
print('- Enter "add" - to add new contact information.')
print('- Enter "change" - to change the the contact information of an existing one.')
print('- Enter "delete" - to delete a contact information.')
print('- Enter "contacts" - to display the contents of the contact book.')
print('- Enter "end" - to exit the program.')
print()
print('For the newly added number just put "0" at the start e.g. (0)9279141839')
print()

Contact_Book_Number = {'Andrew Conti': '09279141839'}  # <- EXAMPLE ONLY
Contact_Book_Email = {'Andrew Conti': 'anconti@donbosco.edu.ph'} # <- EXAMPLE ONLY


def contact():
    while True:
        command = str(input("Enter a Command from the Contact Book Commands:"))
        if command == "display":
            a = input("Enter the name of a personnel in DBTC: ")
            if a in Contact_Book_Number:
                print(f"The contact info of this person is: {Contact_Book_Number[a]},{Contact_Book_Email[a]}")
            else:
                print("name not found! Please try again or enter another command.")
        elif command == "add":
            print("Add a new contact info with the name of the person")
            a = str(input("name: "))
            c = int(input("number: "))
            e = str(input("gmail/email: "))
            b = {a: c}
            d = {a: e}
            Contact_Book_Number.update(b)
            Contact_Book_Email.update(d)
            for key in b:
                print(f"Added person: {key} and New Contact Information: {b[key]},{e}")
        elif command == "change":
            x = str(input("what would you like to change?(number) or (email): "))
            if x == 'number':
                c = str(input("Change Contact Information of a personnel:"))
                if c in Contact_Book_Number:
                    Contact_Book_Number[c] = int(input("New Contact Number:"))
                    print(f"New contact information of {c} is: {Contact_Book_Number[c]}")
                else:
                    print("Name not found! Please try again or enter another command.")
            elif x == 'email':
                c = str(input("Change Contact Information of a personnel:"))
                if c in Contact_Book_Email:
                    Contact_Book_Email[c] = str(input("New Contact gmail/Email:"))
                    print(f"New contact information of {c} is: {Contact_Book_Email[c]}")
                else:
                    print("Name not found! Please try again or enter another command.")
            else:
                print("wrong input try again, use 'number' or 'email'")
        elif command == "delete":
            d = str(input("Delete Contact Information of:"))
            if d in Contact_Book_Number:
                Contact_Book_Number.pop(d)
                Contact_Book_Email.pop(d)
                print(f"the contact information of {d} has been removed/deleted")
            else:
                print("Name not found! Please try again or enter another command.")
        elif command == "contacts":
            print(Contact_Book_Email)
            print(Contact_Book_Number)
        elif command == "end":
            print("Thank You for choosing DBTC! We always do what is best for our bosconian family.")
            exit()

        else:
            print('Please enter the correct command.')


while True:
    try:
        contact()
    except ValueError:
        print("Input must be an integer please try again. Also don't use space.")
