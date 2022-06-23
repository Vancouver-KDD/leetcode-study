from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        offset = 1
        for i in range(1, n+ 1):
            if i == offset * 2:
                offset *= 2
            one_num = 1 + res[i-offset]
            res.append(one_num)
        return res