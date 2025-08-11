class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_rob = max_rob = 0
#so max rob is previous house which is the max val so far
#and prev rob + cur val is 2 houses ago plus current val
#[prev_rob, max_rob, cur_val, next_val, ...]
        for cur_val in nums:
            temp = max(max_rob, prev_rob + cur_val)
            prev_rob = max_rob
            max_rob = temp
        
        return max_rob