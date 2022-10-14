class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binary_search(stack, i):
            l = 0
            r = len(stack) - 1
            while l < r:
                mid = (l + r) // 2
                if stack[mid] == i:
                    return mid
                elif stack[mid] < i:
                    l = mid + 1
                else:
                    r = mid
            return l
                
        stack = [nums[0]]
        for i in nums:
            if stack[-1] < i:
                stack.append(i)
            else:
                place = binary_search(stack, i)
                stack[place] = i
                
        return len(stack)
