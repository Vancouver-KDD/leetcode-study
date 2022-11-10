class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # unique character set of substring
        char_set = set()
        left, right = 0, 0
        result = 0
        
        while right < len(s):
            # if current element is not in set, add it
            if s[right] not in char_set:
                char_set.add(s[right])
                right += 1
                # update result
                result = max(result, len(char_set))
            else:
                # remove left element from set
                char_set.remove(s[left])
                left += 1

        return result

