class Square:
    def __init__(self, line, col):
        self._line = line
        self._col = col

    @property
    def line(self):
        return self._line

    @property
    def column(self):
        return self._col

    def __str__(self):
        return str(self._line) + ", " + str(self._col)

    def __eq__(self, other):
        return self.line == other.line and self.column == other.column
