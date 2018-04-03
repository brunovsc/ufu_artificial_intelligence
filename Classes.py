class Robot:
  def __init__(self, position=0):
    self.clears = 0
    self.rights = 0
    self.lefts = 0
    self.actions = ["right", "left", "clear"]
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
  def __init__(self, spaceConfiguration, robot):
    self.robot = robot
    self.spaceConfiguration = spaceConfiguration
    return
  
  def print_info(self):
    print("\n======== State")
    print("\n============= Space")
    print(self.spaceConfiguration)
    print("============= Robot")
    self.robot.print_info()
    print("\n")
    return
  
  def apply_action(self, action):
    newState = State(self.spaceConfiguration, self.robot)
    if(action == "right"):
      newState.robot.position = 1
    elif(action == "left"):
      newState.robot.position = 0
    elif(action == "clear"):
      newState.spaceConfiguration[newState.robot.position] = "clean"
    
    return newState
    
    def is_final_state(self):
      return self.spaceConfiguration[0] == "clean" && self.spaceConfiguration[1] == "clean"
      
