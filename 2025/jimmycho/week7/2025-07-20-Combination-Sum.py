class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def helper(new_candidates, temp, temp_sum):
            if len(temp) > 150:
                return
            if temp_sum == target:
                result.append(temp[:])
                return
            for i in range(len(new_candidates)):
                if new_candidates[i] > target - temp_sum:
                    return
                temp.append(new_candidates[i])
                temp_sum += new_candidates[i]
                helper(new_candidates[i:], temp, temp_sum)
                temp_sum -= temp.pop()
        helper(candidates, [], 0)
        return result