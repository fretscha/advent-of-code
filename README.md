# advent-of-code

Advent of Code solutions repository using Python 3.12+ and `uv` for dependency management.

## Setup

**Install dependencies:**

```bash
uv sync
```

**Environment configuration:**

Create a `.env` file in the project root with your Advent of Code session cookie:

```
AOC_SESSION_COOKIE=<your_session_cookie_value>
```

## Usage

**Fetch puzzle input, description, and generate solution template:**

```bash
uv run python get_day.py <day> [year]
```

Examples:

- `uv run python get_day.py 1` - Fetches day 1 for current year, saves to `<year>/1/input.txt`, `<year>/1/README.md`, and generates `<year>/1/solve.py` from template
- `uv run python get_day.py 1 2024` - Fetches day 1 for 2024, saves to `2024/1/input.txt`, `2024/1/README.md`, and generates `2024/1/solve.py` from template

**Run solutions:**

```bash
uv run python 2025/1/solve.py
```

## Repository Structure

Solutions are organized by year in directories: `2024/`, `2025/`, etc.

**Utility files:**

- [get_day.py](get_day.py): Fetches puzzle inputs and descriptions from adventofcode.com, saves them to `<year>/<day>/input.txt` and `<year>/<day>/README.md`, and generates `<year>/<day>/solve.py` from template
- [main.py](main.py): Entry point (currently a placeholder)
- [templates/](templates/): Contains Jinja2 templates used to generate solution files

## Dependencies

- `requests`: HTTP client for fetching puzzle inputs
- `python-dotenv`: Loads environment variables from `.env`
- `html-to-markdown`: Converts HTML puzzle descriptions to markdown
- `jinja2`: Template engine for generating solution files
