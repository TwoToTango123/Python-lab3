class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack += [x]

    def pop(self) -> int:
        if self.stack:
            a = self.stack[-1]
            self.stack = self.stack[:-1]
            return a
        else:
            raise IndexError("pop from empty stack")

    def peek(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            raise IndexError("peek to empty stack")

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def __len__(self) -> int:
        count = 0
        for i in self.stack:
            count += 1
        return count

    def min(self) -> int:# за константу для Medium
        minim = self.stack[0]
        for i in self.stack:
            if i < minim:
                minim = i
        return minim
