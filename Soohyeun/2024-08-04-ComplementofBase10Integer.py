class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        curr = n
        mask = 1

        while curr:
            n = n ^ mask
            mask = mask << 1
            curr = curr >> 1

        return n