"""
Test script for anagram, alphabet count and weblogs analyzer functions
"""

import unittest
from typing import List, Tuple, Set
from string import ascii_lowercase as alpha
from HW07_Aditya_Kulkarni import anagrams_cntr, anagrams_lst, anagrams_dd, covers_alphabet, web_analyzer


class TestList(unittest.TestCase):
    """
    Class to test functions from HW07 module
    """

    def test_anagram_lst(self):
        """
        Tests anagram_lst function
        """
        self.assertEqual(anagrams_lst("anagram", "nagaram"), True)
        self.assertNotEqual(anagrams_lst("below", "lbow"), True)
        self.assertEqual(anagrams_lst("study", "dusty"), True)
        self.assertEqual(anagrams_lst("", " "), False)
        self.assertNotEqual(anagrams_lst("250", "2250"), True)
        self.assertEqual(anagrams_lst("250", "520"), True)

    def test_anagrams_dd(self):
        """
        Tests anagrams_dd function
        """
        self.assertEqual(anagrams_dd("anagram", "nagaram"), True)
        self.assertNotEqual(anagrams_dd("below", "lbow"), True)
        self.assertEqual(anagrams_dd("study", "dusty"), True)
        self.assertEqual(anagrams_dd("", " "), False)
        self.assertNotEqual(anagrams_dd("250", "2250"), True)
        self.assertEqual(anagrams_dd    ("250", "520"), True)

    def test_anagrams_cntr(self):
        """
        Tests anagrams_cntr function
        """
        self.assertEqual(anagrams_cntr("anagram", "nagaram"), True)
        self.assertNotEqual(anagrams_cntr("below", "lbow"), True)
        self.assertEqual(anagrams_cntr("study", "dusty"), True)
        self.assertEqual(anagrams_cntr("", " "), False)
        self.assertNotEqual(anagrams_cntr("250", "2250"), True)
        self.assertEqual(anagrams_cntr("250", "520"), True)

    def test_covers_alphabet(self):
        """
        Tests covers_alphabet function
        """
        self.assertEqual(covers_alphabet("AaBbCcDdeEfFgGhHiIJjkKlLmMnNoOPpQqrRSstTuUVvwWxXyYzZ"), True)
        self.assertEqual(covers_alphabet("We promptly judged antique ivory buckles for the next prize"),
                         covers_alphabet(alpha))
        self.assertNotEqual(covers_alphabet("xyz"), True)
        self.assertEqual(covers_alphabet("aabbcdefghijklmnopqrstuvwxyzzabc"), True)
        self.assertEqual(covers_alphabet("The quick brown fox jumps over the lazy dog"), True)
        self.assertNotEqual(covers_alphabet("abcdefghijklmnopqrstuvwxyz"), False)

    def test_web_analyzer(self):
        """
        Tests web_analyzer function
        """
        web_logs: List[Tuple[str, str]] = [('Nanda', 'google.com'), ('Maha', 'google.com'), ('Fei', 'python.org'),
                                           ('Maha', 'google.com'), ('Fei', 'python.org'), ('Nanda', 'python.org'),
                                           ('Fei', 'dzone.com'), ('Nanda', 'google.com'), ('Maha', 'google.com'), ]

        summary: List[Tuple[str, List[str]]] = [('dzone.com', ['Fei']), ('google.com', ['Maha', 'Nanda']),
                                                ('python.org', ['Fei', 'Nanda']), ]
        summary_test: List[Tuple[str, Set[str]]] = [('dzone.com', {'Fei'}), ('google.com', {'Maha', 'Nanda'}),
                                                ('python.org', {'Fei', 'Nanda'}), ]
        self.assertEqual(web_analyzer(web_logs), summary)
        self.assertNotEqual(web_analyzer(web_logs), summary_test)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
