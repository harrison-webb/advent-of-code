def part_one():
    filesystem = Tree("root", None)
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
                    current.files.append({tokens[1]: tokens[0]})
    print(filesystem.subdirectories["/"].subdirectories)


class Tree:
    def __init__(self, name: str, parent):
        self.files = []
        self.subdirectories = {}
        self.parent = parent
        self.name = name


part_one()
