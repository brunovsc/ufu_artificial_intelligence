import AStar
from Classes8Game import State

print("Eight pieces game: ")

# initial_state = input("Initial state (different numbers from 0 to 8): ")

# numbers = initial_state.split(" ")
# configuration = [0, 1, 2, 3, 4, 5, 6, 7, 8]
configuration = [7, 8, 5, 4, 0, 6, 1, 2, 3]
#
# for i in range(len(numbers)):
#     int_numbers.append(int(numbers[i]))

white = 0
for i in range(len(configuration)):
    if configuration[i] == 0:
        white = i
        break

start_state = State(configuration, white)
print(configuration)
print("======================")
# print("Choose a heuristic: ")
# heuristic = input("0 - h1: number of number at wrong position\n1 - h2: sum of horizontal and vertical distances\n")
# heuristic = int(heuristic)
# ret = None
# if heuristic == 0:
ret = AStar.a_star(start_state)#, Classes8Game.State.heuristic_1)
# elif heuristic == 1:
#     ret = AStar.a_star(configuration)#, Classes8Game.State.heuristic_2)

for st in ret:
    st.print_configuration()



print(len(ret))

# resultState = None
#
# option = input("Choose a method: \n0 - Dumb\n1 - Breadth_first\n2 - Depth_first\nOption -> ")
# option = int(option)
# if option == 0:
#     resultState = Dumb.dumb(state)
# elif option == 1:
#     resultState = BreadthSearch.breadth_first_search(state)
# elif option == 2:
#     resultState = DepthSearch.depth_first_search(state)
# else:
#     print("Invalid option for method")
#     exit(0)
#
# if resultState:
#     print("ANSWER")
#     resultState.print_info()
# else:
#     print("404 - Solution not found")
