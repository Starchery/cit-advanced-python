from typing import Iterator, Optional
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


    def __contains__(self, target: int) -> bool:
        def search_node(subtree: Optional[Node]) -> bool:
            if subtree is None:
                return False
            elif target == subtree.data:
                return True
            elif target > subtree.data:
                return search_node(subtree.right)
            else:  # target < subtree.data
                return search_node(subtree.left)

        return search_node(self.root)


    def __iter__(self) -> Iterator[Node]:
        yield from self.inorder()




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
            if new_data == subtree.data:  # the data already exists!
                return False  # insertion failed, nothing to do
            elif new_data < subtree.data:
                if subtree.left is None:
                    # insert a new node in the empty space
                    # where the subtree's left child would be
                    subtree.left = Node(new_data)
                    return True  # insertion successful
                else: # the subtree has a left child
                    # recurse, treating the left child
                    # as its own subtree and inserting
                    # the data into it
                    return insert_node(subtree.left)
            else:  # new_data > subtree.data
                if subtree.right is None:
                    subtree.right = Node(new_data)
                    return True
                else:
                    return insert_node(subtree.right)

        # IMPORTANT: we need this check here
        # so we know to update the BST's
        # `root` attribute
        if self.root is None:
            self.root = Node(new_data)
            return True

        # The kickoff point. Start off with the root node.
        return insert_node(self.root)


    def height(self) -> int:
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
        def height_node(subtree: Optional[Node]) -> int:
            if subtree is None:
                return 0
            else:
                left_height = height_node(subtree.left)
                right_height = height_node(subtree.right)
                return 1 + max(left_height, right_height)

        return height_node(self.root)