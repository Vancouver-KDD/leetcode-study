class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        for idx in range(amount+1):
            #Try each coin and find out the smallest combination
            for coin in coins:
                #If coin is bigger than the index, coin can not fit. 
                #If it is smaller or equal, update the element with smaller combination
                if coin <= idx:
                    dp[idx] = min(dp[idx], dp[idx-coin]+1)
        return dp[-1] if dp[-1] != float("inf") else -1
    
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_res= min_res= 1
        res = max(nums)
        for elem in nums:
            tmp = max_res * elem
            max_res = max(tmp, min_res*elem, elem)
            min_res = min(tmp, min_res*elem, elem)
            res = max(res, max_res)
        return res
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s)+1)
        dp[-1] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                word_len = len(word)
                if i + word_len <= len(s) and s[i:i + word_len] == word and dp[i + word_len]:
                    dp[i] = True

        return dp[0]

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        num_len = len(nums)
        #use dp list that keeps track of LIS
        dp = [0] * (num_len + 1)
        for i in range(num_len-1,-1,-1):
            for j in range(num_len-1, i, -1):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp) + 1

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[m-1][n-1] = 1
        for m_inex in range(m-1,-1,-1):
            for n_index in range(n-1,-1,-1):
                if not (m_inex == m-1 and n_index == n-1):
                    dp[m_inex][n_index] = dp[m_inex+1][n_index] + dp[m_inex][n_index+1]
        return dp[0][0]
