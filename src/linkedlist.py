
from typing import Optional


class Node:
    """ A node for a singly linked list """
    def __init__(self, data: int):
        self.data = data
        self.next: Optional[Node] = None
    def __repr__(self):
        return f"Node({self.data})"
    def __str__(self):
        return f"{self.data}"


class LinkedList:
    """ A singly linked list of ints.  """
    def __init__(self):
        self.head: Optional[Node] = None


    def __iter__(self):
        """ Useful for writing data structures
        allows us to use for loops to iterate
        over values in our structure

        Yields: Node
        """
        cursor = self.head
        while cursor is not None:
            yield cursor
            cursor = cursor.next


    def __len__(self) -> int:
        """ Returns the length of a linked list.  """

        # sums up a list of 1s for every node in the list
        # for a list of 5 elements,
        # [1, 2, 3, 4, 5]
        # returns the sum of
        # [1, 1, 1, 1, 1]
        # aka 5
        return sum(1 for _ in self)


    def __repr__(self) -> str:
        """
        "LinkedList(Node(1)->Node(2)->Node(3)->None)"

        Returns:
            str: list represented as developer-facing string
        """
        result = "LinkedList("
        result += "->".join(repr(node) for node in self)
        result += "->None)"
        return result


    def __str__(self) -> str:
        """
        [1, 2, 3]

        Returns:
            str: list represented as user-facing string
        """
        result = "["
        result += ", ".join(str(node) for node in self)
        result += "]"
        return result


    def __contains__(self, target: int) -> bool:
        """ Tests if some element is in our list.

        Args:
            target (int): the search value.

        Returns:
            bool: whether target is in the list.
        """
        for node in self:
            if node.data == target:
                return True

        return False


    def contains(self, target: int) -> bool:
        return target in self


    def print_list(self):
        for node in self:
            print(node.data)


    def push_front(self, element: int):
        """
        1->2->3
        5    1->2->3
        5--->1->2->3
        5->1->2->3

        Args:
            element (int): The item to add.
        """
        node = Node(element)  # creating a new node
        node.next = self.head
        self.head = node



    def insert_after(self, prev_node: Node, new_data: int):
        """
        insert a new node with (new_data) after prev_node

        [1, 2, 3]
        I want to insert 5 after 2
        The next element after 5 is 3.
            > 5-
            |  |
            |  v
        [1, 2, 3]
        [1, 2, 5, 3]

        Args:
            prev_node (Node): node before new node
            new_data (int): data to insert after prev_node
        """
        node = Node(new_data)
        node.next = prev_node.next
        prev_node.next = node


    def append(self, new_data: int):
        """ 1->2->3
        Node(1)->Node(2)->Node(3)->None

        Args:
            new_data (int): data to add to back of list
        """
        if self.head is None:
            self.head = Node(new_data)
            return

        lastnode = self.head
        while lastnode.next is not None:
            lastnode = lastnode.next

        self.insert_after(lastnode, new_data)


    def remove(self, target: int):
        """
        remove the value 4
        Node(1)->Node(2)->Node(3)->Node(4)->Node(5)->None
        Node(1)->Node(2)->Node(3)---------->Node(5)->None
        Node(1)->Node(2)->Node(3)->Node(5)->None

        Args:
            target (int): value to be removed
        """
        prev = None
        for node in self:
            if node.data == target:
                if prev is not None:
                    prev.next = node.next
                else:
                    self.head = node.next
                return
            prev = node
        return

