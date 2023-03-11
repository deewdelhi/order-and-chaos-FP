import unittest
from board import Board
from game import Game

class TestGame(unittest.TestCase):

    def test__check_for_win__True(self):
        self._game = Game(Board(6,6))
        self._game.set_board_value(0,0,'0')
        self._game.set_board_value(0,1,'0')
        self._game.set_board_value(0,2,'0')
        self._game.set_board_value(0,3,'0')
        self._game.set_board_value(0,4,'0')
        win = self._game.check_for_win()
        self.assertEqual(win,True)

    def test__check_for_win__True_2(self):
        self._game = Game(Board(6,6))
        self._game.set_board_value(0,0,'0')
        self._game.set_board_value(1,0,'0')
        self._game.set_board_value(2,0,'0')
        self._game.set_board_value(3,0,'0')
        self._game.set_board_value(4,0,'0')
        win = self._game.check_for_win()
        self.assertEqual(win,True)


    def test__check_for_win__False(self):
        self._game = Game(Board(6,6))
        self._game.set_board_value(0,0,'0')
        self._game.set_board_value(1,0,'0')
        self._game.set_board_value(2,0,'0')
        self._game.set_board_value(3,0,'0')
        self._game.set_board_value(4,0,'x')
        win = self._game.check_for_win()
        self.assertEqual(win,False)

    def test__check_for_win__False_2(self):
        self._game = Game(Board(6,6))
        self._game.set_board_value(0,0,'0')
        self._game.set_board_value(0,1,'0')
        self._game.set_board_value(0,2,'x')
        self._game.set_board_value(0,3,'0')
        self._game.set_board_value(0,4,'0')
        win = self._game.check_for_win()
        self.assertEqual(win,False)





if __name__ == '__main__':
    unittest.main()

