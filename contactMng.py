from SubmissionProject.add_contact import add_contactinf
from SubmissionProject.load_data import load_data
from SubmissionProject.view_data import view_data
from SubmissionProject.remove_data import remove_dta

privious_data = []

print("Contact Book Management")
print("_____________________________")
privious_data = load_data()

while True:
    print("To add contact press 'a' ")
    print("To remove contact press 'r' ")
    print("To view contact press 'v' ")
    print("To search contact press 'f' ")
    print("To exit press 'e' ")

    inputStatus = input("Choose an option: ")

    if inputStatus == 'e':
        print("Thank you")
        break

    elif inputStatus == 'a':
        try:
            add_contactinf(privious_data)
            #contact_list.append()
              # Write data rows


        except Exception as e:
            print(e)
    elif inputStatus == 'v':
        try:
            view_data()

        except Exception as e:
            print(e)

    elif inputStatus == 'r':
        try:
            remove_dta(privious_data)

        except Exception as e:
            print(e)

    elif inputStatus == 'f':
        try:
            search_data = input("Which data you want: ")
            view_data(search_data)

        except Exception as e:
            print(e)






