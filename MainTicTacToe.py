import MinMax
import AlphaBeta
import time

from ClassesTicTacToe import State

print("TIC TAC TOE")

#state = State([1,1,1,-1,-1,1,-1,1,-1], 1)
#state = State([-1,-1,-1,1,1,-1,1,-1,1], 1)
state = State([1,0,0,0,-1,1,-1,1,-1], 1)
#state = State([1,-1,1,0,1,0,-1,0,-1], 1)
#state = State([0,0,0,0,0,0,0,0,0], 1) # DRAW
# state = State([1,0,1,-1,1,0,-1,0,0], 1) # WIN
#state = State([-1,0,-1,1,-1,1,0,1,0], 1) # LOSS

resultState = None

while True:
    option = input("Choose a method: \n0 - Minimax\n1 - AlphaBeta\nOption -> ")
    option = int(option)
    timeSpent = time.time()
    if option == 0:
        resultState = MinMax.minimax(state)
    elif option == 1:
        resultState = AlphaBeta.alpha_beta(state)
    else:
        print("Invalid option for method")
        exit(0)
    timeSpent = time.time() - timeSpent

    print("\nANSWER")
    if resultState == 0:
        print("DRAW")
    elif resultState == 10:
        print("WIN")
    elif resultState == -10:
        print("LOSS")
    else:
        print("404 - Solution not found")
    print("TIME SPENT: ", timeSpent)
