class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = defaultdict(int)
        freq_max = 0
        left = 0
        max_len = 0
        for right in range(len(s)):
            count[s[right]] += 1
            freq_max = max(freq_max, count[s[right]])

            window_size = right - left + 1
            if window_size - freq_max > k:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
