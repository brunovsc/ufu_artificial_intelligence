import MinMax
import AlphaBeta
import time

from ClassesTicTacToe import State


def print_path(state):
    path = []
    while state != None:
        path.insert(0, state)
        state = state.parent
    for state in path:
        state.draw_board()
    #map(lambda item: item.draw_board(), path)


def print_path2(state):
    while state != None:
        state.draw_board()
        state = state.child
    #map(lambda item: item.draw_board(), path)

print("TIC TAC TOE")

#state = State([1,1,0,-1,-1,1,-1,1,-1], 1) # WIN (1 play)
#state = State([-1,-1,-1,1,1,-1,1,-1,1], 1)
#state = State([1,0,0,0,-1,1,-1,1,-1], 1)
#state = State([1,-1,1,0,1,0,-1,0,-1], 1)
#state = State([1,-1,1,-1,1,-1,0,0,0], 1) # DRAW
#state = State([1,0,1,-1,1,0,-1,0,0], 1) # WIN (3 plays)
#state = State([-1,0,-1,1,-1,1,0,1,0], 1) # LOSS
#state = State([1,-1,1,0,1,0,-1,0,-1], 1) # DRAW
#state = State([1,-1,1,0,0,0,-1,0,0], 1) # DRAW
#state = State([1,-1,1,-1,1,-1,-1,1,-1], 1) # DRAW
state = State([0,0,0,0,0,0,0,0,0], 1) # DRAW
state = State([1,-1,1,0,1,0,-1,0,-1], 1) # DRAW

resultValue = None
path = None
board = []
player = 1

while True:
    #state = State(board, player) # DRAW
    option = input("Choose a method:\n1 - Minimax\n2 - AlphaBeta\n0 - Exit\nOption -> ")
    option = int(option)
    timeSpent = time.time()
    if option == 1:
        resultValue, path = MinMax.minimax(state)
    elif option == 2:
        resultValue, path = AlphaBeta.alpha_beta(state)
    elif option == 3:
        for i in range (0,3):
            for j in range (0,3):
                value = input("Position [%d,%d]: "%(i, j))
                board.append(int(value))
        value = input("Who plays first? ")
        player = int(value)
    elif option == 0:
        exit(0)
    else:
        print("Invalid option for method")
        exit(0)
    timeSpent = time.time() - timeSpent

    print("\nANSWER")
    if resultValue == 0:
        print_path(path)
        print("DRAW")
    elif resultValue == 10:
        print_path(path)
        print("WIN")
    elif resultValue == -10:
        print_path(path)
        print("LOSS")
    else:
        print("404 - Solution not found")
    print("TIME SPENT: ", timeSpent)

