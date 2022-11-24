import unittest
from speciallecture.CSVPrinter import CSVPrinter


class TestCSVPrinter(unittest.TestCase):

    def test_read(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual(2, len(l))

    def test_read2(self):
        printer = CSVPrinter("sample.csv")
        line = printer.read()
        self.assertSetEqual("aaa1", line[0][0])

    def test_read3(self):
        try:
            printer = CSVPrinter('sample.csv')
            printer.read()
            unittest.TestCase.fail("This line should not be invoked")
        except FileNotFoundError as e:
            print('input file does not exist')
