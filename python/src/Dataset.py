import csv

class Dataset:
    
    def __init__(self, filename) -> None:
        self._filename = filename

    def readDataset(self):
        data: list = []
        with open(self._filename, newline = '') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=' ')
            for row in csv_reader:
                for field in row:
                    data.append(field.split(','))
            data = [float(j) for i in data for j in i]
        return data
        