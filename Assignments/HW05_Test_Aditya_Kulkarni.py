"""
@author Aditya A Kulkarni
Tests for functions: reverse, sub_string, find_second, get_lines
"""
import unittest
from typing import List
from HW05_Aditya_Kulkarni import find_second, get_lines, reverse, substring


class TestFunction(unittest.TestCase):
    """Class for testing: reverse, sub_string, find_second, get_lines"""

    def test_reverse(self) -> None:
        """test function for reverse method"""
        self.assertEqual(reverse("abcd"), "dcba")
        self.assertEqual(reverse("level"), "level")
        self.assertNotEqual(reverse("Hello World"), "World Hello")
        self.assertNotEqual(reverse("Hello World"), "dlrow olleh")
        self.assertEqual(reverse("Python is Fun"), "nuF si nohtyP")
        self.assertEqual(reverse(" "), " ")

    def test_substring(self) -> None:
        """test function for sub_string method"""
        self.assertEqual(substring("abc", "abcdefghi"), 0)
        self.assertEqual(substring("abc", "aabcdefghi"), 1)
        self.assertEqual(substring("abc", "aAbcdefghi"), -1)
        self.assertEqual(substring("abcef", "aabcdefghi"), -1)
        self.assertEqual(substring("a bc", "abbbaca bcdefghi"), 6)
        self.assertEqual(substring(" ", "lmn op"), 3)
        self.assertEqual(substring(" ", "lmnop"), -1)

    def test_find_second(self) -> None:
        """test function for find_second method"""
        self.assertEqual(find_second("abba", "abbabba"), 3)
        self.assertEqual(find_second("a", "aababba"), 1)
        self.assertEqual(find_second(" ", "abb ab ba"), 6)
        self.assertEqual(find_second(" ", "abb ab ba"), 6)
        self.assertEqual(find_second(" ", "abcde"), -1)

    def test_get_lines(self) -> None:
        """test function for get_lines method"""
        file_name: str = "C:\\Users\\rajek\\PycharmProjects\\untitled\\test_file.txt"
        expect: List[str] = ['This is line one', 'Line \\ 2 ','',
                             'continued line 2 after blank line ', '                   Line with blank space',
                             '                   ']
        unexpected: List[str] = ['This is line one', 'Line 2 continued line 2 ', 'Line with blank space']
        result: List[str] = list(get_lines(file_name))
        self.assertEqual(expect, result)
        self.assertNotEqual(unexpected, result)
