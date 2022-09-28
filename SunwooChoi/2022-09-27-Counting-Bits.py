class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n + 1):
            # i-1 number of left most bits contains same number of 1's with i // 2
            # i & 1 checks that the omitted bit is 1 or 0
            ans.append(ans[i >> 1] + (i & 1))
        return ans
