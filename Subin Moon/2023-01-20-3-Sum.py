# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 3:
            if sum(nums) != 0:
                return []
            else:
                return [nums]

        if len(nums) < 3:
            return []

        res = set()

        # 1. Split nums into three lists: negative num, positive num, zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        # 2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        # 3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        if z:
            for num in P:
                if -1 * num in N:
                    res.add((-1 * num, 0, num))

            # If there is at least 3 zeros in the list then also include (0, 0, 0)
            if len(z) >= 3:
                res.add((0, 0, 0))

        # 4. For all pairs of negative nums (-3, -1), check to see if their complement (4) exists in the pos num set
        from itertools import combinations
        for x, y in combinations(n, 2):
            target = -1 * (x + y)
            if target in P:
                res.add(tuple(sorted([x, y, target])))

        # 5. For all pairs of positive numbers (1, 1), check to see if their complement (-2) exists in the neg num set
        for x, y, in combinations(p, 2):
            target = -1 * (x + y)
            if target in N:
                res.add(tuple(sorted([x, y, target])))

        return [list(x) for x in res]

    def threeSum_pointers(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1

                else:
                    # sum = 0
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return results
