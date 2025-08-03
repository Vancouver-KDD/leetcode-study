class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort()
        content = 0
        for child in g:
            if not s or g[-1] > s[-1]:
                return content
            if child <= s[-1]:
                s.pop()
                content += 1
        return content