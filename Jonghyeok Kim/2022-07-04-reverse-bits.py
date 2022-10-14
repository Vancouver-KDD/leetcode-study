class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            tmp = n >> i
            tmp = tmp << 31
            tmp = tmp >> i
            res = res ^ tmp
        return res
        #     bit = (n >>i) &1
        #     res |= (bit<<(31-i))
        # return res

        # counter, res = 31, 0
        # while n:
        #     if n % 2 == 1:
        #         res += 2**counter
        #     n = n >> 1
        #     counter -= 1
        # return res

if __name__ == "__main__":
    n = 43261596
    Solution.reverseBits(Solution, n)