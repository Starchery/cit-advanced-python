from src.trees.tree import Node, Tree
import pytest

@pytest.fixture
def example_tree():
    tree = Tree(2)
    tr = tree.root
    tr.left = Node(4)
    tr.left.right = Node(8)
    tr.right = Node(5)
    tr.right.left = Node(9)
    tr.right.right = Node(7)
    return tree


def test_basic_nodes():
    #              (3)      <-- root
    #             /   \
    # node2->   (5)   (5)   <-- node
    #           /
    #         (2)
    node = Node(5)
    assert node.data == 5

    node2 = Node(5, left=Node(2))
    assert node2.data == 5
    assert node2.left.data == 2

    root = Node(3, left=node2, right=node)
    assert root.data == 3
    assert root.left is node2
    assert root.left.data == 5
    assert root.right is node
    assert root.right.data == 5


def test_basic_tree():
    tree = Tree()
    assert tree.root is None

    tree2 = Tree(5)
    assert tree2.root is not None
    assert tree2.root.data == 5
    assert tree2.root.right is None


def test_repr(example_tree):
    string = repr(example_tree)
    assert string == "Tree(Node(2), Node(4), Node(8), Node(5), Node(9), Node(7))"


def test_preorderiter(example_tree):
    lst = [node.data for node in example_tree.preorder()]
    assert lst == [2, 4, 8, 5, 9, 7]


def test_postorderiter(example_tree):
    lst = [node.data for node in example_tree.postorder()]
    assert lst == list(reversed([2, 4, 8, 5, 9, 7]))


def test_inorderiter(example_tree):
    lst = [node.data for node in example_tree.inorder()]
    assert lst == [4, 8, 2, 9, 5, 7]


def test_post_and_pre_opposite(example_tree):
    pre = [node.data for node in example_tree.preorder()]
    post = [node.data for node in example_tree.postorder()]
    assert pre != post
    assert list(reversed(pre)) == post
    assert pre == list(reversed(post))


def test_defaultiter(example_tree):
    lst = [node.data for node in example_tree]
    assert lst == [2, 4, 8, 5, 9, 7]





