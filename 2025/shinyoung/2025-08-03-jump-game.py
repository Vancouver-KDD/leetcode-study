class Solution:
    def canJump(self, nums):
        # Greedy: start at end
        # Time: O(n)
        # Space: O(1)
        
        n=len(nums)
        target=n-1
        
        for i in range(n-1, -1, -1):
            max_jump=nums[i]
            
            if i+max_jump>=target:
                target=i
        return target == 0
    

solution = Solution()
print(solution.canJump([2, 3, 1, 1, 4]))
print(solution.canJump([3, 2, 1, 0, 4]))
            
        
