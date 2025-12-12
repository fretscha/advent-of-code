# https://adventofcode.com/2025/day/4
import logging
import os


def read_input(filename: str) -> list[str]:
    """Read the input file and return lines"""
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]


def count_adjacent_rolls(grid: list[str], row: int, col: int) -> int:
    """Count how many rolls (@) are adjacent to position (row, col)"""
    count = 0

    # Check all 8 adjacent positions
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        # Check bounds
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[new_row]):
            if grid[new_row][new_col] == "@":
                count += 1

    return count


def part1(lines: list[str]) -> int:
    """
    Count rolls of paper that can be accessed by forklifts
    (rolls with fewer than 4 adjacent rolls).
    Returns:
        _type_: int
    """
    accessible_count = 0

    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == "@":
                adjacent_rolls = count_adjacent_rolls(lines, row, col)
                if adjacent_rolls < 4:
                    accessible_count += 1
                    logger.debug(f"Roll at ({row}, {col}) has {adjacent_rolls} adjacent rolls - accessible")

    return accessible_count


def part2(lines: list[str]) -> int:
    """
    Repeatedly remove accessible rolls until no more can be removed.
    Returns:
        _type_: int (total number of rolls removed)
    """
    # Convert to mutable grid
    grid = [list(line) for line in lines]
    total_removed = 0

    while True:
        # Find all accessible rolls in current iteration
        accessible = []
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "@":
                    adjacent_rolls = count_adjacent_rolls(["".join(r) for r in grid], row, col)
                    if adjacent_rolls < 4:
                        accessible.append((row, col))

        # If no accessible rolls, we're done
        if not accessible:
            break

        # Remove all accessible rolls
        for row, col in accessible:
            grid[row][col] = "."
            total_removed += 1

        logger.debug(f"Removed {len(accessible)} rolls this iteration. Total: {total_removed}")

    return total_removed


if __name__ == "__main__":
    DEBUG = os.environ.get("DEBUG", "").lower() in ("1", "t", "true")

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("2025-4")

    if DEBUG:
        logger.setLevel(logging.DEBUG)
        lines = read_input("2025/4/input_test.txt")
    else:
        lines = read_input("2025/4/input.txt")

    # Part 1
    result1 = part1(lines)
    logger.info(f"Part 1: {result1}")

    # Part 2
    result2 = part2(lines)
    logger.info(f"Part 2: {result2}")
