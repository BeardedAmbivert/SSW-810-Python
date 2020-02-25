from typing import Iterator, IO


def get_lines(path: str) -> Iterator[str]:
    try:
        file: IO = open(path, 'r')
    except FileNotFoundError:
        print(f"Can't open")
    else:
        with file:
            for line in file:
                line = line.strip()
                if line == " ":
                    continue
                while line[-1] == "\\":
                    line = line.replace("\\", "") + file.readline().strip("\n")
                ind = line.find("#")
                if ind == 0:
                    continue
                yield line[:ind]
