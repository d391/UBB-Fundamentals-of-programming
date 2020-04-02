from Gomoku import *


class UI:
    def __init__(self, gomoku):
        self._gom = gomoku

    def readMove(self):
        while True:
            try:
                tokens = input("Enter move (row column)> ").split()
                if tokens[0] == "exit":
                    return "exit"
                sq = Square(int(tokens[0]) - 1, int(tokens[1]) - 1)
                return sq
            except Exception as e:
                print("Invalid input! Try again.")

    def run(self):
        print("WELCOME TO GOMOKU!")
        print("If you want to exit, type 'exit' in 'Enter move> '")
        print("The coordinates of the squares must be between 1 and 15")
        ds = [1, 2]
        humanStone = int(input("Choose your stone! Choose 1 for white or 2 for black: "))
        ds.remove(humanStone)
        computerStone = ds[0]

        board = self._gom.board

        humanTurn = True
        humanWin = False
        computerWin = False
        tie = False
        possibleSquares = []
        computerMove = Square(-1, -1)
        defense = False

        while humanWin is False and computerWin is False and tie is False:
            if humanTurn:
                print(str(board))
                print()
                humanMove = self.readMove()
                if type(humanMove) == str:
                    return False

                try:
                    self._gom.moveHuman(humanMove, humanStone)
                    if board.win(humanMove):
                        humanWin = True
                except GomokuError as e:
                    print(str(e))
                    humanTurn = not humanTurn

            else:
                prevMove = computerMove
                computerMove = self._gom.moveComputer(computerStone, humanMove, prevMove, defense, possibleSquares)
                print("Computer move: " + str(computerMove.line + 1) + " " + str(computerMove.column + 1))
                if board.win(computerMove):
                    computerWin = True

            tie = board.tie()
            humanTurn = not humanTurn

        print(str(board))
        print("Game over!")
        if humanWin:
            print("Player wins!")
        elif computerWin:
            print("Computer wins!")
        else:
            print("It's a tie!")
