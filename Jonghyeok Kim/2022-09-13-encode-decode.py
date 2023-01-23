from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res = f"{res}{len(st)}#{st}"
        return res

    def decode(self, strs):
        # write your code here
        start, end, res = 0, 0, []
        while start < len(strs):
            while strs[end] != "#":
                end += 1
            str_len = int(strs[start:end])
            res.append(strs[end+1:end+1+str_len])
            start, end = end+1+str_len, end+1+str_len
        return res

    # def decode(self, strs:str) -> List[str]:
    #     res, i = [], 0

    #     while i < len(strs):
    #         j = i
    #         while strs[j] != "#":
    #             j += 1
    #         length = int(strs[i:j])
    #         res.append(strs[j + 1 : j + 1 + length])
    #         i = j + 1 + length
    #     return res
    
input_list = ["lint","code","love","you"]
encoded = Solution.encode(Solution, input_list)
decoded = Solution.decode(Solution, encoded)
