import unittest
from BoardGame import BoardGame

class TestBoardGame(unittest.TestCase):
    
    def test_print_header(self):
        boardGame = BoardGame()
        self.assertEqual(boardGame.print_header(), "Welcome to a board game", "incorrect salutation")

if __name__ == "__main__":
    unittest.main()

