"""
@author Aditya Kulkarni
class Fraction creates a fraction using 2 numbers passed into the function
It has methods to perform basic arithmetic operations on it, check for equality and 1 Dunder method to print the fraction
"""

from typing import Dict


class Fraction:
    """Creates fraction objects and allows addition, subtraction, multiplication, division and equality check between
    two objects"""
    def __init__(self, numerator: float, denominator: float) -> None:
        """
        Stores
        :param numerator:
        :param denominator:
        checks for denominator input an throws error if it's 0
        """
        self.numerator: float = numerator
        if denominator == 0:
            raise ValueError("Denominator can't be zero")
        else:
            self.denominator: float = denominator

    def __str__(self) -> str:
        """Prints the attributes of the respective object"""
        return f"{self.numerator}/{self.denominator}"

    def plus(self, other: "Fraction") -> "Fraction":
        """Performs addition of the object passed with the object calling the function"""
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)
        else:
            new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            return Fraction(new_numerator, self.denominator * other.denominator)

    def minus(self, other: "Fraction") -> "Fraction":
        """Performs subtraction of the object passed with the object calling the function"""
        if self.denominator == other.denominator:
            return Fraction(self.numerator - other.numerator, self.denominator)
        else:
            new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
            return Fraction(new_numerator, self.denominator * other.denominator)

    def times(self, other: "Fraction") -> "Fraction":
        """Performs multiplication of the object passed with the object calling the function"""
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def divide(self, other: "Fraction") -> "Fraction":
        """Performs division of the object passed with the object calling the function"""
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def equal(self, other: "Fraction") -> bool:
        """Check if the object calling and the one passed are equal"""
        if self.numerator * other.denominator == self.denominator * other.numerator:
            return True
        else:
            return False


def test_suite() -> None:
    """Test the Fraction class and it's methods"""
    f12: Fraction = Fraction(1, 2)
    print(f"f12 = {f12}")
    f24: Fraction = Fraction(2, 4)
    print(f"f24 = {f24}")
    f57: Fraction = Fraction(5, 7)
    print(f"f57 = {f57}")
    print(f"{f12} + {f24} = {f12.plus(f24)} [8/8]")
    print(f"{f57} - {f24} = {f57.minus(f24)} [6/28]")
    print(f"{f12} * {f24} / {f57} = {f12.times(f24).divide(f57)} [14/40]")
    print(f"{f12} + {f24} + {f57} = {f12.plus(f24).plus(f57)} [96/56]")
    f12_new: Fraction = Fraction(1, 2)
    print(f"{f12} == {f12_new} is {f12.equal(f12_new)} [True]")


def get_fraction(display_str: str) -> "Fraction":
    """Helper function to take user input properly"""
    while True:
        try:
            numerator: float = float(input(f"{display_str} numerator "))
            denominator: float = float(input(f"{display_str} denominator "))
        except ValueError as e:
            print(f"Please enter a number: {e}")
        else:
            try:
                fraction: Fraction = Fraction(numerator, denominator)
            except ValueError as ve:
                print(ve)
            else:
                return fraction


def main() -> None:
    """Takes in 2 fraction from user and performs the given operation by the user"""
    operation_map: Dict[str, str] = {'+': 'plus', '-': 'minus', '*': 'times',
                                     '/': 'divide', '=': 'equal'}
    f1: Fraction = get_fraction("For first fraction enter")
    while True:
        try:
            operator: str = input("Choose your operation (+, -, *, /, =) ")
        except KeyError:
            print("Please enter one of the specified operator")
        else:
            break
    f2: Fraction = get_fraction("For second fraction enter")
    print(f"{f1} {operator} {f2} = {getattr(f1, operation_map[operator])(f2)}")


if __name__ == '__main__':
    test_suite()
    main()
