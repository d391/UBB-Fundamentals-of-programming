from Board import *
import random


class Gomoku:
    def __init__(self):
        self._board = Board()

    @property
    def board(self):
        return self._board

    def moveHuman(self, sq, stone):
        """
        Places the stone on the squares with the coordinates given by the player
        :param sq: Square
        :param stone: integer
        :return: updated version of the board
        """
        self._board.move(sq, stone)

    def verifyDanger(self, move, eSq):
        """
        Checks if a formation of 3 squares is made and returns the square with which the formation might be blocked
        :param move: Square
        :param eSq: list
        :return: sq1 or sq2 - the coordinates of such a square
                 sq - of -1, -1 if such a square does not exist
        """
        # column !
        clear = False
        pos = False
        pos2 = False

        if move.line + 3 < 15:
            sq1 = Square(move.line + 3, move.column)
            pos = True
        if move.line - 1 >= 0:
            sq2 = Square(move.line - 1, move.column)
            pos2 = True

        if pos is True:
            for i in range(1, 3):
                if self._board.squares[move.line][move.column] != self._board.squares[move.line + i][move.column]:
                    clear = True
                    break
            if clear is False:
                if sq1 in eSq:
                    return sq1
                if pos2 is True and sq2 in eSq:
                    return sq2

        # column ^
        clear = False
        pos = False
        pos2 = False

        if move.line - 3 >= 0:
            sq1 = Square(move.line - 3, move.column)
            pos = True
        if move.line + 1 < 15:
            sq2 = Square(move.line + 1, move.column)
            pos2 = True

        if pos is True:
            for i in range(1, 3):
                if self._board.squares[move.line][move.column] != self._board.squares[move.line - i][move.column]:
                    clear = True
                    break
            if clear is False:
                if sq1 in eSq:
                    return sq1
                if pos2 is True and sq2 in eSq:
                    return sq2

        # line >
        clear = False
        pos = False
        pos2 = False

        if move.column + 3 < 15:
            sq1 = Square(move.line, move.column + 3)
            pos = True
        if move.line - 1 >= 0:
            sq2 = Square(move.line, move.column - 1)
            pos2 = True

        if pos is True:
            for i in range(1, 3):
                if self._board.squares[move.line][move.column] != self._board.squares[move.line][move.column + i]:
                    clear = True
                    break
            if clear is False:
                if sq1 in eSq:
                    return sq1
                if pos2 is True and sq2 in eSq:
                    return sq2

        # line <
        clear = False
        pos = False
        pos2 = False

        if move.column - 3 >= 0:
            sq1 = Square(move.line, move.column - 3)
            pos = True
        if move.column + 1 < 15:
            sq2 = Square(move.line, move.column + 1)
            pos2 = True

        if pos is True:
            for i in range(1, 3):
                if self._board.squares[move.line][move.column] != self._board.squares[move.line][move.column - i]:
                    clear = True
                    break
            if clear is False:
                if sq1 in eSq:
                    return sq1
                if pos2 is True and sq2 in eSq:
                    return sq2


        # diagonal /^
        clear = False
        pos = False
        pos2 = False

        if move.line - 3 >= 0 and move.column + 3 < 15:
            sq1 = Square(move.line - 3, move.column + 3)
            pos = True
        if move.column - 1 >= 0 and move.line + 1 < 15:
            sq2 = Square(move.line + 1, move.column - 1)
            pos2 = True

        if pos is True:
            for i in range(1, 3):
                if self._board.squares[move.line][move.column] != self._board.squares[move.line - i][move.column + i]:
                    clear = True
                    break
            if clear is False:
                if sq1 in eSq:
                    return sq1
                if pos2 is True and sq2 in eSq:
                    return sq2

        # diagonal / !
        clear = False
        pos = False
        pos2 = False

        if move.line + 3 < 15 and move.column - 3 >= 0:
            sq1 = Square(move.line + 3, move.column - 3)
            pos = True
        if move.line - 1 >= 0 and move.column + 1 < 15:
            sq2 = Square(move.line - 1, move.column + 1)
            pos2 = True

        if pos is True:
            for i in range(1, 3):
                if self._board.squares[move.line][move.column] != self._board.squares[move.line + i][move.column - i]:
                    clear = True
                    break
            if clear is False:
                if sq1 in eSq:
                    return sq1
                if pos2 is True and sq2 in eSq:
                    return sq2

        # diagonal \^
        clear = False
        pos = False
        pos2 = False

        if move.line - 3 >= 0 and move.column - 3 >= 0:
            sq1 = Square(move.line - 3, move.column - 3)
            pos = True
        if move.column + 1 < 15 and move.line + 1 < 15:
            sq2 = Square(move.line + 1, move.column + 1)
            pos2 = True

        if pos is True:
            for i in range(1, 3):
                if self._board.squares[move.line][move.column] != self._board.squares[move.line - i][move.column - i]:
                    clear = True
                    break
            if clear is False:
                if sq1 in eSq:
                    return sq1
                if pos2 is True and sq2 in eSq:
                    return sq2

        # diagonal \ !
        clear = False
        pos = False
        pos2 = False

        if move.line + 3 < 15 and move.column + 3 < 15:
            sq1 = Square(move.line + 3, move.column + 3)
            pos = True
        if move.column - 1 >= 0 and move.line >= 0:
            sq2 = Square(move.line - 1, move.column - 1)
            pos2 = True

        if pos is True:
            for i in range(1, 3):
                if self._board.squares[move.line][move.column] != self._board.squares[move.line + i][move.column + i]:
                    clear = True
                    break
            if clear is False:
                if sq1 in eSq:
                    return sq1
                if pos2 is True and sq2 in eSq:
                    return sq2

        #Special cases
        #  ^
        #  x
        if move.line - 2 >= 0 \
                and self._board.squares[move.line][move.column] == self._board.squares[move.line - 2][move.column] \
                and self._board.squares[move.line - 1][move.column] == 0:
            sq = Square(move.line - 1, move.column)
            return sq

        # x >
        if move.column + 2 < 15 \
                and self._board.squares[move.line][move.column] == self._board.squares[move.line][move.column + 2] \
                and self._board.squares[move.line][move.column + 1] == 0:
            sq = Square(move.line, move.column + 1)
            return sq

        # < x
        if move.column - 2 >= 0 \
                and self._board.squares[move.line][move.column] == self._board.squares[move.line][move.column - 2] \
                and self._board.squares[move.line][move.column - 1] == 0:
            sq = Square(move.line, move.column - 1)
            return sq

        #  x
        #  ^
        if move.line + 2 < 15 \
                and self._board.squares[move.line][move.column] == self._board.squares[move.line + 2][move.column] \
                and self._board.squares[move.line + 1][move.column] == 0:
            sq = Square(move.line + 1, move.column)
            return sq

        #^
        #  x
        if move.line - 2 >= 0 and move.column - 2 >= 0 \
                and self._board.squares[move.line][move.column] == self._board.squares[move.line - 2][move.column - 2] \
                and self._board.squares[move.line - 1][move.column - 1] == 0:
            sq = Square(move.line - 1, move.column - 1)
            return sq

        #    ^
        #  x
        if move.line - 2 >= 0 and move.column + 2 < 15 \
                and self._board.squares[move.line][move.column] == self._board.squares[move.line - 2][move.column + 2] \
                and self._board.squares[move.line - 1][move.column + 1] == 0:
            sq = Square(move.line - 1, move.column + 1)
            return sq

        #  x
        #^
        if move.line + 2 < 15 and move.column - 2 >= 0 \
                and self._board.squares[move.line][move.column] == self._board.squares[move.line + 2][move.column - 2] \
                and self._board.squares[move.line + 1][move.column - 1] == 0:
            sq = Square(move.line + 1, move.column - 1)
            return sq

        #  x
        #    ^
        if move.line + 2 < 15 and move.column + 2 < 15 \
                and self._board.squares[move.line][move.column] == self._board.squares[move.line + 2][move.column + 2] \
                and self._board.squares[move.line + 1][move.column + 1] == 0:
            sq = Square(move.line + 1, move.column + 1)
            return sq

        sq = Square(-1, -1)
        return sq

    def possibleAttack(self, move, possibleSquares):
        """
        Adds to a list all the surrounding squares of a given one
        :param move: Square
        :param possibleSquares: list
        :return: updated version of possibleSquares
        """
        if move.line - 1 >= 0 and move.column - 1 >= 0:
            sq = Square(move.line - 1, move.column - 1)
            possibleSquares.append(sq)

        if move.line - 1 >= 0 and move.column + 1 < 15:
            sq = Square(move.line - 1, move.column + 1)
            possibleSquares.append(sq)

        if move.line + 1 >= 0 and move.column - 1 < 15:
            sq = Square(move.line + 1, move.column - 1)
            possibleSquares.append(sq)

        if move.line + 1 >= 0 and move.column + 1 < 15:
            sq = Square(move.line + 1, move.column + 1)
            possibleSquares.append(sq)

        if move.line + 1 < 15:
            sq = Square(move.line + 1, move.column)
            possibleSquares.append(sq)

        if move.line - 1 >= 0:
            sq = Square(move.line - 1, move.column)
            possibleSquares.append(sq)

        if move.column - 1 >= 0:
            sq = Square(move.line, move.column - 1)
            possibleSquares.append(sq)

        if move.column + 1 < 15:
            sq = Square(move.line, move.column + 1)
            possibleSquares.append(sq)

    def moveComputer(self, stone, humanMove, prevMove, defense, possibleSquares):
        """
        Generates a move for specific situations of the game (blocking the player, trying to win)
        :param stone: integer
        :param humanMove: Square
        :param prevMove: Square
        :param defense: boolean
        :param possibleSquares: list
        :return: the resulted move: Square
        """
        eSq = self._board.emptySquares()
        tSq = self.verifyDanger(humanMove, eSq)
        if tSq.line != -1:
            self.board.move(tSq, stone)
            defense = True
            return tSq
        elif possibleSquares != []:
            while True:
                aSq = self.verifyDanger(prevMove, eSq)
                if aSq.line != -1 and defense is False:
                    self.board.move(aSq, stone)
                    self.possibleAttack(aSq, possibleSquares)
                    return aSq
                else:
                    defense = False
                    bSq = possibleSquares.pop()
                    while self.board.squares[bSq.line][bSq.column] != 0:
                        bSq = possibleSquares.pop()
                    self.board.move(bSq, stone)
                    self.possibleAttack(bSq, possibleSquares)
                    return bSq
        else:
            sq = random.choice(eSq)
            self.possibleAttack(sq, possibleSquares)
            self.board.move(sq, stone)
            return sq
