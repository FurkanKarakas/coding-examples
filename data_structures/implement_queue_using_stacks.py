"""Append all pushed numbers to s1. When you try to pop from the queue, pop from the stack s2 and return this result.
If there are no numbers in s2, then pop all numbers from s1 and append them to s2.

Note that the average run time will be O(1). But at a specific pop operation, it might take arbitrarily many operations
to move the numbers from s1 to s2.
"""


class MyQueue:
    def __init__(self):
        self.s1 = list()
        self.s2 = list()

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if self.s2:
            return self.s2.pop()
        while self.s1:
            self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        return self.s2[-1] if self.s2 else self.s1[0]

    def empty(self) -> bool:
        return len(self.s1) + len(self.s2) == 0


if __name__ == "__main__":
    q = MyQueue()
    for i in range(10):
        q.push(i)
    print(f"Is queue empty? {q.empty()}")
    for _ in range(10):
        print(f"Peek: {q.peek()}")
        print(f"Popped from the queue: {q.pop()}")
