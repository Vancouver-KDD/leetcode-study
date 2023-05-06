# For more description, please visit the blog below.
# https://peterdrinker.tistory.com/479

class Solution:

    """
    Search the target value from the given list using binary search algorithm.

    :param nums: the given list
    :param target: the value to find from the list
    """
    def search(self, nums: list[int], target: int) -> int:
        # Error handling part
        # Length of list check
        length_nums = len(nums)
        if not 1 <= length_nums <= 10**4:
            raise ValueError("Invalid length of list")
        # Element, target boundary check
        for element in nums:
            if not -10**4 < element < 10**4:
                raise ValueError("Out of bound")
        if not -10**4 < target < 10**4:
            raise ValueError("Out of bound")

        start_index = 0
        end_index = length_nums - 1
        middle_index = length_nums // 2
        return self.binary_search_helper(nums, start_index, end_index, target)
    
    # Implement binary search tree helper function which is divide and conquer method
    # Finding the middle index and compare the value with the target
    # If the target is greater than the value of middle index, it tries to search target from the right half side.
    # If the target is less than the value of middle index, it tries to search target from the left half side.
    # Iterate the loop until it finds the target value or middle index equals to the start index.

    """
    This is helper method for binary search.

    :param nums: the given list
    :param start_index: the index number to be started for searching
    :param end_index: the last index number for searching
    :param target: the target number to be searched
    """
    def binary_search_helper(self, nums: list[int], start_index: int, end_index: int, target: int):
        if start_index > end_index:
            return -1
        middle_index = end_index - start_index // 2
        
        if nums[middle_index] < target:
            return self.binary_search_helper(nums, middle_index + 1, end_index, target)
        elif nums[middle_index] > target:
            return self.binary_search_helper(nums, start_index, middle_index - 1, target)
        else:
            return middle_index

# solution = Solution()
# lst = [-1,0,3,5,9,12,13,14]
# target = 9
# print(solution.search(lst, target))
