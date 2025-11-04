class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0 
        end = len(heights)-1
        max_area = 0 

        while start < end: 
            area = (end-start)*min(heights[start], heights[end])
            max_area = max(area, max_area)

            if heights[start] < heights[end]:
                start+=1 
            else: 
                end-=1
        return max_area