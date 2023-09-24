class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newArray =[]
        for x in nums:
            newArray.append(x**2)
        newArray.sort()

        return newArray
            
        