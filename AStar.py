from Classes8Game import Position


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
        else:  # 8
            accumulator += abs(i - 8)
    return accumulator

def a_star(start):
    closed_set = []
    open_set = [start]
    came_from = {}
    g_score = {}
    g_score[start] = 0

    f_score = {}
    f_score[start] = heuristic_1(start.configuration)

    while len(open_set) > 0:

        for i in open_set:
            print(i)

        input("")
        current = open_set.pop(0)
        if current.is_final():
            return reconstruct_path(came_from, current)

        closed_set.append(current)

        for action in current.available_actions():
            new_state = current.move(action)
            if new_state in closed_set:
                continue
            if new_state not in open_set:
                open_set.append(new_state)

            tentative_g_score = g_score[current] + 1
            if new_state in g_score:
                if tentative_g_score >= g_score[new_state]:
                    continue

            came_from[new_state] = current
            g_score[new_state] = tentative_g_score
            f_score[new_state] = g_score[new_state] + heuristic_1(new_state.configuration)

    return None

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        total_path.append(current)
    return total_path
