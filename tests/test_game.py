from unittest import TestCase
from unittest.mock import patch
from snake_ladder.game import SnakeLadderGame as Game


class TestGame(TestCase):

    def setUp(self):
        self.game = Game()
        self.game.setup()

    @patch('snake_ladder.board.Board.user_input', side_effect=[5, 2, 4, 5, 5, 5])
    def test_play_game(self, mock_user_input):
        # Simulate a game where players take turns rolling the dice
        while not self.game.is_over:
            self.game.play()
        
        # Check if the game is over and one player has won
        self.assertTrue(self.game.is_over)
        winner = [player for player in self.game.players if player.current_position == 100]
        self.assertEqual(len(winner), 1)  # Only one winner
        print(f"Winner: {winner[0].name} at position {winner[0].current_position}")