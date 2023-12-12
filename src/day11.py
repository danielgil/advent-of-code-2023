
def part1(input):
    image = [list(line) for line in input]

    empty_rows = set(range(len(image)))
    empty_cols = set(range(len(image[0])))
    for row in range(len(image)):
        for column in range(len(image[0])):
            if image[row][column] != ".":
                if row in empty_rows:
                    empty_rows.remove(row)
                if column in empty_cols:
                    empty_cols.remove(column)
    empty_rows = sorted(list(empty_rows))
    empty_cols = sorted(list(empty_cols))

    print(empty_rows)
    print(empty_cols)

    expanded_image = []

    for row in range(len(image)):
        expanded_image.append([])
        for column in range(len(image[0])):
            expanded_image[-1].append(image[row][column])
            if column in empty_cols:
                expanded_image[-1].append(image[row][column])
        if row in empty_rows:
            expanded_image.append([])
            for column in range(len(image[0])):
                expanded_image[-1].append(image[row][column])
                if column in empty_cols:
                    expanded_image[-1].append(image[row][column])

    galaxies = set()

    for row in range(len(expanded_image)):
        for column in range(len(expanded_image[0])):
            if expanded_image[row][column] == "#":
                galaxies.add((row, column))

    print_image(image)
    print("---")
    print_image(expanded_image)
    print("---")
    print(galaxies)

    total_distance = 0
    for galaxy1 in galaxies:
        for galaxy2 in galaxies:
            if galaxy1 != galaxy2:
                total_distance += distance_between_galaxies(galaxy1, galaxy2)
    print(total_distance)
    return total_distance // 2


def part2(input):
    image = [list(line) for line in input]
    galaxies = set()

    empty_rows = set(range(len(image)))
    empty_cols = set(range(len(image[0])))
    for row in range(len(image)):
        for column in range(len(image[0])):
            if image[row][column] != ".":
                if row in empty_rows:
                    empty_rows.remove(row)
                if column in empty_cols:
                    empty_cols.remove(column)
                galaxies.add((row, column))
    empty_rows = sorted(list(empty_rows))
    empty_cols = sorted(list(empty_cols))

    print(empty_rows)
    print(empty_cols)

    total_distance = 0
    for galaxy1 in galaxies:
        for galaxy2 in galaxies:
            if galaxy1 != galaxy2:
                total_distance += distance_between_galaxies_far_apart(galaxy1, galaxy2, empty_rows, empty_cols)
    return total_distance // 2


def distance_between_galaxies_far_apart(galaxy1, galaxy2, empty_rows, empty_cols):
    y_distance = galaxy1[0] - galaxy2[0] if galaxy1[0] >= galaxy2[0] else galaxy2[0] - galaxy1[0]
    x_distance = galaxy1[1] - galaxy2[1] if galaxy1[1] >= galaxy2[1] else galaxy2[1] - galaxy1[1]
    emptiness_counter = 0

    if galaxy1[0] > galaxy2[0]:
        max_y = galaxy1[0]
        min_y = galaxy2[0]
    else:
        max_y = galaxy2[0]
        min_y = galaxy1[0]

    if galaxy1[1] > galaxy2[1]:
        max_x = galaxy1[1]
        min_x = galaxy2[1]
    else:
        max_x = galaxy2[1]
        min_x = galaxy1[1]

    for empty_row in empty_rows:
        if empty_row > min_y and empty_row < max_y:
            emptiness_counter += 1
    for empty_col in empty_cols:
        if empty_col > min_x and empty_col < max_x:
            emptiness_counter += 1

    return y_distance + x_distance + (emptiness_counter * (1000000 - 1))


def distance_between_galaxies(galaxy1, galaxy2):
    y_distance = galaxy1[0] - galaxy2[0] if galaxy1[0] >= galaxy2[0] else galaxy2[0] - galaxy1[0]
    x_distance = galaxy1[1] - galaxy2[1] if galaxy1[1] >= galaxy2[1] else galaxy2[1] - galaxy1[1]
    print(f"Distance between {galaxy1} and {galaxy2} = {y_distance + x_distance}")
    return y_distance + x_distance

def is_row_empty(image, row):
    for space in image[row]:
        if space != ".":
            return False
    return True


def is_col_empty(image, column):
    for row in image:
        if image[row][column] != ".":
            return False
    return True

def print_image(galaxy):
    for line in galaxy:
        print(" ".join(line))