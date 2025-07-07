class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        counts = [0 for _ in range(len(temperatures))]
        stack = []
        for date, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                counts[stack[-1]] = date - stack[-1]
                stack.pop()
            stack.append(date)
        return counts