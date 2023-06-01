class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        hashset = {0: []}
        for i in nums:
            if i in hashset[0]:
                hashset[0].remove(i)
            else:
                hashset[0].append(i)
        return hashset[0][0]


s = Solution()
lst1 = [2, 2, 1]
lst2 = [4, 1, 2, 1, 2]
lst3 = [1]
print(s.singleNumber(lst1))
print(s.singleNumber(lst2))
print(s.singleNumber(lst3))

# Input: nums = [2,2,1]
# Output: 1

# Input: nums = [4,1,2,1,2]
# Output: 4

# Input: nums = [1]
# Output: 1
