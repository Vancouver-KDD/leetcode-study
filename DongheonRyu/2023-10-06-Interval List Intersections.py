def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i, j = 0, 0
    
        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]
        
            if start1 > end2:
                j += 1
            elif start2 > end1:
                i += 1
            else:
                result.append([max(start1, start2), min(end1, end2)])
                if end1 < end2:
                    i += 1
                else:
                    j += 1
    
        return result