"""based on https://github.com/nedbat/adventofcode2023/blob/main/new.py"""

import pathlib

import pytest

TEST_INPUT = """\
"""

FILE = pathlib.Path("dayX_input.txt").read_text()


def parse_table(text: str) -> list[tuple[str, int]]:
    entries: list[tuple[str, int]] = []
    for line in text.splitlines():
        card, bid = line.split()
        entries.append((card, int(bid)))
    return entries


def part1(text: str) -> int: ...


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (TEST_INPUT, 12345),
        (FILE, 12345),
    ],
)
def test_part1(test_input, expected) -> None:
    assert part1(test_input) == expected


# def part2(text: str)-> int:
#     ...
#
#
# def test_part2() -> None:
#     assert part2(TEST_INPUT) == 123456


if __name__ == "__main__":
    pytest.main([__file__])
    # print(part1(FILE))
    # print(part2(FILE))
