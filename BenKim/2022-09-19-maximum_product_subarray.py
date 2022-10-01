class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_so_far = min_so_far = result = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            
            # 음수와 음수가 곱해져서 최대값이 될 수 있기 때문에 현재까지의 최소값도 유지해나간다
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(max_so_far, result)
        return result