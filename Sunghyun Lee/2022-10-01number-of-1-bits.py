class Solution:
    def hammingWeight(self, n: int) -> int:
        number = n;
        count = 0;
        while (number != 0):
            if(number %2 == 1):
                count +=1;
            number = number >> 1
            
        return count
