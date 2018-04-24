
def heuristic_1(configuration):
    final_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    accumulator = 0
    for i in range(8):
        if configuration[i] != final_state[i]:
            accumulator += 1
    return accumulator


def heuristic_2(configuration):
    accumulator = 0
    for i in range(8):
        if configuration[i] == 0:
            accumulator += abs(i - 0)
        elif configuration[i] == 1:
            accumulator += abs(i - 1)
        elif configuration[i] == 2:
            accumulator += abs(i - 2)
        elif configuration[i] == 3:
            accumulator += abs(i - 3)
        elif configuration[i] == 4:
            accumulator += abs(i - 4)
        elif configuration[i] == 5:
            accumulator += abs(i - 5)
        elif configuration[i] == 6:
            accumulator += abs(i - 6)
        elif configuration[i] == 7:
            accumulator += abs(i - 7)
        else:
            accumulator += abs(i - 8)
    return accumulator


def heuristic_3(configuration):
    return heuristic_1(configuration) + heuristic_2(configuration)

print(heuristic_2([7, 8, 5, 4, 0, 6, 1, 2, 3]))
