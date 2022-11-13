class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        
        for i in strs:
            num = 0
            for j in i:
                num += 26**(ord(j) - 97)
            if num in dic:
                dic[num].append(i)
            else:
                dic[num] = [i]
        
        res = []
        
        for v in dic.values():
            res.append(v)
        
        return res