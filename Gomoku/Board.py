from Square import Square
from GomokuError import GomokuError
from texttable import *


class Board:
    def __init__(self):
        self._squares = [[0]*15, [0]*15, [0]*15, [0]*15, [0]*15, [0]*15, [0]*15, [0]*15, [0]*15, [0]*15, [0]*15, [0]*15, [0]*15, [0]*15, [0]*15]

    @property
    def squares(self):
        return self._squares

    def emptySquares(self):
        """
        Returns all the squares on which a move was not performed.
        :return: esq - list of Squares
        """
        eSq = []
        for i in range(15):
            for j in range(15):
                if self._squares[i][j] == 0:
                    sq = Square(i, j)
                    eSq.append(sq)
        return eSq

    def verifyLine(self, line, col):
        """
        Checks if 5 consecutive elements on a line have the same value
        :param line: integer
        :param col: integer
        :return: True - if they do
                 False, otherwise
        """
        for i in range(1, 5):
            if self._squares[line][col] != self._squares[line][col + i]:
                return False
        if col + 5 < 15 and self._squares[line][col] == self._squares[line][col + 5]:
            return False
        return True

    def verifyColumn(self, line, col):
        """
        Checks if 5 consecutive elements on a column have the same value
        :param line: integer
        :param col: integer
        :return: True - if they do
                 False, otherwise
        """
        for i in range(1, 5):
            if self._squares[line][col] != self._squares[line + i][col]:
                return False
        if line + 5 < 15 and self._squares[line][col] == self._squares[line + 5][col]:
            return False
        return True

    def verifyDiagonal1(self, line, col):
        """
        Checks if 5 consecutive elements on the main diagonal have the same value
        :param line: integer
        :param col: integer
        :return: True - if they do
                 False, otherwise
        """
        for i in range(1, 5):
            if self._squares[line][col] != self._squares[line + i][col + i]:
                return False
        if line + 5 < 15 and col + 5 < 15 and self._squares[line][col] == self._squares[line + 5][col + 5]:
            return False
        return True

    def verifyDiagonal2(self, line, col):
        """
        Checks if 5 consecutive elements on the secondary diagonal have the same value
        :param line: integer
        :param col: integer
        :return: True - if they do
                 False, otherwise
        """
        for i in range(1, 5):
            if self._squares[line][col] != self._squares[line + i][col - i]:
                return False
        if line + 5 < 15 and col - 5 >= 0 and self._squares[line][col] == self._squares[line + 5][col - 5]:
            return False
        return True

    def win(self, sq):
        """
        Checks if a square is part of a winning formation
        :param sq: Square
        :return: True - if it is
                 False, otherwise
        """
        for i in range(0, 5):
            if sq.column - i >= 0 and sq.column + 4 < 15 and self.verifyLine(sq.line, sq.column - i):
                return True
            if sq.line - i >= 0 and sq.line + 4 < 15 and self.verifyColumn(sq.line - i, sq.column):
                return True
            if sq.line - i >= 0 and sq.column - i >= 0 and sq.line + 4 < 15 and sq.column + 4 < 15 and self.verifyDiagonal1(sq.line - i, sq.column - i):
                return True
            if sq.line - i >= 0 and sq.column + i < 15 and sq.line + 4 < 15 and sq.column - 4 >= 0 and self.verifyDiagonal2(sq.line - i, sq.column + i):
                return True
        return False

    def tie(self):
        """
        Checks if there are any unoccupied squares
        :return: True - if there no more moves can be made
                 False, otherwise
        """
        return len(self.emptySquares()) == 0

    def move(self, sq, stone):
        """
        Places a stone on the square with the given coordinates.
        :param sq: Square
        :param stone: integer
        :return: updated version of the board or an error if the move did not respect the rules

        """
        if sq.line >= 15 or sq.line < 0 or sq.column >= 15 or sq.column < 0:
            raise GomokuError("Move outside the board! Please choose numbers between 1 and 15.")

        if self._squares[sq.line][sq.column] != 0:
            raise GomokuError("Square already taken! Please choose a free square.")

        ds = {1: 1, 2: 2}
        self._squares[sq.line][sq.column] = ds[stone]

    def __str__(self):
        t = Texttable()
        ds = {1: "○", 2: "●", 0: " "}
        t.add_row([" ", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        for i in range(15):
            line = self._squares[i][:]
            line.insert(0, i+1)
            for j in range(1, 16):
                line[j] = ds[line[j]]
            t.add_row(line)

        return t.draw()
