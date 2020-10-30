from typing import Iterator, Optional

# from src.trees.tree import Tree, Node
from .tree import Tree, Node


class Bst(Tree):
    """
    A binary search tree of Nodes.

    A BST extends a regular Binary Tree
    by imposing an ordering constraint.

    All nodes to the left of a node must
    be less than that node.

    All nodes to the right of a node must
    be greater than that node.

    All subtrees must also be valid BSTs.

    Attributes
    -----------
    - `root : Optional[Node]`
        - The root/start of our tree, by default `None`.
        If this value is `None`, then the tree is empty.
    """

    def __init__(self, data: Optional[int] = None):
        """
        Create a new BST.

        Parameters
        ----------
        - `data : int`, optional
            - The value the root node will hold, by default `None`.
            If this is not given, the tree will be empty.
        """
        super().__init__(data)

    def __contains__(self, target: int, subtree=False) -> bool:
        """
        Returns whether `target` is contained
        inside of the binary search tree.

        Parameters
        ----------
        target : int
            The value to search for.

        Returns
        -------
        bool
            Whether the value is in the tree or not.
        """
        if subtree == False:
            subtree = self.root

        if subtree is None:
            return False
        elif target == subtree.data:
            return True
        elif target > subtree.data:
            return self.__contains__(target, subtree.right)
        else:  # target < subtree.data
            return self.__contains__(target, subtree.left)

    def __iter__(self) -> Iterator[Node]:
        yield from self.inorder()

    def insert(self, new_data: int, subtree=False) -> bool:
        """
        Adds a node to in the right place
        of the BST.

        Parameters
        ----------
        new_data : int
            The data the new node will be holding.

        Returns
        -------
        bool
            Whether the insertion was successful.
        """
        if subtree == False:
            subtree = self.root
            if subtree is None:
                self.root = Node(new_data)
                return True

        if new_data == subtree.data:  # the data already exists!
            return False  # insertion failed, nothing to do
        elif new_data < subtree.data:
            if subtree.left is None:
                # insert a new node in the empty space
                # where the subtree's left child would be
                subtree.left = Node(new_data)
                return True  # insertion successful
            else:  # the subtree has a left child
                # recurse, treating the left child
                # as its own subtree and inserting
                # the data into it
                return self.insert(new_data, subtree.left)
        else:  # new_data > subtree.data
            if subtree.right is None:
                subtree.right = Node(new_data)
                return True
            else:
                return self.insert(new_data, subtree.right)

    def height(self, subtree=False) -> int:
        """
        Finds the height of a BST.
        The height is defined to be the number of levels.

        The empty tree has height 0.
        A node with no children has height 1.
        A node with children has height (1 + MAX(height Left, height Right)

        Returns
        -------
        int
            The height of the tree.
        """
        if subtree == False:
            subtree = self.root

        if subtree is None:
            return 0
        else:
            left_height = self.height(subtree.left)
            right_height = self.height(subtree.right)
            return 1 + max(left_height, right_height)

    def invert(self, subtree=False):
        """
        Inverts the binary tree.

        In essence, this swaps the left
        and right children of each node
        in the tree.

        The result will no longer
        be a valid binary search tree.
        """
        if subtree == False:
            subtree = self.root

        if subtree is None:
            return

        # swap left and right children
        subtree.left, subtree.right = subtree.right, subtree.left

        if subtree.left:
            self.invert(subtree.left)
        if subtree.right:
            self.invert(subtree.right)
