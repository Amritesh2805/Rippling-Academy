import unittest
from model.Board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.cells = Board()

        #Tests for occupied cells

    def test_is_occupied(self):
        self.cells.update_cell(5,"X")
        self.assertTrue(self.cells.is_occupied(5))
        self.cells.update_cell(6,"O")
        self.assertTrue(self.cells.is_occupied(6))
        self.cells.update_cell(2,"O")
        self.assertTrue(self.cells.is_occupied(2))

        #Test for winner

    def test_is_winner(self):
        self.cells.update_cell(1,"X")
        self.assertFalse(self.cells.is_winner("X"))
        self.cells.update_cell(5,"X")
        self.assertFalse(self.cells.is_winner("X"))
        self.cells.update_cell(9,"X")
        self.assertTrue(self.cells.is_winner("X"))

    def test_is_winner(self):
        self.cells.update_cell(1,"X")
        self.assertFalse(self.cells.is_winner("X"))
        self.cells.update_cell(4,"X")
        self.assertFalse(self.cells.is_winner("X"))
        self.cells.update_cell(7,"X")
        self.assertTrue(self.cells.is_winner("X"))

    def test_is_winner(self):
        self.cells.update_cell(1,"X")
        self.assertFalse(self.cells.is_winner("X"))
        self.cells.update_cell(2,"X")
        self.assertFalse(self.cells.is_winner("X"))
        self.cells.update_cell(3,"X")
        self.assertTrue(self.cells.is_winner("X"))

    def test_is_winner(self):
        self.cells.update_cell(4,"X")
        self.assertFalse(self.cells.is_winner("X"))
        self.cells.update_cell(5,"X")
        self.assertFalse(self.cells.is_winner("X"))
        self.cells.update_cell(6,"X")
        self.assertTrue(self.cells.is_winner("X"))

    def test_is_winner(self):
        self.cells.update_cell(7,"X")
        self.assertFalse(self.cells.is_winner("X"))
        self.cells.update_cell(8,"X")
        self.assertFalse(self.cells.is_winner("X"))
        self.cells.update_cell(9,"X")
        self.assertTrue(self.cells.is_winner("X"))

    def test_is_winner(self):
        self.cells.update_cell(2,"X")
        self.assertFalse(self.cells.is_winner("X"))
        self.cells.update_cell(5,"X")
        self.assertFalse(self.cells.is_winner("X"))
        self.cells.update_cell(8,"X")
        self.assertTrue(self.cells.is_winner("X"))

    def test_is_winner(self):
        self.cells.update_cell(3,"X")
        self.assertFalse(self.cells.is_winner("X"))
        self.cells.update_cell(6,"X")
        self.assertFalse(self.cells.is_winner("X"))
        self.cells.update_cell(9,"X")
        self.assertTrue(self.cells.is_winner("X"))

    def test_is_winner(self):
        self.cells.update_cell(3,"X")
        self.assertFalse(self.cells.is_winner("X"))
        self.cells.update_cell(5,"X")
        self.assertFalse(self.cells.is_winner("X"))
        self.cells.update_cell(7,"X")
        self.assertTrue(self.cells.is_winner("X"))

    def test_is_winner(self):
        self.cells.update_cell(1,"O")
        self.assertFalse(self.cells.is_winner("O"))
        self.cells.update_cell(5,"O")
        self.assertFalse(self.cells.is_winner("O"))
        self.cells.update_cell(9,"O")
        self.assertTrue(self.cells.is_winner("O"))

    def test_is_winner(self):
        self.cells.update_cell(1,"O")
        self.assertFalse(self.cells.is_winner("O"))
        self.cells.update_cell(4,"O")
        self.assertFalse(self.cells.is_winner("O"))
        self.cells.update_cell(7,"O")
        self.assertTrue(self.cells.is_winner("O"))

    def test_is_winner(self):
        self.cells.update_cell(1,"O")
        self.assertFalse(self.cells.is_winner("O"))
        self.cells.update_cell(2,"O")
        self.assertFalse(self.cells.is_winner("O"))
        self.cells.update_cell(3,"O")
        self.assertTrue(self.cells.is_winner("O"))

    def test_is_winner(self):
        self.cells.update_cell(4,"O")
        self.assertFalse(self.cells.is_winner("O"))
        self.cells.update_cell(5,"O")
        self.assertFalse(self.cells.is_winner("O"))
        self.cells.update_cell(6,"O")
        self.assertTrue(self.cells.is_winner("O"))

    def test_is_winner(self):
        self.cells.update_cell(7,"O")
        self.assertFalse(self.cells.is_winner("O"))
        self.cells.update_cell(8,"O")
        self.assertFalse(self.cells.is_winner("O"))
        self.cells.update_cell(9,"O")
        self.assertTrue(self.cells.is_winner("O"))

    def test_is_winner(self):
        self.cells.update_cell(2,"O")
        self.assertFalse(self.cells.is_winner("O"))
        self.cells.update_cell(5,"O")
        self.assertFalse(self.cells.is_winner("O"))
        self.cells.update_cell(8,"O")
        self.assertTrue(self.cells.is_winner("O"))

    def test_is_winner(self):
        self.cells.update_cell(3,"O")
        self.assertFalse(self.cells.is_winner("O"))
        self.cells.update_cell(6,"O")
        self.assertFalse(self.cells.is_winner("O"))
        self.cells.update_cell(9,"O")
        self.assertTrue(self.cells.is_winner("O"))

    def test_is_winner(self):
        self.cells.update_cell(3,"O")
        self.assertFalse(self.cells.is_winner("O"))
        self.cells.update_cell(5,"O")
        self.assertFalse(self.cells.is_winner("O"))
        self.cells.update_cell(7,"O")
        self.assertTrue(self.cells.is_winner("O"))


        #Test for tied game

    def test_is_tied(self):
        self.cells.update_cell(1,"O")
        self.assertFalse(self.cells.is_tied())
        self.cells.update_cell(2,"X")
        self.assertFalse(self.cells.is_tied())
        self.cells.update_cell(3,"O")
        self.assertFalse(self.cells.is_tied())
        self.cells.update_cell(4,"X")
        self.assertFalse(self.cells.is_tied())
        self.cells.update_cell(5,"X")
        self.assertFalse(self.cells.is_tied())
        self.cells.update_cell(6,"O")
        self.assertFalse(self.cells.is_tied())
        self.cells.update_cell(7,"O")
        self.assertFalse(self.cells.is_tied())
        self.cells.update_cell(8,"O")
        self.assertFalse(self.cells.is_tied())
        self.cells.update_cell(9,"X")
        self.assertTrue(self.cells.is_tied())


if __name__ == "__main__":
    unittest.main()

