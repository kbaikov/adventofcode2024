import pathlib
from collections.abc import Iterable

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


def satisfies_rules(update: Update, rules: Iterable[Rule]) -> bool:
    for i, number in enumerate(update):
        for left, right in rules:
            if left == number:
                if right in update[:i]:
                    return False
            elif right == number:
                if left in update[i:]:
                    return False

    return True


def test_satisfies_rules() -> None:
    assert satisfies_rules([75, 97, 47, 61, 53], [(97, 75)]) is False
    assert satisfies_rules([61, 13, 29], [(29, 13)]) is False
    assert satisfies_rules([97, 13, 75, 29, 47], [(97, 75), (75, 13)]) is False
    assert satisfies_rules([75, 47, 61, 53, 29], [(97, 75), (75, 13)]) is True


def part1(text: str) -> int:
    rules, updates = parse_table(text)

    return sum(update[len(update) // 2] for update in updates if satisfies_rules(update, rules))


def test_part1() -> None:
    assert part1(TEST_INPUT) == 143
    assert part1(FILE) == 6505


def fix_update(update: Update, rules: Iterable[Rule]) -> Update:
    """from https://www.reddit.com/r/adventofcode/comments/1h71eyz/comment/m0i09b0/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button"""
    from functools import cmp_to_key

    cmp = cmp_to_key(lambda x, y: 1 - 2 * ((x, y) in set(rules)))

    return sorted(update, key=cmp)
    # new_update = update[:]
    # while not satisfies_rules(new_update, rules):
    #     for rule in rules:
    #         left, right = rule

    #         for i, number in enumerate(update):
    #             if left == number:
    #                 if right in update[:i]:
    #                     new_update.pop(new_update.index(right))
    #                     new_update.insert(i + 1, right)
    #                     break
    #             elif right == number:
    #                 if left in update[i:]:
    #                     new_update.pop(new_update.index(left))
    #                     new_update.insert(i, left)
    #                     break

    # return new_update


def fix_update2(update: Update, rules: Iterable[Rule]) -> Update:
    """from https://www.reddit.com/r/adventofcode/comments/1h71eyz/comment/m0kezt2/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button"""
    return sorted(update, key=lambda x: -sum((x, y) in rules for y in update))


def fix_update3(update: Update, rules: Iterable[Rule]) -> Update:
    """from https://github.com/norvig/pytudes/blob/main/ipynb/Advent-2024.ipynb"""
    from functools import cmp_to_key

    def rule_lookup(m: int, n: int) -> int:
        return +1 if (m, n) in rules else -1

    return sorted(update, key=cmp_to_key(rule_lookup))


def test_fix_update() -> None:
    rules, _ = parse_table(TEST_INPUT)
    assert fix_update([75, 97, 47, 61, 53], rules) == [97, 75, 47, 61, 53]
    assert fix_update([61, 13, 29], rules) == [61, 29, 13]
    assert fix_update([97, 13, 75, 29, 47], rules) == [97, 75, 47, 29, 13]


def broken_rules(update: Update, rules: list[Rule]) -> set[Rule]:
    broken = set()
    for i, number in enumerate(update):
        for left, right in rules:
            if left == number:
                if right in update[:i]:
                    broken.add((left, right))
            elif right == number:
                if left in update[i:]:
                    broken.add((left, right))

    return broken


def part2(text: str) -> int:
    rules, updates = parse_table(text)
    incorrect_updates = [update for update in updates if not satisfies_rules(update, rules)]
    # to_fix = [(u, broken_rules(u, rules)) for u in incorrect_updates]

    fixed_updates = [fix_update3(u, rules) for u in incorrect_updates]
    return sum(update[len(update) // 2] for update in fixed_updates)


def test_part2() -> None:
    assert part2(TEST_INPUT) == 123
    assert part2(FILE) == 6897


if __name__ == "__main__":
    test_part1()
    # print(part1(FILE))
    test_part2()
    print(part2(FILE))
