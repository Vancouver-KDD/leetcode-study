class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        anagram_collection = {}
        for word in strs:
            key = str(sorted(word))
            
            if key not in anagram_collection:
                anagram_collection[key] = []
                
            anagram_collection[key].append(word)
        
        for key, item in anagram_collection.items():
            ans.append(item)

        return ans
