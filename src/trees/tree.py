# From Python 3.8 and on
# You can supply optional "type hints"
# for variables and arguments

from typing import Iterator, Optional
from __future__ import annotations


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
    - `data : int`
        - The payload a node is holding.
    - `left : Node`, optional
        - The left child of the the node, by default `None`.
    - `right : Node`, optional
        - The right child of the the node, by default `None`.
    """
    def __init__(
        self,
        data: int,
        left: Optional[Node] = None,
        right: Optional[Node] = None
    ):
        self.data = data
        self.left = left
        self.right = right


    def __repr__(self) -> str:
        """
        Dev-friendly representation of a Node.

        Example
        -------
        >>> "Node(2)"

        Returns
        -------
        - `str`
            - String representing the Node.
        """
        return f"Node({self.data})"


    def __str__(self) -> str:
        """
        User-friendly representation of a Node.

        Example
        -------
        >>> "2"

        Returns
        -------
        - str
            - String representing the Node.
        """
        return f"{self.data}"


class Tree:
    """
    A binary tree of Nodes.

    Every node thinks of itself as the root node of its own tree.
    This class imposes structure on a collection of nodes
    by keeping track of which one is the "real root."

    Attributes
    -----------
    - `root : Optional[Node]`
        - The root/start of our tree, by default `None`.
        If this value is `None`, then the tree is empty.
    """
    def __init__(self, data: Optional[int] = None):
        """
        Create a new Tree.

        Parameters
        ----------
        - `data : int`, optional
            - The value the root node will hold, by default `None`.
            If this is not given, the tree will be empty.
        """
        self.root: Optional[Node] = None
        if data:
            self.root = Node(data)


    def preorder(self) -> Iterator[Node]:
        """
        Iterator over the nodes of the Tree in preorder.

        Yields
        -------
        - `Node`
            - Each node in the tree, in preorder.
        """
        def preorder_iter(root: Optional[Node]) -> Iterator[Node]:
            """
            Helper for `preorder`.

            We can work one node at a time
            by calling this function recursively.

            To kick it off, it's immediately called
            with the root node of our tree.

            Parameters
            ----------
            - `root : Optional[Node]`
                - The root node of the current subtree.

            Yields
            -------
            - `Node`
                - The nodes of this subtree.
            """
            if root is not None:
                yield root
                yield from preorder_iter(root.left)
                yield from preorder_iter(root.right)
        yield from preorder_iter(self.root)


    def inorder(self) -> Iterator[Node]:
        """
        Iterator over the nodes of the Tree in inorder.

        Yields
        -------
        - `Node`
            - Each node in the tree, in inorder.
        """
        def inorder_iter(root: Optional[Node]) -> Iterator[Node]:
            """
            Helper for `inorder`.

            We can work one node at a time
            by calling this function recursively.

            To kick it off, it's immediately called
            with the root node of our tree.

            Parameters
            ----------
            - `root : Optional[Node]`
                - The root node of the current subtree.

            Yields
            -------
            - `Node`
                - The nodes of this subtree.
            """
            if root is not None:
                yield from inorder_iter(root.left)
                yield root
                yield from inorder_iter(root.right)
        yield from inorder_iter(self.root)


    def postorder(self) -> Iterator[Node]:
        """
        Iterator over the nodes of the Tree in postorder.

        Yields
        -------
        - `Node`
            - Each node in the tree, in postorder.
        """

        def postorder_iter(root: Optional[Node]) -> Iterator[Node]:
            """
            Helper for `postorder`.

            We can work one node at a time
            by calling this function recursively.

            To kick it off, it's immediately called
            with the root node of our tree.

            Parameters
            ----------
            - `root : Optional[Node]`
                - The root node of the current subtree.

            Yields
            -------
            - `Node`
                - The nodes of this subtree.
            """
            if root is not None:
                yield from postorder_iter(root.right)
                yield from postorder_iter(root.left)
                yield root
        yield from postorder_iter(self.root)


    def __iter__(self) -> Iterator[Node]:
        """
        Preorder traversal over Nodes.

        Yields
        -------
        - `Node`
            - The next node in the tree, ordered in preorder.
        """
        yield from self.preorder()


    def __repr__(self) -> str:
        """
        Dev-friendly representation of the Tree.
        Lists nodes in preorder.

        Example
        -------
        >>> "Tree(Node(2), Node(3), Node(5))"

        Returns
        -------
        - `str`
            - String representing the Tree in preorder.
        """
        result: str = "Tree("

        result += ", ".join(repr(node) for node in self)

        result += ")"
        return result