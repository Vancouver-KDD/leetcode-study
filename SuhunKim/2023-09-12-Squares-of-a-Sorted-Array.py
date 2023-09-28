class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([pow(_,2) for _ in nums])