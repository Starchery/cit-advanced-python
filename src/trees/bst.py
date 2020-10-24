from typing import Optional
from src.trees.tree import Tree, Node

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
    def __init__(self, data: Optional[int]=None):
        """
        Create a new BST.

        Parameters
        ----------
        - `data : int`, optional
            - The value the root node will hold, by default `None`.
            If this is not given, the tree will be empty.
        """
        super().__init__(data)


    def search(self, target: int) -> bool:
        """ TODO: implement """
        raise NotImplementedError


    def insert(self, new_data: int) -> bool:
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
        def insert_node(subtree: Optional[Node]) -> bool:
            """
            Helper function.

            Inserts the `new_data` into the given
            subtree recursively.

            We work on one node/subtree at a time
            using recursion.

            To kick it off, we call this function
            with the root node of the BST.

            Parameters
            ----------
            subtree : Optional[Node]
                The current node.

            Returns
            -------
            bool
                Whether the insertion was successful.
            """
            if new_data == subtree.data:
                return False
            elif new_data < subtree.data:
                if subtree.left is None:
                    subtree.left = Node(new_data)
                    return True
                else:
                    return insert_node(subtree.left)
            else:
                if subtree.right is None:
                    subtree.right = Node(new_data)
                    return True
                else:
                    return insert_node(subtree.right)

        if self.root is None:
            self.root = Node(new_data)
            return True

        return insert_node(self.root)
