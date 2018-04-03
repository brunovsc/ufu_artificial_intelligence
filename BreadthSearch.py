from Classes import Robot
from Classes import State

statusA = input("Situation for space A: ")
statusB = input("Situation for space B: ")

robotPosition = input("Robot position: ")

state = State([statusA, statusB], Robot(robotPosition))

state.print_info()

toExplore = []
toExplore.append(state)

while(len(toExplore)):
    
    stateToExplore = toExplore.pop()
    if(stateToExplore.is_final_state()):
        stateToExplore.print_info()
        break
    
    for action in state.robot.actions:
        newState = state.apply_action(action)
        toExplore.append(newState)
    
print("404 - Solution not found")
