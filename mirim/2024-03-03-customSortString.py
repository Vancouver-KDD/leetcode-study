# https://leetcode.com/problems/custom-sort-string/description/


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashMap = {}
        result = ""

        for char in s:
            hashMap[char] = hashMap.get(char, 0) + 1

        for o in order:
            if o in hashMap and hashMap[o] > 0:
                result += o * hashMap[o]

        for key, value in hashMap.items():
            if value > 0 and key not in result:
                result += key * value

        return result
