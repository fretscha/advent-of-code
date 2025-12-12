# https://adventofcode.com/{{year}}/day/{{day}}


def read_input(filename: str) -> list[any]:
    """Read the input file and return lines"""

    with open(filename, "r") as f:
        return f.readlines()


def part1() -> int:
    """
    Compute part 1 solution.
    Returns:
        _type_: int
    """
    return 0


def part2() -> int:
    """
    Compute part 2 solution.
    Returns:
        _type_: int
    """
    return 1


if __name__ == "__main__":
    lines = read_input("{{year}}/{{day}}/input.txt")

    # Part 1
    result1 = part1(lines)
    print(f"Part 1: {result1}")

    # Part 2
    result2 = part2(lines)
    print(f"Part 2: {result2}")
