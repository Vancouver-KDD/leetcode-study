class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_dict = {}
        for text in strs:
            sorted_text = ''.join(sorted(text))
            if sorted_text in sorted_dict:
                sorted_dict[sorted_text].append(text)
            else:
                sorted_dict[sorted_text] = [text]
        return list(sorted_dict.values())
