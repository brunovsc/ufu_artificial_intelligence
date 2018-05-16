import math
from ClassesTicTacToe import State

def alpha_beta(initial_state):
	v, final_state = alpha_beta_max(initial_state, -99, 99)
	return v, final_state


def alpha_beta_max(state, alpha, beta):
	state_avaliation = state.avaliation()
	if state_avaliation[0] == True:
		return state_avaliation[1], state # 10, -10 or 0

	v = -99
	last_state = None
	for action in state.available_actions():
		new_state = State(list(state.configuration), 1, state)
		new_state.play(action)
		new_v = alpha_beta_min(new_state, alpha, beta)
		if new_v[0] > v:
			v = new_v[0]
			last_state = new_v[1]
		if v >= beta:
			return v, last_state
		alpha = max(v,alpha)
	return v, last_state


def alpha_beta_min(state, alpha, beta):
	state_avaliation = state.avaliation()
	if state_avaliation[0] == True:
		return state_avaliation[1], state # 10, -10 or 0

	v = 99
	last_state = None
	for action in state.available_actions():
		new_state = State(list(state.configuration), -1, state)
		new_state.play(action) 
		new_v = alpha_beta_max(new_state, alpha, beta)
		if new_v[0] < v:
			v = new_v[0]
			last_state = new_v[1]
		if v <= alpha:
			return v, last_state
		beta = min(v,beta)
	return v, last_state
