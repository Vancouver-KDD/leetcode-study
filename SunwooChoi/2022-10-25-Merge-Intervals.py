class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # check list is not empty
        if not intervals:
            return []
        
        # sort by first element of inner list
        intervals.sort(key=lambda el: el[0])
        
        ans = []
        
        for interval in intervals:
            # no more merable
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                # update last element's max value
                if interval[1] >= ans[-1][1]:
                    ans[-1][1] = interval[1]
        
        return ans

