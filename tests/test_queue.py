import pytest
from src.queue import Queue

def test_enqueue_and_size():
    queue = Queue()
    assert queue.size() == 0

    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.size() == 2

def test_dequeue_fifo_order():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2

def test_front():
    queue = Queue()
    queue.enqueue(5)
    assert queue.front() == 5

def test_empty_queue_dequeue():
    queue = Queue()
    with pytest.raises(IndexError):
        queue.dequeue()
