import math
from ClassesTicTacToe import State

def play_against(initial_state, first = True):
	state = initial_state
	play = -1
	while state.avaliation()[0] != True:
		if(first == True):
			new_state = State(list(state.configuration), 1, state)
			state.draw_board()
			action = input("Onde jogar? ")
			new_state.configuration[int(action)] = -1
			play = play + 1
			if(new_state.avaliation()[0] == True):
				return new_state.avaliation()[1], new_state
			new_v = minimax(new_state)
			play = play + 1
			state = raiz(new_v[1], play)
		else:
			new_v = minimax(state)
			play = play + 1
			state = raiz(new_v[1], play)
			new_state = State(list(state.configuration), 1, state)
			if(new_state.avaliation()[0] == True):
				return new_state.avaliation()[1], new_state
			state.draw_board()
			action = input("Onde jogar? ")
			new_state.configuration[int(action)] = -1
			play = play + 1			
			state = new_state
	return state.avaliation()[0], state


def raiz(state, position):
	path = []
	while state.parent != None:
		path.insert(0, state)
		state = state.parent
	return path[position]


def minimax(initial_state):
	v, final_state = minimax_max(initial_state)
	return v, final_state


def minimax_max(state):
	state_avaliation = state.avaliation()
	if state_avaliation[0] == True:
		return state_avaliation[1], state # 10, -10 or 0

	v = -99
	last_state = None
	for action in state.available_actions():
		new_state = State(list(state.configuration), 1, state)
		new_state.play(action)
		new_v = minimax_min(new_state)
		if new_v[0] > v:
			v = new_v[0]
			last_state = new_v[1]
	return v, last_state


def minimax_min(state):
	state_avaliation = state.avaliation()
	if state_avaliation[0] == True:
		return state_avaliation[1], state # 10, -10 or 0

	v = 99
	last_state = None
	for action in state.available_actions():
		new_state = State(list(state.configuration), -1, state)
		new_state.play(action)
		new_v = minimax_max(new_state)
		if new_v[0] < v:
			v = new_v[0]
			last_state = new_v[1]
	return v, last_state
