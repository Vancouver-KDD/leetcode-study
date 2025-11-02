class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1Dic = {}
        s2Dic = {}

        for v in s1:
            if not v in s1Dic:
                s1Dic[v] = 0
            s1Dic[v] += 1

        for v in s2[:len(s1)]:
            if not v in s2Dic:
                s2Dic[v] = 0
            s2Dic[v] += 1

        start = 0
        end = len(s1) - 1

        while True:
            if s1Dic == s2Dic:
                return True

            if end + 1 >= len(s2):
                break

            s2Dic[s2[start]] -= 1
            if s2Dic[s2[start]] == 0:
                del s2Dic[s2[start]]
            start += 1

            end += 1
            if not s2[end]  in s2Dic:
                s2Dic[s2[end]] = 0
            s2Dic[s2[end]] += 1


        return False
