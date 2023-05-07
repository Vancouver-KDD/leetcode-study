# hash map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        num_dict = {}

        for i, num in enumerate(nums): # 1
            if target - num in num_dict:
                return [i, num_dict[target - num]]
            num_dict[num] = i      

# 1. enumerate() funciton creates a tuple(index, value)
# ex) enumerate(['a', 'b', 'c']) -> (0, 'a'), (1, 'b'), (2, 'c')

# two pointer
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums = enumerate(nums) # 1

        
        
        nums = sorted(nums, key=lambda x: x[1]) # 2

        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left][1] + nums[right][1] < target:
                left += 1
            elif nums[left][1] + nums[right][1] > target:
                right -= 1
            else:
                return [nums[left][0], nums[right][0]]

# 1. Since we need to return the index, keep the (index, values) as tuples
# 2. - Values must be sorted, to use a two-pointer
#    - Sort by value
#    - Python's sort() uses Timsort, which is O(n logn)