import unittest
from TicTacToeBoardGame import TicTacToeBoardGame

class TestTicTacToeBoardGame(unittest.TestCase):
    
    def test_print_header(self):
        ticTacToeBoardGame = TicTacToeBoardGame()
        self.assertEqual(ticTacToeBoardGame.print_header(), "Welcome to a board game", "incorrect salutation")

if __name__ == "__main__":
    unittest.main()

