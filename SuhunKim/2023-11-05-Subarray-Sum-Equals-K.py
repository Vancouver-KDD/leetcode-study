class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_count = {0: 1}
        cumulative_sum = 0
        count = 0

        for num in nums:
            cumulative_sum += num

            if cumulative_sum - k in sum_count:
                count += sum_count[cumulative_sum - k]

            sum_count[cumulative_sum] = sum_count.get(cumulative_sum, 0) + 1

        return count