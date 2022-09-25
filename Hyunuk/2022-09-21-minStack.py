class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        prev = val if not self.stk else self.stk[-1][1]
        prev = min(val, prev)
        self.stk.append((val, prev))

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
