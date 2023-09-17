class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #FIRST APPROACH - Time Limit Exceeded
        # if len(nums) == 3:
        #     return sum(nums)

        # nums1=[]

        # if len(nums) > 3:
        #     nums.sort()
        #     # print(nums)
        #     start =0
        #     for x in combinations(nums,3):
        #         testVal = (x[0]+x[1]+x[2])
        #         nums1.append(testVal)

        #         testVal0 = min(nums1, key=lambda x: abs(target - x ))         
                        
        
        # return testVal0
        
        if len(nums) == 3:
            return sum(nums)
        else:
            nums.sort()
            # set temp as max
            temp = 1000
            for x in range(len(nums)-2):
                val1 = x+1
                val2 = len(nums)-1

                while val1 < val2:
                    total = nums[val1] + nums[x] + nums[val2]
                    if total == target:
                        return total
                    if abs(target - total) < abs(target - temp):
                        temp = total
                    if target < total:
                        val2-=1
                    else:
                        val1+=1

        return temp