from SubmissionProject.duplicate_check import duplicate_check
import csv
contact_list = []
def add_contactinf(csvData):
    #print(csvData)
    try:
        Name    = str(input("Enter Contact Name: "))
        Email   = input("Enter Email: ")
        PhoneNumber   = int (input("Enter Phone Number: "))
        Address = input("Enter Address: ")
        contact_dtls = {"Name" : Name, "Email" : Email, "PhoneNumber" : PhoneNumber, "Address" : Address}
        duplicate_status = duplicate_check(csvData, str(PhoneNumber))
        if((duplicate_status) == False):
            contact_list.append(contact_dtls)
            with open("contact_list.csv", mode="a", newline="") as contact_file:
                writer = csv.DictWriter(contact_file, fieldnames=["Name", "Email", "PhoneNumber", "Address"])
                if (len(csvData) == 0):
                    writer.writeheader()  # Write column headers
                writer.writerows(contact_list)

                csvData["Name"].append(Name)
                csvData["Email"].append(Email)
                csvData["PhoneNumber"].append(PhoneNumber)
                csvData["Address"].append(Address)
        else: print("The phone number already exists")
        #return contact_dtls
    except ValueError as e:
        print("Please provide a valid data")
        add_contactinf(csvData)
    except Exception as e:
        print(f"Somee problem arrise {e}")
        add_contactinf(csvData)




