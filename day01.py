import pathlib
from collections import Counter

TEST_INPUT = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""

FILE = pathlib.Path("day01_input.txt").read_text()


def parse_table(text: str) -> tuple[list[int], list[int]]:
    left: list[int] = []
    right: list[int] = []
    for line in text.splitlines():
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))
    return left, right


def part1(text: str) -> int:
    left, right = parse_table(text)
    left.sort()
    right.sort()
    return sum(abs(l - r) for l, r in zip(left, right))


def test_part1() -> None:
    assert part1(TEST_INPUT) == 11


if __name__ == "__main__":
    answer = part1(FILE)
    # print(answer)


def part2(text: str) -> int:
    left, right = parse_table(text)
    counted = Counter(right)
    return sum(x * counted[x] for x in left)


def test_part2() -> None:
    assert part2(TEST_INPUT) == 31


if __name__ == "__main__":
    answer = part2(FILE)
    print(answer)
