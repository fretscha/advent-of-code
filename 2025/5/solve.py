# https://adventofcode.com/2025/day/5
import logging
import os


def read_input(filename: str) -> tuple[list[tuple[int, int]], list[int]]:
    """Read the input file and return ranges and ingredient IDs"""
    with open(filename, "r") as f:
        content = f.read().strip()

    # Split by blank line
    sections = content.split("\n\n")

    # Parse ranges
    ranges = []
    for line in sections[0].split("\n"):
        if line.strip():
            parts = line.strip().split("-")
            ranges.append((int(parts[0]), int(parts[1])))

    # Parse ingredient IDs
    ingredient_ids = []
    for line in sections[1].split("\n"):
        if line.strip():
            ingredient_ids.append(int(line.strip()))

    return ranges, ingredient_ids


def is_fresh(ingredient_id: int, ranges: list[tuple[int, int]]) -> bool:
    """Check if an ingredient ID is fresh (falls within any range)"""
    for start, end in ranges:
        if start <= ingredient_id <= end:
            return True
    return False


def part1(ranges: list[tuple[int, int]], ingredient_ids: list[int]) -> int:
    """
    Count how many available ingredient IDs are fresh.
    Returns:
        _type_: int
    """

    fresh_count = 0
    for ingredient_id in ingredient_ids:
        if is_fresh(ingredient_id, ranges):
            logger.debug(f"Ingredient ID {ingredient_id} is fresh")
            fresh_count += 1
        else:
            logger.debug(f"Ingredient ID {ingredient_id} is spoiled")

    return fresh_count


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping ranges"""
    if not ranges:
        return []

    # Sort ranges by start position
    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]

    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]

        # If current range overlaps or is adjacent to last range, merge them
        if current_start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append((current_start, current_end))

    return merged


def count_ids_in_ranges(ranges: list[tuple[int, int]]) -> int:
    """Count total number of IDs covered by ranges"""
    merged = merge_ranges(ranges)
    total = 0

    for start, end in merged:
        # Range is inclusive, so count is (end - start + 1)
        total += end - start + 1
        logger.debug(f"Range {start}-{end} contains {end - start + 1} IDs")

    return total


def part2(ranges: list[tuple[int, int]], ingredient_ids: list[int]) -> int:
    """
    Count total number of ingredient IDs considered fresh by the ranges.
    Returns:
        _type_: int
    """
    return count_ids_in_ranges(ranges)


if __name__ == "__main__":
    DEBUG = os.environ.get("DEBUG", "").lower() in ("1", "t", "true")

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("2025-5")

    if DEBUG:
        logger.setLevel(logging.DEBUG)
        ranges, ingredient_ids = read_input("2025/5/input_test.txt")
    else:
        ranges, ingredient_ids = read_input("2025/5/input.txt")

    # Part 1
    result1 = part1(ranges, ingredient_ids)
    logger.info(f"Part 1: {result1}")

    # Part 2
    result2 = part2(ranges, ingredient_ids)
    logger.info(f"Part 2: {result2}")
