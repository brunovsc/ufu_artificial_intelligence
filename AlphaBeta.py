import math
from ClassesTicTacToe import State

def alpha_beta(initial_state):
	initial_state.draw_board()
	v = alpha_beta_max(initial_state, -99, 99)
	return v


def alpha_beta_max(state, alpha, beta):
	state_avaliation = state.avaliation()
	if state_avaliation[0] == True:
		return state_avaliation[1] # 10, -10 or 0

	v = -99
	for action in state.available_actions():
		new_state = State(list(state.configuration), 1)
		new_state.play(action)
		v = max(v, alpha_beta_min(new_state, alpha, beta))
		if v >= beta:
			return v
		alpha = max(v,alpha)
	return v


def alpha_beta_min(state, alpha, beta):
	state_avaliation = state.avaliation()
	if state_avaliation[0] == True:
		return state_avaliation[1] # 10, -10 or 0

	v = 99
	for action in state.available_actions():
		new_state = State(list(state.configuration), -1)
		new_state.play(action)
		v = min(v, alpha_beta_max(new_state, alpha, beta))
		if v <= alpha:
			return v
		beta = min(v,beta)
	return v
