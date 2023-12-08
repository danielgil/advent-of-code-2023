import re
def part1(data):
    total = 0
    for scorecard in data:
        split_scorecard = scorecard.split(":")[1].split("|")
        winning_numbers = re.findall(r'\d+', split_scorecard[0])
        own_numbers = re.findall(r'\d+', split_scorecard[1])
        wins = len([number for number in winning_numbers if number in own_numbers])
        if wins <= 1:
            total += wins
        else:
            total += 2 ** (wins - 1)
    return total


def part2(data):
    total = 0
    pile = []
    for scorecard in data:
        split_scorecard = scorecard.split(":")[1].split("|")
        winning_numbers = re.findall(r'\d+', split_scorecard[0])
        own_numbers = re.findall(r'\d+', split_scorecard[1])
        pile.append({"winning": winning_numbers, "own": own_numbers})

    for index in range(len(pile)):
        total += get_scorecards(index, pile)
    return total

def get_scorecards(current_index, pile):
    if current_index >= len(pile):
        return 0
    wins = len([number for number in pile[current_index]["winning"] if number in pile[current_index]["own"]])

    score = 1
    for index in range(current_index + 1, current_index + wins + 1):
        score += get_scorecards(index, pile)
    return score




