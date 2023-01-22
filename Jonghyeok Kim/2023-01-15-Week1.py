class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for num in nums:
            if num in num_dict:
                return True
            else:
                num_dict[num] = 1
        return False
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = collections.Counter(s)
        t_dict = collections.Counter(t)
        return s_dict == t_dict
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for idx, num in enumerate(nums):
            if num not in sum_dict:
                sum_dict[target - num] = idx
            else:
                return [sum_dict[num], idx]
            
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for st in strs:
            dict_key = [0] * 26
            for ch in st:
                dict_key[ord(ch) - ord('a')] += 1
            dict_key = str(dict_key)
            if dict_key in hash_map:
                hash_map[dict_key].append(st)
            else:
                hash_map[dict_key] = [st]
        return hash_map.values()
    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ord_dict = collections.Counter(nums)
        tuple_dict = list(ord_dict.items())
        tuple_dict = sorted(tuple_dict, key=lambda x: x[1], reverse=True)
        return [x[0] for x in tuple_dict[:k]]
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        res = [1]*len(nums)
        pro = 1
        for idx, num in enumerate(nums):
            if idx:
                pro *= nums[idx-1]
            res[idx] = pro
        pro = 1
        for idx, num in enumerate(nums[::-1]):
            if idx:
                pro *= nums[len(nums)-idx]
            res[len(nums)-idx-1] *= pro
        return res

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            # Row Validator
            rowDict = {}
            for j in range(9):
                if board[i][j] != "." and board[i][j] in rowDict:
                    return False
                else:
                    rowDict[board[i][j]] = 1
            
            # Col Validator
            colDict = {}
            for j in range(9):
                if board[j][i] != "." and board[j][i] in colDict:
                    return False
                else:
                    colDict[board[j][i]] = 1

        for i in range(3):
            for j in range(3):
                iStart, jStart = i*3, j*3
                subDict = {}
                for k in range(3):
                    for q in range(3):
                        if board[iStart + k][jStart + q] != "." and board[iStart + k][jStart + q] in subDict:
                            return False
                        else:
                            subDict[board[iStart + k][jStart + q]] = 1

        return True
    
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    """
    @param: s: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, s):
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
    
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        def visit_child(child):
            if child not in consecutive_counter:
                return 0
            if consecutive_counter[child]:
                return consecutive_counter[child]

            consecutive_counter[child] = visit_child(child-1) + 1
            return consecutive_counter[child]

        consecutive_counter = {element: 0 for element in nums}
        longest = 0

        for num in nums:
            if not consecutive_counter[num]:
                consecutive_counter[num] = visit_child(num-1) + 1
            longest = max(longest, consecutive_counter[num])
        return longest
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for ch in s:
            if ch.isalpha():
                clean += ch.lower()
            elif ch.isnumeric():
                clean += ch
        left, right = 0, len(clean)-1
        while left <= right:
            if clean[left] == clean[right]:
                left += 1
                right -= 1
            else:
                return False
        return True