import pytest
from src.linked_list import LinkedList

def test_append_and_size():
    ll = LinkedList()
    assert ll.size() == 0

    ll.append(1)
    ll.append(2)
    assert ll.size() == 2

def test_prepend():
    ll = LinkedList()
    ll.prepend(3)
    assert ll.size() == 1
    assert ll.head.value == 3

def test_remove():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.remove(1)
    assert ll.size() == 1
    assert ll.head.value == 2

def test_find():
    ll = LinkedList()
    ll.append(5)
    ll.append(6)
    node = ll.find(6)
    assert node.value == 6

def test_is_empty():
    ll = LinkedList()
    assert ll.is_empty()
    ll.append(1)
    assert not ll.is_empty()
