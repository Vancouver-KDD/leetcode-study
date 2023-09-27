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



def longestSubstring(self, s: str, k: int) -> int:
            
        max_length = 0
    
        for char in set(s):
            if s.count(char) >= k:
                substrings = s.split(char)
                for substring in substrings:
                    if len(substring) >= k:
                        max_length = max(max_length, len(substring))
    
        return max_length