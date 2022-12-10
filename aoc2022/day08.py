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


def part_two():
    max = 0
    tree_grid = None
    with open("input08.txt") as file:
        tree_grid = file.read().split()
    for i in range(1, len(tree_grid) - 1):
        for j in range(1, len(tree_grid[0]) - 1):
            score = calculate_senic_score(i, j, tree_grid)
            if score > max:
                max = score
    return max


def calculate_senic_score(i, j, grid):
    # count number of trees left, right, above, and below tree at (i,j), terminating when we see a
    # tree with height greater or equal to tree at (i,j)

    return (
        visible_trees_above(i, j, grid)
        * visible_trees_below(i, j, grid)
        * visible_trees_left(i, j, grid)
        * visible_trees_right(i, j, grid)
    )


def visible_trees_above(i, j, grid):
    visible_trees = 0
    for k in range(i - 1, -1, -1):
        visible_trees += 1
        if grid[k][j] >= grid[i][j]:
            break
    return visible_trees


def visible_trees_below(i, j, grid):
    visible_trees = 0
    for k in range(i + 1, len(grid)):
        visible_trees += 1
        if grid[k][j] >= grid[i][j]:
            break
    return visible_trees


def visible_trees_left(i, j, grid):
    visible_trees = 0
    for k in range(j - 1, -1, -1):
        visible_trees += 1
        if grid[i][k] >= grid[i][j]:
            break
    return visible_trees


def visible_trees_right(i, j, grid):
    visible_trees = 0
    for k in range(j + 1, len(grid[0])):
        visible_trees += 1
        if grid[i][k] >= grid[i][j]:
            break
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


print(part_two())
