class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = {}
        L = 0
        cur_sum = 0
        max_sum = 0

        for R in range(len(nums)):
            # Add the current element to the window
            if nums[R] in window:
                window[nums[R]] += 1
            else:
                window[nums[R]] = 1
            cur_sum += nums[R]

            # If the window size exceeds k, slide the window
            if R - L + 1 > k:
                window[nums[L]] -= 1
                cur_sum -= nums[L]
                if window[nums[L]] == 0:
                    del window[nums[L]]
                L += 1

            # Ensure we only consider sums of windows with exactly k unique elements
            if R - L + 1 == k and len(window) == k:
                max_sum = max(max_sum, cur_sum)

        return max_sum

