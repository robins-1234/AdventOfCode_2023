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
            current_start = digits[1]
            current_end = digits[1] + digits[2] - 1
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

    ##gather mapdata
    maps = gather_map_data(input)
    maps = [sorted(map) for map in maps]

    # seperate seeds
    seed_pairs = seperate_seeds(seeds)

    minimum = get_minimum(maps, seed_pairs)

    print(minimum)


def get_minimum(maps, seed_pairs):
    minimum = -1
    for pair in seed_pairs:
        minimum = analyze_seeds(maps, minimum, pair)
    return minimum


def analyze_seeds(maps, minimum, pair):
    for seed in range(pair[0], pair[0] + pair[1]):
        seed = get_next_value(seed, maps)
        if (minimum == -1) | (seed < minimum):
            minimum = seed
    print("seedpair complete")
    return minimum


def get_next_value(seed, maps):
    for ranges_of_current_map in maps:
        for current_range in ranges_of_current_map:
            if (seed >= current_range[0]) & (seed <= current_range[1]):
                seed = seed - current_range[2]
                break
    return seed


main(readInput())
"""  
humidity-to-location map:
60 56 37
56 93 4

Bessere nach schlechtere Werte:
0-56 -> 93-96 -> 56-93 -> >96


temperature-to-humidity map:
0 69 1
1 0 69

69-70 -> 0-69 -> >70
"""
