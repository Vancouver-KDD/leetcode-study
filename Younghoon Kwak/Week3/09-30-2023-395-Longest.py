class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        char_dict = {}
        for ss in s: 
            if ss in char_dict.keys():
                count = char_dict[ss]  
                char_dict[ss] = count + 1
            else:
                char_dict[ss] = 1
                
        print(char_dict)

        sum = 0
        for s in char_dict.keys():
            if char_dict[s] >= k:
                sum = sum + char_dict[s]

        return sum