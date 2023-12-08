
card_to_score = {
    "2": "b",
    "3": "c",
    "4": "d",
    "5": "e",
    "6": "f",
    "7": "g",
    "8": "h",
    "9": "i",
    "T": "j",
    "J": "k",
    "Q": "l",
    "K": "m",
    "A": "n"
}

card_to_score_part2 = {
    "J": "a",
    "2": "b",
    "3": "c",
    "4": "d",
    "5": "e",
    "6": "f",
    "7": "g",
    "8": "h",
    "9": "i",
    "T": "j",
    "Q": "k",
    "K": "l",
    "A": "m"
}

key_to_type = {
    "a": "high",
    "b": "pair",
    "c": "double pair",
    "d": "trio",
    "e": "full",
    "f": "poker",
    "g": "5kind"
}
def part1(data):
    hands = [{"cards": line.split(" ")[0], "bid": int(line.split(" ")[1])} for line in data]
    for hand in hands:
        hand["score"] = score_cards(hand["cards"])

    sorted_hands = sorted(hands, key=lambda x: x["score"])

    rank = 1
    for hand in sorted_hands:
        hand["rank"] = rank
        rank += 1

    total = 0
    for hand in hands:
        total += hand["rank"] * hand["bid"]
    return total

def score_cards(cards):
    card_list = sorted(list(cards))
    types = {}
    for card in card_list:
        if card in types:
            types[card] += 1
        else:
            types[card] = 1
    types = list(reversed(sorted(types.values())))

    if types[0] == 5:
        score = "g"
    elif types[0] == 4:
        score = "f"
    elif types[0] == 3 and types[1] == 2:
        score = "e"
    elif types[0] == 3:
        score = "d"
    elif types[0] == 2 and types[1] == 2:
        score = "c"
    elif types[0] == 2:
        score = "b"
    else:
        score = "a"
    for card in cards:
        score += card_to_score[card]
    return score

def part2(data):
    hands = [{"cards": line.split(" ")[0], "bid": int(line.split(" ")[1])} for line in data]
    for hand in hands:
        hand["score"] = score_cards_part2(hand["cards"])

    sorted_hands = sorted(hands, key=lambda x: x["score"])

    rank = 1
    for hand in sorted_hands:
        hand["rank"] = rank
        rank += 1

    total = 0
    for hand in hands:
        total += hand["rank"] * hand["bid"]
    return total




def score_cards_part2(cards):
    card_list = sorted(list(cards))
    types = {}
    jokers = 0
    for card in card_list:
        if card == "J":
            jokers += 1
        else:
            if card in types:
                types[card] += 1
            else:
                types[card] = 1
    types = list(reversed(sorted(types.values())))
    if types:
        types[0] += jokers

    if not types:
        score = "g"
    elif types[0] == 5:
        score = "g"
    elif types[0] == 4:
        score = "f"
    elif types[0] == 3 and types[1] == 2:
        score = "e"
    elif types[0] == 3:
        score = "d"
    elif types[0] == 2 and types[1] == 2:
        score = "c"
    elif types[0] == 2:
        score = "b"
    else:
        score = "a"
    for card in cards:
        score += card_to_score_part2[card]
    return score



