import unittest
from Board import *
from Gomoku import Gomoku


class testBoard(unittest.TestCase):

    def setUp(self):
        self._board = Board()

    def testEmptySquares(self):
        self.assertEqual(len(self._board.emptySquares()), 225)

    def testVerifyLine(self):
        self._board.squares[0][0] = 1
        self._board.squares[0][1] = 1
        self._board.squares[0][2] = 1
        self._board.squares[0][3] = 1
        self._board.squares[0][4] = 1
        self.assertEqual(True, self._board.verifyLine(0, 0))
        self._board.squares[0][4] = 0
        self.assertEqual(False, self._board.verifyLine(0, 0))
        self._board.squares[0][4] = 1
        self._board.squares[0][5] = 1
        self.assertEqual(False, self._board.verifyLine(0, 0))

    def testVerifyColumn(self):
        self._board.squares[9][14] = 1
        self._board.squares[10][14] = 1
        self._board.squares[11][14] = 1
        self._board.squares[12][14] = 1
        self._board.squares[13][14] = 1
        self.assertEqual(True, self._board.verifyColumn(9, 14))
        self._board.squares[13][14] = 0
        self.assertEqual(False, self._board.verifyColumn(9, 14))
        self._board.squares[13][14] = 1
        self._board.squares[14][14] = 1
        self.assertEqual(False, self._board.verifyColumn(9, 14))

    def testVerifyDiagonal(self):
        self._board.squares[0][0] = 1
        self._board.squares[1][1] = 1
        self._board.squares[2][2] = 1
        self._board.squares[3][3] = 1
        self._board.squares[4][4] = 1
        self.assertEqual(True, self._board.verifyDiagonal1(0, 0))
        self._board.squares[4][4] = 0
        self.assertEqual(False, self._board.verifyDiagonal1(0, 0))
        self._board.squares[4][4] = 1
        self._board.squares[5][5] = 1
        self.assertEqual(False, self._board.verifyDiagonal1(0, 0))

        self._board.squares[0][14] = 1
        self._board.squares[1][13] = 1
        self._board.squares[2][12] = 1
        self._board.squares[3][11] = 1
        self._board.squares[4][10] = 1
        self.assertEqual(True, self._board.verifyDiagonal2(0, 14))
        self._board.squares[4][10] = 0
        self.assertEqual(False, self._board.verifyDiagonal2(0, 14))
        self._board.squares[4][10] = 1
        self._board.squares[5][9] = 1
        self.assertEqual(False, self._board.verifyDiagonal2(0, 14))

    def testWin(self):
        self._board.squares[0][0] = 1
        self._board.squares[1][1] = 1
        self._board.squares[2][2] = 1
        self._board.squares[3][3] = 1
        self._board.squares[4][4] = 1

        self._board.squares[0][14] = 1
        self._board.squares[1][13] = 1
        self._board.squares[2][12] = 1
        self._board.squares[3][11] = 1
        self._board.squares[4][10] = 1

        self._board.squares[14][0] = 1
        self._board.squares[14][1] = 1
        self._board.squares[14][2] = 1
        self._board.squares[14][3] = 1
        self._board.squares[14][4] = 1

        self._board.squares[0][14] = 1
        self._board.squares[1][14] = 1
        self._board.squares[2][14] = 1
        self._board.squares[3][14] = 1
        self._board.squares[4][14] = 1

        for i in range(5):
            sq = Square(14, i)
            self.assertEqual(True, self._board.win(sq))
            sq = Square(i, 14)
            self.assertEqual(True, self._board.win(sq))
            sq = Square(i, i)
            self.assertEqual(True, self._board.win(sq))
            sq = Square(i, 14-i)
            self.assertEqual(True, self._board.win(sq))

    def testTie(self):
        for i in range(15):
            for j in range(15):
                if j % 2 == 0:
                    self._board.squares[i][j] = 1
                else:
                    self._board.squares[i][j] = 2

        self.assertEqual(True, self._board.tie())

    def testMove(self):
        sq = Square(0, 0)
        self._board.move(sq, 1)
        self.assertEqual(1, self._board.squares[0][0])
        sq = Square(0, 0)
        try:
            self._board.move(sq, 1)
        except GomokuError as e:
            self.assertEqual("Square already taken! Please choose a free square.", str(e))
        sq = Square(0, 15)
        try:
            self._board.move(sq, 1)
        except GomokuError as e:
            self.assertEqual("Move outside the board! Please choose numbers between 1 and 15.", str(e))


