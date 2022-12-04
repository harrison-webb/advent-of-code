"""
A: Rock
B: Paper
C: Scissors

X: Rock
Y: Paper
Z: Scissors

Shape Scores:
Rock: 1
Paper: 2
Scissors: 3

Outcome Scores:
Lose: 0
Tie: 3
Win: 6
"""


def part_one():
    win_map = {"A": "Z", "B": "X", "C": "Y", "X": "C", "Y": "A", "Z": "B"}
    point_map = {"X": 1, "Y": 2, "Z": 3}
    equal_map = {"A": "X", "B": "Y", "C": "Z"}
    score = 0
    with open("input.txt") as file:
        for line in file:
            trimmed_line = (
                line.strip()
            )  # strip only removes whitespace at beginning & end of string, so lines look like "A Y"
            opponent = trimmed_line[0]
            me = trimmed_line[2]
            score += point_map[me]
            if equal_map[opponent] == me:
                score += 3
            elif win_map[me] == opponent:
                score += 6
    return score


def part_two():
    """
    X: Lose (0 points)
    Y: Draw (3 points)
    Z: Win (6 points)
    """
    point_map = {"X": 0, "Y": 3, "Z": 6}
    plays = {
        "A": {"X": 3, "Y": 1, "Z": 2},
        "B": {"X": 1, "Y": 2, "Z": 3},
        "C": {"X": 2, "Y": 3, "Z": 1},
    }
    score = 0
    with open("input.txt") as file:
        for line in file:
            trimmed_line = line.strip()
            opponent = trimmed_line[0]  # A(rock), B(paper), or C(scissors)
            command = trimmed_line[2]  # X(lose), Y(draw), or Z(win)
            score += point_map[command]
            score += plays[opponent][command]
    return score


print(part_two())
