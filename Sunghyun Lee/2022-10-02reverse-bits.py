class Solution:
    def reverseBits(self, n: int) -> int:
        number = n;
        binary = "";
        for i in range(32):
            binary += str((number %2))
            number = number // 2
            
        return int(binary, 2)
