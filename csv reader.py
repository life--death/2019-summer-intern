import csv
class information():
    def __init__(self, process_name=None, operation=None, path=None, result=None, detail=None):
        if result == 1:
            self.name = process_name
            self.job = operation
            self.path = path
            self.detail = Detail

def reader(name:str):
    result = []
    with open(name, newline='') as csvfile:
        temp = csv.(csvfile, delimiter=' ', quotechar='|')
        for row in temp:
            if result = "success":
                result.append(information(row[0],row[1],row[2],row[3],row[4]))
    return result
