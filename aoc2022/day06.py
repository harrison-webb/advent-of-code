def part_one():
    with open("input06.txt") as file:
        input = file.readline()
        for i, char in enumerate(input):
            if len(input[i : i + 4]) == len(set(input[i : i + 4])):
                return i + 4


def part_two():
    """
    in progress
    want to have a 14-wide window that jumps start index to (old index + 1) when a duplicate is found
    """
    with open("input06.txt") as file:
        input = file.readline()
        i = 0
        seen_chars = {}
        for i, char in enumerate(input):
            if char in seen_chars:
                seen_chars = {}
                continue


def part_two_bad():
    with open("input06.txt") as file:
        input = file.readline()
        for i, char in enumerate(input):
            if len(input[i : i + 14]) == len(set(input[i : i + 14])):
                return i + 14


print(part_two_bad())
