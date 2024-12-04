import csv

data_dict = {}
def load_data():
    with open("contact_list.csv", "r") as contact_file:
        datas = csv.DictReader(contact_file)

        for header in datas.fieldnames:
            data_dict[header] = []

        for row in datas:
            for key, value in row.items():
                data_dict[key].append(value)

        return data_dict
