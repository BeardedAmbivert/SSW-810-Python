"""Contains Functions for list copy, intersection and difference, funcitons to remove vowels and check passwords \
a class to create check for customers in a queue"""
from typing import List, Any, Optional


def list_copy(l: List[Any]) -> List[Any]:
    """takes list as a input and returns the copy of the list using list comprehension"""
    return [item for item in l]


def list_intersect(l1: List[Any], l2: List[Any]) -> List[Any]:
    """takes two list as parameters and returns a new list as output that includes common elements from the two list"""
    return [item for item in l1 if item in l2]


def list_difference(l1: List[Any], l2: List[Any]) -> List[Any]:
    """The function takes two list as parameters and returns a new list as output that includes common elements from \
    the two list"""
    return [item for item in l1 if item not in l2]


def remove_vowels(string: str) -> str:
    """removes the words which begins with a vowel"""
    return " ".join([word for word in string.split() if word[0].lower() not in ['a', 'e', 'i', 'o', 'u']])


def check_pwd(password: str) -> bool:
    """takes a input string and returns a bool value"""
    # if len(password) > 0 and password[0].isdigit():
    #     upper: List[Any] = [letter for letter in password if letter.isupper()]
    #     lower: List[Any] = [letter for letter in password if letter.islower()]
    #     return len(upper) > 1 and len(lower) > 0
    # else:
    #     return False
    # Professor's solution
    return len(password) >= 4 \
        and sum([1 for c in password if c.isupper()]) >= 2 \
        and sum([1 for c in password if c.islower()]) >= 1 \
        and password[0].isdigit()


def reorder(l: List[Any]) -> List[Any]:
    """returns a copy of argument list sorted in ascending order"""
    sorted_list: List[Any] = list()
    sorted_list.append(l[0])
    for i in range(1, len(l)):
        index: int = 0
        while index < i and l[i] > sorted_list[index]:
            index += 1
        sorted_list.insert(index, l[i])
    return sorted_list


class DonutQueue:
    """tracks customers as they arrive at the donut shop.  Customers are added to the queue so they can be served \
    in the order they arrived with the exception that priority customers """

    def __init__(self) -> None:
        """create two separate lists for the normal and priority guests """
        self.normal_customer: List[str] = list()
        self.priority_customer: List[str] = list()

    def arrive(self, name: str, vip: bool) -> None:
        """notes customer information"""
        if vip:
            self.priority_customer.append(name)
        else:
            self.normal_customer.append(name)

    def next_customer(self) -> Optional[str]:
        """returns the name of the next customer to be served where all priority customers are served in the order they\
         arrived before any non-priority customer. """
        if len(self.priority_customer) > 0:
            return self.priority_customer.pop(0)
        elif len(self.normal_customer) > 0:
            return self.normal_customer.pop(0)
        else:
            return None

    def waiting(self) -> Optional[str]:
        """returns a comma separated string with the names of the customers waiting in the order they will be served"""
        queue: List[str] = self.priority_customer.copy()
        queue.extend(self.normal_customer)
        if len(queue) > 0:
            return ", ".join(queue)
        else:
            return None
