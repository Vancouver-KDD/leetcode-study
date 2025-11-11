class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        r = [0 for _ in range(len(temperatures))]
        s = []
        for i, t in enumerate(temperatures):
            if not s:
                s.append([t, i])
            else:
                while len(s) > 0 and s[-1][0] < t:
                    p = s.pop()
                    r[p[1]] = i - p[1]
                s.append([t, i])
        return r