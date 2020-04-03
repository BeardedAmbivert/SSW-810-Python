"""
@author: Aditya Kulkarni
Automated tests for Fraction class
"""

import unittest

from HW03_Aditya_Kulkarni import Fraction


class TestFraction(unittest.TestCase):
    """ test class for Fraction"""

    def test_init(self):
        """testing class constructor"""
        f: Fraction = Fraction(3, 4)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)

    def test_init_exception(self):
        """ check for zero in denominator"""
        with self.assertRaises(ValueError):
            Fraction(3,0)
            Fraction(9,0)
            Fraction(5,-2)
            Fraction(0,-2)
            Fraction(0,0)

    def test_str(self):
        """ verify if the dunder method prints objects as expected """
        f25: Fraction = Fraction(2, -5)
        if f25.denominator < 0:
            self.assertEqual(str(f25), f"{-1 * f25.numerator}/{-1 * f25.denominator}")
        else:
            self.assertEqual(str(f25), f"{f25.numerator}/{f25.denominator}")

    def test_simplify(self):
        """verifies if the Fraction is simplified"""
        self.assertEqual(str(Fraction(9, 27).simplify()), str(Fraction(1, 3)))
        self.assertFalse(str(Fraction(5, 7)) == str(Fraction(4, 12).simplify()))

    def test_add(self):
        """ verify Fraction addition """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 + f34, Fraction(10, 8))
        self.assertEqual(f12, Fraction(1, 2))

    def test_sub(self):
        """ verify fraction subtraction """
        f12: Fraction = Fraction(1, 2)
        f14: Fraction = Fraction(1, 4)
        self.assertEqual(f12 - f14, Fraction(1, 4))

    def test_mul(self):
        """ verify fraction multiplication """
        f25: Fraction = Fraction(2, 5)
        f23: Fraction = Fraction(2, 3)
        self.assertEqual(f23 * f25, Fraction(4, 15))

    def test_div(self):
        """ verify fraction division """
        f25: Fraction = Fraction(2, 5)
        f23: Fraction = Fraction(2, 3)
        self.assertEqual(f23 / f25, Fraction(5, 3))

    def test_equal(self):
        """ verify fraction equality """
        f23: Fraction = Fraction(2,3)
        f25: Fraction = Fraction(2, 5)
        self.assertEqual(f25, f25)
        self.assertFalse(f23 == f25)

    def test_notequal(self):
        """ verify fraction non-equality """
        f23: Fraction = Fraction(2, 3)
        f25: Fraction = Fraction(2, 5)
        self.assertFalse(f23 != f23)
        self.assertNotEqual(f23, f25)

    def test_lessthan(self):
        """ verify if one fraction is less than another """
        f12: Fraction = Fraction(1, 2)
        f23: Fraction = Fraction(2, 3)
        f25: Fraction = Fraction(2, 5)
        self.assertLess(f25, f12)
        self.assertTrue(f12, f25)
        self.assertFalse(f23 < f23)

    def test_lessequal(self):
        """ verify if one fraction is less than or equal to another """
        f12: Fraction = Fraction(1, 2)
        f23: Fraction = Fraction(2, 3)
        f25: Fraction = Fraction(2, 5)
        self.assertLessEqual(f25, f12)
        self.assertLessEqual(f23, f23)
        self.assertFalse(f12 <= f25)

    def test_greatthan(self):
        """ verify if one fraction is greater than another """
        f12: Fraction = Fraction(1, 2)
        f23: Fraction = Fraction(2, 3)
        f25: Fraction = Fraction(2, 5)
        self.assertGreater(f12, f25)
        self.assertFalse(f23 > f23)
        self.assertFalse(f25 > f12)

    def test_greatequal(self):
        """ verify if one fraction is greater than or equal to another """
        f12: Fraction = Fraction(1, 2)
        f23: Fraction = Fraction(2, 3)
        f25: Fraction = Fraction(2, 5)
        self.assertGreaterEqual(f12,f25)
        self.assertGreaterEqual(f23,f23)
        self.assertFalse(f25 >= f12)

    def test_3_operands(self):
        """ verify expressions with more than two operands """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f44: Fraction = Fraction(4, 4)
        self.assertTrue(f12 + f34 + f44 == Fraction(72, 32))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
