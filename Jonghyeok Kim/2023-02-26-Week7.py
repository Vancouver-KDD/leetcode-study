class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        Most_freq = freq.most_common()[0][1]
        Found_most = sum([freq[key] == Most_freq for key in freq])
        return max(len(tasks), (Most_freq - 1) * (n + 1) + Found_most)
    

View on Github
class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
            
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
    
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        can_len = len(candidates)
        def dfs(start, comb, comb_sum):
            if comb_sum == target:
                res.append(comb.copy())
                return
            if start >= can_len or comb_sum > target:
                return
            dfs(start, comb + [candidates[start]], comb_sum + candidates[start])
            dfs(start+1, comb, comb_sum)
        dfs(0,[],0)
        return res
    
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # base case
        if len(nums) == 1:
            return [nums[:]]  # nums[:] is a deep copy

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(nums, sub):
            res.append(sub)
            if len(nums) == 0:
                return
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i-1]:
                    dfs(nums[i+1:], sub+[nums[i]])
        dfs(nums, [])
        return res
            
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(candidates, comb, comb_sum):
            if comb_sum == target:
                res.append(comb.copy())
            if comb_sum > target:
                return
            for idx, n in enumerate(candidates):
                if idx == 0 or candidates[idx-1] != candidates[idx]:
                    dfs(candidates[idx+1:], comb + [candidates[idx]], comb_sum + candidates[idx])
        dfs(candidates, [], 0)

        return res
    
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if not (-1<r<ROWS and -1<c<COLS and word[i] == board[r][c] and (r,c) not in path):
                return False
            path.add((r,c))
            res = (dfs(r - 1, c, i + 1) or
                   dfs(r + 1, c, i + 1) or
                   dfs(r, c - 1, i + 1) or
                   dfs(r, c + 1, i + 1))
            path.remove((r,c))
            
            return res
        for r in range(ROWS):
            for c in range(COLS):
                res = dfs(r, c, 0)
                if res:
                    return True
        return False
        
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(left, sub):
            if left == len(s):
                res.append(sub.copy())
                return
            for right in range(left, len(s)):
                if is_palindrome(left, right):
                    sub.append(s[left:right+1])
                    dfs(right+1, sub)
                    sub.pop()
                
        def is_palindrome(left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -=1
            return True
        
        dfs(0,[])
        return res

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return ""
        letter = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        def dfs(i, sub):
            if len(sub) == len(digits):
                res.append(sub)
                return
            string = letter[digits[i]]
            for s in string:
                dfs(i+1, sub+s)
     
        dfs(0,"")
        return res