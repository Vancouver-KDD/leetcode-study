class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [];
        for i in range(n+1):
            count = 0
            number = i;
            while (number != 0):
                if number % 2 == 1:
                    count +=1;
                number = number // 2
            ans.append(count)
        return ans
         
