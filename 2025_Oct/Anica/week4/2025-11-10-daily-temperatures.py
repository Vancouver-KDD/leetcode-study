class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures): 
            if not stack: 
                stack.append([temp, i])
            else: 
                while stack and stack[-1][0] < temp: 
                    lower_temp_index = stack.pop()[1]
                    res[lower_temp_index] = i - lower_temp_index 
                stack.append([temp, i])
        return res

            



