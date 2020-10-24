from typing import Optional
from src.trees.tree import Tree, Node

class Bst(Tree):
    def __init__(self, data: Optional[int]=None):
        super().__init__(data)


    def search(self, target: int) -> bool:
        raise NotImplementedError


    def insert(self, new_data: int) -> bool:
        def insert_node(subtree: Optional[Node]) -> bool:
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
