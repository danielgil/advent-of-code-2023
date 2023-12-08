import re
from math import lcm

def part1(data):
    instructions = list(data[0])

    nodes = {}

    for line in data[2:]:
        matches = re.search(r'(\w+) = \((\w+), (\w+)\)', line)
        name = matches.group(1)
        left = matches.group(2)
        right = matches.group(3)
        nodes[name] = {"left": left, "right": right}

    current_node = "AAA"
    steps = 0

    while True:
        for instruction in instructions:
            if current_node == "ZZZ":
                return steps
            if instruction == "L":
                current_node = nodes[current_node]["left"]
            else:
                current_node = nodes[current_node]["right"]
            steps += 1


def part2(data):
    instructions = list(data[0])

    nodes = {}
    starting_nodes = []

    for line in data[2:]:
        matches = re.search(r'(\w+) = \((\w+), (\w+)\)', line)
        name = matches.group(1)
        left = matches.group(2)
        right = matches.group(3)
        nodes[name] = {"left": left, "right": right}
        if name[-1] == "A":
            starting_nodes.append(name)

    all_cycles = [find_z(node, instructions, nodes) for node in starting_nodes]
    return lcm(*all_cycles)


def find_z(starting_node, instructions, nodes):
    current_node = starting_node
    steps = 0

    while True:
        for instruction in instructions:
            if current_node[-1] == "Z":
                return steps
            if instruction == "L":
                current_node = nodes[current_node]["left"]
            else:
                current_node = nodes[current_node]["right"]
            steps += 1
