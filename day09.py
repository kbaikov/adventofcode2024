import pathlib
from itertools import chain
import pytest

TEST_INPUT = """\
2333133121414131402
"""

FILE = pathlib.Path("day09_input.txt").read_text()


def checksum(data: str) -> int:
    """Calculate the checksum of a string of digits.

    add up the result of multiplying each of these blocks' position with the file ID number
    it contains. The leftmost block is in position 0.
    """
    return sum(i * int(digit) for i, digit in enumerate(data))


@pytest.mark.parametrize("test_input, expected", [("0099811188827773336446555566", 1928)])
def test_checksum(test_input, expected) -> None:
    assert checksum(test_input) == expected


def my_getitem(container, i: int, default=None):
    try:
        return container[i]
    except IndexError:
        return default


def order_string(data: str) -> str:
    data = data.strip()
    file_lengths = data[0::2]
    space_lengths = data[1::2]
    return "".join(str(i) * int(digit) + "." * int(my_getitem(space_lengths, i, 0)) for i, digit in enumerate(file_lengths))


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("12345", "0..111....22222"),
        ("2333133121414131402", "00...111...2...333.44.5555.6666.777.888899"),
    ],
)
def test_order_string(test_input, expected) -> None:
    assert order_string(test_input) == expected


def rearrange(data: str) -> str:
    # 12345 -> 022111222......
    file_lengths = data[0::2]  # 1,  3,  5
    space_lengths = data[1::2]  # 2,  4,  6
    list_of_ids = [str(i) * int(digit) for i, digit in enumerate(file_lengths)]  # ["0", "111", "22222"]
    reversed_list_of_ids = chain.from_iterable(list_of_ids[::-1])  # "222221110"

    result_len = sum(int(digit) for digit in file_lengths)
    result = []
    # "0..111....22222" -> "022111222"
    for i, digit in enumerate(list(order_string(data))):
        if result_len == len(result):
            break
        if digit == ".":
            result.append(next(reversed_list_of_ids))
        else:
            result.append(digit)
    return "".join(result)


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("12345", "022111222"),
        ("2333133121414131402", "0099811188827773336446555566"),
    ],
)
def test_rearrange(test_input, expected) -> None:
    assert rearrange(test_input) == expected


def part1(text: str) -> int:
    return checksum(rearrange(text))


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (TEST_INPUT, 1928),
        (FILE, 5268653987),
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
    # pytest.main([f"{__file__}::test_part1"])
    print(part1(FILE))
    # print(part2(FILE))
