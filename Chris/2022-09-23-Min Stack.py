class MinStack:

    def __init__(self):
        
        self.stack = []

    def push(self, val: int) -> None:
        
        if not self.stack or self.stack[-1][1] > val:
            minVal = val
        else:
            minVal = self.stack[-1][1]
        
        self.stack.append([val, minVal])
        

    def pop(self) -> None:
        
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()