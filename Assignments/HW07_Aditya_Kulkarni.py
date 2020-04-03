"""
Functions to check for anagrams: anagrams_lst, anagrams_dd, anagrams_cntr;
Function to check if a sentence has all the alphabets
A Web analyzer to check for employee website visit logs
"""
from collections import defaultdict, Counter
from typing import DefaultDict, List, Tuple, Set
from string import ascii_lowercase as alpha


def anagrams_lst(str1: str, str2: str) -> bool:
    """
    Checks if given two strings are anagrams of each other using strings and list
    :param str1:
    :param str2:
    :return: bool
    """
    return sorted(list(str1)) == sorted(list(str2))


def anagrams_dd(str1: str, str2: str) -> bool:
    """
    Checks if given two strings are anagrams of each other using default dictionary
    :param str1:
    :param str2:
    :return: bool
    """
    anag_dd: DefaultDict = defaultdict(int)
    for c in str1:
        anag_dd[c] += 1
    for c in str2:
        anag_dd[c] -= 1
    return not any(anag_dd.values())


def anagrams_cntr(str1: str, str2: str) -> bool:
    """
    Checks if given two strings are anagrams of each other using counter
    :param str1:
    :param str2:
    :return: bool
    """
    return Counter(str1) == Counter(str2)


def covers_alphabet(sentence: str) -> bool:
    """
    Checks to see if a sentence has all the characters of a string
    :param sentence:
    :return: bool
    """
    sentence_cntr: Counter = Counter(sentence.lower())
    for a in alpha:
        sentence_cntr[a] -= 1
    return max(sentence_cntr.values()) >= 0 and min(sentence_cntr.values()) >= 0


def web_analyzer(weblogs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]:
    """
    Creats a summary of logs of each distinct website visited by each employee
    :param weblogs:
    :return: List of logs
    """
    logs_dd: DefaultDict[str, Set[str]] = defaultdict(set)
    for k, v in weblogs:
        logs_dd[v].add(k)
    return [(k, sorted(v)) for k, v in sorted(logs_dd.items())]
