import re


def readInput():
    file = open("Day_06\input.txt", "r")
    result = file.readlines()
    file.close
    return result


def get_edges(race, step):
    if step == -1:
        iterator = range(race[0], 0, step)
    else:
        iterator = range(0, race[0])

    for i in iterator:
        race_range = i * (race[0] - i)
        if race_range > race[1]:
            return i


def first(input: list):
    times = re.findall(r"\d+", input[0])
    distances = re.findall(r"\d+", input[1])
    races = []
    for i in range(0, len(times)):
        races.append((int(times[i]), int(distances[i])))

    result = 1
    for race in races:
        result = result * (get_edges(race, -1) - get_edges(race, 1) + 1)
    print(result)


def second(input: list):
    times = re.findall(r"\d+", input[0])
    distances = re.findall(r"\d+", input[1])

    race = ["", ""]
    for i in range(0, len(times)):
        race[0] = race[0] + times[i]
        race[1] = race[1] + distances[i]
    race = [int(i) for i in race]

    result = 1
    result = result * (get_edges(race, -1) - get_edges(race, 1) + 1)
    print(result)


first(readInput())
second(readInput())
