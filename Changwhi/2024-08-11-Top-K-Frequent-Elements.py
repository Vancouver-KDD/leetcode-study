class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # loop thorugh nums
        # using dic to store value and frequency
        # print out the k most freqent elements

        value_frequency = {}  # store number and occurrence

        # The indices in this array correspond to the occurrences, 
        # while the values correspond to the numbers in the given array.
        frequent = [[] for i in range(len(nums)+1)]  

        for i in range(len(nums)):
            value_frequency[nums[i]] = 1 + value_frequency.get(nums[i], 0)
        for key, value in value_frequency.items():
            print("key {} value {}".format(key, value))
            frequent[value].append(key)

        result = []     
        for index in range(len(frequent) -1, -1, -1):
            for number in frequent[index]:  # to handle a situation that contains more than 2 value
                result.append(number)
                if len(result) == k:
                    return result