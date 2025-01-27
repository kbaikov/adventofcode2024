import itertools
import pathlib
from dataclasses import dataclass

import pytest

TEST_INPUT = """\
2333133121414131402
"""

FILE = pathlib.Path("day09_input.txt").read_text()


@dataclass
class Segment:
    id: int
    length: int
    space: int


def checksum(data: str | list[str]) -> int:
    """Calculate the checksum of a string of digits.

    add up the result of multiplying each of these blocks' position with the file ID number
    it contains. The leftmost block is in position 0.
    """
    return sum(i * int(digit) for i, digit in enumerate(data) if digit != ".")


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("0099811188827773336446555566", 1928),
        (list("0099811188827773336446555566"), 1928),
        (list("00992111777.44.333....5555.6666.....8888.."), 2858),
    ],
)
def test_checksum(test_input, expected) -> None:
    assert checksum(test_input) == expected


def checksum2(data: list[Segment]) -> int:
    """Calculate the checksum of a string of digits.

    add up the result of multiplying each of these blocks' position with the file ID number
    it contains. The leftmost block is in position 0.
    """
    return checksum("".join(str(segment.id) * segment.length + "." * segment.space for segment in data))


def my_getitem(container, i: int, default=None):
    try:
        return container[i]
    except IndexError:
        return default


def ordered_segments(data: str) -> list[Segment]:
    file_lengths = data[0::2]
    space_lengths = data[1::2]
    segments = [
        Segment(id=i, length=int(obj[0]), space=int(obj[1]))
        for i, obj in enumerate(itertools.zip_longest(file_lengths, space_lengths, fillvalue=0))
    ]
    return segments


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("12345", [Segment(0, 1, 2), Segment(1, 3, 4), Segment(2, 5, 0)]),
        ("233313", [Segment(0, 2, 3), Segment(1, 3, 3), Segment(2, 1, 3)]),
    ],
)
def test_ordered_segments(test_input, expected) -> None:
    assert ordered_segments(test_input) == expected


def order_string(data: str) -> str:
    # "12345"->"0..111....22222"
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


def order_string_list(segments: list[Segment]) -> list[str]:
    result = []
    for s in segments:
        result.extend([str(s.id)] * s.length + ["."] * s.space)
    return result


def order_string_list2(segments: list[Segment]) -> list[str]:
    result = []
    for s in segments:
        result.extend([str(s.id)] * s.length + ["." * s.space])
    return result


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            [Segment(0, 1, 2), Segment(1, 3, 4), Segment(2, 5, 0)],
            ["0", "..", "1", "1", "1", "....", "2", "2", "2", "2", "2", ""],
        ),
    ],
)
def test_order_string_list2(test_input, expected) -> None:
    assert order_string_list2(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            [Segment(0, 1, 2), Segment(1, 3, 4), Segment(2, 5, 0)],
            ["0", ".", ".", "1", "1", "1", ".", ".", ".", ".", "2", "2", "2", "2", "2"],
        ),
    ],
)
def test_order_string_list(test_input, expected) -> None:
    assert order_string_list(test_input) == expected


def rearrange_list(data: str) -> list[str]:
    segments = ordered_segments(data)
    reversed_list_of_ids = itertools.chain.from_iterable([[s.id] * s.length for s in segments[::-1]])
    result = []
    result_len = sum(s.length for s in segments)
    for digit in order_string_list(segments):
        if len(result) == result_len:
            break
        if digit == ".":
            result.append(str(next(reversed_list_of_ids)))

    return result


def part1(text: str) -> int:
    return checksum(rearrange_list(text.strip()))


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (TEST_INPUT, 1928),
        (FILE, 6415184586041),
    ],
)
def test_part1(test_input, expected) -> None:
    assert part1(test_input) == expected


def rearrange_list2(data: str) -> list[Segment]:
    segments = ordered_segments(data)
    # segments_reversed = segments[::-1]
    free_space = {s.space: segments.index(s) for s in segments}
    # next_segment=segments_reversed.pop()
    result = segments[:]
    for s_to_move in segments[::-1]:
        if i := free_space[s_to_move.length]:
            result.insert(i, s_to_move)
    return result


def part2(text: str) -> int:
    a = rearrange_list2(text.strip())
    print("".join(str(segment.id) * segment.length + "." * segment.space for segment in a))
    # return checksum2(rearrange_list2(text.strip()))


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (TEST_INPUT, 2858),
        (FILE, 6415184586041),
    ],
)
def test_part2(test_input, expected) -> None:
    assert part2(test_input) == expected


if __name__ == "__main__":
    # pytest.main([f"{__file__}::test_checksum"])
    # print(part1(FILE))
    print(part2(TEST_INPUT))
