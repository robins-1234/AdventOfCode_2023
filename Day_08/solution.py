import math
import re


def read_input():
    file = open("input.txt", "r")
    result = file.read().strip().split('\n')
    file.close()
    return result


class NodeList:

    def __init__(self, *lines):
        self.elements = dict()
        for line in lines:
            words = re.findall('\w*', line)
            while "" in words:
                words.remove("")
            self.add_node(words[0], words[1], words[2])

    def add_node(self, name, left, right):
        self.elements[name] = (left, right)

    def parse_tree(self, node, direction):
        if direction == "L":
            return self.elements[node][0]
        else:
            return self.elements[node][1]

    def get_starting_nodes(self):
        starters = []
        for e in self.elements:
            if e[2] == "A":
                starters.append(e)
        return starters


def first(file_input: list[str]):
    direction, *others = file_input
    tree = NodeList(*others[1::])

    count = 0
    current_node = "AAA"
    while current_node != "ZZZ":
        for letter in direction:
            current_node = tree.parse_tree(current_node, letter)
            count += 1
            if current_node == "ZZZ":
                break
    return count


def get_node_value(direction, node, tree) -> int:
    count = 0
    while node[2] != "Z":
        for letter in direction:
            count += 1
            node = tree.parse_tree(node, letter)
            if node[2] == "Z":
                break
    return count


def second(file_input: list[str]):
    direction, *others = file_input
    tree = NodeList(*others[1::])

    starting_nodes = tree.get_starting_nodes()

    path_values = []
    for node in starting_nodes:
        path_values.append(get_node_value(direction, node, tree))

    return math.lcm(*path_values)


assert first(read_input()) == 15517
assert second(read_input()) == 14935034899483
