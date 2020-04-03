"""
Test Case module for HW08 functions date_arithmetic, file_reader and class File Analyzer
"""
import unittest
import datetime
from HW08_Aditya_Kulkarni import date_arithmetic, file_reader, FileAnalyzer


class TestFileMod(unittest.TestCase):
    """
    Class for testing functions date_arithmetic, file_reader and class FileAnalyzer
    """

    def test_date_arithmetic(self):
        """test cases for date arithmetic function"""
        self.assertEqual(date_arithmetic(), (datetime.datetime(2000, 3, 1, 0, 0),
                                             datetime.datetime(2017, 3, 2, 0, 0),
                                             241))
        self.assertNotEqual(date_arithmetic(), (datetime.datetime(2010, 3, 1, 0, 0),
                                                datetime.datetime(2020, 3, 2, 0, 0),
                                                -241))

    def test_file_reader(self):
        """test cases for file reader function"""
        file = 'C:\\Users\\rajek\\PycharmProjects\\untitled\\test.csv'
        file1 = 'C:\\Users\\rajek\\PycharmProjects\\untitled\\test1.txt'

        test_op = [['123', 'Jin He', 'Computer Science'],
                   ['234', 'Nanda Koka', 'Software Engineering'],
                   ['345', 'Benji Cai', 'Software Engineering']]
        test_op1 = [['CWID', 'Name', 'Major'],
                    ['123', 'Jin He', 'Computer Science'],
                    ['234', 'Nanda Koka', 'Software Engineering'],
                    ['345', 'Benji Cai', 'Software Engineering']]

        output = list(file_reader(file, 3, header=False))
        output1 = list(file_reader(file1, 3, sep='|', header=True))
        output1_false = list(file_reader(file1, 3, sep='|', header=False))

        self.assertEqual(output, test_op)
        self.assertNotEqual(output, test_op1)
        self.assertEqual(output1, test_op)
        self.assertEqual(output1_false, test_op1)
        self.assertNotEqual(output1, test_op1)
        self.assertNotEqual(output1_false, test_op)

    def test_FileAnalyzer(self):
        """test cases for file analyzer class"""
        f = FileAnalyzer("C:\\Users\\rajek\\Documents\\Assignments")
        self.assertEqual(f.files_summary, {'hello.py': {'class': 0, 'function': 1, 'line': 59, 'char': 443}})

        self.assertNotEqual(f.files_summary, {'hello.py': {'class': 1, 'function': 3, 'line': 58, 'char': 45}})


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
