#This is an elevator program
#August 2nd 2019

print("Elevator runs")

class elevator:
    #initalizer
    def __init__(self, cap, buts, level, direction):
        self.capacity = cap
        self.status = buts
        self.level = level
        self.direction = direction

    def door_open(self):
        print ("The door opened")

    def getStatus(self):
        print ("The elevator is on level " + str(self.level) + ", going " + self.direction)

class floors:
    def __init__(self, buttons):
        self.info = buttons
        
#initiate the building
floor_buttons = {"firstFloor": None, "secondFloor": None, "thirdFloor": "up", "fourthFloor": None, "fifthFloor": None}
inside_buttons = {"firstFloor": False, "secondFloor": True, "thirdFloor": False, "fourthFloor": True, "fifthFloor": False}
#index_dic = {"firstFloor": 1, "secondFloor": 2, "thirdFloor": 3, "fourthFloor": 4, "fifthFloor": 5}
capacity = 13
Tuna = elevator(capacity, inside_buttons, 1, "up")
building = floors(floor_buttons)
Tuna.getStatus()

#elevator running
for floor, direction in floor_buttons.items():
    if (building.info[floor] == Tuna.direction) or (inside_buttons[floor] == True):
        print (floor + ", door opened, picked up")
        Tuna.door_open()
    else :
        print (floor + ", ignored")
