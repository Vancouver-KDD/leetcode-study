class MinStack:

    def __init__(self):
        self.min_stack = []

    def push(self, val: int) -> None:
        min_val = val
        if len(self.min_stack) > 0:
            min_val = min(min_val, self.min_stack[-1][1])
        self.min_stack.append([val, min_val])

    def pop(self) -> None:
        self.min_stack.pop()

    def top(self) -> int:
        return self.min_stack[-1][0]

    def getMin(self) -> int:
        return self.min_stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()