class Iterable:
    def __init__(self):
        self._list = []
        self._index = -1

    @property
    def list(self):
        return self._list

    def append(self, value):
        self._list.append(value)

    def remove(self, value):
        return self._list.remove(value)

    def find(self, value):
        for val in self._list:
            if value == val:
                return True
        return False

    def __setitem__(self, key, value):
        self._list[key] = value

    def __delitem__(self, key):
        del self._list[key]

    def __next__(self):
        if self._index < len(self._list) - 1:
            self._index += 1
            return self._list[self._index]
        else:
            raise StopIteration

    def __iter__(self):
        self._index = -1
        return self
