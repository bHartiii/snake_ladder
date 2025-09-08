import unittest
from snake_ladder.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("TestPlayer")

    def test_initial_position(self):
        self.assertEqual(self.player.current_position, 0)

    def test_move(self):
        self.player.move(10)
        self.assertEqual(self.player.current_position, 10)
        self.player.move(25)
        self.assertEqual(self.player.current_position, 25)
        self.player.move(100)
        self.assertEqual(self.player.current_position, 100)