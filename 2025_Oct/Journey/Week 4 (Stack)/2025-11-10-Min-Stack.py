class MinStack:
    def __init__(self):
        # create an empty list to use as a stack
        # each element will store (value, current_min)
        self.stack = []

    def push(self, val: int) -> None:
        # if the stack is not empty and the last min is smaller than the new value,
        # keep the same minimum as before
        if self.stack and self.stack[-1][1] < val:
            self.stack.append((val, self.stack[-1][1]))
        # otherwise, the new value becomes the new minimum
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        # remove the top element from the stack
        self.stack.pop()

    def top(self) -> int:
        # return the top value (first item of the pair)
        return self.stack[-1][0]

    def getMin(self) -> int:
        # return the current minimum (second item of the pair)
        return self.stack[-1][1]


# Example of how the class is used:
# obj = MinStack()
# obj.push(-2)
# obj.push(0)
# obj.push(-3)
# print(obj.getMin())  # -> -3
# obj.pop()
# print(obj.top())     # -> 0
# print(obj.getMin())  # -> -2
