# brute force
def sortedSquares(self, nums):
        nArr = []
        for i in nums:
           nArr.append(i * i)

        return sorted(nArr)  


def sortedSquares2(nums):
      nArr = []
      l,r = 0, len(nums)-1

      while l<=r:
            if nums[l] * nums[l] >  nums[r] * nums[r]:
                  nArr.append(nums[l] * nums[l])
                  l += 1
            else:
                  nArr.append(nums[r]*nums[r])
                  r -= 1
        
      return nArr[::-1]               

print(sortedSquares2([-4,-1,0,3,10]))