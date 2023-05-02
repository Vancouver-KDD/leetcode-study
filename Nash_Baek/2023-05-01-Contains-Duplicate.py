class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Error handling
        
        # It requires O(1) of time complexity
        if len(nums) == 0 or len(nums) > 10**5:
            raise ValueError("Invalid length of list")
            
        # It requires O(N) of time complexity
        for element in nums:
            if element < -10**9 or element > 10**9:
                raise ValueError("Invalid range of value")

        # Change the data type from list to set to remove duplicated elements.
        # The time complexity of set is O(1)
        # However, the conversion from list to set requires O(N)
        # N is the length of nums

        # The size of set depends on the number of duplicated elements.
        # The worst case of space complexity is O(N)
        # N is the length of nums
        
        set_nums = set(nums)

        # Comparing the length between nums and set_nums
        # If the length is same, it does not contain duplicated elements.
        
        # If the length is different, it means there are duplicated elements in the array.
        # The comparison requires O(1) because it simply compares two numbers.
        
        if len(nums) != len(set_nums):
            return True
        else:
            return False
