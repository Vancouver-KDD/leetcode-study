def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_value = 0
        current = 0

        for i in range(k):
            current += nums[i]
        
        max_value = current

        for i in range(k,len(nums)):
            current += nums[i] - nums[i-k]
            max_value = max(max_value,current)
        return max_value/k


def findMaxAverage(nums, k):
    max_avg = float('-inf')

    for i in range(len(nums) - k + 1):
        subarray = nums[i:i + k]
        avg = sum(subarray) / k
        max_avg = max(max_avg, avg)

    return max_avg