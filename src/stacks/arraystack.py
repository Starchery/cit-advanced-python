# A stack has some data
# and some related operations on that data
# I probably want a class

from typing import Any


class ArrayStack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def pop(self):
        if not self.is_empty():
            return self.data.pop()

    def push(self, value: Any):
        self.data.append(value)

    def peek(self):
        if not self.is_empty():
            return self.data[-1]

    def is_top_even(self):
        if not self.is_empty():
            val = self.peek()
            return val and val % 2 == 0
        else:
            return False

    def __repr__(self):
        # official representation for an object
        # only developers see this
        return "Stack(" + repr(self.data)[1:-1] + ")"

    def __str__(self):
        # user facing data
        # the way we want the USER
        #       to see our object
        return "Stack(" + str(self.data)[1:-1] + ")"
