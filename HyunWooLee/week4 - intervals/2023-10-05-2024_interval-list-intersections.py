class Solution:
    '''
    runtime: O(n)
    space; O(n)
    '''
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []

        first_index, second_index = 0, 0

        first_len, second_len = len(firstList), len(secondList)

        while first_index < first_len and second_index < second_len:
            first_interval = firstList[first_index]
            second_interval = secondList[second_index]

            first_start, first_end = first_interval[0], first_interval[1]
            second_start, second_end = second_interval[0], second_interval[1]

            left = max(first_start, second_start)
            right = min(first_end, second_end)

            if left <= right:
                result.append([left, right])

            if first_end <= second_end:
                first_index += 1
            else:
                second_index += 1

        return result