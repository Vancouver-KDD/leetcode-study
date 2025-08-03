class Solution:
    def findContentChildren(self, g, s):
        # Time: O(n + m)
        # Time (including sorting): O(n log n + m log m)
        # Space for auxiliary: O(1)
        # Space (including sorting + worst case): O(n + m)
        
        g.sort()
        s.sort()
        
        i=j=0
        
        while i<len(g):
            while j<len(s) and g[i]>s[j]:
                j+=1
            if j < len(s):
                i += 1
                j += 1
            else:
                break
        return i
                
                
solution = Solution()
print(solution.findContentChildren([1, 2, 3], s=[1, 1]))
print(solution.findContentChildren([1, 2], s=[1, 2, 3]))
