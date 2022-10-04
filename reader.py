import csv

def read_file(filePath):
    reader = csv.reader(open(filePath))

    result = {}
    for row in reader:
        key = row[0]
        if key in result:
            # implement your duplicate row handling here
            pass
        result[key] = row[1:]
    print(result)

    return result
    # with open(filePath, 'r') as file:
    #     reader = csv.reader(file)
    #     for row in reader:
    #         print(row)

    # return data;