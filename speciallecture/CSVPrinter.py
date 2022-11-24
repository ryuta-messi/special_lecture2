import csv


class CSVPrinter:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        with open(self.file_name) as file:
            reader = csv.reader(file)
            lines = [row for row in reader]
        return lines