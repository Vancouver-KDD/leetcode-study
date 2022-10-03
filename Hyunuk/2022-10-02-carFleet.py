class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(key=lambda x: x[0])
        stk = []
        for p, s in reversed(pair):
            curr = (target - p) / s
            stk.append((target-p) / s)
            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()
        return len(stk)
