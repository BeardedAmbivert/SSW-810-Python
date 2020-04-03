"""Test Case Suit for List operations in Python"""

import unittest
from HW06_Aditya_Kulkarni import list_copy, list_intersect, list_difference, remove_vowels, check_pwd, DonutQueue


class TestUtility(unittest.TestCase):
    """Test case Class for List Copy"""

    def test_list_copy(self):
        """Test case function for list copy"""
        self.assertEqual((['LP', 'ID']), list_copy(['LP', 'ID']))
        self.assertEqual((["", ""]), list_copy(["", ""]))
        self.assertEqual((["", ""]), list_copy(["", ""]))
        self.assertEqual([], list_copy([]))
        self.assertNotEqual([], list_copy([""]))
        self.assertNotEqual(["1", 2, "3"], list_copy(["1", 2, 3]))

    def test_list_intersect(self):
        """Testing list_intersect function """
        self.assertEqual(list_intersect([1, 2, 3], [1, 3, 5]), [1, 3])
        self.assertNotEqual(list_intersect([3], [2, 4]), [3])
        self.assertEqual(list_intersect([], []), [])
        self.assertNotEqual(list_intersect([1, 2, 3], []), [1])
        self.assertEqual(list_intersect([1], []), [])

    def test_list_difference(self):
        """Testing list_difference function"""
        self.assertEqual(list_difference([1, 2, 3], [1, 3, 5]), [2])
        self.assertNotEqual(list_difference([3], [2, 4]), [2, 3, 4])
        self.assertEqual(list_difference([], []), [])
        self.assertNotEqual(list_difference([1, 2, 3], []), [1])
        self.assertEqual(list_difference([1], []), [1])

    def test_remove_vowels(self):
        """Testing remove vowels"""
        self.assertEqual("Hello World", remove_vowels("Hello World"))
        self.assertEqual("my favorite daughter", remove_vowels("Amy is my favorite daughter"))
        self.assertNotEqual("Amy is my favorite daughter", remove_vowels("my daughter"))
        self.assertEqual("", remove_vowels("Amy"))

    def test_check_pwd(self):
        """Testing check_pwd function"""
        self.assertEqual(check_pwd("1ARnold"), True)
        self.assertEqual(check_pwd("oOps"), False)
        self.assertEqual(check_pwd("12345ZZZ"), False)
        self.assertEqual(check_pwd("12345ZZZaa"), True)
        self.assertEqual(check_pwd(" "), False)
        self.assertEqual(check_pwd(""), False)


class DonutQueueTest(unittest.TestCase):
    """Test Case Class For Donut Queue"""

    def test_queue(self):
        """Test case function for donut queue class"""
        dq = DonutQueue()
        self.assertIsNone(dq.next_customer())
        dq.arrive("Sujit", False)
        dq.arrive("Fei", False)
        dq.arrive("Prof JR", True)
        self.assertEqual(dq.waiting(), "Prof JR, Sujit, Fei")
        dq.arrive("Nanda", True)
        self.assertEqual(dq.waiting(), "Prof JR, Nanda, Sujit, Fei")
        self.assertEqual(dq.next_customer(), "Prof JR")
        self.assertEqual(dq.next_customer(), "Nanda")
        self.assertEqual(dq.next_customer(), "Sujit")
        self.assertEqual(dq.waiting(), "Fei")
        self.assertEqual(dq.next_customer(), "Fei")
        self.assertIsNone(dq.next_customer())


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
