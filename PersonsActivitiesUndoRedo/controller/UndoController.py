class UndoController:

    def __init__(self):
        self._operations = []
        self._index = -1
        self._undosDone = -1
        self._redosDone = -1

    def index(self):
        return self._index

    def undo(self):
        if self._index < 0:
            return False
        self._operations[self._index].undo()
        self._undosDone += 1
        self._index -= 1
        return True

    def redo(self):
        if self._index >= len(self._operations) and self._undosDone <= self._redosDone:
            return False
        self._operations[self._index].redo()
        self._redosDone += 1
        self._index += 1
        return True

    def addOperation(self, op):
        self._operations = self._operations[:self._index + 1]
        self._index += 1
        self._operations.append(op)


class CascadeOperation:
    def __init__(self):
        self._operations = []

    def add(self, operation):
        self._operations.append(operation)

    def undo(self):
        for o in self._operations:
            o.undo()

    def redo(self):
        for o in self._operations:
            o.redo()


class Operation:
    def __init__(self, undoFunction, redoFuntion):
        self._undoFunction = undoFunction
        self._redoFunction = redoFuntion

    def undo(self):
        self._undoFunction.call()

    def redo(self):
        self._redoFunction.call()


class Function:
    def __init__(self, funct, *param):
        self._funct = funct
        self._param = param

    def call(self):
        self._funct(*self._param)
