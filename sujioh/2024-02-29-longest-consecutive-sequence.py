class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if (num - 1) not in num_set:
                current_streak = 1
                while (num + current_streak) in num_set:
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
