class Solution:
    def trap(self, height: List[int]) -> int:
        sum = 0
        left_max = height[0]
        right_max = height[-1]

        i = 1
        j = len(height) - 2
        while i <= j :
            if left_max < height[i]:
                left_max = height[i]
            
            if right_max < height[j]:
                right_max = height[j]

            if left_max <= right_max:
                sum += left_max - height[i]
                i += 1
            else:
                sum += right_max - height[j]
                j -= 1

        return sum
