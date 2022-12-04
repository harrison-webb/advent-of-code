def part_one():
    sum = 0
    with open("input03.txt") as file:
        for item_list in file.read().split():
            compartment_one, compartment_two = set(), set()
            for i, char in enumerate(item_list):
                if i < len(item_list) / 2:
                    compartment_one.add(char)
                else:
                    compartment_two.add(char)
            shared_item = compartment_one.intersection(compartment_two).pop()
            sum += get_priority(shared_item)
    return sum


def part_two():
    sum = 0
    with open("input03.txt") as file:
        lines = file.read().split()
        for i in range(0, len(lines), 3):  # loop by groups of three
            shared = (
                set(lines[i]).intersection(set(lines[i + 1]), set(lines[i + 2])).pop()
            )
            sum += get_priority(shared)
    return sum


def get_priority(char: str):
    if ord(char) >= 97:  # lowercase
        return ord(char) - 96
    else:
        return ord(char) - 38


print(part_two())
