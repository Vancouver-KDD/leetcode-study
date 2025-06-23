class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)  # Get the number of days
        answer = [0] * n  # Initialize the result array with 0s
        stack = []  # Stack to keep indices of days

        for i in range(n):  # Iterate through each day
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # Compare current temp with the top of the stack
                prev_day = stack.pop()
                # Pop until current temperature is not greater than stack top
                answer[prev_day] = i - prev_day
                # Store the number of days waited
            stack.append(i)
            # Push current day index to stack for future comparison

        return answer  # Return the final result array
