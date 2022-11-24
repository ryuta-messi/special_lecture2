import unittest
from speciallecture.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):

    def test_read(self):
        printer = CSVPrinter("/home/runner/work/special_lecture2/special_lecture2/tests/sample.csv")
        l = printer.read()
        self.assertEqual(3,len(l))

    def test_read2(self):
        printer = CSVPrinter("/home/runner/work/special_lecture2/special_lecture2/tests/sample.csv")
        line = printer.read()
        self.assertSetEqual("bbb2",line[1][1])

    def test_read3(self):
        try:
            printer = CSVPrinter('/home/runner/work/special_lecture2/special_lecture2/tests/sample.csv')
            printer.read()
            unittest.TestCase.fail("This line should not be invoked")
        except FileNotFoundError as e:
           print('input file does not exist')
