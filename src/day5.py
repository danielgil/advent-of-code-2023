import re


def part1(data):
    seeds = re.findall(r'\d+', data[0])

    print(f"Seeds = {seeds}")

    maps = []
    for line in data[2:]:
        if not line:
            continue
        if "map" in line:
            maps.append([])
            continue
        split_line = re.findall(r'\d+', line)
        add_range_to_map(maps[-1], int(split_line[0]), int(split_line[1]), int(split_line[2]))

    locations = []
    for seed in seeds:
        locations.append(find_seed_location(int(seed), maps))
    return min(locations)

def part2(data):
    pairs = re.findall(r'\d+ \d+', data[0])
    seed_ranges = []
    for seed_range in pairs:
        split_pair = seed_range.split(" ")
        seed_ranges.append((int(split_pair[0]), int(split_pair[0]) + int(split_pair[1])))
    print(f"Seed ranges = {seed_ranges}")

    maps = []
    for line in data[2:]:
        if not line:
            continue
        if "map" in line:
            maps.append([])
            continue
        split_line = re.findall(r'\d+', line)
        add_range_to_map(maps[-1], int(split_line[0]), int(split_line[1]), int(split_line[2]))

    current_ranges = seed_ranges
    for map in maps:
        next_ranges = []
        for current_range in current_ranges:
            next_ranges += find_range_in_map(map, current_range)
        current_ranges = next_ranges

    return min([range[0] for range in current_ranges])


def find_seed_location(seed, maps):
    current_index = seed
    for map in maps:
        current_index = find_in_map(map, current_index)
    return current_index


def add_range_to_map(map, destination_range_start, source_range_start, range_length):
    map.append({"start": source_range_start, "delta": destination_range_start - source_range_start, "length": range_length})


def find_in_map(map, index):
    for range_dict in map:
        start = range_dict["start"]
        end = range_dict["start"] + range_dict["length"]

        if start <= index < end:
            return index + range_dict["delta"]
    return index


def find_range_in_map(map, range):
    """
    Given a map and a range, return a list of ranges describing all the elements after being mapped
    """
    print(f"finding range {range} in map {map}")
    mapped_ranges = []
    unmapped_ranges = [range]

    for range_dict in map:
        remaining_ranges = unmapped_ranges.copy()
        unmapped_ranges = []
        for considered_range in remaining_ranges:
            start = range_dict["start"]
            end = range_dict["start"] + range_dict["length"]

            # The considered range is completely contained in the range_dict
            if start <= considered_range[0] < end and start <= considered_range[1] < end:
                mapped_ranges.append((considered_range[0] + range_dict["delta"], considered_range[1] + range_dict["delta"]))
                continue
            # The considered range has the lower bound inside the range_dict
            if start <= considered_range[0] < end <= range[1]:
                mapped_ranges.append((considered_range[0] + range_dict["delta"], end - 1 + range_dict["delta"]))
                unmapped_ranges.append((end, considered_range[1]))
                continue
            # The considered range has the upper bound inside the range_dict
            if considered_range[0] < start <= considered_range[1] < end:
                unmapped_ranges.append((considered_range[0], start - 1))
                mapped_ranges.append((start + range_dict["delta"], considered_range[1] + range_dict["delta"]))
                continue
            # The considered range is bigger than range_dict in both directions
            if considered_range[0] < start <= end < considered_range[1]:
                unmapped_ranges.append((considered_range[0], start - 1))
                mapped_ranges.append((start + range_dict["delta"], end + range_dict["delta"]))
                unmapped_ranges.append((end + 1, considered_range[1]))
                continue
            # The considered range doesn't overlap with the range_dict
            if considered_range[1] < start or considered_range[0] >= end:
                unmapped_ranges.append(considered_range)
    return mapped_ranges + unmapped_ranges

