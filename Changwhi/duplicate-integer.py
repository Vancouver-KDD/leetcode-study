class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         numbers = []
         for num in nums:
            if num in numbers:
                return True
            else:
                numbers.append(num)
         return False