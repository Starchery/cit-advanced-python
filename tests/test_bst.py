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


@pytest.fixture
def example_tree2():
    tree = Bst()
    tree.insert(2)
    tree.insert(4)
    tree.insert(8)
    tree.insert(5)
    tree.insert(9)
    tree.insert(7)
    return tree


def test_bst_inherits_tree():
    tree = Bst(5)
    tree.root.left = Node(2)
    tree.root.right = Node(7)
    lst = [node.data for node in tree.preorder()]
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

    lst = [node.data for node in example_tree.preorder()]
    assert lst == [5, 2, 1, 4, 3, 8, 7, 6, 9]


def test_insert_order1(example_tree):
    tree = Bst()
    tree.insert(2)
    tree.insert(4)
    tree.insert(8)
    tree.insert(5)
    tree.insert(9)
    tree.insert(7)
    lst = [node.data for node in tree.preorder()]
    examplelst = [node.data for node in example_tree.preorder()]
    assert lst != examplelst


def test_search(example_tree):
    assert example_tree.__contains__(5)
    assert example_tree.__contains__(2)
    assert example_tree.__contains__(4)
    assert example_tree.__contains__(8)
    assert example_tree.__contains__(7)
    assert example_tree.__contains__(9)

    assert not example_tree.__contains__(10)
    assert not example_tree.__contains__(11)
    assert not example_tree.__contains__(0)
    assert not example_tree.__contains__(500)


def test_search2(example_tree):
    assert 5 in example_tree
    assert 2 in example_tree
    assert 4 in example_tree
    assert 8 in example_tree
    assert 7 in example_tree
    assert 9 in example_tree

    assert 10 not in example_tree
    assert 11 not in example_tree
    assert 0 not in example_tree
    assert 500 not in example_tree




def test_height(example_tree, example_tree2):
    assert example_tree.height() == 3
    assert example_tree2.height() == 5

    empty = Bst()
    assert empty.height() == 0
    empty.insert(1)
    assert empty.height() == 1

