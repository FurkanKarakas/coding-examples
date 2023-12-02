class MinStack:
    """This class implements a MinStack which retrieves the minimum element in O(1) time.
    It supports adding elements on top of stack, popping, and retrieving the min element.
    """

    def __init__(self):
        self.minElement: int | float = float("inf")
        self.minElements: list[int] = list()
        self.stack: list[int] = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.minElement:
            self.minElements.append(val)
            self.minElement = val

    def pop(self) -> None:
        if len(self.stack) > 0:
            removed = self.stack.pop(-1)
            if len(self.minElements) > 0 and removed == self.minElements[-1]:
                _ = self.minElements.pop(-1)
                if len(self.minElements) > 0:
                    self.minElement = self.minElements[-1]
                else:
                    self.minElement = float("inf")

    def top(self) -> int | None:
        if len(self.stack) > 0:
            return self.stack[-1]
        return None

    def getMin(self) -> int | float | None:
        return self.minElement if self.minElement != float("inf") else None


if __name__ == "__main__":
    obj = MinStack()
    obj.push(5)
    obj.push(7)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()

    print(f"Top item: {param_3} Min element: {param_4}")
