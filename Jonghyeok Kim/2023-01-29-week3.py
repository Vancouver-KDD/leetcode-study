class Solution:
    def isValid(self, s: str) -> bool:

        def is_closing(st:str) -> bool:
            if st == ")" or st == "}" or st == "]":
                return True
            return False
        
        def is_match(open_st: str, close_st: str) -> bool:
            if open_st == "(" and close_st == ")":
                return True
            if open_st == "[" and close_st == "]":
                return True
            if open_st == "{" and close_st == "}":
                return True
            return False

        q = collections.deque([])
        for st in s:
            if is_closing(st):
                if len(q) == 0:
                    return False
                item = q.pop()
                if not is_match(item, st):
                    return False
            else:
                q.append(st)
        return True if len(q) == 0 else False
    
class MinStack:

    def __init__(self):
        self.min_stack = []
        self.internal_stack = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        if len(self.internal_stack) == 0:
            self.internal_stack.append(val)
        elif len(self.internal_stack) != 0 and self.internal_stack[-1] >= val:
            self.internal_stack.append(val)

    def pop(self) -> None:
        elem = self.min_stack.pop()
        if self.internal_stack[-1] == elem:
            self.internal_stack.pop()

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.internal_stack[-1]
    
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        def is_operator(st):
            if st == "+" or st == "-" or st == "*" or st == "/":
                return True
        
        def operate_sign(op, item_one, item_two):
            res, item_one, item_two = 0, int(item_one), int(item_two)
            if op == "+":
                res = item_two + item_one
            elif op == "*":
                res = item_two * item_one
            elif op == "-":
                res = item_two - item_one
            elif op == "/":
                res = item_two / item_one
            return res
        
        internal_stack = []

        for s in tokens:
            if not is_operator(s):
                internal_stack.append(s)
            else:
                item_one = internal_stack.pop()
                item_two = internal_stack.pop()
                operator_res = operate_sign(s, item_one, item_two)
                internal_stack.append(operator_res)
        return int(internal_stack[0])


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(left, right, pairs):
            if left == 0:
                if right > 0:
                    pairs += ")" * right
                nonlocal res
                res.append(pairs)
                return
            dfs(left-1, right, pairs + "(")
            if left < right:
                dfs(left, right-1, pairs + ")")
        dfs(n-1, n, "(")

        return res
    
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = collections.deque([])
        res = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            # pop the most recent temp from the stack if it is smaller than the incoming temp
            while len(stack) and stack[-1][1] < temp:
                p_idx, p_temp = stack.pop()
                res[p_idx] = idx - p_idx
            stack.append((idx, temp))
        return res

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lst = [[position[i], speed[i]]  for i in range(len(position))]
        lst = sorted(lst, key=lambda a : a[0], reverse=True)
        time_list = []
        # loop until the head reach the target
        for p, s in lst:
            t = (target-p) / s
            time_list.append(t)
            if len(time_list) > 1 and time_list[-2] >= time_list[-1]:
                time_list.pop()
        return len(time_list)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, res = [], 0
        for i, h in enumerate(heights+ [0]):
            while stack and heights[stack[-1]] > h:
                H = heights[stack.pop()]
                W = i if not stack else i - stack[-1] - 1
                res = max(res, H*W)
            stack.append(i)
        return res
    
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1
    
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r, m = 0, len(matrix) - 1, 0
        while l <= r:
            m = (l+r) // 2
            if matrix[m][0] <= target and matrix[m][-1] >= target:
                break
            if matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1
        row = m
        
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l+r) // 2
            if matrix[row][m] == target:
                return True
            if matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1

        return False
    
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r, res = 0, len(nums)-1, float("inf")
        # If all sorted, return the head
        if nums[l] <= nums[r]:
            return nums[l]

        while l <= r:
            m = (r + l) // 2
            res = min(res, nums[m], nums[l])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res