class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            temp = numbers[left] + numbers[right]

            if temp == target:
                return [left + 1, right + 1]
            elif temp < target:
                left += 1
            else:
                right -= 1
        return False