def part_one():
    with open("input10.txt") as file:
        input = file.read().split("\n")
    register = 1
    target = 20
    signal_strengths = []
    i = 1
    for line in input:
        if i == target:
            signal_strengths.append(i * register)
            target += 40
        if line == "noop":
            i += 1
        else:
            val = int(line.split()[1])
            for j in range(2):
                if i == target:
                    signal_strengths.append(i * register)
                    target += 40
                i += 1
            register += val
    return sum(signal_strengths)


def part_two():
    with open("input10.txt") as file:
        input = file.read().split("\n")
    register = 1
    i = 1
    for line in input:
        draw_pixel(register, i)

        if line == "noop":
            i += 1
        else:
            val = int(line.split()[1])
            for j in range(2):
                draw_pixel(register, i)
                i += 1
            register += val

        if i % 40 == 0:
            print()


def draw_pixel(register, i):
    if i >= register - 1 and i <= register + 1:
        print("#", end="")
    else:
        print(".", end="")


part_two()
