import re


regex = "\d+"


def readInput():
    file = open("Day_05\input2.txt", "r")
    result = file.readlines()
    file.close
    return result


def gather_map_data(input: list):
    current_map = []
    maps = []
    del input[0]
    for line in input:
        if any(char.isdigit() for char in line):
            digits = re.findall(regex, line)
            digits = [int(i) for i in digits]
            current_start = digits[0]
            current_end = digits[0] + digits[2] - 1
            diff = digits[1] - digits[0]
            current_range = [current_start, current_end, diff]
            current_map.append(current_range)
        else:
            if len(current_map) > 0:
                maps.append(current_map)
            current_map = []
    maps.append(current_map)
    return maps


def seperate_seeds(seeds):
    seed_pairs = []
    while len(seeds) > 0:
        seed_pairs.append([seeds[0], seeds[1]])
        del seeds[0]
        del seeds[0]
    return seed_pairs


def main(input):
    seeds = []

    # gather seeds
    seeds = re.findall(regex, input[0])
    seeds = [int(i) for i in seeds]
    seed_pairs = seperate_seeds(seeds)

    ##gather mapdata
    maps = gather_map_data(input)
    maps = [sorted(map) for map in maps]
    maps.reverse()

    ##trylocations, starting with best location
    best_location_found = False
    minimum = 0
    best_location = 0
    while not best_location_found:
        best_location = minimum
        for map in maps:
            best_location = find_best_spot(map, best_location)
            print(best_location)
        for pair in seed_pairs:
            if best_location in range(pair[0], pair[0] + pair[1]):
                best_location_found = True
                break
        minimum += 1
        print()
    print(minimum - 1)


def find_best_spot(current_map, best_location):
    for current_range in current_map:
        if best_location in range(current_range[0], current_range[1]):
            return best_location + current_range[2]
    return best_location


main(readInput())
