class State:
    def __init__(self, position, mapStatus):
        self.robotPosition = position
        self.mapStatus = mapStatus

    def printState(self):
        print("Position: ", self.robotPosition, " - Map: ", self.mapStatus[0]," , ", self.mapStatus[1])

    def verifyMap(self):
        for space in self.mapStatus:
            if(space == "dirty"):
                return False
        return True

    def workStartLeft(self):
        if (state1.mapStatus[0] == "dirty"):
            print("CLEAR")
            state1.mapStatus[0] == "clean"

        print("MOVE RIGHT")
        state1.robotPosition = "R"

        if (state1.mapStatus[1] == "dirty"):
            print("CLEAR")

        print("FINISH")
        return

    def workStartRight(self):
        if (state1.mapStatus[1] == "dirty"):
            print("CLEAR")
            state1.mapStatus[1] == "clean"

        print("MOVE LEFT")
        state1.robotPosition = "L"

        if (state1.mapStatus[0] == "dirty"):
            print("CLEAR")

        print("FINISH")
        return

state1 = State("R", ["dirty", "dirty"])

state1.printState()

if(state1.robotPosition == "L"):
    state1.workStartLeft()
else:
    state1.workStartRight()
