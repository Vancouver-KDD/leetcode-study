class Solution:
    def sortedSquares(self, nums):
        # Approach 1: square then sort
        results = []
        for i in nums:
            x = i * i 
            results.append(x)
        results.sort()
        return results
        # O(n)

        # Approach 2: two pointer
        # res = []
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     if abs(nums[l]) >= abs(nums[r]):
        #         res.append(nums[l] * nums[l])
        #         l += 1
        #     else:
        #         res.append(nums[r] * nums[r])
        #         r -= 1
        # return reversed(res)

        # O(n * logn)
    

                        

    