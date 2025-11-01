from collections import Counter

# O(MN)
class SuboptimalSolution(object):
    def checkInclusion(self, s1, s2):
        pattern = Counter()
        pattern_s2 = Counter()
        for char in s1:
            pattern[ord(char) - ord('a')] += 1

        for char in s2:
            pattern_s2[ord(char) - ord('a')] += 1

        pointer = 0
        while pointer < len(s2):
            pattern_s2 = Counter()
            for char_two in range(pointer, min(pointer + len(s1), len(s2))):
                pattern_s2[ord(s2[char_two]) - ord('a')] += 1

            if pattern == pattern_s2:
                return True
            pointer += 1

        return False

# O(26N)

class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        # Build pattern (26 letters indexed 0..25)
        pattern = Counter()
        for ch in s1:
            pattern[ord(ch) - ord('a')] += 1

        # Build first window
        pattern_s2 = Counter()
        for i in range(len(s1)):
            pattern_s2[ord(s2[i]) - ord('a')] += 1

        # Check first window
        if all(pattern[k] == pattern_s2[k] for k in range(26)):
            return True

        # Slide by 1 each time: remove left, add right, then compare
        for start in range(1, len(s2) - len(s1) + 1):
            left = ord(s2[start - 1]) - ord('a')
            right = ord(s2[start + len(s1) - 1]) - ord('a')
            pattern_s2[left] -= 1
            pattern_s2[right] += 1

            if all(pattern[k] == pattern_s2[k] for k in range(26)):
                return True

        return False



# O(N)
class OptimalSolution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        a = ord('a')
        s1_count = Counter()
        s2_count = Counter()

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - a] += 1
            s2_count[ord(s2[i]) - a] += 1

        matches = 0
        for i in range(26):
            if s1_count.get(i, 0) == s2_count.get(i, 0):
                matches += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            idx = ord(s2[right]) - a
            prev = s2_count.get(idx, 0)
            s2_count[idx] = prev + 1
            if s1_count.get(idx, 0) == s2_count.get(idx, 0):
                matches += 1
            elif s1_count.get(idx, 0) + 1 == prev + 1:
                matches -= 1

            idx = ord(s2[left]) - a
            prev = s2_count.get(idx, 0)
            s2_count[idx] = prev - 1
            if s1_count.get(idx, 0) == s2_count.get(idx, 0):
                matches += 1
            elif s1_count.get(idx, 0) - 1 == prev - 1:
                matches -= 1
            left += 1

        return matches == 26
