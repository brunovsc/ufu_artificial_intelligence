import math
from ClassesTicTacToe import State

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
