```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
```

### O(n log(n))

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        sub = []

        for i in range(n):
            curr = nums[i]
            if not sub or curr > sub[-1]:
                sub.append(curr)
            else:
                sub[bisect.bisect_left(sub, curr)] = curr
        return len(sub)
```