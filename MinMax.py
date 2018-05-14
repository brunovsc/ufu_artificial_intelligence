import math
from ClassesTicTacToe import State

def minimax(initial_state):
	v = minimax_max(initial_state)
	return v


def minimax_max(state):
	state_avaliation = state.avaliation()
	if state_avaliation[0] == True:
		return state_avaliation[1] # 10, -10 or 0

	v = -99
	for action in state.available_actions():
		new_state = State(list(state.configuration), 1)
		new_state.play(action)
		v = max(v, minimax_min(new_state))
	return v


def minimax_min(state):
	state_avaliation = state.avaliation()
	if state_avaliation[0] == True:
		return state_avaliation[1] # 10, -10 or 0

	v = 99
	for action in state.available_actions():
		new_state = State(list(state.configuration), -1)
		new_state.play(action)
		v = min(v, minimax_max(new_state))
	return v
