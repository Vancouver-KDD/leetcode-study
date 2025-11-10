class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indices_stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while len(indices_stack) != 0:
                latest = indices_stack.pop() # 6
                if temperatures[latest] < temp:
                    res[latest] = i - latest
                else:
                    indices_stack.append(latest)
                    break
            indices_stack.append(i)

        return res