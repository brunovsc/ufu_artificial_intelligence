from Classes8Game import State

def depth_first_search(state):
    def state_not_explored(state_to_explore):
        flag = False
        for explored in explored_states:
            if state_to_explore.configuration == explored.configuration:
                flag = True
        print(state_to_explore.configuration, flag)
        return not flag

    def recursive_depth(state_to_explore, path=[]):
        state_to_explore.path.append(state_to_explore)
        explored_states.append(state_to_explore)
        if state_to_explore.is_final():
            return state_to_explore
        for action in state_to_explore.available_actions():
            new_state = State(list(state_to_explore.configuration), state_to_explore.white_space)
            print('config before movement: ',new_state.configuration)
            print('action: ',action)
            new_state.configuration, new_state.white_space = new_state.move(action)
            print('config after movement: ',new_state.configuration)
            generate_states.append(new_state)
            if state_not_explored(new_state):
                return recursive_depth(new_state)

    explored_states = []
    generate_states = []
    solution = recursive_depth(state)

    return None if not solution else solution.path, len(generate_states), len(explored_states)


test_config = [1,2,0,3,4,5,6,7,8]
print(depth_first_search(State(test_config, 2)))