class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        li = []
        res = 0
        start1, start2, end1, end2 = 0, 0, 0, 0
        for idx,f in enumerate(fruits):
            if len(li) == 0:
                li.append(f)
                start1, end1 = idx, idx
            elif len(li) == 1 and f not in li:
                li.append(f)
                start2, end2 = idx, idx
            elif len(li) == 1 and f in li:
                end1 = idx
            elif len(li) == 2 and f == li[0]:
                end1 = idx
            elif len(li) == 2 and f == li[1]:
                end2 = idx
            else:
                lnth = max(end1-start1, end2-start1, end1-start2, end2-start2) + 1
                res = max(res, lnth)
                if fruits[idx-1] == li[0]:
                    start1, end1 = end2+1, idx-1
                    start2, end2 = idx, idx
                    li.pop(1)
                    li.append(f)
                else:
                    if end1 > start2:
                        start1, end1 = end1+1, idx-1
                        start2, end2 = idx, idx
                        li.pop(0)
                        li.append(f)
                    else:
                        start1 = start2
                        end1 = end2
                        start2, end2 = idx, idx
                        li.pop(0)
                        li.append(f)
                    
        lnth = max(end1-start1, end2-start1, end1-start2, end2-start2) + 1
        return max(res, lnth)