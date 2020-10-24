from src.trees.bst import Bst
from src.trees.tree import Node

import pytest

@pytest.fixture
def example_tree():
    tree = Bst(5)
    tree.root.left = Node(2)
    tree.root.left.right = Node(4)
    tree.root.right = Node(8)
    tree.root.right.left = Node(7)
    tree.root.right.right = Node(9)
    return tree

def test_bst_inherits_tree():
    tree = Bst(5)
    tree.root.left = Node(2)
    tree.root.right = Node(7)
    lst = [node.data for node in tree]
    assert lst == [5, 2, 7]


def test_insert(example_tree):
    tree = Bst()
    tree.insert(5)
    tree.insert(2)
    tree.insert(4)
    tree.insert(8)
    tree.insert(7)
    tree.insert(9)
    treelist = [node.data for node in tree]
    exampletreelist = [node.data for node in example_tree]
    assert treelist == exampletreelist


def test_insert_order(example_tree):
    example_tree.insert(6)
    example_tree.insert(1)
    example_tree.insert(5)
    example_tree.insert(3)

    lst = [node.data for node in example_tree]
    assert lst == [5, 2, 1, 4, 3, 8, 7, 6, 9]


def test_insert_order1(example_tree):
    tree = Bst()
    tree.insert(2)
    tree.insert(4)
    tree.insert(8)
    tree.insert(5)
    tree.insert(9)
    tree.insert(7)
    lst = [node.data for node in tree]
    examplelst = [node.data for node in example_tree]
    assert lst != examplelst