## recursion without memoization

example nums = [1,2,3,1]
if I rub 0, then I can rub 2 or 3
if I rub 1, then I can rub 3
rub 0 or 1 ? 
base case?
return if there isn't anything else to rub
else
max(1 + rob([3,1]), 2 + rob([1]))


```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) < 1:
            return 0
        return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
```

## memoization
Instead of slicing nums each time (which makes a new list), we’ll use an index i to represent “start robbing from house i”.

The key is i (the current index in nums).
If we know the maximum money we can rob starting from index i, we can reuse it later.

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n
        def dp(i):
            if i >= n:
                return 0
            if memo[i] > -1:
                return memo[i]

            memo[i] = max(nums[i] + dp(i + 2), dp(i + 1))
            return memo[i]
        return dp(0)
```

### Example: nums = [2, 7, 9, 3, 1]
We’ll track function calls and memo updates.

### Step-by-step Execution

**Call dp(0)**
```
rob_this = 2 + dp(2) → need dp(2)

skip_this = dp(1) → need dp(1)
```
**Call dp(2)**
```
rob_this = 9 + dp(4) → need dp(4)

skip_this = dp(3) → need dp(3)
```

**Call dp(4)**
```
rob_this = 1 + dp(6) → dp(6) is beyond length → returns 0

skip_this = dp(5) → beyond length → returns 0

Result = max(1 + 0, 0) = 1
✅ Store in memo: memo[4] = 1
```

**Call dp(3)**
```
rob_this = 3 + dp(5) → returns 0

skip_this = dp(4) → found in memo: 1 (reused!)

Result = max(3 + 0, 1) = 3
✅ Store in memo: memo[3] = 3
```
**Back to dp(2)**
```
rob_this = 9 + dp(4) → 1 from memo → total 10

skip_this = dp(3) → 3 from memo

Result = max(10, 3) = 10
✅ Store in memo: memo[2] = 10
```
**Call dp(1)**
```
rob_this = 7 + dp(3) → 3 from memo → total 10

skip_this = dp(2) → 10 from memo

Result = max(10, 10) = 10
✅ Store in memo: memo[1] = 10
```
**Back to dp(0)**
```
rob_this = 2 + dp(2) → 10 from memo → total 12

skip_this = dp(1) → 10 from memo

Result = max(12, 10) = 12
✅ Store in memo: memo[0] = 12
```
