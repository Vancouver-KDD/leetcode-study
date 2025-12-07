class Solution(object):
    def __init__(self):
        self.answer = list()
        self.check = set()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        temp = []
        self.search(candidates, target, temp)
        return self.answer
        

    def search(self, candidates, target , temp):
        if sum(temp) == target:
            t = tuple(sorted(temp))
            if t not in self.check:
                self.check.add(t)
                self.answer.append(list(temp))
            return
        elif sum(temp) > target:
            return

        for c in candidates:
            temp.append(c)
            self.search(candidates, target, temp)
            temp.pop()
