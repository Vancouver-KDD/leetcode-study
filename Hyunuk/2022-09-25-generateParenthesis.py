class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(arr, l, r):
            if len(arr) == n*2:
                ret.append(''.join(arr))
                return
            if l < n:
                arr.append("(")
                helper(arr, l+1, r)
                arr.pop()
            if r < l:
                arr.append(")")
                helper(arr, l, r+1)
                arr.pop()
            
        ret = []
        helper([], 0, 0)
        return ret
