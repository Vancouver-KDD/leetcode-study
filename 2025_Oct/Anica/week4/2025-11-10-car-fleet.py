class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort()
        stack = []

        for p, s in pair[::-1]:
            stack.append((target-p)/s)
            if len(stack) >= 2: 
                if stack[-1] <= stack[-2]:
                    stack.pop() 
        return len(stack)
