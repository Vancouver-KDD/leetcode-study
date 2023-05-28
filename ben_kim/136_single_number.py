class Solution(object):
    def singleNumber(self, nums):
        uniq_num = 0;
    
        for idx in nums:        
            uniq_num = uniq_num ^ idx; # 1
            
        return uniq_num;

# 1. Concept of XOR
#   - uniq_num ^= idx;
#   - a ^ 0 = a
#   - a ^ a = 0
#   - a ^ b ^ a = (a ^ a)^ b = b