def part_one():
    f = open("input09.txt")
    input = f.read().split("\n")
    f.close()
    head_position = tail_position = [0, 0]
    tail_position_list = set()
    tail_position_list.add(tuple(tail_position))
    for command in input:
        direction = command[0]
        steps = int(command[2])
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


print(part_one())
