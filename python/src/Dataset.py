import csv


class Dataset:

    def __init__(self, filename) -> None:
        self._filename = '../../data/' + filename

    def read(self):
        data: list = []
        with open(self._filename, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=' ')
            for row in csv_reader:
                for field in row:
                    data.append([float(x) for x in field.split(',')])
        return data
