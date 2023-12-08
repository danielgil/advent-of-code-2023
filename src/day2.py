import re
from src.utils import pretty_print

red_regex = re.compile(r" (\d+) red")
green_regex = re.compile(r" (\d+) green")
blue_regex = re.compile(r" (\d+) blue")


def part1(input: str):
    games = parse_games(input)

    total = 0
    for game in games:
        if is_possible(game):
            total += game["id"]
    return total

def part2(input: str):
    games = parse_games(input)

    total = 0
    for game in games:
        power = game["max_red"] * game["max_green"] * game["max_blue"]
        total += power
    return total


def is_possible(game):
    max_red = 12
    max_gren = 13
    max_blue = 14
    return game["max_red"] <= max_red and game["max_blue"] <= max_blue and game["max_green"] <= max_gren


def parse_games(input):
    game_counter = 0
    games = []
    for line in input:
        game_counter += 1
        game = {
            "id": game_counter,
            "sets": [],
            "max_red": 0,
            "max_green": 0,
            "max_blue": 0
        }
        for game_set in line.split(";"):
            parsed_set = {"blue": 0, "red": 0, "green": 0}
            if red_regex.search(game_set):
                parsed_set["red"] = int(red_regex.search(game_set).group(1))
                if parsed_set["red"] > game["max_red"]:
                    game["max_red"] = parsed_set["red"]
            if green_regex.search(game_set):
                parsed_set["green"] = int(green_regex.search(game_set).group(1))
                if parsed_set["green"] > game["max_green"]:
                    game["max_green"] = parsed_set["green"]
            if blue_regex.search(game_set):
                parsed_set["blue"] = int(blue_regex.search(game_set).group(1))
                if parsed_set["blue"] > game["max_blue"]:
                    game["max_blue"] = parsed_set["blue"]
            game["sets"].append(parsed_set)
        games.append(game)
    pretty_print({"result": games})
    return games