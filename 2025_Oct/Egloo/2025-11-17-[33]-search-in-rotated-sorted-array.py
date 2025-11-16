"""
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""
"""
s , e, m 

구간이 정렬 되어 있고, 값이 그 안에 있으면 거기서 binary search 
만약 정렬된 구간에 포함이 안되어 있으면 다른쪽 시도 

질문1. binary search 와 값이 정렬 된 구간에 포함되어 있는지 
확인하는 코드는 같이 쓰이는 가? 아니면 구 간에 없으면 
"""
class Solution(object):
    def search(self, nums, target):

        return 0
    def binarySearch(self, nums, i, j, target):

        while i <= j:
            m = (i+j)//2

            if nums[m] == target:
                return 



if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0

    s = Solution()
    r = s.search(nums, target)
    print(r)
