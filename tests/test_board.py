from unittest import TestCase
from unittest.mock import patch
from game.board import Board
import game.config as config



class TestBoard(TestCase):
    def setUp(self):
        self.board = Board()

    @patch('builtins.input', side_effect=['3'])
    def test_user_input_valid(self, mock_input):
        roll = self.board.user_input()
        self.assertEqual(roll, 3)

    @patch('builtins.input', side_effect=['invalid', '5'])
    def test_user_input_invalid_then_valid(self, mock_input):
        roll = self.board.user_input()
        self.assertEqual(roll, 5)

    def test_update_player_position_normal_move(self):
        new_position = self.board.update_player_position(10, 4)
        self.assertEqual(new_position, 14)

    def test_update_player_position_ladder(self):
        new_position = self.board.update_player_position(6, 1) 
        self.assertEqual(new_position, 33)

    def test_update_player_position_snake(self):
        new_position = self.board.update_player_position(35, 1)
        self.assertEqual(new_position, 19)

    def test_update_player_position_exceeds_board_size(self):
        new_position = self.board.update_player_position(98, 5)
        self.assertEqual(new_position, 98)