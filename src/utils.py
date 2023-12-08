import pathlib
import json
from pygments import formatters, highlight, lexers


def get_input(filename: str):
    puzzle_input = pathlib.Path(filename).read_text().strip().splitlines()
    print(f"Read {len(puzzle_input)} lines from {filename}")
    return puzzle_input


def pretty_print(input: dict):
    formatted_result = json.dumps(input, indent=4)
    highlighted_result = highlight(formatted_result, lexers.JsonLexer(), formatters.TerminalFormatter())
    print(highlighted_result)
