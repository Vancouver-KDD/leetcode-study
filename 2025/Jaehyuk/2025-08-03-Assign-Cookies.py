class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        p1 = 0
        p2 = 0
        output = 0
        g = sorted(g)
        s = sorted(s)
        while len(g) > p1 and len(s) > p2:
            if s[p2] >= g[p1]:
                p1 += 1
                output += 1
            p2 += 1
        
        return output