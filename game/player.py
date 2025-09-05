class Player:
    def __init__(self, name):
        self.name = name
        self.current_position = 0

    def move(self, new_position):
        self.current_position = new_position
        print(f"{self.name} moved to position {self.current_position}")

