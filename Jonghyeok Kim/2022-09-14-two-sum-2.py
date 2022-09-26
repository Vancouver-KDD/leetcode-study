class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_pointer, end_pointer = 0, len(numbers)-1
        while start_pointer < end_pointer:
            two_sum = numbers[start_pointer] + numbers[end_pointer]
            if two_sum == target:
                return [start_pointer+1, end_pointer+1]
            elif two_sum > target:
                end_pointer -= 1
            else:
                start_pointer += 1
