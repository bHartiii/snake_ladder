import config
class Board:
    
    def __init__(self):
        self.ladder_positions_map = config.ladder_positions_map
        self.snake_positions_map = config.snake_positions_map


    def user_input(self):
        while True:
            try:
                roll = int(input("Press Enter to roll the dice: "))
                if roll in range(config.min_dice_value, config.max_dice_value + 1):
                    return roll
                else:
                    print("Invalid input. Please press Enter to roll the dice.")
            except ValueError:
                print("Invalid input. Please press Enter to roll the dice.")


    def update_player_position(self, current_position, roll):
        ## Check if the move is valid
        if current_position + roll > config.board_size:
            print(f"player rolled {roll} but cannot move from {current_position} to {current_position + roll} (exceeds 100).")
            return current_position

        ## check if the new position is a ladder or snake
        new_position = current_position + roll

        if new_position in self.ladder_positions_map:
            print(f"player climbed a ladder from {new_position} to {self.ladder_positions_map[new_position]}")
            new_position = self.ladder_positions_map[new_position]
        elif new_position in self.snake_positions_map:
            print(f"Player got bitten by a snake from {new_position} to {self.snake_positions_map[new_position]}")
            new_position = self.snake_positions_map[new_position]
        
        return new_position
    
