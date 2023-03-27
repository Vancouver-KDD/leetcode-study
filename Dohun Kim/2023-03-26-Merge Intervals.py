class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]
        for start, end in intervals:
            if start <= output[-1][1]:
                # merge
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start, end])
        return output