class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]  
        :rtype: int
        """

        i, j = 0, len(nums)-1
        sv = nums[0]

        while i <= j:
            m = (i+j) // 2

            if nums[i] <= nums[m]:
                print("A", i, m, j)
                sv = min(sv, nums[i])
                i = m+1
            else:
                print("B", i, m, j)
                sv = min(sv, nums[m+1])
                j = m
        print("answer:", sv)
        return sv


if __name__ == "__main__":
    a = [3,4,5,1,2]
    b = [4,5,6,7,0,1,2]
    c = [11,13,15,17]
    d = [8,9,0,1,2,3,4,5,6,7]

    s = Solution()
    ch = True
    if ch:
        assert s.findMin(a) == 1
        assert s.findMin(b) == 0
        assert s.findMin(c) == 11
        assert s.findMin(d) == 0
        assert s.findMin([1]) == 1
        assert s.findMin([1,2,3]) == 1
        assert s.findMin([2,1]) == 1
    assert s.findMin([3,1,2]) == 1