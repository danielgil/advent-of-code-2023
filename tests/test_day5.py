from src.utils import get_input
from src.day5 import part1, part2, find_range_in_map

def test_day5_part1_example():
    inputs = get_input("inputs/day5/day5_example.txt")
    assert part1(inputs) == 35

def test_day5_part1():
    inputs = get_input("inputs/day5/day5.txt")
    assert part1(inputs) == 289863851

def test_day5_part2_example():
    inputs = get_input("inputs/day5/day5_example.txt")
    assert part2(inputs) == 46

def test_day5_part2():
    inputs = get_input("inputs/day5/day5.txt")
    assert part2(inputs) == 60568880


def test_find_range_in_map():
    map = [{"start": 5, "delta": 10, "length": 5}]
    test_range = (10, 20)
    assert [test_range] == find_range_in_map(map, test_range)
    test_range = (1, 5)
    assert sorted([(1, 4), (15, 15)]) == sorted(find_range_in_map(map, test_range))
    test_range = (9, 13)
    assert sorted([(19, 19), (10, 13)]) == sorted(find_range_in_map(map, test_range))
    test_range = (7, 8)
    assert [(17, 18)] == find_range_in_map(map, test_range)
    test_range = (3, 12)
    assert sorted([(3, 4), (15, 20), (11, 12)]) == sorted(find_range_in_map(map, test_range))

    map = [{"start": 5, "delta": 10, "length": 5}, {"start": 20, "delta": 10, "length": 10}]
    test_range = (1, 50)
    assert sorted([(1, 4), (11, 19), (15, 20), (30, 40), (31, 50)]) == sorted(find_range_in_map(map, test_range))


