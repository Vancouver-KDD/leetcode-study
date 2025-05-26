class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = set()
        # We want to start adding from the smallest number, so that we can early exit once
        # the total sum exceeds the target
        candidates.sort()
        
        def helper(i, total, temp):
            if total == target:
                # Adding the list to the set raises 'unhashable type; 'list''
                # Convert it to a tuple instead.
                results.add(tuple(temp))
                return
            elif total > target or i >= len(candidates):
                return
            
            total += candidates[i]
            temp.append(candidates[i])
            helper(i + 1, total, temp)
            # backtrack
            total -= candidates[i]
            temp.pop()
            helper(i + 1, total, temp)
        
        helper(0, 0, [])
        return [list(t) for t in results]
