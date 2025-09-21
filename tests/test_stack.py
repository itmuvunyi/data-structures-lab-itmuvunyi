import pytest
from src.stack import Stack

def test_push_and_size():
    stack = Stack()
    assert stack.size() == 0

    stack.push(1)
    assert stack.size() == 1

    stack.push(2)
    assert stack.size() == 2

def test_pop_lifo_order():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1

def test_peek():
    stack = Stack()
    stack.push(5)
    assert stack.peek() == 5

def test_empty_stack_pop():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()
