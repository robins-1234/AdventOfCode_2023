def read_input() -> list[str]:
    file = open("input.txt", "r")
    result = file.read().strip().split('\n')
    file.close()
    return result


def calc_layer(prev_layer) -> list[int]:
    next_layer = []
    for i in range(0, len(prev_layer) - 1):
        next_layer.append(prev_layer[i + 1] - prev_layer[i])
    return next_layer


def calc_line_result(line, calc_positive) -> int:
    layers = [[int(i) for i in line.split(" ")]]
    
    while True:
        next_layer = calc_layer(layers[len(layers) - 1])
        layers.append(next_layer)
        if all(x == 0 for x in next_layer):
            for i in range(len(layers) - 2, -1, -1):
                prev_layer = layers[i + 1]
                current_layer = layers[i]

                if calc_positive:
                    last_digit = current_layer[len(current_layer) - 1] + prev_layer[len(prev_layer) - 1]
                    current_layer.append(last_digit)
                else:
                    first_digit = current_layer[0] - prev_layer[0]
                    current_layer.insert(0, first_digit)

            if calc_positive:
                return layers[0][len(layers[0]) - 1]
            else:
                return layers[0][0]


def first(file_input: list[str]) -> int:
    all_line_results = []
    for line in file_input:
        line_result = calc_line_result(line, True)

        all_line_results.append(line_result)

    result = 0
    for line_result in all_line_results:
        result += line_result
    return result


def second(file_input: list[str]) -> int:
    all_line_results = []
    for line in file_input:
        line_result = calc_line_result(line, False)
        all_line_results.append(line_result)

    result = 0
    for line_result in all_line_results:
        result += line_result
    return result


assert first(read_input()) == 1819125966
assert second(read_input()) == 1140
