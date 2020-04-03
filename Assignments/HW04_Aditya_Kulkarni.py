"""Functions for counting vowels, finding last occurrence and my_enumerate"""

from typing import List, Sequence, Any, Optional, Iterator


def count_vowels(s: str) -> int:
    """Counts all the vowels in a given string"""
    vowels: List[str] = ['a', 'e', 'i', 'o', 'u']
    count: int = 0
    for letter in s.lower():
        if letter in vowels:
            count += 1
    return count


def last_occurrence(target: Any, sequence: Sequence[Any]) -> Optional[int]:
    """Finds the last occurrence of a value in a given sequence"""
    for i in range(len(sequence) - 1, -1, -1):
        if sequence[i] == target:
            return i
    return None


def my_enumerate(seq: Sequence[Any]) -> Iterator[Any]:
    """Mimics python's enumerate method"""
    for i in range(len(seq)):
        yield i, seq[i]
