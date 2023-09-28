def longestSubstring(self, s: str, k: int) -> int:
            
        if len(s) < k:
            return 0

        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for char in s:
            if char_count[char] < k:
                return max(self.longestSubstring(substring, k) for substring in s.split(char))

        return len(s)



def longestSubstring2(self, s: str, k: int) -> int:
            
        if len(s) < k:
            return 0

        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for char in s:
            if char_count[char] < k:
                max_length = 0
                for substring in s.split(char):
                    max_length = max(max_length, self.longestSubstring(substring, k))
                return max_length

        return len(s)
