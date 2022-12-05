def part_one():
    stacks = initialize_stacks()
    with open("input05.txt") as file:
        file_array = file.read().split("\n")
        for line in file_array:
            if "m" in line:  # moving algorithm begins once lines start with "move"
                cleaned_line = [int(x) for x in line.split() if x.isnumeric()]
                for i in range(cleaned_line[0]):
                    stacks[cleaned_line[2]].append(stacks[cleaned_line[1]].pop())
    return "".join([stack[-1] for stack in stacks[1:]])


def part_two():
    stacks = initialize_stacks()
    with open("input05.txt") as file:
        file_array = file.read().split("\n")
        for line in file_array:
            if "m" in line:  # moving algorithm begins once lines start with "move"
                cleaned_line = [int(x) for x in line.split() if x.isnumeric()]
                num_moves, move_from, move_to = (
                    cleaned_line[0],
                    cleaned_line[1],
                    cleaned_line[2],
                )
                # slice last (num_moves) elements from stack
                stuff_getting_moved = stacks[move_from][-(num_moves):]
                # remove sliced section from first list
                stacks[move_from] = stacks[move_from][:-(num_moves)]
                stacks[move_to].extend(stuff_getting_moved)

    return "".join([stack[-1] for stack in stacks[1:]])


def convert_index_to_stack_number(x):
    """Given the index of a letter from the input "crate diagram", return the corresponding crate it belongs to

    Ex:
    [A] [B]
    [D] [X] [Y]
    [R] [N] [P]
     1   2   3

    in this diagram, the bottom right item [P] has index 9 and belongs to crate 3: (9+3)/4 = 3
    """
    return (x + 3) // 4


def initialize_stacks():
    # 10 stacks, first stack is empty so I can use crate 1 == index 1
    stacks = [[], [], [], [], [], [], [], [], [], []]
    with open("input05.txt") as file:
        file_array = file.read().split("\n")
        for line in file_array:
            if "[" in line:  # crate stack initialization
                for i, char in enumerate(line):
                    if char.isalpha():
                        stack_number = convert_index_to_stack_number(i)
                        stacks[stack_number].insert(0, char)

    return stacks


print(part_two())
