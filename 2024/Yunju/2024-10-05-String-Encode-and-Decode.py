#String Encode and Decode
#https://neetcode.io/problems/string-encode-and-decode
#해답 참고

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: 
            res += str(len(s))+"#" + s
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        i=0

        while i<len(s):
            j=i
            while s[j] != '#': # s[j]가 '#'이 아닐때까지 반복
                j+= 1
            length = int(s[i:j]) #첫번째 루프에서 length는 s[0:1] == 첫번째로 쓴 str(len(s)) 이 값..
            i = j + 1
            j = i + length
            res.append(s[i:j]) #이 때 추가됨.
            i=j

        return res



solution = Solution()

strs = ["hello", "world", "py#thon"]

encoded_str = solution.encode(strs)
print("Encoded:", encoded_str)

decoded_strs = solution.decode(encoded_str)
print("Decoded:", decoded_strs)