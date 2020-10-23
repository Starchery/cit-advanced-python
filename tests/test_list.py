from src.linkedlist import Node, LinkedList


def test_node():
    n = Node(5)
    assert n.data == 5
    assert n.next is None

def test_list():
    l = LinkedList()
    l.head = Node(1)
    l.head.next = Node(2)
    l.head.next.next = Node(3)
    assert l.head is not None
    assert l.head.next is not None
    assert l.head.next.next is not None
    assert l.head.next.next.next is None

def test_print():
    l = LinkedList()
    first = Node(3)
    l.head = first
    second = Node(4)
    first.next = second
    third = Node(5)
    second.next = third
    l.print_list()

def test_search():
    l = LinkedList()
    l.head = Node(1)
    l.head.next = Node(2)
    l.head.next.next = Node(3)
    assert l.contains(3)
    assert l.contains(2)
    assert l.contains(1)
    assert not l.contains(5)


def test_push1():
    l = LinkedList()
    l.head = Node(1)
    l.head.next = Node(2)
    l.head.next.next = Node(3)
    l.push_front(5)
    assert l.contains(5)
    assert l.head.data == 5



def test_push2():
    l = LinkedList()
    l.push_front(3)
    l.push_front(2)
    l.push_front(1)
    assert l.contains(1)
    assert l.contains(2)
    assert l.contains(3)
    assert l.head.data == 1

def test_iter():
    linklist = LinkedList()
    linklist.push_front(3)
    linklist.push_front(2)
    linklist.push_front(1)
    result = []
    for node in linklist:
        result.append(node.data)
    assert result == [1, 2, 3]



# 1
# 1->5
# 1->3->5
def test_insert():
    l = LinkedList()
    headnode = Node(1)
    l.head = headnode
    l.insert_after(headnode, 5)
    assert l.contains(5)
    assert l.contains(1)
    l.insert_after(headnode, 3)
    assert l.contains(3)
    assert l.head.data == 1
    assert l.head.next.data == 3
    assert l.head.next.next.data == 5


# 1->2
def test_append():
    l = LinkedList()
    l.append(1)
    assert l.contains(1)
    assert l.head.data == 1
    l.append(2)
    assert l.contains(2)
    assert l.head.next.data == 2


def test_remove():
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    assert l.contains(2)
    l.remove(2)
    assert not l.contains(2)

def test_remove_empty():
    l = LinkedList()
    assert l.head is None
    l.remove(5)
    assert l.head is None


def test_remove_head():
    l = LinkedList()
    l.append(1)
    assert l.contains(1)
    assert l.head is not None
    l.remove(1)
    assert not l.contains(1)
    assert l.head is None


test_print()

# l
# Node(1)->None
# Node(1)->Node(2)->None
# Node(1)->Node(2)->Node(3)->None
