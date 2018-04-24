from Classes8Game import State

explored_states = []
generate_states = []


def depth_search(state):
    states_to_explore = []
    explored_states = []

    generated_states = 0
    states_to_explore.append(state)

    while len(states_to_explore) > 0:
        current = states_to_explore[0]
        del states_to_explore[0]

        explored_states.append(current)
        if current.is_final():
            return reconstruct_path(current), generated_states, len(explored_states)

        children = []
        for action in current.available_actions():
            new_configuration, new_white_space = current.move(action)
            new_state = State(new_configuration, new_white_space)
            new_state.predecessor = current

            alreadyExplored = False
            for state_explored in explored_states:
                if state_explored.configuration == new_state.configuration:
                    alreadyExplored = True

            if not alreadyExplored:
                children.append(new_state)

        states_to_explore = children + states_to_explore
        generated_states += len(children)

    return None, None, None

def reconstruct_path(current):
    total_path = [current]
    while current.predecessor is not None:
        current = current.predecessor
        total_path.append(current)
    return total_path