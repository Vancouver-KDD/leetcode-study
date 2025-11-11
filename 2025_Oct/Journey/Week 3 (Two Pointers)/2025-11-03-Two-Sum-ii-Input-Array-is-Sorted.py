class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Use two pointers:
        # 'l' starts from the beginning, 'r' starts from the end
        l = 0
        r = len(numbers) - 1

        # Keep checking until the two pointers meet
        while l < r:
            # Calculate the sum of the two numbers
            total = numbers[l] + numbers[r]

            # If the sum equals the target, return the 1-based indices
            if total == target:
                return [l + 1, r + 1]

            # If the sum is smaller than the target,
            # move the left pointer right to increase the sum
            elif total < target:
                l += 1

            # If the sum is greater than the target,
            # move the right pointer left to decrease the sum
            else:
                r -= 1