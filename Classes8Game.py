class State:
    finalState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    def __init__(self, configuration):
        self.configuration = configuration
        for i in range(2):
            for j in range(2):
                if self.configuration[i][j] == 0:
                    self.white_space = WhiteSpace(Position(i, j))
        return

    def heuristic_1(self):
        accumulator = 0
        for i in range(2):
            for j in range(2):
                if self.configuration[i][j] != self.finalState[i][j]:
                    accumulator += 1
        return accumulator

    def heuristic_2(self):
        accumulator = 0
        for i in range(2):
            for j in range(2):
                if self.configuration[i][j] == 0:
                    accumulator += Position(i, j).distance_to(Position(0, 0))
                elif self.configuration[i][j] == 1:
                    accumulator += Position(i, j).distance_to(Position(0, 1))
                elif self.configuration[i][j] == 2:
                    accumulator += Position(i, j).distance_to(Position(0, 2))
                elif self.configuration[i][j] == 3:
                    accumulator += Position(i, j).distance_to(Position(1, 0))
                elif self.configuration[i][j] == 4:
                    accumulator += Position(i, j).distance_to(Position(1, 1))
                elif self.configuration[i][j] == 5:
                    accumulator += Position(i, j).distance_to(Position(1, 2))
                elif self.configuration[i][j] == 6:
                    accumulator += Position(i, j).distance_to(Position(2, 0))
                elif self.configuration[i][j] == 7:
                    accumulator += Position(i, j).distance_to(Position(2, 1))
                else:  # 8
                    accumulator += Position(i, j).distance_to(Position(2, 2))
        return accumulator

    def is_final(self):
        for i in range(2):
            for j in range(2):
                if self.configuration[i][j] != self.finalState[i][j]:
                    return False
        return True


class Position:
    def __init__(self, position_x, position_y):
        self.positionX = position_x
        self.positionY = position_y
        return

    def distance_to(self, target_position):
        distance = abs(target_position.positionX - self.positionX) + abs(target_position.positionY - self.positionY)
        return distance


class WhiteSpace:
    actions = ["right", "down", "left", "up"]
    path = []

    def __init__(self, position=Position(1, 1)):
        self.position = position
        return

    def available_actions(self):
        current_actions = list(self.actions)
        if self.position.positionX == 0:  # white space is in left column
            current_actions.remove("left")
        elif self.position.positionX == 2:  # white space is in right column
            current_actions.remove("right")

        if self.position.positionY == 0:  # white space is in top row
            current_actions.remove("up")
        elif self.position.positionY == 2:  # white space is in bottom row
            current_actions.remove("down")

        return current_actions

    def move(self, action):
        self.path.append(action)
        return

