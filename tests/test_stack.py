from src.stacks.arraystack import *
from src.stacks.liststack import *

# Test-Driven Development
# TDD

# Unit tests
# I want to write tests for small pieces
# in isolation

# I want to make sure all the individual
# components work

# Testing my assumptions/expectations

def test_push():
    s = ListStack()
    s.push(3)
    # This condition MUST be true.
    # if it isn't the test has failed.
    assert len(s) == 1


def test_pop():
    s = ListStack()
    s.push(3)
    s.push(4)
    top = s.pop()
    assert top == 4

def test_peek():
    s = ListStack()
    s.push(3)
    assert s.peek() == 3

def test_popping_changes_length():
    s = ListStack()
    s.push(3)
    s.push(4)
    s.pop()
    assert len(s) == 1

def test_pop_empty():
    s = ListStack()
    top = s.pop()
    assert top is None

def test_is_empty():
    s = ListStack()
    assert s.is_empty()
    s.push(3)
    assert not s.is_empty()

def test_push_cant_be_empty():
    s = ListStack()
    s.push(3)
    s.push(4)
    s.push(5)
    assert not s.is_empty()
    s.pop()
    assert not s.is_empty()

def test_list_stack():
    stack = ListStack()
    stack.push_front(3)
    stack.push_front(5)
    stack.push_front(6)
    assert stack.contains(5)
    assert 6 in stack
    assert 3 in stack
    assert stack.head is not None


# Determining if a string of parentheses is valid
def is_valid(string: str) -> bool:
    """
    Given a string only containing the characters
        '(' ')',  '[' ']', '{' '}'

    The brackets close in the correct order
    VALID:    "()" "()[]{}" "([{}])"
    INVALID:  "(]"          "([)]"
    INVALID:  "]["
    INVALID:  "["

    Args:
        string (str): a string containing parens, brackets, braces

    Returns:
        bool: whether the delimiters are balanced
    """
    stack = ListStack()
    delimiters = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    for char in string:
        # if char is an opening bracket
        if char in delimiters.values():
            stack.push(char)
        # if char is a closing bracket
        elif char in delimiters.keys():
            if stack.is_empty():
                return False
            elif delimiters[char] != stack.pop():
                return False

    return stack.is_empty()


def test_parentheses():
    assert is_valid("()")
    assert is_valid("[]")
    assert is_valid("()[]{}")
    assert is_valid("([{}])")

    assert not is_valid("(]")
    assert not is_valid("([)]")
    assert not is_valid("][")
    assert not is_valid("]")
    assert not is_valid("{")