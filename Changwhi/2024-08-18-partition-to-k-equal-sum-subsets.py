class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k:
            return False

        reqSum = total // k
        subSets = [0] * k
        nums.sort(reverse = True)

        def recurse(i):
            if i == len(nums):    
                return True

            for j in range(k):
                if subSets[j] + nums[i] <= reqSum:
                    subSets[j] += nums[i]

                    if recurse(i + 1):
                        return True

                    subSets[j] -= nums[i]

                    # Important line, otherwise function will give TLE
                    if subSets[j] == 0:
                        break

                    """
                    Explanation:
                    If subSets[j] = 0, it means this is the first time adding values to that subset.
                    If the backtrack search fails when adding the values to subSets[j] and subSets[j] remains 0, it will also fail for all subSets from  
                    subSets[j+1:].
                    Because we are simply going through the previous recursive tree again for a different j+1 position.
                    So we can effectively break from the for loop or directly return False.
                    """

            return False

        return recurse(0)