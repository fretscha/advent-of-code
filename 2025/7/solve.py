# https://adventofcode.com/2025/day/7
import logging
import os


def read_input(filename: str) -> list[any]:
    """Read the input file and return lines"""

    with open(filename, "r") as f:
        return f.readlines()


def part1(lines: list[str]) -> int:
    """
    Count beam splits in tachyon manifold.
    Beams move downward. When they hit a splitter, two new downward beams
    are created from the positions immediately to the left and right.
    Returns:
        _type_: int
    """

    grid = [line.rstrip("\n") for line in lines]

    # position (S)
    start_col = -1
    for col_idx in range(len(grid[0])):
        if grid[0][col_idx] == "S":
            start_col = col_idx
            break

    active_columns = {start_col}

    # track already hit splitters
    hit_splitters = set()

    split_count = 0

    for row_idx in range(1, len(grid)):
        new_columns = set()

        for col in active_columns:
            # splitter hit
            if grid[row_idx][col] == "^":
                # count once
                if (row_idx, col) not in hit_splitters:
                    hit_splitters.add((row_idx, col))
                    split_count += 1

                    # two new beams emerge
                    if col - 1 >= 0:
                        new_columns.add(col - 1)
                    if col + 1 < len(grid[row_idx]):
                        new_columns.add(col + 1)
            elif grid[row_idx][col] == ".":
                new_columns.add(col)

        active_columns = new_columns

    return split_count


def part2(lines: list[str]) -> int:
    """
    Count unique timelines for quantum particle.
    The particle takes BOTH paths at each splitter, creating different timelines.
    Count unique endpoint columns where the particle can exit.
    Returns:
        _type_: int
    """
    grid = [line.rstrip("\n") for line in lines]

    # position (S)
    start_col = -1
    for col_idx in range(len(grid[0])):
        if grid[0][col_idx] == "S":
            start_col = col_idx
            break

    # key is column, value is number of different paths reaching it
    path_counts = {start_col: 1}

    for row_idx in range(1, len(grid)):
        new_path_counts = {}

        for col, count in path_counts.items():
            # splitter hit
            if grid[row_idx][col] == "^":
                # two new beams emerge
                if col - 1 >= 0:
                    new_path_counts[col - 1] = new_path_counts.get(col - 1, 0) + count
                if col + 1 < len(grid[row_idx]):
                    new_path_counts[col + 1] = new_path_counts.get(col + 1, 0) + count
            elif grid[row_idx][col] == ".":
                new_path_counts[col] = new_path_counts.get(col, 0) + count

        path_counts = new_path_counts

    return sum(path_counts.values())


if __name__ == "__main__":
    DEBUG = os.environ.get("DEBUG", "").lower() in ("1", "t", "true")

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("2025-7")

    if DEBUG:
        logger.setLevel(logging.DEBUG)
        lines = read_input("2025/7/input_test.txt")
    else:
        lines = read_input("2025/7/input.txt")

    # Part 1
    result1 = part1(lines)
    logger.info(f"Part 1: {result1}")

    # Part 2
    result2 = part2(lines)
    logger.info(f"Part 2: {result2}")
