
def eraseOverlap(intervals):
    intervals.sort()

    res = 0
    prevEnd = intervals[0][1]
    
    for start,end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            res +=1
            prevEnd = min(end,prevEnd)
    return res

print(eraseOverlap([[1,2],[2,3],[1,3]]))