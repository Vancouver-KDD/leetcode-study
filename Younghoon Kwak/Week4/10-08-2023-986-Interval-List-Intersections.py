class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n1, n2 = len(firstList), len(secondList)
        if n1==0 or n2==0:
            return []
        e1, e2 = firstList[0], secondList[0]
        startPoint = e1[0]
        if e1[0]<e2[0]:
            startPoint = e2[0]
        endPoint = e1[1]
        if e1[1]>e2[1]:
            endPoint = e2[1]      
        if n2>1 and e1[1]>= secondList[1][0]:
            secondList.pop(0)
        elif n1>1 and e2[1]>= firstList[1][0]:
            firstList.pop(0)
        else:
            if n1>=1:
                firstList.pop(0)
            if n2>=1:
                secondList.pop(0)
        if startPoint <= endPoint:
            output = [[startPoint, endPoint]]
            output.extend(self.intervalIntersection(firstList, secondList))
            return output
        return self.intervalIntersection(firstList, secondList)