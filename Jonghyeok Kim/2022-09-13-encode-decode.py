class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, strs:str) -> List[str]:
        res, i = [], 0

        while i < len(strs):
            j = i
            while strs[j] != "#":
                j += 1
            length = int(strs[i:j])
            res.append(strs[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res