import pathlib
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


Point = tuple[int, int]
Grid = dict[Point, str]


def part1(text: str) -> int:
    lines = text.splitlines()
    grid: Grid = {(x, y): column for x, row in enumerate(lines) for y, column in enumerate(row)}

    g = list(grid.keys())
    D = list(product((-1, 0, 1), repeat=2))
    T = list("XMAS")
    result = 0
    for i, j in g:
        for di, dj in D:
            match = [grid.get((i + di * n, j + dj * n)) for n in range(4)]
            if match == T:
                result += 1
    return result


def test_part1() -> None:
    assert part1(TEST_INPUT) == 18


if __name__ == "__main__":
    answer = part1(FILE)
    # print(answer)


def point_lookup(point: Point, grid: Grid) -> int:
    i, j = point
    directions = -1, 0, 1
    T = list("MAS"), list("SAM")
    result = 0
    for _ in T:
        match = [grid.get((i + d, j + d)) for d in directions]
        match2 = [grid.get((i + d, j - d)) for d in directions]

        if match in T and match2 in T:
            result += 1
    return result


def part2(text: str) -> int:
    grid: Grid = {(x, y): column for x, row in enumerate(text.splitlines()) for y, column in enumerate(row)}

    return int(sum(point_lookup(point, grid) for point in grid) / 2)


def test_part2() -> None:
    assert part2(TEST_INPUT) == 9


if __name__ == "__main__":
    answer = part2(FILE)
    print(answer)
