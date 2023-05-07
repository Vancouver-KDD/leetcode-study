class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # brute force
        # for i in range(0, len(nums)):
        #     duplicate = nums[i]

        #     for j in range(i+1, len(nums)):
        #         if nums[j] == duplicate:
        #             return True

        # return False

        # using Hashset
        # con = set()

        # for ele in nums:

        #     if ele in con:
        #         return True
        #     else :
        #         con.add(ele)

        # return False

        # using set(list)
        # con = set(nums)
        
        # if len(con) == len(nums):
        #     return False

        # else:
        #     return True

        # using sort , range len(newList) - 1 
        newList = sorted(nums)

        for i in range(0, len(newList) - 1):
            
            if newList[i] == newList[i+1]:
                return True

        return False
        

