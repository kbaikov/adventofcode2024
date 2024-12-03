import pathlib
import re

TEST_INPUT = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

FILE = pathlib.Path("day03_input.txt").read_text()


def part1(text: str) -> int:
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    found = list(pattern.findall(text))
    return sum(int(x) * int(y) for x, y in found)


def test_part1():
    assert part1(TEST_INPUT) == 161


if __name__ == "__main__":
    answer = part1(FILE)
    # print(answer)


def part2(text: str) -> int:
    # text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    # text.replace("\\n", "")
    # do_matches = [i.end() for i in re.finditer(r"do\(\)", text, re.MULTILINE)]
    # dont_matches = [i.end() for i in re.finditer(r"don't\(\)", text, re.MULTILINE)]
    # split idea is from https://www.reddit.com/r/adventofcode/comments/1h5obsr/comment/m08ng5n/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    do_split = text.split("do()")
    dont_split = [x.split("don't") for x in do_split]
    result = "".join(x[0] for x in dont_split)
    # do_matches.insert(0, 0)
    # dont_matches.insert(len(dont_matches), 99999999999999999999999)
    # text_ranges = [(a, b) for a, b in zip(do_matches, dont_matches)]
    # result = ""
    # for x, y in text_ranges:
    #     result += text[x:y]
    # print(do_split)
    # print(dont_split)
    # print(result)

    return part1(result)


def test_part2():
    assert part2("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))") == 48


if __name__ == "__main__":
    print(part2(FILE))
