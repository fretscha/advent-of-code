# https://adventofcode.com/2025/day/1


def read_input(filename: str) -> list[any]:
    """Read the input file and return lines"""

    with open(filename, "r") as f:
        return f.readlines()


def part1(rotations: list[str]) -> int:
    """
    Compute count of zeros.
    Returns:
        _type_: int
    """
    position = 50
    zeros = 0
    for rotation in rotations:
        direction = rotation[0]
        steps = int(rotation[1:])
        if direction == "R":
            position += steps
        elif direction == "L":
            position -= steps
        if position % 100 == 0:
            zeros += 1
    return zeros


def part2(rotations: list[str]) -> int:
    """
    Compute count of clicks pass zero.
    Returns:
        _type_: int
    """
    position = 50
    zeros = 0
    for rotation in rotations:
        direction = rotation[0]
        steps = int(rotation[1:])
        for step in range(steps):
            if direction == "R":
                position += 1
            elif direction == "L":
                position -= 1
            position %= 100
            if position == 0:
                zeros += 1
    return zeros


if __name__ == "__main__":
    lines = read_input("2025/1/input.txt")

    # Part 1
    result1 = part1(lines)
    print(f"Part 1: {result1}")

    # Part 2
    result2 = part2(lines)
    print(f"Part 2: {result2}")
