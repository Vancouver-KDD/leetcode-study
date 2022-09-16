# 🥲 time out solution 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # 현재 요소 이후로 배열을 슬라이싱 한 후, 요소가 있는지 확인한다
        for i, num in enumerate(nums):
            if num in nums[i+1:]:
                return True
        return False