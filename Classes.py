class Robot:
    def __init__(self, position="left"):
        self.clears = 0
        self.rights = 0
        self.lefts = 0
        self.position = position
        return

    def clear(self):
        print("CLEANING")
        self.clears += 1
        return

    def move_left(self):
        print("MOVING LEFT")
        self.lefts += 1
        return

    def move_right(self):
        print("MOVING RIGHT")
        self.rights += 1
        return

    def turn_off(self):
        print("FINISHING PROCESS")
        self.print_info()
        return

    def total_actions(self):
        return self.clears + self.rights + self.lefts

    def print_info(self):
        print("Position: %s\nTotal Actions: %d\n ----- Clears = %d\n ----- Right Moves = %d\n ----- Left Moves = %d" %
              (self.position, self.total_actions(), self.clears, self.rights, self.lefts))
        return


class State:
    def __init__(self, position):
        self.robot = Robot(position)
        self.spaceConfiguration = ["clean", "clean"]
        return
