import pathlib

TEST_INPUT = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

FILE = pathlib.Path("day06_input.txt").read_text()

Point = tuple[int, int]
Grid = dict[Point, str]


def parse_table(text: str) -> Grid:
    lines = text.splitlines()
    grid: Grid = {(x, y): column for x, row in enumerate(lines) for y, column in enumerate(row)}
    return grid


def part1(text: str) -> int:
    grid = parse_table(text)
    print(grid)
    return 0


def test_part1() -> None:
    assert part1(TEST_INPUT) == 41


# def part2(text: str)-> int:
#     ...
#
#
# def test_part2() -> None:
#     assert part2(TEST_INPUT) == 123456


if __name__ == "__main__":
    test_part1()
    # print(part1(FILE))
    # print(part2(FILE))
