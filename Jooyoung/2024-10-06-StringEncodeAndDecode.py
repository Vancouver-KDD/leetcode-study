from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        es = ""

        for s in strs:
            es += f"{len(s)}#{s}"

        return es


    def decode(self, s: str) -> List[str]:
        ds = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1
            ds.append(s[i:i+length])
            i += length

        return ds

solution = Solution()
encoded = solution.encode(["neet", "code", "love", "you"])
print("Encoded: ", encoded)

decoded = solution.decode(encoded)
print("Decoded: ", decoded)
