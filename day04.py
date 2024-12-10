import pathlib
from collections import defaultdict
from itertools import product

TEST_INPUT = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

FILE = pathlib.Path("day04_input.txt").read_text()


# def parse_table(text: str) -> list[tuple[str, int]]:
#     entries: list[tuple[str, int]] = []
#     for line in text.splitlines():
#         card, bid = line.split()
#         entries.append((card, int(bid)))
#     return entries


def part1(text: str) -> int:
    text = text.splitlines()
    Grid = defaultdict(str) | {(x, y): column for x, row in enumerate(text) for y, column in enumerate(row)}

    g = list(Grid.keys())
    D = list(product((-1, 0, 1), repeat=2))
    T = list("XMAS")
    result = 0
    for i, j in g:
        for di, dj in D:
            match = [Grid[i + di * n, j + dj * n] for n in range(4)]
            if match == T:
                result += 1
    return result


def test_part1():
    assert part1(TEST_INPUT) == 18


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
