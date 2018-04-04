def dumb(state):
    if state.spaceConfiguration[state.robot.position] == "dirty":
        state.robot.actionsTaken.append('clear')
        state.spaceConfiguration[state.robot.position] = "clean"

    if state.robot.position == 0:
        state.robot.actionsTaken.append('right')
        state.robot.position = 1
    else:
        state.robot.actionsTaken.append('left')
        state.robot.position = 0

    if state.spaceConfiguration[state.robot.position] == "dirty":
        state.robot.actionsTaken.append('clear')
        state.spaceConfiguration[state.robot.position] = "clean"

    return state
