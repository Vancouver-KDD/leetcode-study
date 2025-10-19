class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = defaultdict(list)
        for word in strs:
            sorted_list = sorted(word)
            word_map["".join(sorted_list)].append(word)

        return list(word_map.values()) 
            
     