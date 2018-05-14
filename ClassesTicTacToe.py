class State:
    initial_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    path = []

    def __init__(self, configuration, marker):
        self.configuration = configuration
        self.marker = marker
        return

    def avaliation(self):
        for i in range(8):
            if self.configuration[i] == 0:
                return (False, 0) # NOT END GAME

        if self.configuration[0] == self.configuration[1] == self.configuration[2]:
            if self.configuration[0] == 1:
                return (True, 10)
            elif self.configuration[0] == -1:
                return (True, -10)
        if self.configuration[3] == self.configuration[4] == self.configuration[5]:
            if self.configuration[3] == 1:
                return (True, 10)
            elif self.configuration[3] == -1:
                return (True, -10)
        if self.configuration[6] == self.configuration[7] == self.configuration[8]:
            if self.configuration[6] == 1:
                return (True, 10)
            elif self.configuration[6] == -1:
                return (True, -10)
        if self.configuration[0] == self.configuration[3] == self.configuration[6]:
            if self.configuration[0] == 1:
                return (True, 10)
            elif self.configuration[0] == -1:
                return (True, -10)
        if self.configuration[1] == self.configuration[4] == self.configuration[7]:
            if self.configuration[1] == 1:
                return (True, 10)
            elif self.configuration[1] == -1:
                return (True, -10)
        if self.configuration[2] == self.configuration[5] == self.configuration[8]:
            if self.configuration[2] == 1:
                return (True, 10)
            elif self.configuration[2] == -1:
                return (True, -10)
        if self.configuration[0] == self.configuration[4] == self.configuration[8]:
            if self.configuration[4] == 1:
                return (True, 10)
            elif self.configuration[4] == -1:
                return (True, -10)
        if self.configuration[2] == self.configuration[4] == self.configuration[6]:
            if self.configuration[4] == 1:
                return (True, 10)
            elif self.configuration[4] == -1:
                return (True, -10)
        
        return (True, 0) # DRAW


    def available_actions(self):
        available_positions = []
        for i in range(8):
            if self.configuration[i] == 0:
                available_positions.append(i)

        return available_positions

    def play(self, position):
        self.configuration[position] = self.marker


    def print_configuration(self):
        print("%2d \t%2d \t%2d" % (self.configuration[0], self.configuration[1], self.configuration[2]))
        print("%2d \t%2d \t%2d" % (self.configuration[3], self.configuration[4], self.configuration[5]))
        print("%2d \t%2d \t%2d" % (self.configuration[6], self.configuration[7], self.configuration[8]))
        print("-----")
        return