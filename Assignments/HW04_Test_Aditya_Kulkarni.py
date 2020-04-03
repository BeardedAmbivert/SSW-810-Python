"""
@author: Aditya Kulkarni
Automated tests for functions: count_vowels, last_occurrence and generator my_enumerate
"""

import unittest
from typing import List, Any
from HW04_Aditya_Kulkarni import count_vowels, last_occurrence, my_enumerate


class TestFraction(unittest.TestCase):
    """Class for testing count_vowels, last_occurrence functions and my_enumerate generator"""

    def test_count_vowels(self) -> None:
        """test function for count_vowels method"""
        self.assertEqual(count_vowels("Hello World"), 3)
        self.assertNotEqual(count_vowels("Hello World"), 6)
        self.assertNotEqual(count_vowels(""), 3)
        self.assertEqual(count_vowels("qwrtypsdfghjklzxccvbnm"), 0)
        self.assertTrue(count_vowels("aeiou") == 5)
        self.assertFalse(count_vowels("aeiou") == 0)

    def test_last_occurrence(self) -> None:
        """test function for last_occurrence method"""
        self.assertEqual(last_occurrence("h", "Hello World"), None)
        self.assertEqual(last_occurrence("l", "Hello World"), 9)
        self.assertTrue(last_occurrence(" ", "Hello World") == 5)
        self.assertFalse(last_occurrence(" ", "Hello World") == 8)
        self.assertEqual(last_occurrence("  ", "Hello World"), None)

    def test_my_enumerate(self) -> None:
        """test function for my_enumerate generator"""
        word: str = "Bello"
        numbers: List[int] = [1, 2, 3, 4]
        mix: List[Any] = [1, "one", 2, "two"]
        self.assertEqual(list(my_enumerate(word)), list(enumerate(word)))
        self.assertNotEqual(list(my_enumerate(numbers)), list(enumerate(mix)))
        self.assertTrue(list(my_enumerate(numbers)) == list(enumerate(numbers)))
        self.assertFalse(list(my_enumerate(word)) == list(enumerate(mix)))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
