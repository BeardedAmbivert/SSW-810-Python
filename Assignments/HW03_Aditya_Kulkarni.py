"""@author Aditya Kulkarni class Fraction creates a fraction using 2 numbers passed into the function It has methods
to perform basic arithmetic operations on it, check for equality and 1 Dunder method to print the fraction """


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
        self.numerator: float = float(numerator)
        self.denominator: float = float(denominator)
        if denominator == 0:
            raise ValueError("Denominator can't be zero")
        elif denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def simplify(self) -> "Fraction":
        """converts the fraction to it's simplest form """
        num: float = self.numerator
        den: float = self.denominator
        while den:
            num, den = den, num % den
        if num == 1:
            return self
        else:
            return Fraction(self.numerator / num, self.denominator / num)

    def __str__(self) -> str:
        """Prints the attributes of the respective object"""
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other: "Fraction") -> "Fraction":
        """Performs addition of the object passed with the object calling the function"""
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)
        else:
            new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            return Fraction(new_numerator, self.denominator * other.denominator)

    def __sub__(self, other: "Fraction") -> "Fraction":
        """Performs subtraction of the object passed with the object calling the function"""
        if self.denominator == other.denominator:
            return Fraction(self.numerator - other.numerator, self.denominator)
        else:
            new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
            return Fraction(new_numerator, self.denominator * other.denominator)

    def __mul__(self, other: "Fraction") -> "Fraction":
        """Performs multiplication of the object passed with the object calling the function"""
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """Performs division of the object passed with the object calling the function"""
        if other.numerator == 0:
            raise ZeroDivisionError("denominator can't have 0")
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other: "Fraction") -> bool:
        """Check if the object calling and the one passed are equal"""
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __ne__(self, other: "Fraction") -> bool:
        """Check if the object calling and the one passed are not equal"""
        return self.numerator * other.denominator != self.denominator * other.numerator

    def __lt__(self, other: "Fraction") -> bool:
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __le__(self, other: "Fraction") -> bool:
        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __gt__(self, other: "Fraction") -> bool:
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __ge__(self, other: "Fraction") -> bool:
        return self.numerator * other.denominator >= self.denominator * other.numerator
