class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False

        subset_sum = total_sum // k
        chosen = [False] * len(nums)
        nums.sort(reverse=True)

        def backtrack(index, count, curr_sum):
            if count == k - 1:
                return True

            if curr_sum > subset_sum:
                return False

            if curr_sum == subset_sum:
                return backtrack(0, count + 1, 0)

            for j in range(index, len(nums)):
                if not chosen[j]:
                    chosen[j] = True

                    if backtrack(j + 1, count, curr_sum + nums[j]):
                        return True
                    chosen[j] = False
            return False

        return backtrack(0, 0, 0)