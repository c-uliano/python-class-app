class Character:

    # ? constructor. Constructs the instance 
    def __init__(self, type, name, power_points = 10, inventory = [], can_teleport = False):
        self.type = type
        self.name = name
        self.power_points = power_points
        self.inventory = inventory
        self.can_teleport = can_teleport