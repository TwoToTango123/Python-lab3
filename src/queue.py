class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x: int) -> None:
        self.queue.append(x)

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)

    def front(self) -> int:
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.queue[0]

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def __len__(self) -> int:
        return len(self.queue)
