def dailyTemperatures(T: List[int]) -> List[int]:
    n = len(T)
    ans = [0] * n
    stack = []  
    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            prev = stack.pop()
            ans[prev] = i - prev
        stack.append(i)
    return ans
