class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        res = []
        for word in strs:
            temp = [0] * 26
            for char in word:
                temp[ord(char) - ord("a")] += 1
            if not hmap.get(tuple(temp), 0):
                    hmap[tuple(temp)] = []
            #Python does not allow to put list as a key since list is mutable.
            #Key should be immutable
            hmap[tuple(temp)].append(word)

        for words in hmap.values():
            res.append(words)
            
        return res