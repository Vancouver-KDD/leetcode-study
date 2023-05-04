# For more description, please visit the blog below.

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Error handling part
        # 1. Length of list check
        # 2. Boundary of element check
        # Each of them requires O(N) of time complexity.
        if not 1 <= len(prices) <= 10**5:
            raise ValueError("The length of prices should be from 1 to 10^5.")
            # return 0
        
        for element in prices:
            if not 0 <= element <= 10**4:
                raise ValueError("The boundary of prices have to be from 0 to 10^4")
                # return 0


        # Subtract index2 - index1 while moving the pointer from index0 to last index of the given list.
        # The result of subtraction will be appended into set.
        # Set data type automatically remove duplicated elements.
        # After that, find and return the maximum element from the set
        # This logic requires O(N^2) of time complexity.
        set_list = set()
        for i in range(len(prices) -1):
            for element in prices:
                if prices.index(element) != (len(prices) - 1):
                    set_list.add(prices[-1] - element)
            prices.pop(-1)
        # print(set_list)
        
        if len(set_list) == 0:
            return 0

        return max(set_list) if max(set_list) >= 0 else 0
    

solution = Solution()
lst = [7,1,5,3,6,4]
print(solution.maxProfit(lst))