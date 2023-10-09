class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        if not firstList or not secondList: return res
        
        intervalFromFirst, intervalFromSecond = firstList.pop(0), secondList.pop(0);

        while True:
            popFirst, popSecond = False, False
            if intervalFromFirst[0] <= intervalFromSecond[0] and intervalFromFirst[1] >= intervalFromSecond[1]:
                res.append(intervalFromSecond)
                popSecond = True
            elif intervalFromFirst[0] >= intervalFromSecond[0] and intervalFromFirst[1] <= intervalFromSecond[1]:
                res.append(intervalFromFirst)
                popFirst = True
            elif intervalFromFirst[0] <= intervalFromSecond[0] and intervalFromFirst[1] >= intervalFromSecond[0]:
                res.append([intervalFromSecond[0], intervalFromFirst[1]])
                popFirst = True
            elif intervalFromFirst[1] >= intervalFromSecond[0] and intervalFromFirst[0] <= intervalFromSecond[1]:
                res.append([intervalFromFirst[0], intervalFromSecond[1]])
                popSecond = True
            else:
                if intervalFromFirst[1] > intervalFromSecond[1]:
                    popSecond = True
                elif intervalFromFirst[1] < intervalFromSecond[1]:
                    popFirst = True
            
            if firstList and popFirst:
                intervalFromFirst = firstList.pop(0)
            elif secondList and popSecond:
                intervalFromSecond = secondList.pop(0)
            else:
                break

        return res