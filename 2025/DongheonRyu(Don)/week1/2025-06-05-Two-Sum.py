def twoSum(self, nums: List[int], target: int) -> List[int]:
        
    # o(n^2)
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if(j != i and nums[i]+nums[j] == target):
                return [i,j]

    return                 

            
    # o(n)
def two_sum2(nums, target):
    num_map = {}

    for i in range(len(nums)):
        
        complement = target - nums[i]

        if complement in num_map:
            return [num_map[complement], i]

        num_map[nums[i]] = i

    return 