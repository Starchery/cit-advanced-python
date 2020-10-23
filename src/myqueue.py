# Use a list as my backing data/representation

class ArrayQueue:
    def __init__(self):
        self.data = []

    def enqueue(self, value: int):
        self.data.insert(0, value)

    def dequeue(self):
        if not self.is_empty():
            return self.data.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __repr__(self):
        # official representation for an object
        # only developers see this
        return "Queue(" + repr(self.data)[1:-1] + ")"

    def __str__(self):
        # user facing data
        # the way we want the USER
        #       to see our object
        return "Queue(" + str(self.data)[1:-1] + ")"