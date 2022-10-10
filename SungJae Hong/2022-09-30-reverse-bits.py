class Solution:
    def reverseBits(self, n: int) -> int:
        # put the bits into a list
        rep = list("{:032b}".format(n))
        # reverse the list
        rep.reverse()
        dec_number = 0
        for digit in rep:
            # converting the bits to decimals here.
            dec_number = dec_number*2 + int(digit)
        return dec_number

class Solution2:
    def reverseBits(self, n: int) -> int:
        output = 0
        power = 31
        while n != 0:
            output += (n&1) << power
            n = n >> 1
            power -= 1
        return output