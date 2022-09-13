class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def is_valid(cnt1, cnt2):
            for i in range(26):
                if cnt1[i] != cnt2[i]:
                    return False
            return True
        
        if len(s1) > len(s2):
            return False
        s1_cnt, s2_cnt = [0] * 26, [0] * 26
        for i in s1:
            s1_cnt[ord(i) - ord("a")] += 1
        
        l, r = 0, 0
        while r < len(s2):    
            while sum(s2_cnt) < sum(s1_cnt):
                s2_cnt[ord(s2[r]) - ord("a")] += 1
                r += 1
            if is_valid(s1_cnt, s2_cnt):
                return True
            s2_cnt[ord(s2[l]) - ord("a")] -= 1
            l += 1
        return False
