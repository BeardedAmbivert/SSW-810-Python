"""Functions for reversing a string , finding a substring and \
 finding second occurrence in a string, getting valid sentences from a string"""
from typing import Iterator, IO


def reverse(s: str) -> str:
    """reverses a string"""
    return "".join([ch for ch in s][::-1])


def substring(target: str, s: str) -> int:
    """Finds the index location of target in the given string """
    if target in s:
        for ind, let in enumerate(s):
            if target[0] == let:
                if target == s[ind:len(target)+ind]:
                    return ind
    return -1


def find_second(target: str, string: str) -> int:
    """Finds the index location of the second occurrence of the target in given string"""
    if target in string:
        first_occurrence: int = string.find(target)
        if first_occurrence >= 0:
            return string.find(target, first_occurrence + 1)
    else:
        return -1


def get_lines(path: str) -> Iterator[str]:
    """Reads a file and outputs sentences without comments"""
    try:
        file: IO = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"Can't open")
    else:
        with file:
            for line in file:
                line = line.rstrip("\n")
                while line.endswith("\\"):
                    line = line[:-1] + file.readline().strip("\n")
                if "#" in line:
                    if line[0] == "#":
                        continue
                    else:
                        yield line[:line.find("#")]
                else:
                    yield line
