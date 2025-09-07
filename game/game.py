from player import Player
from board import Board

class SnakeLadderGame:
    def __init__(self):
        self.players = []
        self.is_over = False

    def setup(self):
        print(f"Starting game: Snake and Ladders")

        ## Board initialization
        self.board = Board()

        ## Player initialization
        self.players.append(Player("Alice"))

    def play(self):
        for player in self.players:
            roll = self.board.user_input()
            new_position = self.board.update_player_position(player.current_position, roll)
            player.move(new_position)
            if player.current_position == 100:
                print(f"{player.name} has won the game!")
                self.is_over = True
                break

    def end(self):
        print("Game has ended.")


if __name__ == "__main__":
    game = SnakeLadderGame()
    game.setup()
    while not game.is_over:
        game.play()

    game.end()
