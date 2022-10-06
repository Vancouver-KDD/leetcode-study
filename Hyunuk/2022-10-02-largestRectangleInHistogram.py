class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ret = 0
        stk = []
        for i, v in enumerate(heights):
            start = i
            while stk and stk[-1][1] > v:
                idx, h = stk.pop()
                ret = max(ret, h * (i - idx))
                start = idx
            stk.append((start, v))
        for i, v in stk:
            ret = max(ret, v * (len(heights) - i))
        return ret
