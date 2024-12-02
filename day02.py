import pathlib

TEST_INPUT = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

FILE = pathlib.Path("day02_input.txt").read_text()


def parse_table(text: str) -> list[list[int]]:
    entries: list[list[int]] = []
    for line in text.splitlines():
        entries.append([int(x) for x in line.split()])
    return entries


def is_safe(entry: list[int]) -> bool:
    pairs = list(zip(entry, entry[1:]))

    if not all(1 <= abs(x - y) <= 3 for x, y in pairs):
        return False
    if all((x - y) > 0 for x, y in pairs):
        return True
    elif all((x - y) < 0 for x, y in pairs):
        return True
    return False


def is_really_unsafe(entry: list[int]) -> bool:
    for i, x in enumerate(entry):
        new_list = entry[:i] + entry[i + 1 :]
        if is_safe(new_list):
            return True
    return False


def part1(text: str) -> int:
    entries = parse_table(text)
    return sum(is_safe(entry) for entry in entries)


def test_part1():
    assert part1(TEST_INPUT) == 2


if __name__ == "__main__":
    answer = part1(FILE)
    # print(answer)


def part2(text: str) -> int:
    entries = parse_table(text)
    result = []
    for entry in entries:
        if is_safe(entry):
            result.append(True)
        else:
            result.append(is_really_unsafe(entry))
    return sum(result)


def test_part2():
    assert part2(TEST_INPUT) == 4


if __name__ == "__main__":
    answer = part2(FILE)
    print(answer)
