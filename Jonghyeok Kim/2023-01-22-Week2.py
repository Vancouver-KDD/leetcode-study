class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx, num in enumerate(numbers):
            if target - num not in hash_map:
                hash_map[num] = idx
            else:
                return [hash_map[target - num]+1, idx+1]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx, num in enumerate(nums):
            if idx != 0 and nums[idx-1] == num:
                continue
            target = -1 * num
            hash_map = {}
            for n in nums[idx+1:]:
                diff = target - n
                if diff in hash_map:
                    if not res or res[-1] != [num, diff, n]:
                        res.append([num, diff, n])
                else:
                    hash_map[n] = 1
        return res
    
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            water_height = min(height[left], height[right])
            distance = right - left
            max_water = max(max_water, water_height * distance)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
    
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p, max_p, res = prices[0], prices[0], 0
        for i in prices:
            if i < min_p:
                min_p = i
                max_p = i
            if i > max_p:
                max_p = i
                res = max(res, max_p-min_p)
        return res

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, res, cur_len, sub_string = 0, 0, 0, {}
        for st in s:
            cur_len += 1
            while st in sub_string:
                del sub_string[s[left]]
                left += 1
                cur_len -= 1
            sub_string[st] = 1
            res = max(cur_len, res)
        return res
    
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        max_ch, left, right, res = 0,0,0,0
        
        for st in s:
            hash_map[st] = hash_map.get(st, 0) + 1
            while right - left + 1 - max(hash_map.values()) > k:
                hash_map[s[left]] -= 1
                left += 1

            res = max(res, right-left+1)
            right += 1
        return res
    
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_s1 = Counter(s1)
        len_s1 = len(s1)
        for idx, ch in enumerate(s2):
            if ch in hash_s1:
                hash_s1[ch] -= 1
            if idx >= len_s1 and s2[idx-len_s1] in hash_s1:
                hash_s1[s2[idx-len_s1]] += 1
            if all([value == 0 for value in hash_s1.values()]):
                return True
        return False
    
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()  # index
        l = r = 0
        # O(n) O(n)
        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
