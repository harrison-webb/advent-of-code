def part_one():
    f = open("input09.txt")
    input = f.read().split("\n")
    f.close()
    head_position = tail_position = [0, 0]
    tail_position_list = set()
    tail_position_list.add(tuple(tail_position))
    for command in input:
        tokens = command.split()
        direction = tokens[0]
        steps = int(tokens[1])
        for i in range(steps):
            head_previous = head_position
            if direction == "U":
                head_position = [head_position[0], head_position[1] + 1]
            elif direction == "D":
                head_position = [head_position[0], head_position[1] - 1]
            elif direction == "L":
                head_position = [head_position[0] - 1, head_position[1]]
            elif direction == "R":
                head_position = [head_position[0] + 1, head_position[1]]
            if (
                (head_position[0] - tail_position[0]) ** 2
                + (head_position[1] - tail_position[1]) ** 2
            ) ** (0.5) > 1.5:
                tail_position = head_previous
                tail_position_list.add(tuple(tail_position))
    return len(tail_position_list)


def part_two():
    f = open("input09.txt")
    input = f.read().split("\n")
    f.close()
    segments = []
    for i in range(10):
        segments.append([0, 0])
    tail_position = segments[-1]
    tail_position_list = set()
    tail_position_list.add(tuple(tail_position))

    for command in input:
        tokens = command.split()
        direction = tokens[0]
        steps = int(tokens[1])
        for i in range(steps):
            if direction == "U":
                segments[0] = [segments[0][0], segments[0][1] + 1]
            elif direction == "D":
                segments[0] = [segments[0][0], segments[0][1] - 1]
            elif direction == "L":
                segments[0] = [segments[0][0] - 1, segments[0][1]]
            elif direction == "R":
                segments[0] = [segments[0][0] + 1, segments[0][1]]
            for j in range(len(segments)):
                if j == 0:
                    continue
                if (
                    (segments[j - 1][0] - segments[j][0]) ** 2
                    + (segments[j - 1][1] - segments[j][1]) ** 2
                ) ** 0.5 > 1.5:
                    dx = dy = 0
                    unit = []
                    x = segments[j - 1][0] - segments[j][0]
                    y = segments[j - 1][1] - segments[j][1]
                    if x == 0:
                        unit = [0, int(y / abs(y))]
                    elif y == 0:
                        unit = [int(x / abs(x)), 0]
                    else:
                        unit = [int(x / abs(x)), int(y / abs(y))]
                    segments[j] = [
                        segments[j][0] + unit[0],
                        segments[j][1] + unit[1],
                    ]
                    tail_position_list.add(tuple(segments[-1]))
    print(tail_position_list)
    return len(tail_position_list)


print(part_two())
