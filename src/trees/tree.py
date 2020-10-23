# From Python 3.8 and on
# You can supply optional "type hints"
# for variables and arguments

from typing import Optional


class Node:
    """
    A node of a binary tree.

    A single node can represent a tree,
    where its children have children,
    and those children have children, etc.

    A node doesn't know whether it is the
    *root node* of a tree, however.
    Every node thinks of itself as the "root node."

    Attributes
    ----------
    data : int
        The payload a node is holding.
    left : Node, optional
        The left child of the the node, by default None
    right : Node, optional
        The right child of the the node, by default None
    """
    def __init__(self, data: int, left=None, right=None):
        self.data: int = data
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right
    def __repr__(self):
        return f"Node({self.data})"
    def __str__(self):
        return f"{self.data}"


class Tree:
    def __init__(self, data: Optional[int] = None):
        self.root: Optional[Node] = None
        if data:
            self.root = Node(data)


    def preorder(self):
        def preorder_iter(root: Optional[Node]):
            if root is not None:
                yield root
                yield from preorder_iter(root.left)
                yield from preorder_iter(root.right)
        yield from preorder_iter(self.root)


    def inorder(self):
        def inorder_iter(root: Optional[Node]):
            if root is not None:
                yield from inorder_iter(root.left)
                yield root
                yield from inorder_iter(root.right)
        yield from inorder_iter(self.root)


    def postorder(self):
        def postorder_iter(root: Optional[Node]):
            if root is not None:
                yield from postorder_iter(root.right)
                yield from postorder_iter(root.left)
                yield root
        yield from postorder_iter(self.root)


    def __iter__(self):
        """ Preorder traversal """
        yield from self.preorder()


    def __repr__(self) -> str:
        result = "Tree("

        result += ", ".join(repr(node) for node in self)

        result += ")"
        return result