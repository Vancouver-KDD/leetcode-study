class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anag_dict = {}
        for string in strs:

            count = [0] * 26
            for s in string:
                count[ord(s) - ord('a')] += 1

            tuple_count = tuple(count)
            if tuple_count not in anag_dict:
                anag_dict[tuple_count] = [string]

            else:
                anag_dict[tuple_count].append(string)

        
        return list(anag_dict.values())







        
        
        