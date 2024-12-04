from SubmissionProject.load_data import load_data

def view_data(search_data=''):
    datas = load_data()
    num_rows = len(next(iter(datas.values())))

    headers = list(datas.keys())
    print("\t".join(headers))

    for i in range(num_rows):
        row = [datas[header][i] for header in headers]
        if(search_data != ''):
            is_have = row.count(str(search_data))
            if(is_have):
                print("\t".join(row))
        else:
            print("\t".join(row))