# https://adventofcode.com/2025/day/2

import logging
import os


def read_input(filename: str) -> list[tuple[int, int]]:
    """Read the input file and return lis"""
    with open(filename, "r") as f:
        return f.read().strip()


def is_invalid_id(num: int) -> bool:
    """Check if a number is invalid (sequence of digits repeated twice)"""
    s = str(num)
    length = len(s)

    # Must be even length to be repeated pattern
    if length % 2 != 0:
        return False

    # Check if first half equals second half
    mid = length // 2
    return s[:mid] == s[mid:]


def parse_ranges(input_str: str) -> list[tuple[int, int]]:
    """Parse comma-separated ranges like '11-22,95-115'"""
    ranges = []
    parts = input_str.split(",")
    for part in parts:
        part = part.strip()
        if part:
            start, end = part.split("-")
            ranges.append((int(start), int(end)))
    return ranges


def part1(input_str: str) -> int:
    """
    Find all invalid IDs in the ranges and sum them.
    Returns:
        _type_: int
    """
    ranges = parse_ranges(input_str)
    total = 0

    for start, end in ranges:
        subtotal_ = 0
        for num in range(start, end + 1):
            if is_invalid_id(num):
                logger.debug(f"Invalid ID found: {num}")
                subtotal_ += num
        logger.debug(f"Processed range {start}-{end} : Subtotal = {subtotal_}")
        total += subtotal_

    return total


def is_invalid_id_part2(num: int) -> bool:
    """Check if a number is invalid (sequence of digits repeated at least twice)"""
    s = str(num)
    length = len(s)

    # Try all possible pattern lengths from 1 to length//2
    for pattern_len in range(1, length // 2 + 1):
        # Check if the entire string can be made by repeating the pattern
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            repetitions = length // pattern_len
            if repetitions >= 2 and pattern * repetitions == s:
                return True

    return False


def part2(input_str: str) -> int:
    """
    Find all invalid IDs (repeated at least twice) in the ranges and sum them.
    Returns:
        _type_: int
    """
    ranges = parse_ranges(input_str)
    total = 0

    for start, end in ranges:
        sub_total = 0
        for num in range(start, end + 1):
            if is_invalid_id_part2(num):
                logger.debug(f"Invalid ID found: {num}")
                sub_total += num
        logger.debug(f"Processed range {start}-{end} : Subtotal = {sub_total}")
        total += sub_total
    return total


if __name__ == "__main__":
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("2025-2")

    if DEBUG:
        logger.setLevel(logging.DEBUG)
        lines = read_input("2025/2/input_test.txt")
    else:
        lines = read_input("2025/2/input.txt")

    # Part 1
    result1 = part1(lines)
    logger.info(f"Part 1: {result1}")

    # Part 2
    result2 = part2(lines)
    logger.info(f"Part 2: {result2}")
