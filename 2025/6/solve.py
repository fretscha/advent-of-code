# https://adventofcode.com/2025/day/6
import logging
import os


def read_input(filename: str) -> list[any]:
    """Read the input file and return lines"""

    with open(filename, "r") as f:
        return f.readlines()


def part1(lines: list[str]) -> int:
    """
    Compute part 1 solution.
    Returns:
        _type_: int
    """
    rows = [line.rstrip("\n").split() for line in lines if line.strip()]
    # rotate rows to columns
    cols = list(zip(*rows))
    grand_total = 0
    for col in cols:
        if col[-1] == "+":
            _sum = 0
            for val in col[:-1]:
                _sum += int(val)
            grand_total += _sum
        elif col[-1] == "*":
            prod = 1
            for val in col[:-1]:
                prod *= int(val)
            grand_total += prod
    return grand_total


def part2(lines: list[str]) -> int:
    """
    Compute part 2 solution - read the worksheet character-by-character right-to-left.
    Each vertical column of digits forms a number (top = MSD, bottom = LSD).
    Returns:
        _type_: int
    """
    # Pad all lines to same length
    max_len = max(len(line.rstrip("\n")) for line in lines)
    padded_lines = [line.rstrip("\n").ljust(max_len) for line in lines]

    # Separate data rows from operator row
    data_rows = padded_lines[:-1]
    operator_row = padded_lines[-1]

    # Find operator positions (which define problems)
    operator_positions = []
    for i, c in enumerate(operator_row):
        if c in ["+", "*"]:
            operator_positions.append(i)

    # Process each problem
    grand_total = 0
    for op_pos in operator_positions:
        operator = operator_row[op_pos]
        numbers = []

        # Scan rightward from operator position to collect digit columns
        scan_pos = op_pos
        while scan_pos < max_len:
            # Get vertical column
            col = [data_rows[r][scan_pos] for r in range(len(data_rows))]

            # Stop if we hit another operator or problem boundary
            if scan_pos > op_pos and operator_row[scan_pos] in ["+", "*"]:
                break

            # Collect digits in this column (top to bottom)
            digits = [c for c in col if c.isdigit()]
            if digits:
                # Form number from digits (top = MSD, bottom = LSD)
                num = int("".join(digits))
                numbers.append(num)
            elif scan_pos > op_pos and all(c == " " for c in col):
                # Empty column marks end of this problem
                break

            scan_pos += 1

        # Compute result for this problem
        if numbers:
            if operator == "+":
                result = sum(numbers)
            else:  # operator == "*"
                result = 1
                for n in numbers:
                    result *= n
            grand_total += result

    return grand_total


if __name__ == "__main__":
    DEBUG = os.environ.get("DEBUG", "").lower() in ("1", "t", "true")

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("2025-6")

    if DEBUG:
        logger.setLevel(logging.DEBUG)
        lines = read_input("2025/6/input_test.txt")
    else:
        lines = read_input("2025/6/input.txt")

    # Part 1
    result1 = part1(lines)
    logger.info(f"Part 1: {result1}")

    # Part 2
    result2 = part2(lines)
    logger.info(f"Part 2: {result2}")
