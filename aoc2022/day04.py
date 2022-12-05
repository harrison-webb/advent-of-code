def part_one():
    pairs = 0
    with open("input04.txt") as file:
        for line in file.read().split():
            # an example input line looks like "2-4,6-8", meaning elf 1 gets sections 2, 3, 4 and elf 2 gets sections 6, 7, 8
            # sections extracts the start and end indexes for both sections from every line
            sections = [int(x) for x in line.replace(",", "-").split("-")]
            start1, end1 = sections[0], sections[1]
            start2, end2 = sections[2], sections[3]
            # check if interval 1 contains interval 2 or vice-versa
            if ((start1 <= start2) and (end1 >= end2)) or (
                (start2 <= start1) and (end2 >= end1)
            ):
                pairs += 1
    return pairs


def part_two():
    pairs = 0
    with open("input04.txt") as file:
        for line in file.read().split():
            sections = [int(x) for x in line.replace(",", "-").split("-")]
            start1, end1 = sections[0], sections[1]
            start2, end2 = sections[2], sections[3]
            if (start1 <= end2 and end1 >= start2) or (
                start2 <= end1 and end2 >= start1
            ):
                pairs += 1
    return pairs


print(f"part one: {part_one()}")
print(f"part two: {part_two()}")
