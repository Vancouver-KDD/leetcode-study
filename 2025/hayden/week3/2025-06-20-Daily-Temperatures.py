class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)

        return result
