import pathlib
from itertools import product

TEST_INPUT = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

FILE = pathlib.Path("day07_input.txt").read_text()


def parse_table(text: str) -> list[tuple[int, tuple[int]]]:
    entries = []
    for line in text.splitlines():
        test_value, _, coeficients = line.partition(":")
        entries.append((int(test_value), tuple(int(c) for c in coeficients.split())))
    return entries


def is_valid(test_value: int, coeficients: tuple[int, ...]) -> bool:
    operators = product(["+", "*"], repeat=len(coeficients) - 1)
    # pairs = tuple(pairwise(coeficients))
    for operator in operators:
        s = eval(f"{coeficients[0]} {operator[0]} {coeficients[1]}")
        for i, op in enumerate(operator[1:], start=2):
            # print(operator, i)
            s = eval(f"{s} {op} {coeficients[i]} ")
        if test_value == s:
            return True
        else:
            continue
    return False


def test_is_valid() -> None:
    assert is_valid(292, (11, 6, 16, 20)) is True
    assert is_valid(3267, (81, 40, 27)) is True


def part1(text: str) -> int:
    entries = parse_table(text)
    return sum(entry[0] for entry in entries if is_valid(*entry))


def test_part1() -> None:
    assert part1(TEST_INPUT) == 3749
    assert part1(FILE) == 1153997401072


# def part2(text: str)-> int:
#     ...
#
#
# def test_part2() -> None:
#     assert part2(TEST_INPUT) == 123456


if __name__ == "__main__":
    # test_part1()
    # test_is_valid()
    print(part1(FILE))
    # print(part2(FILE))
