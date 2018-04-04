from Classes import Robot
from Classes import State


def depth_first_search(state):

    def state_not_explored(state_to_explore):
        flag = False
        for explored in explored_states:
            if state_to_explore.equals_state(explored):
                flag = True
        return not flag

    def recursive_depth(state_to_explore, path=[]):
        path.append(state_to_explore)
        explored_states.append(state_to_explore)
        print("EXPLORING %s %s %d" % (state_to_explore.spaceConfiguration[0], state_to_explore.spaceConfiguration[1], state_to_explore.robot.position))
        input("Enter...")
        if state_to_explore.is_final_state():
            return state_to_explore
        for action in state_to_explore.robot.actions:
            new_state = State(list(state_to_explore.spaceConfiguration), Robot(state_to_explore.robot.position, list(state_to_explore.robot.actionsTaken)))
            new_state.apply_action(action)
            if state_not_explored(new_state):
                return recursive_depth(new_state)

        

    explored_states = []
    solution = recursive_depth(state)
    
    return solution

