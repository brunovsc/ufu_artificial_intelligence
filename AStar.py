

def a_star(start_state):
    closed_set = []
    open_set = [start_state]

    came_from = {}
    cost_to_state = {}

    came_from[start_state] = None
    cost_to_state[start_state] = 0

    while len(open_set) > 0:
        current_state = open_set.pop(0)
        if current_state.is_final():
            break

        for action in current_state.white_space.available_actions():
            new_state = current_state.white_space.move(action)
            new_cost = cost_to_state[current_state] + 1
            if new_state not in cost_to_state or new_cost < cost_to_state[new_state]:
                cost_to_state[new_state] = new_cost





def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far