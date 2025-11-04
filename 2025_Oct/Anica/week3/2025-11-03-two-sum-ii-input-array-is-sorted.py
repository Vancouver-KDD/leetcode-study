
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0 
        end = len(numbers)-1
        while start<end: 
            summation = numbers[start] + numbers[end]
            if target == summation: 
                return [start+1, end+1]
            elif target > summation: 
                start+=1 
            else: 
                end-=1
        return -1