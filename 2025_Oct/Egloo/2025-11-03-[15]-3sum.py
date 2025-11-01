class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        resultSet = set()
        resultList = list()

        for k in range(len(nums)-2):
            i, j = k+1, len(nums)-1

            while i < j:
                tSum = nums[k] + nums[i] + nums[j]
                if tSum == 0:
                    tSet = (nums[k], nums[i], nums[j])
                    if not tSet in resultSet:
                        resultSet.add(tSet)
                        resultList.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                elif tSum < 0:
                    i += 1
                elif tSum > 0:
                    j -= 1

        return resultList

                    
        