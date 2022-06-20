class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMaxProduct = 1
        currMinProduct = 1

        msf = max(nums)

        for i in nums:
            temp = i * currMaxProduct
            currMaxProduct = max(currMaxProduct * i, currMinProduct * i, i)
            currMinProduct = min(temp, currMinProduct * i, i)
            msf = max(msf, currMaxProduct)
        return msf
