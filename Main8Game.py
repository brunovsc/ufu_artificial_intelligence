import AStar
from Classes8Game import State

print("Eight pieces game!\n==================")
initial_state = input("Initial state (different numbers from 0 to 8): ")
if len(initial_state) == 0:
    # configuration = [7, 8, 5, 4, 0, 6, 1, 2, 3]  # class example
    # configuration = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # configuration = [1, 2, 0, 3, 4, 5, 6, 7, 8]
    # configuration = [4, 6, 1, 2, 0, 7, 5, 8, 3]  # didn't stop
    # configuration = [3, 8, 6, 1, 4, 2, 0, 7, 5]
    configuration = [0, 8, 7, 4, 6, 2, 1, 5, 3]
    # configuration = [8, 7, 6, 5, 4, 3, 2, 1, 0]  # depth 28
    # configuration = [1, 2, 3, 7, 8, 0, 6, 5, 4]  # didn't stop
    print("\nUsing debug configuration: ")
    print(configuration)
else:
    if len(initial_state) != 17:
        print("Invalid number of pieces")
        exit(0)
    else:
        numbers_string = initial_state.split(" ")
        configuration = []
        for i in range(len(numbers_string)):
            configuration.append(int(numbers_string[i]))

white = 0
for i in range(len(configuration)):
    if configuration[i] == 0:
        white = i
        break

start_state = State(configuration, white)
print("\nChoose a method: ")
method = input("1 - A* with h1: number of number at wrong position\n"
               "2 - A* with h2: sum of horizontal and vertical distances\n"
               "3 - Depth First\n"
               "4 - Compare all methods\n"
               "Option -> ")
method = int(method)
print("\nRunning...")

final_path = None
generated_states = 0
explored_states = 0
if method == 1:
    final_path, generated_states, explored_states = AStar.a_star(start_state, 1)
elif method == 2:
    final_path, generated_states, explored_states = AStar.a_star(start_state, 2)
elif method == 3:
    print("TO DO")
    # final_path, generated_states, explored_states = DepthSearch.depth_search(start_state)
elif method == 4:
    final_path_h1, generated_states_h1, explored_states_h1 = AStar.a_star(start_state, 1)
    print("A* (h1) - Done !")
    final_path_h2, generated_states_h2, explored_states_h2 = AStar.a_star(start_state, 2)
    print("A* (h2) - Done !")
    # print("TO DO")
    # final_path, generated_states, explored_states = DepthSearch.depth_search(start_state)
    # print("Depth Search - Done !")
    print("Comparison\n==========")
    # print("Depth Search - Solution depth: %d, Expanded nodes: %d, Explored nodes: %d" % (final_path_h1[0].cost,
    #                                                                                     generated_states_h1,
    #                                                                                     explored_states_h1))
    print("A* (h1) - Solution depth: %d, Expanded nodes: %d, Explored nodes: %d" % (final_path_h1[0].cost,
                                                                                    generated_states_h1,
                                                                                    explored_states_h1))
    print("A* (h2) - Solution depth: %d, Expanded nodes: %d, Explored nodes: %d" % (final_path_h2[0].cost,
                                                                                    generated_states_h2,
                                                                                    explored_states_h2))
else:
    print("Invalid heuristic")
    exit(0)

if method != 4:
    if final_path is None:
        print("404 - Solution not found")
    else:
        for st in final_path:
            st.print_configuration()

        print("Solution depth = %d" % final_path[0].cost)
        print("Total of states generated = %d" % generated_states)
        print("Total of states explored = %d" % explored_states)

