from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # ans_cnt: count of each character in s1
        ans_cnt = Counter(s1)
        # ans_set: unique characters in s1 (for quick check)
        ans_set = set(s1)
        # curr_cnt: count of characters in the current window of s2
        curr_cnt = defaultdict(int)
        # left: start position of the window
        left = 0

        # Move 'right' from the start to the end of s2
        for right in range(len(s2)):
            # If the current character is part of s1
            if s2[right] in ans_set:
                curr_cnt[s2[right]] += 1

                # If we have too many of this character,
                # move the left pointer to reduce the count
                while curr_cnt[s2[right]] > ans_cnt[s2[right]]:
                    curr_cnt[s2[left]] -= 1
                    left += 1

                # If the counts match, we found a permutation
                if ans_cnt == curr_cnt:
                    return True
            else:
                # If the character is not in s1,
                # reset the current window
                curr_cnt = defaultdict(int)
                left = right + 1

        # No permutation found
        return False