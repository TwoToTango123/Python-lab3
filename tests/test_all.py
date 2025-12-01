import pytest
from src.factorial import factorial, factorial_recursive
from src.fibo import fibo, fibo_recursive
from src.queue import Queue
from src.stack import Stack
from src.sorts import (
    bubble_sort, quick_sort, counting_sort,
    radix_sort, bucket_sort, heap_sort
)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

def test_factorial_recursive():
    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
    assert factorial_recursive(5) == 120
    with pytest.raises(ValueError, match="n must be non-negative"):
        factorial_recursive(-1)

def test_fibo():
    assert fibo(0) == 0
    assert fibo(1) == 1
    assert fibo(10) == 55

def test_fibo_recursive():
    assert fibo_recursive(0) == 0
    assert fibo_recursive(1) == 1
    assert fibo_recursive(10) == 55
    with pytest.raises(ValueError, match="n must be non-negative"):
        fibo_recursive(-1)

def test_queue():
    q = Queue()
    assert q.is_empty()
    q.enqueue(1)
    q.enqueue(2)
    assert not q.is_empty()
    assert q.front() == 1
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.is_empty()
    with pytest.raises(IndexError, match="dequeue from empty queue"):
        q.dequeue()

def test_stack():
    s = Stack()
    assert s.is_empty()
    s.push(3)
    s.push(1)
    s.push(2)
    assert not s.is_empty()
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.min() == 1
    assert len(s) == 2
    s.pop()
    s.pop()
    assert s.is_empty()
    with pytest.raises(IndexError, match="pop from empty stack"):
        s.pop()

@pytest.mark.parametrize("sort_func", [
    bubble_sort, quick_sort, counting_sort, heap_sort
])
def test_integer_sorts(sort_func):
    arr = [3, -1, 4, 1, 5, -2]
    assert sort_func(arr) == [-2, -1, 1, 3, 4, 5]

def test_radix_sort():
    arr = [3, 6, 4, 1, 5, 9]
    assert radix_sort(arr) == [1, 3, 4, 5, 6, 9]

def test_bucket_sort():
    arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
    assert bucket_sort(arr) == sorted(arr)

def test_sorts_empty():
    for sort in [bubble_sort, quick_sort, counting_sort, radix_sort, heap_sort, bucket_sort]:
        assert sort([]) == []
