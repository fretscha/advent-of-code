# https://adventofcode.com/2025/day/3
import logging
import os


def read_input(filename: str) -> list[str]:
    """Read the input file and return lines"""
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]


def find_max_joltage(bank: str) -> int:
    """Find the maximum joltage from a bank by selecting 2 batteries"""
    max_joltage = 0

    # Try all pairs of batteries (not necessarily adjacent)
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            # Form the joltage from these two batteries (in order)
            joltage = int(bank[i] + bank[j])
            if joltage > max_joltage:
                max_joltage = joltage
                logger.debug(f"Bank {bank}: Found new max {joltage} at positions {i},{j}")

    return max_joltage


def part1(lines: list[str]) -> int:
    """
    Find the total output joltage by summing max joltage from each bank.
    Returns:
        _type_: int
    """
    total = 0
    for bank in lines:
        if bank:  # Skip empty lines
            max_joltage = find_max_joltage(bank)
            logger.debug(f"Bank {bank[:20]}...: max joltage = {max_joltage}")
            total += max_joltage

    return total


def find_max_joltage_n(bank: str, n: int) -> int:
    """Find the maximum joltage from a bank by selecting exactly n batteries"""
    # We want to select n digits that form the largest number
    # Strategy: greedily select the largest digit at each position
    # that still leaves enough digits remaining

    result = []
    remaining_needed = n
    start_pos = 0

    for _ in range(n):
        # We need to leave enough digits after this selection
        # to complete the remaining selections
        max_digit = -1
        max_pos = -1

        # Look through positions where we can still select remaining_needed digits
        end_pos = len(bank) - remaining_needed + 1

        for i in range(start_pos, end_pos):
            digit = int(bank[i])
            if digit > max_digit:
                max_digit = digit
                max_pos = i

        result.append(str(max_digit))
        logger.debug(f"Selected digit {max_digit} from position {max_pos}")
        start_pos = max_pos + 1
        remaining_needed -= 1

    return int("".join(result))


def part2(lines: list[str]) -> int:
    """
    Find the total output joltage by selecting exactly 12 batteries from each bank.
    Returns:
        _type_: int
    """
    total = 0
    for bank in lines:
        if bank:  # Skip empty lines
            max_joltage = find_max_joltage_n(bank, 12)
            logger.debug(f"Bank {bank[:20]}...: max 12-digit joltage = {max_joltage}")
            total += max_joltage

    return total


if __name__ == "__main__":
    DEBUG = os.environ.get("DEBUG", "").lower() in ("1", "t", "true")
    print(f"DEBUG={DEBUG}")
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("2025-3")

    if DEBUG:
        logger.setLevel(logging.DEBUG)
        lines = read_input("2025/3/input_test.txt")
    else:
        lines = read_input("2025/3/input.txt")

    # Part 1
    result1 = part1(lines)
    logger.info(f"Part 1: {result1}")

    # Part 2
    result2 = part2(lines)
    logger.info(f"Part 2: {result2}")
