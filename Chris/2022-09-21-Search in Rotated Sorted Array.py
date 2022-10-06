class Solution:
    def search(self, nums: List[int], target: int) -> int:  
        l = 0
        r = len(nums)-1


        while(l<=r):
            mid = (l+r)//2
            midVal = nums[mid]
            leftVal = nums[l]
            rightVal = nums[r]

            if(midVal == target):
                return mid

            #the scope we are looking is fully sorted
            if(leftVal < rightVal):
                if(target > midVal):
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                #the scope we are looking is partially sorted
                #7,0,1,2      
                if(target > midVal):
                    if(target > leftVal):
                        l = mid + 1
                    else:
                        r = mid - 1
                else: # target < midVal
                    if(target >= leftVal):
                        r = mid - 1
                    else:
                        l = mid + 1



        return -1