from Classes8Game import Position
from Classes8Game import State
import operator


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


def apply_heuristic(heuristic, configuration):
    if heuristic == 1:
        return heuristic_1(configuration)
    else:
        return heuristic_2(configuration)


def a_star(start, heuristic):
    closed_set = []
    open_set = [start]

    start.heuristic = apply_heuristic(heuristic, start.configuration)
    start.cost = 0

    states_generated = 0

    while len(open_set) > 0:

        open_set.sort(key=operator.attrgetter('evaluation'))
        current = open_set.pop(0)

        if current.is_final():
            return reconstruct_path(current)

        closed_set.append(current)

        for action in current.available_actions():
            new_configuration, new_white_space = current.move(action)

            states_generated += 1

            new_heuristic = apply_heuristic(heuristic, new_configuration)
            new_cost = current.cost + 1
            new_state = State(new_configuration, new_white_space, new_heuristic, new_cost, current)

            if new_state.is_final():
                return reconstruct_path(new_state), states_generated, len(closed_set)

            already_closed = False
            for closed_state in closed_set:
                if closed_state.configuration == new_state.configuration:
                    already_closed = True
                    break

            if already_closed:
                continue

            already_opened = False
            state_opened = None
            for opened_state in open_set:
                if opened_state.configuration == new_state.configuration:
                    already_opened = True
                    state_opened = opened_state
                    break

            if already_opened:
                if new_state.evaluation < state_opened.evaluation:
                    open_set.remove(state_opened)
                    open_set.append(new_state)
            else:
                open_set.append(new_state)

    return None, None, None


def reconstruct_path(current):
    total_path = [current]
    while current.predecessor is not None:
        current = current.predecessor
        total_path.append(current)
    return total_path