class testGomoku(unittest.TestCase):

    def setUp(self):
        self._game = Gomoku()

    def testMoveHuman(self):
        sq = Square(0, 0)
        self._game.moveHuman(sq, 1)
        self.assertEqual(1, self._game.board.squares[0][0])
        sq = Square(0, 0)
        try:
            self._game.moveHuman(sq, 1)
        except GomokuError as e:
            self.assertEqual("Square already taken! Please choose a free square.", str(e))
        sq = Square(0, 15)
        try:
            self._game.moveHuman(sq, 1)
        except GomokuError as e:
            self.assertEqual("Move outside the board! Please choose numbers between 1 and 15.", str(e))

    def testVerifyDanger(self):
        #column
        self._game.board.squares[1][0] = 1
        self._game.board.squares[2][0] = 1
        self._game.board.squares[3][0] = 1
        sq = Square(1, 0)
        eSq = self._game.board.emptySquares()
        sq1 = self._game.verifyDanger(sq, eSq)
        sq2 = Square(4, 0)
        self.assertEqual(sq2, sq1)

        sq = Square(3, 0)
        sq1 = self._game.verifyDanger(sq, eSq)
        sq2 = Square(0, 0)
        self.assertEqual(sq2, sq1)

        #line
        self._game.board.squares[0][1] = 1
        self._game.board.squares[0][2] = 1
        self._game.board.squares[0][3] = 1
        sq = Square(0, 1)
        eSq = self._game.board.emptySquares()
        sq1 = self._game.verifyDanger(sq, eSq)
        sq2 = Square(0, 4)
        self.assertEqual(sq2, sq1)

        sq = Square(0, 3)
        sq1 = self._game.verifyDanger(sq, eSq)
        sq2 = Square(0, 0)
        self.assertEqual(sq2, sq1)

        #diagonal 1
        self._game.board.squares[1][1] = 1
        self._game.board.squares[2][2] = 1
        self._game.board.squares[3][3] = 1
        sq = Square(1, 1)
        eSq = self._game.board.emptySquares()
        sq1 = self._game.verifyDanger(sq, eSq)
        sq2 = Square(4, 4)
        self.assertEqual(sq2, sq1)

        sq = Square(3, 3)
        sq1 = self._game.verifyDanger(sq, eSq)
        sq2 = Square(0, 0)
        self.assertEqual(sq2, sq1)

        #diagonal 2
        self._game.board.squares[13][1] = 1
        self._game.board.squares[12][2] = 1
        self._game.board.squares[11][3] = 1
        sq = Square(13, 1)
        eSq = self._game.board.emptySquares()
        sq1 = self._game.verifyDanger(sq, eSq)
        sq2 = Square(10, 4)
        self.assertEqual(sq2, sq1)

        sq = Square(11, 3)
        sq1 = self._game.verifyDanger(sq, eSq)
        sq2 = Square(14, 0)
        self.assertEqual(sq2, sq1)

        #special cases
        self._game.board.squares[7][8] = 1
        sq = Square(7, 8)

        self._game.board.squares[5][6] = 1
        sq1 = Square(6, 7)
        sq2 = self._game.verifyDanger(sq, eSq)
        self.assertEqual(sq2, sq1)

        self._game.board.squares[5][6] = 0
        self._game.board.squares[5][8] = 1
        sq1 = Square(6, 8)
        sq2 = self._game.verifyDanger(sq, eSq)
        self.assertEqual(sq2, sq1)

        self._game.board.squares[5][8] = 0
        self._game.board.squares[5][10] = 1
        sq1 = Square(6, 9)
        sq2 = self._game.verifyDanger(sq, eSq)
        self.assertEqual(sq2, sq1)

        self._game.board.squares[5][10] = 0
        self._game.board.squares[7][6] = 1
        sq1 = Square(7, 7)
        sq2 = self._game.verifyDanger(sq, eSq)
        self.assertEqual(sq2, sq1)

        self._game.board.squares[7][6] = 0
        self._game.board.squares[7][10] = 1
        sq1 = Square(7, 9)
        sq2 = self._game.verifyDanger(sq, eSq)
        self.assertEqual(sq2, sq1)

        self._game.board.squares[7][10] = 0
        self._game.board.squares[9][6] = 1
        sq1 = Square(8, 7)
        sq2 = self._game.verifyDanger(sq, eSq)
        self.assertEqual(sq2, sq1)

        self._game.board.squares[9][6] = 0
        self._game.board.squares[9][8] = 1
        sq1 = Square(8, 8)
        sq2 = self._game.verifyDanger(sq, eSq)
        self.assertEqual(sq2, sq1)

        self._game.board.squares[9][8] = 0
        self._game.board.squares[9][10] = 1
        sq1 = Square(8, 9)
        sq2 = self._game.verifyDanger(sq, eSq)
        self.assertEqual(sq2, sq1)

    def testPossibleAttack(self):
        posAtt = []
        posAtt1 = []

        sq = Square(6, 7)
        posAtt1.append(sq)
        sq = Square(6, 9)
        posAtt1.append(sq)
        sq = Square(8, 7)
        posAtt1.append(sq)
        sq = Square(8, 9)
        posAtt1.append(sq)
        sq = Square(8, 8)
        posAtt1.append(sq)
        sq = Square(6, 8)
        posAtt1.append(sq)
        sq = Square(7, 7)
        posAtt1.append(sq)
        sq = Square(7, 9)
        posAtt1.append(sq)

        sq = Square(7, 8)
        self._game.possibleAttack(sq, posAtt)
        self.assertEqual(posAtt, posAtt1)

    def testMoveComputer(self):
        self._game.board.squares[1][0] = 1
        self._game.board.squares[2][0] = 1
        self._game.board.squares[3][0] = 1
        sq = Square(3, 0)
        sq1 = self._game.moveComputer(2, sq, sq, False, [])
        sq2 = Square(0, 0)
        self.assertEqual(sq1, sq2)
