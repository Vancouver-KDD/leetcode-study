"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution:
    # Hash set
    # Time complexity: O(n^2): outer loop(n) and inner loop (n) = n^2
    # Space complexity: O(n): extra space for a hash set
    def threeSum(self, nums: list[int]):
        # Use set to avoid duplicates
        triplets = set()

        # iterate through to len(nums) - 3 element to avoid index out bound error
        # [1, 2, 3, 4, 5] from 1 to 3 only so that 3 can have 4, 5
        for i in range(len(nums) - 2):
            seen = set()
            for j in range(i + 1, len(nums)):
                complement = 0 - nums[i] - nums[j]  # n1 + n2 + n3 = 0
                # Check if the complement of the current value is in the set
                if complement in seen:
                    triplet = tuple(sorted([nums[i], nums[j], complement]))
                    triplets.add(triplet)
                else:
                    seen.add(nums[j])

        return list(triplets)

    # Two pointers
    # Time complexity: O(n^2): outer loop(n) and inner loop (n) = n^2
    # Space complexity: O(n): to store triplets in the worst case
    def threeSumTwoPointer(self, nums: list[int]):
        nums.sort()

        triplets = set()

        for i in range(len(nums) - 2):
            # Check for duplicates and skip if found
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                # Initialize left and right pointers
            l, r = i + 1, len(nums) - 1

            # iterate through sub-list
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    # append the triplet to the set
                    triplet = tuple(sorted([nums[i], nums[l], nums[r]]))
                    triplets.add(triplet)

                    # move the left pointer to the next unique element
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    # move both pointers
                    l += 1
                    r -= 1
                # If the current triplet does not sum to 0, move the pointers accordingly
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return list(triplets)


def main():
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))
    print(s.threeSumTwoPointer([-1,0,1,2,-1,-4]))

    print(s.threeSum([0,1,1]))
    print(s.threeSumTwoPointer([0,1,1]))

    print(s.threeSum([0,0,0]))
    print(s.threeSumTwoPointer([0,0,0]))


if __name__ == "__main__":
    main()
