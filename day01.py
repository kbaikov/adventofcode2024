import re
import pathlib
from dataclasses import dataclass

TEST_INPUT = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""

FILE = pathlib.Path("day01_input.txt").read_text()


def parse_table(text: str) -> list[tuple[str, int]]:
    entries: list[tuple[str, int]] = []
    for line in text.splitlines():
        card, bid = line.split()
        entries.append((card, int(bid)))
    return entries


def part1(text: str) -> int: ...


def test_part1():
    assert part1(TEST_INPUT) == 11


if __name__ == "__main__":
    answer = part1(FILE)
    print(answer)


# def part2(text: str)-> int:
#     ...
#
#
# def test_part2():
#     assert part2(TEST_INPUT) == 123456
#
#
#
# if __name__ == "__main__":
#     answer = part2(FILE)
#     print(answer)
