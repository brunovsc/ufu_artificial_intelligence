from Classes import Robot
from Classes import State


def breadth_first_search(state):

    # initialize the list of states to explore with initial state
    states_to_explore = [state]
    # initialize the list of explored states as empty
    explored_states = []

    # selects the initial state as the first state to explore
    state_being_explored = states_to_explore[0]

    # while there are states to explore in the list
    while len(states_to_explore) > 0:

        # verify if stateToExplore is a final state
        if state_being_explored.is_final_state():
            return state_being_explored

        # otherwise, expands stateToExplore
        for action in state.robot.actions:
            # for each action, get the new state based on the state being explored
            new_state = State(list(state_being_explored.spaceConfiguration),
                              Robot(state_being_explored.robot.position, list(state_being_explored.robot.actionsTaken)))
            new_state.apply_action(action)

            # check if the new state is in the lists
            already_explored = False
            already_listed = False

            # check if the new state is in the list of already explored states
            for st in explored_states:
                if new_state.equals_state(st):
                    already_explored = True
                    break

            # check if the new state is in the list of states to explore(if the state wasn't found in the explored list)
            if not already_explored:
                for st in states_to_explore:
                    if new_state.equals_state(st):
                        already_listed = True
                        break

            # adds the generated state to the list of states to be explored, if it wasn't found in any lists
            if not already_listed and not already_explored:
                states_to_explore.append(new_state)

        # add stateToExplore in the list of states already explored
        explored_states.append(state_being_explored)
        # remove stateToExplore from the list of states to explore
        states_to_explore.remove(state_being_explored)
        # selecting next state to be explored
        if len(states_to_explore) > 0:
            state_being_explored = states_to_explore[0]
        else:
            return None
