def part_one():
    sum, max = 0, 0
    with open("input.txt") as file:
        for line in file:
            if line == "\n":
                if sum > max:
                    max = sum
                sum = 0
            else:
                sum += int(line.strip())
    return max


def part_one_tiny():
    with open("input.txt") as file:
        return max(
            sum(map(lambda x: int(x), arr.split())) for arr in file.read().split("\n\n")
        )


def part_two():
    sum, first, second, third = 0, 0, 0, 0
    with open("input.txt") as file:
        for line in file:
            if line == "\n":
                if sum > first:
                    third = second
                    second = first
                    first = sum
                elif sum > second:
                    third = second
                    second = sum
                elif sum > third:
                    third = sum
                sum = 0
            else:
                sum += int(line.strip())
    return first + second + third


print("part one: ", part_one_tiny())
# print("part two: ", part_two())
