class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return None if not self.stack else self.stack[-1]

    def getMin(self) -> int:
        return None if not self.stack else min(self.stack)
