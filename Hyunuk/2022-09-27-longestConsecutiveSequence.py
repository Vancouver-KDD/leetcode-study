class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        seen = set()
        ret = 0
        for num in nums:
            if num in seen:
                continue
            origin = num
            seen.add(num)
            temp = [num]
            
            while num - 1 in nums and num - 1 not in seen:
                num -= 1
                seen.add(num)
                temp.append(num)
            
            num = origin
            while num + 1 in nums and num + 1 not in seen:
                num += 1
                seen.add(num)
                temp.append(num)
                
            ret = max(ret, len(temp))    
        return ret
