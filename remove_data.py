from SubmissionProject.duplicate_check import duplicate_check
def remove_dta(csvData):
    phone_number = input("Provide phone number to remove the data: ")
    is_present = duplicate_check(csvData, str(phone_number))

    if (is_present== True):
        phone_list = csvData["PhoneNumber"] #(phone_number)
        indx = phone_list.index(str(phone_number))
        headers = list(csvData.keys())
        for header in headers:
            del (csvData[header][indx])
        print("Successfully remove.")
    else:
        print("Sorry! no such record.")

