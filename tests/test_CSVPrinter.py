import unittest
import sys
sys.path.append('../speciallecture2')
from speciallecture.CSVPrinter import CSVPrinter


class TestCSVPrinter(unittest.TestCase):

    def test_read(self):
        printer = CSVPrinter("./tests/sample.csv")
        l = printer.read()
        self.assertEqual(3, len(l))

    def test_read2(self):
        printer = CSVPrinter("./tests/sample.csv")
        line = printer.read()
        self.assertEqual("aaa1", line[0][0])

    def test_read3(self):
        try:
            printer = CSVPrinter('./tests/sample2.csv')
            printer.read()
            unittest.TestCase.fail("This line should not be invoked")
        except FileNotFoundError as e:
            print('input file does not exist')
