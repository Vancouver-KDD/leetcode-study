class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # """"
        # [2,3,4] -> 234 + 1  -> [2, 3 ,5]

        # [1,0,9] -> 109 + 1 -> [1, 1, 0]
        
        # """"
        # res = 0 
        # loops thr the digits (List)
        # res = res + ele
        # res = res*10
        # ele = res % 10
        # List.append(ele)
        # res = res /10
        # return List[::-1]


        res = 0

        for ele in digits:
            res *= 10
            res = res + ele

        res += 1

        print(res)

        ans = []

        while res :
            ele = res % 10
            ans.append(ele)

            res = res // 10


        return ans[::-1]

        