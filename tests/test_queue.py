from src.myqueue import ArrayQueue

# Test-Driven Development
# TDD

# Unit tests
# I want to write tests for small pieces
# in isolation

# I want to make sure all the individual
# components work

# Testing my assumptions/expectations

def test_enqueue():
    s = ArrayQueue()
    s.enqueue(3)
    # This condition MUST be true.
    # if it isn't the test has failed.
    assert len(s.data) == 1


def test_dequeue():
    s = ArrayQueue()
    s.enqueue(3)
    s.enqueue(4)
    top = s.dequeue()
    assert top == 3

def test_peek():
    s = ArrayQueue()
    s.enqueue(3)
    assert s.peek() == 3

def test_dequeueing_changes_length():
    s = ArrayQueue()
    s.enqueue(3)
    s.enqueue(4)
    s.dequeue()
    assert len(s.data) == 1

def test_dequeue_empty():
    s = ArrayQueue()
    top = s.dequeue()
    assert top is None
    assert s.peek() is None

def test_is_empty():
    s = ArrayQueue()
    assert s.is_empty()
    s.enqueue(3)
    assert not s.is_empty()

def test_enqueue_cant_be_empty():
    s = ArrayQueue()
    s.enqueue(3)
    s.enqueue(4)
    s.enqueue(5)
    assert not s.is_empty()
    s.dequeue()
    assert not s.is_empty()
