class GomokuError(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg
