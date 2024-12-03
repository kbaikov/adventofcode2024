"""based on https://github.com/nedbat/adventofcode2023/blob/main/new.py"""

import re
import pathlib
from dataclasses import dataclass

TEST_INPUT = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

FILE = pathlib.Path("day03_input.txt").read_text()


# def parse_table(text: str) -> list[tuple[str, int]]:
#     entries: list[tuple[str, int]] = []
#     for line in text.splitlines():
#         card, bid = line.split()
#         entries.append((card, int(bid)))
#     return entries


def part1(text: str) -> int:
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    found = list(pattern.findall(text))
    return sum(int(x) * int(y) for x, y in found)


def test_part1():
    assert part1(TEST_INPUT) == 161


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
