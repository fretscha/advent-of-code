import os
import sys
from datetime import datetime
from pathlib import Path

import requests
from dotenv import load_dotenv
from html_to_markdown import convert
from jinja2 import Environment, FileSystemLoader

load_dotenv()

SESSION_COOKIE = os.getenv("AOC_SESSION_COOKIE")

cookies = {"session": SESSION_COOKIE}


def get_input(day: int, year: int = None) -> str:
    if year is None:
        year = datetime.now().year

    response = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input", cookies=cookies
    )
    response.raise_for_status()
    return response.text


def get_puzzle(day: int, year: int = None) -> str:
    if year is None:
        year = datetime.now().year

    response = requests.get(
        f"https://adventofcode.com/{year}/day/{day}", cookies=cookies
    )
    response.raise_for_status()
    return convert(response.text)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get_input.py <day> [year]")
        sys.exit(1)

    day = int(sys.argv[1])
    year = int(sys.argv[2]) if len(sys.argv) > 2 else datetime.now().year

    puzzle_input = get_input(day, year)
    puzzle_page = get_puzzle(day, year)
    # Create directory structure
    output_dir = os.path.join(str(year), str(day))
    os.makedirs(output_dir, exist_ok=True)

    # Write input to file
    output_file = os.path.join(output_dir, "input.txt")
    with open(output_file, "w") as f:
        f.write(puzzle_input)

    print(f"Input saved to {output_file}")

    # Write input to file
    output_file = os.path.join(output_dir, "README.md")
    with open(output_file, "w") as f:
        f.write(puzzle_page)

    print(f"Puzzle saved to {output_file}")

    # solve.py
    path = Path(f"{year}/{day}/solve.py")
    if not path.exists():
        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template("solve.py")
        rendered_content = template.render(year=year, day=day)
        with open(path, "w") as f:
            f.write(rendered_content)
