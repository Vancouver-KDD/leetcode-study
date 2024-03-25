# https://leetcode.com/problems/partition-labels/


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}

        for i, c in enumerate(s):
            lastIdx[c] = i

        rs = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIdx[c])

            if i == end:
                rs.append(size)
                size = 0
        return rs
