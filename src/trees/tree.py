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
    """
    A binary tree of Nodes.

    Every node thinks of itself as the root node of its own tree.
    This class imposes structure on a collection of nodes
    by keeping track of which one is the "real root."

    Attributes
    -----------
    root : Optional[Node]
        The root/start of our tree, by default None.
        If this value is None, then the tree is empty.
    """
    def __init__(self, data: Optional[int] = None):
        """
        Parameters
        ----------
        data : int, optional
            The value the root node will hold, by default None
            If this is not given, the tree will be empty.
        """
        self.root: Optional[Node] = None
        if data:
            self.root = Node(data)


    def preorder(self):
        """
        Iterator over the nodes of the Tree in preorder.

        Yields
        -------
        Node
            Each node in the tree, in preorder.
        """
        def preorder_iter(root: Optional[Node]):
            if root is not None:
                yield root
                yield from preorder_iter(root.left)
                yield from preorder_iter(root.right)
        yield from preorder_iter(self.root)


    def inorder(self):
        """
        Iterator over the nodes of the Tree in inorder.

        Yields
        -------
        Node
            Each node in the tree, in inorder.
        """
        def inorder_iter(root: Optional[Node]):
            if root is not None:
                yield from inorder_iter(root.left)
                yield root
                yield from inorder_iter(root.right)
        yield from inorder_iter(self.root)


    def postorder(self):
        """
        Iterator over the nodes of the Tree in postorder.

        Yields
        -------
        Node
            Each node in the tree, in postorder.
        """

        def postorder_iter(root: Optional[Node]):
            if root is not None:
                yield from postorder_iter(root.right)
                yield from postorder_iter(root.left)
                yield root
        yield from postorder_iter(self.root)


    def __iter__(self):
        """
        Preorder traversal over Nodes.

        Yields
        -------
        Node
            The next node in the tree, ordered in preorder.
        """
        yield from self.preorder()


    def __repr__(self) -> str:
        """
        Dev-friendly representation of the Tree.
        Lists nodes in preorder.

        Example
        -------
        "Tree(Node(2), Node(3), Node(5))"

        Returns
        -------
        str
            String representing the Tree in preorder.
        """
        result = "Tree("

        result += ", ".join(repr(node) for node in self)

        result += ")"
        return result