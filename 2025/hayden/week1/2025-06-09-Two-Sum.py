#First way, brute force, O(n^2)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #two pointers. second poitner is going to be 1 in front of the first pointer

        new_list= []

        for first in range(len(nums)):
            #the first argument is the skip in rnage()
            for second in range(first + 1,len(nums)):
                if nums[first] + nums[second] == target:
                    new_list.append(first)
                    new_list.append(second)
        
        return new_list
    


#Second way, using hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {} #making a dictionary to store what we've already seen

        #enumreate() is a built in function for python to get both the index and value.
        for index, item in enumerate(nums):
            
            need = target - item

            if need in seen:
                return [seen[need], index]

            #if it's not in the set, 
            seen[item] = index
        return seen
        
