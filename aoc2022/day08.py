def part_one():
    visible_trees = 0
    tree_grid = None
    with open("input08.txt") as file:
        tree_grid = file.read().split()
    # calculate the trees around the edge of the grid
    visible_trees += 2 * len(tree_grid) + 2 * len(tree_grid[0]) - 4
    for i in range(1, len(tree_grid) - 1):
        for j in range(1, len(tree_grid[0]) - 1):
            if is_visible_top(i, j, tree_grid):
                visible_trees += 1
            elif is_visible_bottom(i, j, tree_grid):
                visible_trees += 1
            elif is_visible_left(i, j, tree_grid):
                visible_trees += 1
            elif is_visible_right(i, j, tree_grid):
                visible_trees += 1
    return visible_trees


def is_visible_top(i, j, grid):
    height = grid[i][j]
    for k in range(i):
        if grid[k][j] >= height:
            return False
    return True


def is_visible_bottom(i, j, grid):
    height = grid[i][j]
    for k in range(len(grid) - 1, i, -1):
        if grid[k][j] >= height:
            return False
    return True


def is_visible_left(i, j, grid):
    height = grid[i][j]
    for k in range(j):
        if grid[i][k] >= height:
            return False
    return True


def is_visible_right(i, j, grid):
    height = grid[i][j]
    for k in range(len(grid[0]) - 1, j, -1):
        if grid[i][k] >= height:
            return False
    return True


print(part_one())
