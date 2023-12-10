import re


def readInput():
    file = open("Day_05\input.txt", "r")
    result = file.readlines()
    file.close
    return result


def main(input):
    regex = "\d+"
    maps = []
    current_map = []

    seeds = []
    ##gather mapdata
    for line in input:
        if line[0:5] == "seeds":
            seeds = re.findall(regex, input[input.index(line)])
            seeds = [int(i) for i in seeds]
            continue

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

    minimum = -1
    for seed in seeds:
        for ranges_of_current_map in maps:
            for current_range in ranges_of_current_map:
                if (seed >= current_range[0]) & (seed <= current_range[1]):
                    seed = seed - current_range[2]
                    break
        if (minimum == -1) | (seed < minimum):
            minimum = seed

    print(minimum)


main(readInput())
