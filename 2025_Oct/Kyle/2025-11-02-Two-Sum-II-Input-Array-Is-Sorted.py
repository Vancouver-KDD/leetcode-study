
# Not using sorted array
class AlternativeSolution(object):
    def twoSum(self, numbers, target):
        hash_map = {}

        for index, value in enumerate(numbers):
             hash_map[value] = index + 1

        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in hash_map:
                return [i + 1, hash_map[complement]]

# Using sorted array
class Solution(object):
    def twoSum(self, numbers, target):
        low = 0
        high = len(numbers) - 1
        while low < high:
            sum = numbers[low] + numbers[high]

            if sum == target:
                return [low + 1, high + 1]
            elif sum < target:
                low += 1
            else:
                high -= 1
        # In case there is no solution, return [-1, -1].
        return [-1, -1]