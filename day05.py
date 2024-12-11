import re
import pathlib
from dataclasses import dataclass

TEST_INPUT = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

FILE = pathlib.Path("day05_input.txt").read_text()

Rule = tuple[int, int]
Update = list[int]


def parse_table(text: str) -> tuple[list[Rule], list[Update]]:
    rules = []
    updates = []
    rules_str, updates_str = text.split("\n\n")
    for line in rules_str.splitlines():
        x, y = line.split("|")
        rules.append((int(x), int(y)))
    for line in updates_str.splitlines():
        updates.append([int(x) for x in line.split(",")])
    return rules, updates


def satisfies_rules(update: Update, rules: list[Rule]) -> bool:
    # left, right = [x[0] for x in rules], [x[1] for x in rules]

    for i, number in enumerate(update):
        for left, right in rules:
            if left == number:
                if right in update[:i]:
                    return False
            elif right == number:
                if left in update[i:]:
                    return False

    return True


def test_satisfies_rules():
    assert satisfies_rules([75, 97, 47, 61, 53], [(97, 75)]) is False
    assert satisfies_rules([61, 13, 29], [(29, 13)]) is False
    assert satisfies_rules([97, 13, 75, 29, 47], [(97, 75), (75, 13)]) is False
    assert satisfies_rules([75, 47, 61, 53, 29], [(97, 75), (75, 13)]) is True


def part1(text: str) -> int:
    rules, updates = parse_table(text)

    return sum(update[len(update) // 2] for update in updates if satisfies_rules(update, rules))


def test_part1():
    assert part1(TEST_INPUT) == 143


if __name__ == "__main__":
    print(part1(FILE))
    # print(test_part1())
    # test_satisfies_rules()


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
