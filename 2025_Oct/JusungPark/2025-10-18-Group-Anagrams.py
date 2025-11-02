class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        for s in strs:
            char = [0]*26
            for ch in s:
                char[ord(ch) - ord('a')] += 1
            key = tuple(char)
            if key in ana:
                ana[key].append(s)
            else: ana[key] = [s]
            
        result = []
        for key, value in ana.items():
            result.append(value)