class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # We'll use a stack to keep track of days (indexes) that we haven't found a warmer day for yet.
        stack = []

        # This list will store how many days we need to wait for a warmer temperature.
        # Initialize all with 0 because some days might not have any warmer days.
        answer = [0] * len(temperatures)

        # Go through each day in the temperature list
        for i in range(len(temperatures)):

            # While the current day's temperature is higher than
            # the temperature of the last day stored in the stack:
            # it means we have found a warmer day for that previous day.
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # Take that day (index) out from the stack
                j = stack.pop()
                # Calculate how many days we waited for a warmer day
                answer[j] = i - j

            # Add the current day (index) to the stack,
            # because we haven't found a warmer day for it yet.
            stack.append(i)

        # Return the final list showing how many days to wait for each day.
        return answer