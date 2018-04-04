import Dumb
import BreadthSearch
import DepthSearch
from Classes import State
from Classes import Robot

print("Vacuum Cleaner initial status: ")

statusA = input("Situation for space A: ")
statusB = input("Situation for space B: ")

robotPositionString = input("Robot position: ")

robotPosition = -1
if robotPositionString == 'A':
    robotPosition = 0
elif robotPositionString == 'B':
    robotPosition = 1
else:
    print("Invalid initial position for the robot")
    exit(0)

state = State([statusA, statusB], Robot(robotPosition))

resultState = None

option = input("Choose a method: \n0 - Dumb\n1 - Breadth_first\n2 - Depth_first\nOption -> ")
option = int(option)
if option == 0:
    resultState = Dumb.dumb(state)
elif option == 1:
    resultState = BreadthSearch.breadth_first_search(state)
elif option == 2:
    resultState = DepthSearch.depth_first_search(state)
else:
    print("Invalid option for method")
    exit(0)

if resultState:
    print("ANSWER")
    resultState.print_info()
else:
    print("404 - Solution not found")
