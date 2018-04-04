class Robot:
    actions = ["right", "left", "clear"]

    def __init__(self, position=0, actions=[]):
        self.position = position
        self.actionsTaken = actions
        return


class State:
    def __init__(self, space_configuration, robot):
        self.robot = robot
        self.spaceConfiguration = space_configuration
        return
  
    def print_info(self):
        position = "A"
        if self.robot.position == 1:
            position = "B"
        print("State: [%s , %s] \nPosition %s" % (self.spaceConfiguration[0], self.spaceConfiguration[1],
                                                  position))
        print("Actions: ", self.robot.actionsTaken)
        return
  
    def apply_action(self, action):
        self.robot.actionsTaken.append(action)
        if action == "right":
            self.robot.position = 1
        elif action == "left":
            self.robot.position = 0
        elif action == "clear":
            self.spaceConfiguration[self.robot.position] = "clean"
    
    def is_final_state(self):
        print("Verifying final state as %s %s" % (self.spaceConfiguration[0], self.spaceConfiguration[1]))
        return self.spaceConfiguration[0] == "clean" and self.spaceConfiguration[1] == "clean"

    def equals_state(self, state_to_compare):
        return self.spaceConfiguration[0] == state_to_compare.spaceConfiguration[0] and \
            self.spaceConfiguration[1] == state_to_compare.spaceConfiguration[1] and \
            self.robot.position == state_to_compare.robot.position
