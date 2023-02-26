class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        for i in candidates:
            q = deque()
            q.append([i])
            while q:
                combo = q.popleft()
                if sum(combo) == target:
                    result.append(combo)
                    continue
                for j in candidates:
                    if j >= combo[-1]:
                        new_combo = combo + [j]
                        if sum( new_combo ) <= target:
                            q.append( new_combo )
                        else:
                            break
        return result