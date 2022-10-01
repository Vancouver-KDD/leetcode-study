class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # list as stack
        
        for index, curTemp in enumerate(temperatures):
            
            while len(stack) != 0 and stack[-1][0] < curTemp:
                t, i = stack.pop()
                res[i] = index - i    
            stack.append([curTemp, index])
        
        return res
        
            
    