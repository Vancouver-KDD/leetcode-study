class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # 초기값은 배열의 첫번째 값으로 설정한다. 
        # 최대값이 음수가 될수도 있기 때문에 0으로 설정하지 않는다 
        maxSum = nums[0]
        currSum = 0

        for num in nums:

            # 현재까지의 합이 음수라면 앞의 합들은 버리고 새로 최대값을 구해나간다
            if currSum < 0:
                currSum = 0
            currSum += num
            if currSum >= maxSum:
                maxSum = currSum
        return maxSum