class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        new_digits = int(''.join(str(e) for e in digits)) + 1
        res = [int(x) for x in str(new_digits)]
        return res


s = Solution()
lst1 = [1, 2, 3]  # return [1, 2, 4]
lst2 = [4, 3, 2, 1]  # return [4, 3, 2, 2]
lst3 = [9]  # return [1, 0]
lst4 = [1, 2, 3, 9]  # return [1, 2, 4, 0]
print(s.plusOne(lst1))
print(s.plusOne(lst2))
print(s.plusOne(lst3))
print(s.plusOne(lst4))
