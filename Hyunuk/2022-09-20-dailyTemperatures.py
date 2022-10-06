class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        ret = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                pos = stk.pop()
                ret[pos] = i - pos
            stk.append(i)
        return ret
