# from src.linkedlist import *
from ..linkedlist import *

# Inheritance
# A ListStack IS A LinkedList
# I can represent that by inheriting from LinkedList
class ListStack(LinkedList):
    def __init__(self):
        super().__init__()


    def push(self, value: int):
        self.push_front(value)


    # alternative implementation
    def pop(self):
        if self.head:
            result = self.head
            self.head = self.head.next
            return result.data


    def peek(self):
        if self.head:
            return self.head.data


    def is_empty(self):
        return len(self) == 0
