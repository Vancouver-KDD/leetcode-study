class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        total = 0
        res = float('inf') 
        # 최소값을 구할때 result 값을 float('inf') - 가장 큰 숫자로 저장해줘야 하는 이유 : 나중에 res = min(res, r-l+1)로 최솟값을 구할건데, 0이거나 다른 숫자면 그 숫자가 가장 작은 숫자로 계속해서 나올 수 있음...
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)  # 최소 길이 갱신
                total -= nums[l]  # 왼쪽 포인터 값을 합에서 빼고
                l += 1  # 왼쪽 포인터 이동
        
         # 최소 길이가 갱신되지 않았으면 0을 반환
        return res if res != float('inf') else 0
