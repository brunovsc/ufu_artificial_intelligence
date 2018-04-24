
class Position:
    def __init__(self, position_x, position_y):
        self.positionX = position_x
        self.positionY = position_y
        return

    def distance_to(self, target_position):
        distance = abs(target_position.positionX - self.positionX) + abs(target_position.positionY - self.positionY)
        return distance


class State:
    final_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    #actions = ["right", "down", "left", "up"]
    actions = ["up", "left", "down", "right"]
    path = []

    def __init__(self, configuration, white_space, heuristic = 0, cost = 0, predecessor = None):
        self.configuration = configuration
        self.white_space = white_space
        self.heuristic = heuristic
        self.cost = cost
        self.evaluation = self.heuristic + self.cost
        self.predecessor = predecessor
        return

    def __lt__(self, other):
        if self.evaluation != other.evaluation:
            return self.evaluation < other.evaluation
        else:
            return self.configuration < other.configuration

    def is_final(self):
        for i in range(8):
            if self.configuration[i] != self.final_state[i]:
                return False
        return True

    def available_actions(self):
        current_actions = list(self.actions)
        if self.white_space == 0 or self.white_space == 1 or self.white_space == 2:  # white space is in top row
            current_actions.remove("up")
        if self.white_space == 6 or self.white_space == 7 or self.white_space == 8:  # white space is in bottom row
            current_actions.remove("down")
        if self.white_space == 0 or self.white_space == 3 or self.white_space == 6:  # white space is in left column
            current_actions.remove("left")
        if self.white_space == 2 or self.white_space == 5 or self.white_space == 8:  # white space is in right column
            current_actions.remove("right")

        return current_actions

    def move(self, action):
        new_configuration = list(self.configuration)
        white_space = self.white_space
        if action == "up":
            new_configuration[self.white_space] = new_configuration[self.white_space - 3]
            new_configuration[self.white_space - 3] = 0
            white_space = self.white_space - 3
        elif action == "down":
            new_configuration[self.white_space] = new_configuration[self.white_space + 3]
            new_configuration[self.white_space + 3] = 0
            white_space = self.white_space + 3
        elif action == "right":
            new_configuration[self.white_space] = new_configuration[self.white_space + 1]
            new_configuration[self.white_space + 1] = 0
            white_space = self.white_space + 1
        elif action == "left":
            new_configuration[self.white_space] = new_configuration[self.white_space - 1]
            new_configuration[self.white_space - 1] = 0
            white_space = self.white_space - 1

        return new_configuration, white_space

    def print_configuration(self):
        print("%d %d %d" % (self.configuration[0], self.configuration[1], self.configuration[2]))
        print("%d %d %d" % (self.configuration[3], self.configuration[4], self.configuration[5]))
        print("%d %d %d" % (self.configuration[6], self.configuration[7], self.configuration[8]))
        print("-----")
        return
