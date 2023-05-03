# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # iterate through the "nums" list to check if the current number exists in the dictionary
        # return True if number exists, else add the current number to the dictionary
        # iteration will continue if the list doesn't contain a duplicate,
        # therefore, return False if the end of the list is reached
        nums_dict = {}
        for number in nums:
            if number in nums_dict:
                return True
            else:
                nums_dict[number] = 0
        return False
