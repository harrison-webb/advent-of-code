def part_one():
    filesystem = Tree("/", None)
    current = filesystem
    with open("input07.txt") as file:
        for line in file.read().split("\n"):
            tokens = line.split()
            if tokens[0] == "$":
                if line == "$ cd .." and current != filesystem:
                    current = current.parent
                elif tokens[1] == "cd":
                    if tokens[2] not in current.subdirectories:
                        current.subdirectories[tokens[2]] = Tree(tokens[2], current)
                    current = current.subdirectories[tokens[2]]
            else:
                # this else branch covers the output of "ls" command
                # if a directory is listed, add it to the subdirectories of current directory
                if tokens[0] == "dir":
                    current.subdirectories[tokens[1]] = Tree(tokens[1], current)
                else:
                    # last possibility is a file is listed, so add {filename: filesize} to current.files
                    current.files.append((tokens[1], int(tokens[0])))
    calculate_node_sizes(filesystem)
    return sum(find_nodes_smaller_than(100000, filesystem))


def part_one_better():
    directories = {}
    current_directories = []
    with open("input07.txt") as file:
        for line in file.read().split("\n"):
            tokens = line.split()
            if line == "$ cd ..":
                # remove most recent directory from current_directories
                current_directories.pop()
            elif line.startswith("$ cd"):
                # append to current_directories
                if tokens[2] not in directories:
                    directories[tokens[2]] = 0
                current_directories.append(tokens[2])
            elif line.startswith("dir"):
                # might not need this
                True
            elif line[0].isnumeric():
                # add size of file to each directory in current_directories
                for dir in current_directories:
                    directories[dir] += int(tokens[0])
    sum = 0
    for key, value in directories.items():
        if value <= 100000:
            sum += value
    return sum


def parse_tree(tree):
    size = 0

    for name, directory in tree.subdirectories.items():
        size += parse_tree(directory)
    for file in tree.files:
        size += file[1]
    if size <= 100000:
        return size
    else:
        return 0


def find_nodes_smaller_than(size, tree):
    node_list = []
    if tree.size <= size:
        node_list.append(tree.size)
    for name, directory in tree.subdirectories.items():
        node_list.extend(find_nodes_smaller_than(size, directory))
    return node_list


def calculate_node_sizes(tree):
    size = 0
    for file in tree.files:
        size += file[1]
    for name, directory in tree.subdirectories.items():
        size += calculate_node_sizes(directory)
    tree.size = size
    return size


class Tree:
    def __init__(self, name: str, parent):
        self.files = []
        self.subdirectories = {}
        self.parent = parent
        self.name = name
        self.size = 0


print(part_one())
